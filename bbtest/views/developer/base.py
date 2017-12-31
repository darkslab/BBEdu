from django.views.generic import TemplateView
from bbtest.auth.mixins import DeveloperLoginRequiredMixin


class DashboardView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/dashboard.html"
