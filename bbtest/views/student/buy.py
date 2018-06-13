from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _, pgettext
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.views.generic import TemplateView, UserContextMixin, View
from .mixins import NonRunningTestsRequiredMixin
from bbtest.models import TestDomain, Test
from bbtest.http import TightJsonResponse
from bbtest.models.shopping.handle import CartHandleAccessMixin


TEST_DOMAIN_IDS_DISPLAY = [ 7911, 7912 ]
TEST_DOMAIN_IDS_ALLOWED = [ 7912 ]


def get_test_domain_or_404(test_domain_id):
    return get_object_or_404(
        TestDomain.objects.filter(pk__in=TEST_DOMAIN_IDS_ALLOWED).prefetch_related("sections"),
        pk=test_domain_id,
    )


class BuyTestDomainsView(StudentPermissionRequiredMixin, NonRunningTestsRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/buy_test_domains.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domains"] = TestDomain.objects.filter(pk__in=TEST_DOMAIN_IDS_DISPLAY).all()
        for domain in kwargs["test_domains"]:
            if domain.pk in (7911,):
                domain.is_available = False
            else:
                domain.is_available = True

        return super().get_context_data(**kwargs)


class BuyTestsView(StudentPermissionRequiredMixin, NonRunningTestsRequiredMixin, UserContextMixin, TemplateView):
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


class BuyTestsCartView(StudentPermissionRequiredMixin, NonRunningTestsRequiredMixin, CartHandleAccessMixin, View):
    def get(self, request, test_domain_id, *args, **kwargs):
        test_domain = get_test_domain_or_404(test_domain_id)

        # DARK_TODO  implement this!
        if len(self.cart_handle()):
            self.cart_handle().empty()
            self.cart_handle().save()

        data = self.__response(test_domain)
        data.update({
            "success": True,
        })
        return TightJsonResponse(data)

    def post(self, request, test_domain_id, *args, **kwargs):
        test_domain = get_test_domain_or_404(test_domain_id)
        # DARK_TODO  implement this!
        pass

    def __response(self, domain):
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
        for item in self.cart_handle():
            if response["data"].get("language") is None:
                response["data"]["language"] = item.language()
            response["data"]["sections"].append(item.test().section.pk)
            response["totals"]["line_items"].append({
                "description": _(item.description()),
                "amount": pgettext("/student/buy-tests/xxxx/cart/", "%(amount).0f cred.") % { "amount": item.price() },
            })
        if response["data"].get("language") is None:
            response["data"]["language"] = Test.LANGUAGE_KK
        discount = self.cart_handle().subtotal() - self.cart_handle().total()
        if discount > 0:
            response["totals"]["subtotals"].append({
                "description": pgettext("/student/buy-tests/xxxx/cart/", "Discount"),
                "amount": pgettext("/student/buy-tests/xxxx/cart/", "-%(amount).0f cred.") % { "amount": discount },
            })
        response["totals"]["total"] = pgettext("/student/buy-tests/xxxx/cart/", "%(amount).0f cred.") % { "amount": self.cart_handle().total() }

        available_tests = Test.approved_tests.next_tests(self.cart_handle().buyer(), domain, response["data"]["language"])
        for section_id in [ str(test.section_id) for test in available_tests ]:
            if section_id not in response["sections"]:
                continue
            response["sections"][section_id] = True

        response["affordable"] = False
        if self.cart_handle().buyer().balance_account().balance() >= self.cart_handle().total():
            response["affordable"] = True

        return response
