from django.shortcuts import get_object_or_404
from django.contrib.messages import success
from django.urls import reverse
from django.utils.translation import pgettext, get_language
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin
from .mixins import DeveloperAcknowledgementRequiredMixin
from bbtest.views.generic import FormView
from bbtest.forms.test import TestForm
from bbtest.models import TestDomain, Test


class TestsView(DeveloperPermissionRequiredMixin, DeveloperAcknowledgementRequiredMixin, FormView):
    template_name = "developer/tests.html"
    form_class = TestForm
    unaccepted_acknowledgement_redirect_urlpattern = "bbtest:developer_acknowledgement"

    def get_context_data(self, **kwargs):
        kwargs["empty_language_code"] = Test.LANGUAGE_XX

        kwargs["nis"] = get_object_or_404(TestDomain.objects.prefetch_related("sections"), pk=7911)
        kwargs["nis_data"] = []
        for section in kwargs["nis"].sections.all():
            data = {
                "section": section,
                "language": None,
                "specification": {},
            }

            if section.id in (9540, 9544):
                data["language"] = {
                    "title": pgettext("/developer/tests/", "Choose test language"),
                    "choices": [],
                }
                for language in Test.LANGUAGES:
                    if language[0] == Test.LANGUAGE_XX:
                        continue
                    data["language"]["choices"].append(language)
                    data["specification"][language[0]] = section.specification[language[0]][get_language()]

            elif section.id == 9541:
                data["language"] = {
                    "title": pgettext("/developer/tests/", "Choose type"),
                    "choices": [
                        (Test.LANGUAGE_KK, pgettext("Test language", "Kazakh 1")),
                        (Test.LANGUAGE_RU, pgettext("Test language", "Kazakh 2")),
                    ],
                }
                data["specification"][Test.LANGUAGE_KK] = section.specification[Test.LANGUAGE_KK][get_language()]
                data["specification"][Test.LANGUAGE_RU] = section.specification[Test.LANGUAGE_RU][get_language()]

            elif section.id == 9542:
                data["language"] = {
                    "title": pgettext("/developer/tests/", "Choose type"),
                    "choices": [
                        (Test.LANGUAGE_RU, pgettext("Test language", "Russian 1")),
                        (Test.LANGUAGE_KK, pgettext("Test language", "Russian 2")),
                    ],
                }
                data["specification"][Test.LANGUAGE_RU] = section.specification[Test.LANGUAGE_RU][get_language()]
                data["specification"][Test.LANGUAGE_KK] = section.specification[Test.LANGUAGE_KK][get_language()]

            elif section.id == 9543:
                data["specification"][Test.LANGUAGE_XX] = section.specification[Test.LANGUAGE_XX][get_language()]

            kwargs["nis_data"].append(data)

        kwargs["unt"] = get_object_or_404(TestDomain.objects, pk=7912)

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self._test = form.create_test_suite(self.request.user)
        success(self.request, pgettext("Success alert message", "You have created a new Test."))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("bbtest:build_test", kwargs={ "code": self._test.code })
