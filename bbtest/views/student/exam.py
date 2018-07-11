from django.utils.translation import ugettext as _
from django.utils.timezone import now
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin, inject_questions_and_report_into_started_response
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from .mixins import CurrentQuizSetRequiredMixin
from bbtest.http import TightJsonResponse


class ExamView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/exam.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domain"] = self.quiz_set().test_domain
        return super().get_context_data(**kwargs)


def exam_response(quiz_set):
    response = {}
    current_quiz = None
    for quiz in quiz_set.quizzes.all():
        if quiz.is_finished:
            continue
        current_quiz = quiz
        break

    now_at = now()
    if current_quiz is None:
        response["status"] = "concluded"
    elif current_quiz.started_at is None:
        response["status"] = "queued"
        response["section"] = _(current_quiz.test.section.name)
        # DARK_TODO  implement this!
        response["instructions"] = "Ut at egestas nunc. Ut suscipit luctus mattis. Maecenas quis magna ut arcu ullamcorper ornare. Praesent sollicitudin sodales elit ut pulvinar. Sed vehicula felis a nulla hendrerit hendrerit. Pellentesque egestas sit amet nisl a condimentum. Donec cursus varius sem. Nulla tincidunt lorem eget magna dictum finibus. Integer nec diam gravida tellus convallis posuere ac nec dui. Cras pellentesque purus lectus, id ullamcorper neque varius vitae. Proin tincidunt leo nec ipsum tincidunt efficitur. Praesent facilisis lacinia ipsum quis rutrum."
    elif now_at > current_quiz.due_at:
        response["status"] = "expired"
    else:
        response["status"] = "started"
        response["seconds"] = (current_quiz.due_at - now_at).seconds
        inject_questions_and_report_into_started_response(response, current_quiz.test)
        if current_quiz.report is None:
            for data in response["report"]["answers"]:
                data["answer"] = None
        else:
            response["report"] = current_quiz.report

    return response


class ExamContinueView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = exam_response(self.quiz_set())
        response.update({
            "success": True,
        })
        return TightJsonResponse(response)


class ExamStartView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        response = exam_response(self.quiz_set())
        response.update({
            "success": True,
        })
        return TightJsonResponse(response)


class ExamSkipView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        response = exam_response(self.quiz_set())
        response.update({
            "success": True,
        })
        return TightJsonResponse(response)


class ExamEndView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        response = exam_response(self.quiz_set())
        response.update({
            "success": True,
        })
        return TightJsonResponse(response)


class ExamReportView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        response = exam_response(self.quiz_set())
        response.update({
            "success": True,
        })
        return TightJsonResponse(response)
