from bbtest.views.generic import TemplateView, UserContextMixin
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from .mixins import CurrentQuizSetRequiredMixin


class ExamView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/exam.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domain"] = self.quiz_set().test_domain
        return super().get_context_data(**kwargs)
