from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _, pgettext
from django.urls import reverse
from django.core.cache import cache
from json import loads
from decimal import Decimal

from urllib3 import add_stderr_logger
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
from django.conf import settings


if settings.DEBUG:
    # test
    bundles_manual =  {
        'ru': [{9539: 'b1d8', 9540: 'c4dd', 9541: '477e', 9542: '425e', 9543: '48c8', 9544: 'cfd3'}, 
               {9539: '84b0', 9540: '596c', 9541: '88f3', 9542: '7912', 9543: 'c2ab', 9544: 'bc6f'}, 
               {9539: '',     9544: '',     9541: '',     9543: '',     9540: ''    , 9542: ''}, 
               {9539: '1f77', 9540: '0073', 9541: '3aa2', 9542: 'cf6f', 9543: '5208', 9544: '4234'}, 
               {9539: '',     9544: '',     9541: '',     9543: '',     9540: ''    , 9542: ''}], 
        'kk': [{9539: '5655', 9540: '8323', 9541: 'b2fe', 9542: 'f654', 9543: 'cf9e', 9544: '25e3'}, 
               {9539: '1f77', 9540: '0073', 9541: '3aa2', 9542: 'cf6f', 9543: '5208', 9544: '4234'},
               {9539: '',     9544: '',     9541: '',     9543: '',     9540: ''    , 9542: ''}, 
               {9539: '',     9544: '',     9541: '',     9543: '',     9540: ''    , 9542: ''}, 
               {9539: '',     9544: '',     9541: '',     9543: '',     9540: ''    , 9542: ''}]}
else:
    # production
    # 'kk': [{9539: '2c08', 9540: '0a60', 9541: '3525', 9542: '69ed', 9543: '4e4f', 9544: 'bf79'}
    #        {9539: 'a603', 9540: '1c2c', 9541: 'ea72', 9542: 'a550', 9543: '989c', 9544: '3bdf'}
    #        {9539: 'f905', 9540: '7db3', 9541: 'c1d4', 9542: '5ccf', 9543: '628d', 9544: '7253'}
    #        {9539: ''    , 9540: '7d54', 9541: '406e', 9542: 'e58b', 9543: 'f009', 9544: '4f87'}
    #        {9539: ''    , 9540: '29a4', 9541: ''    , 9542: '3405', 9543: 'f77f', 9544: 'c8be'}]
    # 'ru': [{9539: '5ea0', 9540: '48be', 9541: '4c39', 9542: 'e518', 9543: 'ed26', 9544: 'c305'}
    #        {9539: 'cd50', 9540: 'c362', 9541: '2aa9', 9542: '2468', 9543: '5fe6', 9544: 'a2f4'}
    #        {9539: 'f77d', 9540: 'b7fa', 9541: '4baf', 9542: '0eee', 9543: 'dde1', 9544: '3aec'}
    #        {9539: ''    , 9540: 'f164', 9541: 'aee3', 9542: 'e361', 9543: '402d', 9544: '0efe'}
    #        {9539: ''    , 9540: 'a7d8', 9541: ''    , 9542: '58fb', 9543: 'b5ce', 9544: '6159'}]
    

    bundles_manual = {
        'kk': [{9539: '2c08', 9540: '0a60', 9541: '3525', 9542: '69ed', 9543: '4e4f', 9544: 'bf79'}, 
               {9539: 'a603', 9540: '1c2c', 9541: 'ea72', 9542: 'a550', 9543: '989c', 9544: '3bdf'},
               {9539: 'f905', 9540: '7db3', 9541: 'c1d4', 9542: '5ccf', 9543: '628d', 9544: '7253'},
               {9539: '',     9540: ''    , 9541: ''    , 9542: '',     9543: ''    , 9544: ''    },
               {9539: '',     9540: ''    , 9541: ''    , 9542: '',     9543: ''    , 9544: ''    }], 
        'ru': [{9539: '5ea0', 9540: '48be', 9541: '4c39', 9542: 'e518', 9543: 'ed26', 9544: 'c305'}, 
               {9539: 'cd50', 9540: 'c362', 9541: '2aa9', 9542: '2468', 9543: '5fe6', 9544: 'a2f4'},
               {9539: 'f77d', 9540: 'b7fa', 9541: '4baf', 9542: '0eee', 9543: 'dde1', 9544: '3aec'},
               {9539: '',     9540: ''    , 9541: ''    , 9542: '',     9543: ''    , 9544: ''    },
               {9539: '',     9540: ''    , 9541: ''    , 9542: '',     9543: ''    , 9544: ''    }]
            }



