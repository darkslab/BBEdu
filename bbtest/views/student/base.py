from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.views.generic import TemplateView


class DashboardView(StudentPermissionRequiredMixin, TemplateView):
    template_name = "student/dashboard.html"
