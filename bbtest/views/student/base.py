from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin


class DashboardView(StudentPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/dashboard.html"
