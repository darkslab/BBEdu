from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import get_language
from django.shortcuts import get_object_or_404
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin
from bbtest.developer_agreements import AGREEMENT_TEXTS
from bbtest.models import DeveloperAcknowledgement
from .mixins import DeveloperAcknowledgementRequiredMixin


class DashboardView(DeveloperPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "developer/dashboard.html"

    def get_context_data(self, **kwargs):
        tests = self.request.user.tests.select_related("section__domain").order_by("-created_at")
        paginator = Paginator(tests, 25)

        try:
            kwargs["tests"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["tests"] = paginator.page(1)
        except EmptyPage:
            kwargs["tests"] = paginator.page(paginator.num_pages)

        return super().get_context_data(**kwargs)


class OfferView(DeveloperPermissionRequiredMixin, DeveloperAcknowledgementRequiredMixin, UserContextMixin, TemplateView):
    template_name = "developer/offer.html"

    def get_context_data(self, **kwargs):
        acknowledgement = get_object_or_404(DeveloperAcknowledgement.objects, developer=self.request.user)
        kwargs["agreement_text"] = AGREEMENT_TEXTS[acknowledgement.agreement_code][get_language()]
        return super().get_context_data(**kwargs)
