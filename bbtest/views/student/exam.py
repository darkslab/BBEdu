from bbtest.views.generic import TemplateView, View, UserContextMixin
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from .mixins import CurrentQuizSetRequiredMixin
from bbtest.http import TightJsonResponse


class ExamView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/exam.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domain"] = self.quiz_set().test_domain
        return super().get_context_data(**kwargs)


class ExamContinueView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    # DARK_TODO  implement this!

    def get(self, request, *args, **kwargs):
        return TightJsonResponse({
            "success": True,
            "status": "concluded",
        })

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
