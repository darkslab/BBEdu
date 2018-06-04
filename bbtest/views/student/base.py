from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.views.generic import TemplateView, UserContextMixin


class DashboardView(StudentPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/dashboard.html"
