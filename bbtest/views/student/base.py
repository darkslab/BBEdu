from django.views.generic import TemplateView
from bbtest.auth.mixins import StudentLoginRequiredMixin


class DashboardView(StudentLoginRequiredMixin, TemplateView):
    template_name = "student/dashboard.html"
