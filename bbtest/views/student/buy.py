from django.shortcuts import get_object_or_404
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.views.generic import TemplateView, UserContextMixin
from .mixins import NonRunningTestsRequiredMixin
from bbtest.models import TestDomain, Test


class BuyTestDomainsView(StudentPermissionRequiredMixin, NonRunningTestsRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/buy_test_domains.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domains"] = TestDomain.objects.all()
        return super().get_context_data(**kwargs)


class BuyTestsView(StudentPermissionRequiredMixin, NonRunningTestsRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/buy_tests.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domain"] = get_object_or_404(TestDomain.objects.prefetch_related("sections"), pk=self.kwargs["test_domain_id"])
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
