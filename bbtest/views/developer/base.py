from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from bbtest.auth.mixins import DeveloperLoginRequiredMixin


class DashboardView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/dashboard.html"


class NewTestView(DeveloperLoginRequiredMixin, TemplateView):
    # DARK_TODO  finish this page
    template_name = "developer/dashboard.html"


class ShowTestView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/show_test.html"

    def get_context_data(self, **kwargs):
        kwargs["test"] = get_object_or_404(self.request.user.tests, code=kwargs.get("code"))
        kwargs["section_name"] = _(kwargs["test"].section.name)
        return super().get_context_data(**kwargs)
