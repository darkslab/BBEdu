from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _, pgettext
from django.urls import reverse
from django.core.cache import cache
from json import loads
from decimal import Decimal
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin
from .mixins import NonCurrentQuizSetRequiredMixin
from bbtest.models import TestDomain, Test
from bbtest.http import TightJsonResponse
from bbtest.models.shopping.handle import CartHandleAccessMixin
from bbtest.forms.buy import BuyTestsCartForm
from bbtest.models.shopping.items import *
from bbtest.models.shopping.items.map import TEST_SECTION_MAP
from bbtest.models.shopping.items.test import TestItem
from bbtest.models.shopping.exceptions import ItemError
from bbtest.models.shopping import items
from bbtest.models.shopping.operate import charge
from bbtest.payment_processors import CreditPaymentProcessor


def get_test_domain_or_404(test_domain_id):
    return get_object_or_404(
        TestDomain.objects.filter(pk__in=[ 7911, 7912, 7913 ]).prefetch_related("sections"),
        pk=test_domain_id,
    )


class BuyTestDomainsView(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/buy_test_domains.html"

    def get(self, request, *args, **kwargs):
        ga_events_checkout_credits = request.GET.get("ga_events_checkout_credits")
        if ga_events_checkout_credits is not None:
            self.request.session["ga_events"] = self.request.session.get("ga_events", []) + [[ "checkout", { "event_category": "credits", "value": int(ga_events_checkout_credits) } ]]
            return redirect("bbtest:student_buy_test_domains")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["nis"] = TestDomain.objects.get(pk=7911)
        kwargs["unt"] = TestDomain.objects.get(pk=7912)
        kwargs["nufypet"] = TestDomain.objects.get(pk=7913)

        return super().get_context_data(**kwargs)


class BuyTestsView(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/buy_tests.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domain"] = get_test_domain_or_404(self.kwargs["test_domain_id"])
        for section in kwargs["test_domain"].sections.all():
            section.minutes = section.duration // 60

        kwargs["test_langs"] = None
        if kwargs["test_domain"].pk != 7913:
            kwargs["test_langs"] = [ test_lang for test_lang in Test.LANGUAGES if test_lang[0] != Test.LANGUAGE_XX ]

        return super().get_context_data(**kwargs)


class BuyTestsCartView(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, CartHandleAccessMixin, View):
    def get(self, request, test_domain_id, *args, **kwargs):
        test_domain = get_test_domain_or_404(test_domain_id)
        cache_cart_type_key = "cart-type-%s" % request.user.pk
        cache_cart_old_items = "cart-old-items-%s" % request.user.pk
        cache_cart_timeout = 86400

        if cache.get(cache_cart_type_key) not in [ "test-domain-%s" % test_domain.pk, None ]:
            is_emptied = False
            is_restored = False

            if len(self.cart_handle()):
                self.cart_handle().empty()
                is_emptied = True

            old_items = cache.get(cache_cart_old_items, [])
            cache.delete(cache_cart_old_items)
            if len(old_items):
                for old_item in old_items:
                    if old_item["item_class"] not in items.__all__:
                        continue
                    try:
                        getattr(items, old_item["item_class"]).instantiate_from_meta_data(self.cart_handle(), old_item["meta_data"])
                        is_restored = True
                    except ItemError:
                        pass

            if is_emptied or is_restored:
                self.cart_handle().save()
            if is_restored:
                cache.set(cache_cart_type_key, "test-domain-%s" % test_domain.pk, cache_cart_timeout)
            else:
                cache.delete(cache_cart_type_key)

        data = self.__response(test_domain)
        data.update({
            "success": True,
        })
        return TightJsonResponse(data)

    def post(self, request, test_domain_id, *args, **kwargs):
        test_domain = get_test_domain_or_404(test_domain_id)
        form = BuyTestsCartForm(self.cart_handle().buyer(), test_domain, data=request.POST)
        if not form.is_valid():
            return TightJsonResponse({
                "success": False,
                "errors": loads(form.errors.as_json()),
            }, status=400)

        for item in self.cart_handle():
            if not isinstance(item, TestItem) or not len(form.cleaned_data["data"]["sections"]):
                self.cart_handle().remove_item(item)
                continue
            try:
                section_id_index = form.cleaned_data["data"]["sections"].index(item.test().section_id)
                form.cleaned_data["data"]["sections"].pop(section_id_index)
                continue
            except ValueError:
                pass
            self.cart_handle().remove_item(item)

        if len(form.cleaned_data["data"]["sections"]):
            available_tests = self.cart_handle().buyer().next_tests(test_domain, form.cleaned_data["data"]["language"])
            for section_id in form.cleaned_data["data"]["sections"]:
                try:
                    TEST_SECTION_MAP[str(section_id)](
                        self.cart_handle(),
                        next(test for test in available_tests if test.section_id == section_id),
                        self.cart_handle().buyer(),
                        form.cleaned_data["data"]["language"],
                    )
                except StopIteration:
                    pass

        self.cart_handle().save()

        cache_cart_type_key = "cart-type-%s" % request.user.pk
        if len(self.cart_handle()):
            cache.set(cache_cart_type_key, "test-domain-%s" % test_domain.pk, 86400)
        else:
            cache.delete(cache_cart_type_key)

        data = self.__response(test_domain, form.cleaned_data["data"]["language"])
        data.update({
            "success": True,
        })
        return TightJsonResponse(data)

    def __response(self, domain, default_language=Test.LANGUAGE_KK):
        # DARK_COMM  It's assumed that cart only contains tests that belong to the domain (parameter) at this point

        response = {
            "totals": {
                "line_items": [],
                "subtotals": [],
            },
            "sections": {},
            "data": {
                "sections": [],
            },
        }

        for section in domain.sections.all():
            response["sections"][str(section.pk)] = {
                "enabled": False,
                "price": None,
                "variant": None,
            }
        discount = Decimal("0.00")
        for item in self.cart_handle():
            if response["data"].get("language") is None:
                response["data"]["language"] = item.language()
            response["data"]["sections"].append(item.test().section.pk)
            response["totals"]["line_items"].append({
                "description": _(item.description()),
                "amount": pgettext("/student/buy-tests/xxxx/cart/", "%(amount).0f cred.") % { "amount": item.price() },
            })
            discount += item.discount()
        if response["data"].get("language") is None:
            response["data"]["language"] = default_language
        if discount > 0:
            response["totals"]["subtotals"].append({
                "description": pgettext("/student/buy-tests/xxxx/cart/", "Discount"),
                "amount": pgettext("/student/buy-tests/xxxx/cart/", "-%(amount).0f cred.") % { "amount": discount },
            })
        response["totals"]["total"] = pgettext("/student/buy-tests/xxxx/cart/", "%(amount).0f cred.") % { "amount": self.cart_handle().total() }

        available_tests = self.cart_handle().buyer().next_tests(domain, response["data"]["language"])
        for test in available_tests:
            section_id = str(test.section_id)
            response["sections"][section_id]["variant"] = _("page:/student/buy-tests/xxxx/:test_variant:%(test_code)s") % { "test_code": test.code.upper() }
            if section_id not in response["sections"]:
                continue
            response["sections"][section_id]["enabled"] = True
            if test.is_free:
                response["sections"][section_id]["price"] = pgettext("/student/buy-tests/xxxx/cart/", "Free")
            else:
                amount = Decimal("0.00")
                try:
                    if TEST_SECTION_MAP[section_id] in (
                        KazakhLanguageNISItem,
                        RussianLanguageNISItem,
                        EnglishLanguageNISItem,
                        MathematicalLiteracyCompulsoryUNTItem,
                        ReadingLiteracyCompulsoryUNTItem,
                        HistoryOfKazakhstanCompulsoryUNTItem,
                    ):
                        amount = Decimal("120.00")
                    elif TEST_SECTION_MAP[section_id] in (
                        MathematicsProfileUNTItem,
                        PhysicsProfileUNTItem,
                        ChemistryProfileUNTItem,
                        BiologyProfileUNTItem,
                        GeographyProfileUNTItem,
                        HistoryProfileUNTItem,
                        EnglishLanguageProfileUNTItem,
                        FrenchLanguageProfileUNTItem,
                        GermanLanguageProfileUNTItem,
                        KazakhLanguageAndLiteratureProfileUNTItem,
                        RussianLanguageAndLiteratureProfileUNTItem,
                        HumanSocietyRightProfileUNTItem,
                    ):
                        amount = Decimal("180.00")
                    elif TEST_SECTION_MAP[section_id] in (
                        MathematicsNISItem,
                    ):
                        amount = Decimal("240.00")
                    elif TEST_SECTION_MAP[section_id] in (
                        QuantitativeNISItem,
                    ):
                        amount = Decimal("360.00")
                    elif TEST_SECTION_MAP[section_id] in (
                        MathematicsNUFYPETItem,
                        PhysicsNUFYPETItem,
                        BiologyChemistryNUFYPETItem,
                        ThinkingSkillsNUFYPETItem,
                    ):
                        amount = Decimal("480.00")
                except KeyError:
                    pass
                response["sections"][section_id]["price"] = pgettext("/student/buy-tests/xxxx/cart/", "%(amount).0f cred.") % { "amount": amount }

        response["affordable"] = False
        if self.cart_handle().buyer().balance_account().balance() >= self.cart_handle().total():
            response["affordable"] = True

        return response


class BuyTestsCheckoutView(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, CartHandleAccessMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            cart_total = self.cart_handle().total()
            if cart_total.is_zero():
                self.cart_handle().checkout()
            else:
                charge(
                    CreditPaymentProcessor(self.cart_handle().total()),
                    self.cart_handle(),
                )
            self.request.session["ga_events"] = self.request.session.get("ga_events", []) + [[ "checkout", { "event_category": "tests", "value": round(cart_total) } ]]
            return TightJsonResponse({
                "success": True,
                "url": reverse("bbtest:student_exam"),
            })
        except ItemError as error:
            # DARK_TODO  change "message" to "errors" array?
            return TightJsonResponse({
                "success": False,
                "message": str(error),
            })
