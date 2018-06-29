from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _, pgettext
from json import loads
from decimal import Decimal
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.views.generic import TemplateView, UserContextMixin, View
from .mixins import NonCurrentQuizSetRequiredMixin
from bbtest.models import TestDomain, Test
from bbtest.http import TightJsonResponse
from bbtest.models.shopping.handle import CartHandleAccessMixin
from bbtest.forms.buy import BuyTestsCartForm
from bbtest.models.shopping.items.map import TEST_SECTION_MAP
from bbtest.models.shopping.items.test import TestItem
from bbtest.models.shopping.exceptions import ItemError
from bbtest.models.shopping import items
from bbtest.models.shopping.operate import charge
from bbtest.payment_processors import CreditPaymentProcessor


TEST_DOMAIN_IDS_DISPLAY = [ 7911, 7912 ]
TEST_DOMAIN_IDS_ALLOWED = [ 7912 ]


def get_test_domain_or_404(test_domain_id):
    return get_object_or_404(
        TestDomain.objects.filter(pk__in=TEST_DOMAIN_IDS_ALLOWED).prefetch_related("sections"),
        pk=test_domain_id,
    )


class BuyTestDomainsView(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/buy_test_domains.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domains"] = TestDomain.objects.filter(pk__in=TEST_DOMAIN_IDS_DISPLAY).all()
        for domain in kwargs["test_domains"]:
            if domain.pk in (7911,):
                domain.is_available = False
            else:
                domain.is_available = True

        return super().get_context_data(**kwargs)


class BuyTestsView(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/buy_tests.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domain"] = get_test_domain_or_404(self.kwargs["test_domain_id"])
        for section in kwargs["test_domain"].sections.all():
            section.minutes = section.duration // 60

            if section.pk in (9545, 9546, 9547):
                section.price = 120
            elif section.pk in (9548, 9549, 9550, 9551, 9552, 9553, 9554, 9555, 9556, 9557, 9558, 9559):
                section.price = 180
            else:
                section.price = 0

        kwargs["test_langs"] = [ test_lang for test_lang in Test.LANGUAGES if test_lang[0] != Test.LANGUAGE_XX ]

        return super().get_context_data(**kwargs)


class BuyTestsCartView(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, CartHandleAccessMixin, View):
    def get(self, request, test_domain_id, *args, **kwargs):
        test_domain = get_test_domain_or_404(test_domain_id)

        if request.session.get("cart_type") not in [ "test-domain-%s" % test_domain.pk, "empty" ]:
            is_emptied = False
            is_restored = False

            if len(self.cart_handle()):
                self.cart_handle().empty()
                is_emptied = True

            old_items = request.session.pop("cart_old_items", [])
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
                request.session["cart_type"] = "test-domain-%s" % test_domain.pk
            else:
                request.session["cart_type"] = "empty"

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

        if len(self.cart_handle()):
            request.session["cart_type"] = "test-domain-%s" % test_domain.pk
        else:
            request.session["cart_type"] = "empty"

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
            response["sections"][str(section.pk)] = False
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
        for section_id in [ str(test.section_id) for test in available_tests ]:
            if section_id not in response["sections"]:
                continue
            response["sections"][section_id] = True

        response["affordable"] = False
        if self.cart_handle().buyer().balance_account().balance() >= self.cart_handle().total():
            response["affordable"] = True

        return response


class BuyTestsCheckoutView(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, CartHandleAccessMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            charge(
                CreditPaymentProcessor(self.cart_handle().total()),
                self.cart_handle(),
            )
            # DARK_TODO  implement this!
            return TightJsonResponse({
                "success": True,
                "url": "https://google.com/",
            })
        except ItemError as error:
            return TightJsonResponse({
                "success": False,
                "message": str(error),
            })
