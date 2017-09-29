from django.views.generic import TemplateView
from bbtest.auth.mixins import DeveloperLoginRequiredMixin


class DeveloperDashboardView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/dashboard.html"
