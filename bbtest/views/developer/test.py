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

        kwargs["Klass_4_ru"] = get_object_or_404(TestDomain.objects.prefetch_related("sections"), pk=7911)
        kwargs["Klass_4_ru_data"] = []
        for section in kwargs["Klass_4_ru"].sections.all():
            data = {
                "section": section,
                "language": None,
                "specification": {},
            }
            # if section.id in range(9540, 9999):
            data["language"] = {
                "title": pgettext("/developer/tests/", "Choose test language"),
                "choices": [],
            }
            data["language"]["choices"].append(Test.LANGUAGES[2])
            data["specification"][Test.LANGUAGE_RU] = test_specification(section, Test.LANGUAGE_RU, get_language())
            kwargs["Klass_4_ru_data"].append(data)


        kwargs["Klass_9_ru"] = get_object_or_404(TestDomain.objects.prefetch_related("sections"), pk=7912)
        kwargs["Klass_9_ru_data"] = []
        for section in kwargs["Klass_9_ru"].sections.all():
            data = {
                "section": section,
                "language": None,
                "specification": {},
            }
            data["language"] = {
                "title": pgettext("/developer/tests/", "Choose test language"),
                "choices": [],
            }
            data["language"]["choices"].append(Test.LANGUAGES[2])
            data["specification"][Test.LANGUAGE_RU] = test_specification(section, Test.LANGUAGE_RU, get_language())
            kwargs["Klass_9_ru_data"].append(data)
        
    

        kwargs["Klass_4_kz"] = get_object_or_404(TestDomain.objects.prefetch_related("sections"), pk=7913)
        kwargs["Klass_4_kz_data"] = []
        for section in kwargs["Klass_4_kz"].sections.all():
            data = {
                "section": section,
                "language": None,
                "specification": {},
            }
            data["language"] = {
                "title": pgettext("/developer/tests/", "Choose test language"),
                "choices": [],
            }
            data["language"]["choices"].append(Test.LANGUAGES[1])
            data["specification"][Test.LANGUAGE_KK] = test_specification(section, Test.LANGUAGE_KK, get_language())
            kwargs["Klass_4_kz_data"].append(data)

        
        kwargs["Klass_9_kz"] = get_object_or_404(TestDomain.objects.prefetch_related("sections"), pk=7914)
        kwargs["Klass_9_kz_data"] = []
        for section in kwargs["Klass_9_kz"].sections.all():
            data = {
                "section": section,
                "language": None,
                "specification": {},
            }
            data["language"] = {
                "title": pgettext("/developer/tests/", "Choose test language"),
                "choices": [],
            }
            data["language"]["choices"].append(Test.LANGUAGES[1])
            data["specification"][Test.LANGUAGE_KK] = test_specification(section, Test.LANGUAGE_KK, get_language())
            kwargs["Klass_9_kz_data"].append(data)

        print(kwargs.keys())
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print("form_valid")
        self._test = form.create_test_suite(self.request.user)
        success(self.request, pgettext("Success alert message", "You have created a new Test."))
        return super().form_valid(form)

    def get_success_url(self):
        print("get_success_url")
        return reverse("bbtest:build_test", kwargs={"code": self._test.code})
