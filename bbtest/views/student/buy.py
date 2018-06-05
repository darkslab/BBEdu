from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.views.generic import TemplateView, UserContextMixin
from .mixins import NonRunningTestsRequiredMixin
from bbtest.models import TestDomain


class BuyTestDomainsView(StudentPermissionRequiredMixin, NonRunningTestsRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/buy_test_domains.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domains"] = TestDomain.objects.all()
        return super().get_context_data(**kwargs)


class BuyTestsView(StudentPermissionRequiredMixin, NonRunningTestsRequiredMixin, UserContextMixin, TemplateView):
    pass
