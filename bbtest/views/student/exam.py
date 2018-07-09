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
    def get(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        pass


class ExamStartView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        pass


class ExamSkipView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        pass


class ExamEndView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        pass


class ExamReportView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        pass
