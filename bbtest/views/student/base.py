from bbtest.auth.mixins import StudentLoginRequiredMixin
from bbtest.views.generic import TemplateView


class DashboardView(StudentLoginRequiredMixin, TemplateView):
    template_name = "student/dashboard.html"
