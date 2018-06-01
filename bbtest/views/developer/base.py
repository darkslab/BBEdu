from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin
from bbtest.views.generic import TemplateView, UserContextMixin


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
