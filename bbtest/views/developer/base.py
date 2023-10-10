from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import get_language
from django.shortcuts import get_object_or_404
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, ExpertPermissionRequiredMixin, StaffPermissionRequiredMixin
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.texts import DEVELOPER_AGREEMENT_TEXTS
from bbtest.models import DeveloperAcknowledgement, Test
from .mixins import DeveloperAcknowledgementRequiredMixin


class DashboardView(StaffPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "developer/dashboard.html"

    def get_context_data(self, **kwargs):
        paginator = Paginator(
            self.request.user.tests.select_related("section__domain").order_by("-created_at"),
            25,
        )
        try:
            kwargs["tests"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["tests"] = paginator.page(1)
        except EmptyPage:
            kwargs["tests"] = paginator.page(paginator.num_pages)
        paginator.page_indexes = self.page_indexes(kwargs["tests"], 5)

        for test in kwargs["tests"]:
            test.display_language = ""
            if test.language != Test.LANGUAGE_XX:
                test.display_language = next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == test.language)

        return super().get_context_data(**kwargs)


class OfferView(DeveloperPermissionRequiredMixin, DeveloperAcknowledgementRequiredMixin, UserContextMixin, TemplateView):
    template_name = "developer/offer.html"

    def get_context_data(self, **kwargs):
        acknowledgement = get_object_or_404(DeveloperAcknowledgement.objects, developer=self.request.user)
        kwargs["acknowledgement"] = acknowledgement
        kwargs["agreement_text"] = DEVELOPER_AGREEMENT_TEXTS[acknowledgement.agreement_code][get_language()]
        return super().get_context_data(**kwargs)
