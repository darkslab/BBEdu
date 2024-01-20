from django.shortcuts import get_object_or_404
from django.contrib.messages import success
from django.urls import reverse
from django.utils.translation import pgettext, get_language
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, ExpertPermissionRequiredMixin, StaffPermissionRequiredMixin
from .mixins import DeveloperAcknowledgementRequiredMixin
from bbtest.views.generic import FormView
from bbtest.views.common import UserContextMixin
from bbtest.forms.test import TestForm
from bbtest.models import TestDomain, Test
from bbtest.texts import test_specification


class TestsView(StaffPermissionRequiredMixin, UserContextMixin, FormView):
    template_name = "developer/tests.html"
    form_class = TestForm

    def get_context_data(self, **kwargs):
        kwargs["empty_language_code"] = Test.LANGUAGE_XX
        kwargs["domain_list"] = []
        kwargs["domain_data_list"] = []
        user = self.request.user

        if user.is_superuser:
            domain_dict = {
                domain: domain.sections.all() for domain in TestDomain.objects.prefetch_related("sections").all()
            }

        elif user.user_permissions.get().codename == "developer" and user.developer_profile is not None:
            section_list = user.developer_profile.section.prefetch_related("domain").all()
            domain_dict = {}

            for section_obj in section_list:
                domain = section_obj.domain
                domain_dict[domain] = domain_dict.get(domain, []) + [section_obj] 
        else:
            domain_dict = {}

        # print(user.user_permissions.get().codename, user.developer_profile)
        # kwargs["domain_list"] = list(domain_dict.keys())

        for domain, section_list in domain_dict.items():
            domain_name = domain.name
            domain_data = []

            for section in section_list:
                data = {
                    "section": section,
                    "language": None,
                    "specification": {},
                }
                data["language"] = {
                    "title": pgettext("/developer/tests/", "Choose test language"),
                    "choices": [],
                }
                if "ru" in domain_name:
                    data["language"]["choices"].append(Test.LANGUAGES[2])
                    data["specification"][Test.LANGUAGE_RU] = test_specification(section, Test.LANGUAGE_RU, get_language())
                elif "kz" in domain_name:
                    data["language"]["choices"].append(Test.LANGUAGES[1])
                    data["specification"][Test.LANGUAGE_KK] = test_specification(section, Test.LANGUAGE_KK, get_language())

                domain_data.append(data)

            kwargs["domain_list"].append(domain)
            kwargs["domain_data_list"].append([domain_name, domain_data])
        # from pprint import pprint
        # pprint(kwargs)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print("form_valid")
        self._test = form.create_test_suite(self.request.user)
        success(self.request, pgettext("Success alert message", "You have created a new Test."))
        return super().form_valid(form)

    def get_success_url(self):
        print("get_success_url")
        return reverse("bbtest:build_test", kwargs={"code": self._test.code})
