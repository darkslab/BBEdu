from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin
from bbtest.auth.mixins import StudentPermissionRequiredMixin


class ResultsView(StudentPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/results/base.html"