def get_test_domain_or_404(test_domain_id):
    return get_object_or_404(
        TestDomain.objects.filter(pk__in=[ 7911, 7912, 7913, 7915, 7916 ]).prefetch_related("sections"),
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
        # kwargs["law"] = TestDomain.objects.get(pk=7915)
        kwargs["proftest"] = TestDomain.objects.get(pk=7916)

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


class BuyTestsViewNIS(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/buy_tests_bundle_NIS.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domain"] = get_test_domain_or_404(self.kwargs["test_domain_id"])
        for section in kwargs["test_domain"].sections.all():
            section.minutes = section.duration // 60

        kwargs["test_langs"] = None
        if kwargs["test_domain"].pk != 7913:
            kwargs["test_langs"] = [ test_lang for test_lang in Test.LANGUAGES if test_lang[0] != Test.LANGUAGE_XX ]

        kwargs["bundles_names_manual_list"] = [{"pk": i, "name": "{} {}".format(pgettext("Bundle", "Bundle"), i+1)} for i in range(5)]
        kwargs["hide_section_modifier"] = "display: true;" if settings.DEBUG else "display: none;"
        return super().get_context_data(**kwargs)


class BuyTestsCartView(StudentPermissionRequiredMixin, NonCurrentQuizSetRequiredMixin, CartHandleAccessMixin, View):
    def get(self, request, test_domain_id, *args, **kwargs):
        test_domain = get_test_domain_or_404(test_domain_id)
        cache_cart_type_key = "cart-type-%s" % request.user.pk
        cache_cart_bundle_key = "cart-bundle-%s" % request.user.pk
        cache_cart_bundle_lang_key = "cart-bundle-lang-%s" % request.user.pk
        cache_cart_old_items = "cart-old-items-%s" % request.user.pk
        cache_cart_timeout = 86400

        print("cache.get(cache_cart_bundle_key)", cache_cart_bundle_key, cache.get(cache_cart_bundle_key))
        if cache.get(cache_cart_type_key) not in [ "test-domain-%s" % test_domain.pk ]:
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

        if test_domain.pk == 7911:
            data = self.__response_bundle(test_domain, bundle_pk=cache.get(cache_cart_bundle_key, -1), default_language=cache.get(cache_cart_bundle_lang_key, Test.LANGUAGE_KK))
        else:
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

        if test_domain.pk != 7911:
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

        else:
            available_tests = {test.code: test for test in self.cart_handle().buyer().remained_tests(test_domain, form.cleaned_data["data"]["language"])}
            bundle_pk = int(form.cleaned_data["data"]["selected_bundle_pk"])
            if len(form.cleaned_data["data"]["sections"]) and bundle_pk >= 0:
                for section_id, testcode in bundles_manual[form.cleaned_data["data"]["language"]][bundle_pk].items():
                    if testcode in available_tests.keys():
                        TEST_SECTION_MAP[str(section_id)](
                            self.cart_handle(),
                            available_tests[testcode],
                            self.cart_handle().buyer(),
                            form.cleaned_data["data"]["language"],
                        )
            
            cache_cart_bundle_key = "cart-bundle-%s" % request.user.pk
            cache_cart_bundle_lang_key = "cart-bundle-lang-%s" % request.user.pk
            if len(self.cart_handle()):
                cache.set(cache_cart_bundle_key, bundle_pk, 86400)
                cache.set(cache_cart_bundle_lang_key, form.cleaned_data["data"]["language"], 86400)
            else:
                cache.delete(cache_cart_bundle_key)
            
        self.cart_handle().save()

        cache_cart_type_key = "cart-type-%s" % request.user.pk
        if len(self.cart_handle()):
            cache.set(cache_cart_type_key, "test-domain-%s" % test_domain.pk, 86400)
        else:
            cache.delete(cache_cart_type_key)

        # print(form.cleaned_data)
        # data = self.__response(test_domain, form.cleaned_data["data"]["language"])
        if test_domain.pk == 7911:
            data = self.__response_bundle(test_domain, form.cleaned_data["data"]["language"], form.cleaned_data["data"]["selected_bundle_pk"], len(form.cleaned_data["data"]["sections"]))
        else:
            data = self.__response(test_domain, form.cleaned_data["data"]["language"])
        data.update({
            "success": True,
        })
        return TightJsonResponse(data)


    def __response_bundle(self, domain, default_language=Test.LANGUAGE_KK, bundle_pk=-1, sect_len=0):
        

        bundle_pk = int(bundle_pk)
        available_tests = {test.code: test for test in self.cart_handle().buyer().remained_tests(domain, default_language)}

        # if sect_len and bundle_pk >= 0:
        #     for section_id, testcode in bundles_manual[default_language][bundle_pk].items():
        #         if testcode in available_tests.keys():
        #             TEST_SECTION_MAP[str(section_id)](
        #                 self.cart_handle(),
        #                 available_tests[testcode],
        #                 self.cart_handle().buyer(),
        #                 default_language,
        #             )

        #     self.cart_handle().save()

        response = {
            "totals": {
                "line_items": [],
                "subtotals": [],
            },
            "sections": {},
            "bundles": {},
            "data": {
                "sections": [],
            },
            "selected_bundle_pk": bundle_pk
        }

        ## copied from __response
        for section in domain.sections.all():
            response["sections"][str(section.pk)] = {
                "enabled": False,
                "price": None,
                "variant": None,
            }
        discount = Decimal("0.00")

        cart = self.cart_handle()
        # print(type(cart), cart)
        # print("__products", getattr(cart, "__products"))
        for item in self.cart_handle():
            print("item", item)
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
        ## end copied from __response

        

        # for test in available_tests:
        if bundle_pk >= 0:
            for section_id, testcode in bundles_manual[default_language][bundle_pk].items():
                section_id = str(section_id)

                response["sections"][section_id]["variant"] = _("page:/student/buy-tests/xxxx/:test_variant:%(test_code)s") % { "test_code": testcode.upper() }

                if len(testcode) == 0 or testcode not in available_tests.keys():
                    continue
                # if section_id not in response["sections"]:
                #     continue
                # if testcode in available_tests.keys():
                response["sections"][section_id]["enabled"] = True

                if available_tests[testcode].is_free:
                    response["sections"][section_id]["price"] = pgettext("/student/buy-tests/xxxx/cart/", "Free")
                else:
                    amount = Decimal("0.00")
                    try:
                        if TEST_SECTION_MAP[section_id] in (
                            KazakhLanguageNISItem,
                            RussianLanguageNISItem,
                            EnglishLanguageNISItem,
                            NaturalScienceNISItem,
                        ):
                            amount = Decimal("600.00")
                        elif TEST_SECTION_MAP[section_id] in (
                            MathematicsNISItem,
                        ):
                            amount = Decimal("1000.00")
                        elif TEST_SECTION_MAP[section_id] in (
                            QuantitativeNISItem,
                        ):
                            amount = Decimal("1500.00")
                    except KeyError:
                        pass
                    response["sections"][section_id]["price"] = pgettext("/student/buy-tests/xxxx/cart/", "%(amount).0f cred.") % { "amount": amount }

        response["affordable"] = False
        if self.cart_handle().buyer().balance_account().balance() >= self.cart_handle().total():
            response["affordable"] = True

        # available_tests = [str(test) for test in available_tests]
        # order = ['Natural Science', 'Mathematics', 'Kazakh Language', 'Russian Language', 'English Language', 'Quantitative']
        order = [9539, 9540, 9541, 9542, 9543, 9544]
        # print("__response_bunde", available_tests)

        # response["bundles"] = {}
        for i, bund in enumerate(bundles_manual[default_language]):
            response["bundles"][str(i)] = {
                "enabled": [],
                "state": 0,     # 0: empty, 1: available, 2: complited
                "variant": []
            }
            for sect in order:
                test_variant = bund[sect]
                if len(test_variant) > 0:
                    response["bundles"][str(i)]["enabled"].append(test_variant in available_tests.keys())
                    response["bundles"][str(i)]["variant"].append(test_variant)
                    # print(test_variant, test_variant in available_tests)
                else:
                    response["bundles"][str(i)]["enabled"].append(False)
                    response["bundles"][str(i)]["variant"].append("")
            if all([v == "" for v in response["bundles"][str(i)]["variant"]]): 
                response["bundles"][str(i)]["state"] = 0    # 0: empty
            elif all([v == False for v in response["bundles"][str(i)]["enabled"]]): 
                response["bundles"][str(i)]["state"] = 2    # 2: complited
            else:
                response["bundles"][str(i)]["state"] = 1    # 1: available

        return response
            

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
        # print("available_tests", available_tests)
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
                        # KazakhLanguageNISItem,
                        # RussianLanguageNISItem,
                        # EnglishLanguageNISItem,
                        # NaturalScienceNISItem,
                    ):
                        amount = Decimal("600.00")
                    elif TEST_SECTION_MAP[section_id] in (
                        MathematicalLiteracyCompulsoryUNTItem,
                        ReadingLiteracyCompulsoryUNTItem,
                        HistoryOfKazakhstanCompulsoryUNTItem,
                    ):
                        amount = Decimal("80.00")
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
                        amount = Decimal("90.00")
                    # elif TEST_SECTION_MAP[section_id] in (
                        # MathematicsNISItem,
                    # ):
                    #     amount = Decimal("1000.00")
                    # elif TEST_SECTION_MAP[section_id] in (
                    #     QuantitativeNISItem,
                    # ):
                    #     amount = Decimal("1500.00")
                    elif TEST_SECTION_MAP[section_id] in (
                        MathematicsNUFYPETItem,
                        PhysicsNUFYPETItem,
                        BiologyChemistryNUFYPETItem,
                        ThinkingSkillsNUFYPETItem,
                    ):
                        amount = Decimal("480.00")
                    elif TEST_SECTION_MAP[section_id] in (
                        LawItem,
                    ):
                        amount = Decimal("200.00")
                    elif TEST_SECTION_MAP[section_id] in (
                        ProftestItem,
                    ):
                        amount = Decimal("200.00")
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
            if cart_total.is_zero():    # if free go directly to test
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
