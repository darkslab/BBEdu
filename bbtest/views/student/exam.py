from datetime import timedelta
from json import loads

from django.contrib.messages import error, success, warning
from django.core.cache import cache
from django.db.models import F
from django.db.transaction import atomic
from django.utils.timezone import now
from django.utils.translation import pgettext, pgettext_lazy
from ool import ConcurrentUpdate

from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.forms.exam import ExamReportForm
from bbtest.http import TightJsonResponse
from bbtest.models import Quiz, Test
from bbtest.texts import (
    inject_texts_into_response,
    test_instructions,
    test_instructions_title,
    test_video,
)
from bbtest.utils.json import tight_dumps
from bbtest.views.common import (
    UserContextMixin,
    inject_questions_and_report_into_started_response,
)
from bbtest.views.generic import TemplateView, View

from .mixins import CurrentQuizSetRequiredMixin


class ExamView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "test/exam.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domain"] = self.quiz_set().test_domain
        kwargs["is_current"] = self.quiz_set().is_current

        current_test = self.current_quiz().test
        question_list = current_test.questions.values("id", "has_calculator", "has_periodic_table").order_by("testtoquestionrelation")

        kwargs["has_periodic_table"] = tight_dumps([q["has_periodic_table"] for q in question_list])
        kwargs["has_calculator"] = tight_dumps([q["has_calculator"] for q in question_list])

        return super().get_context_data(**kwargs)


class ExamMixin:
    def queued_response(self):
        data = {
            "success": True,
            "status": "queued",
            "section": test_instructions_title(self.current_quiz().test),
            "instructions": test_instructions(self.current_quiz().test),
            "username": self.current_quiz().quiz_set.student.username,
        }
        # if test_video(self.current_quiz().test):
        #     data["video"] = test_video(self.current_quiz().test)
        return data

    def started_response(self, now_at, reload=False, alert=None):
        current_test = self.current_quiz().test
        question_list = current_test.questions.values("id", "has_calculator", "has_periodic_table").order_by("testtoquestionrelation")

        response = {
            "success": True,
            "status": "started",
            "section": test_instructions_title(current_test),
            "seconds": (self.current_quiz().due_at - now_at).seconds,
            "reload": reload,
            "alert": alert,
            "username": self.current_quiz().quiz_set.student.username,
            "has_periodic_table": [q["has_periodic_table"] for q in question_list],
            "has_calculator": [q["has_calculator"] for q in question_list],
        }
        inject_questions_and_report_into_started_response(response, current_test)
        inject_texts_into_response(response, current_test)
        if self.current_quiz().report is None:
            for data in response["report"]["answers"]:
                data["answer"] = None
        else:
            response["report"] = self.current_quiz().report
        return response

    def expired_response(self):
        return {
            "success": True,
            "status": "expired",
        }

    def concluded_response(self):
        return {
            "success": True,
            "status": "concluded",
        }

    def current_status(self, now_at):
        if self.current_quiz() is None:
            return "concluded"
        elif self.current_quiz().started_at is None:
            return "queued"
        elif now_at > self.current_quiz().due_at:
            return "expired"
        else:
            return "started"


class ExamContinueView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, ExamMixin, View):
    def get(self, request, *args, **kwargs):
        now_at = now()
        if self.current_status(now_at) == "queued":
            return TightJsonResponse(self.queued_response())
        elif self.current_status(now_at) == "started":
            return TightJsonResponse(self.started_response(now_at))
        elif self.current_status(now_at) == "expired":
            return TightJsonResponse(self.expired_response())
        elif self.current_status(now_at) == "concluded":
            try:
                self.quiz_set().is_current = None
                self.quiz_set().save()
                return TightJsonResponse(self.concluded_response())
            except ConcurrentUpdate as e:
                pass
                return TightJsonResponse({
                    "success": False,
                    "error_msg": f'ExamContinueView.get: ConcurrentUpdate failed: {e}',
                })
        return TightJsonResponse({
            "success": False,
            "error_msg": f'ExamContinueView.get: Should not be reached',
        })


class ExamStartView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, ExamMixin, View):
    def post(self, request, *args, **kwargs):
        now_at = now()
        if self.current_status(now_at) != "queued":
            return TightJsonResponse({
                "success": False,
                "error_msg": 'ExamStartView.post: self.current_status(now_at) != "queued"',
            })

        try:
            with atomic(savepoint=False):
                self.quiz_set().save()
                self.current_quiz().started_at = now_at
                self.current_quiz().due_at = now_at + timedelta(seconds=self.current_quiz().test.duration)
                self.current_quiz().save()
        except ConcurrentUpdate as e:
            return TightJsonResponse({
                "success": False,
                "error_msg": f"ExamStartView.post: ConcurrentUpdate failed {e}",
            })

        return TightJsonResponse(self.started_response(now_at))


class ExamSkipView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, ExamMixin, View):
    def post(self, request, *args, **kwargs):
        now_at = now()
        if self.current_status(now_at) != "queued":
            return TightJsonResponse({
                "success": False,
                "error_msg": 'ExamSkipView.post: self.current_status(now_at) != "queued"',
            })

        try:
            with atomic(savepoint=False):
                self.quiz_set().save()
                self.current_quiz().is_finished = True
                self.current_quiz().save()

            cache.delete("test-progress-%s-%s" % (self.quiz_set().student_id, self.current_quiz().test.section_id))

            self.reset_current_quiz()
            if self.current_status(now_at) == "queued":
                return TightJsonResponse(self.queued_response())
            elif self.current_status(now_at) == "concluded":
                self.quiz_set().is_current = None
                self.quiz_set().save()
                return TightJsonResponse(self.concluded_response())
        except ConcurrentUpdate as e:
            return TightJsonResponse({
                "success": False,
                "error_msg": f"ExamSkipView.post: ConcurrentUpdate failed {e}",
            })
        
        return TightJsonResponse({
                "success": False,
                "error_msg": f'ExamSkipView.post: self.current_status(now_at) not in ("queued", "concluded")',
            })


class ExamEndView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, ExamMixin, View):
    def post(self, request, *args, **kwargs):
        now_at = now()
        if self.current_status(now_at) not in ("started", "expired"):
            return TightJsonResponse({
                "success": False,
                "error_msg": f'ExamEndView.post: self.current_status(now_at) not in ("started", "expired")',
            })

        try:
            # if now_at < self.current_quiz().due_at:
            #     answer_list = self.current_quiz().get_answers_ids()
            #     if None in answer_list:
            #         now_at = now()
            #         indices_of_none = [str(index + 1) for index, value in enumerate(answer_list) if value is None]
            #         warning(request, pgettext("Student finish exam", "Вы не ответили на вопрос: ") + ", ".join(indices_of_none) )
            #         return TightJsonResponse(self.started_response(now_at, reload=True))

            # if now_at < self.current_quiz().started_at + timedelta(minutes=3):
            #     alert_msg = "Должно пройти минимум 3 минуты."
            #     # error(request, pgettext("Student finish exam", "Должно пройти минимум 3 минуты."))
            #     return TightJsonResponse(self.started_response(now_at, reload=False, alert=alert_msg))

            if now_at < self.current_quiz().due_at:
                answer_list = self.current_quiz().get_answers_ids()
                count = sum([1 for value in answer_list if value is not None])
                if count < 3:
                    alert_msg = "Ответьте минимум на 3 вопроса."
                    # error(request, pgettext("Student finish exam", "Ответьте минимум на 3 вопроса.") )
                    return TightJsonResponse(self.started_response(now_at, reload=False, alert=alert_msg))

            with atomic(savepoint=False):
                self.quiz_set().save()
                self.current_quiz().is_finished = True
                if self.current_status(now_at) == "started":
                    self.current_quiz().ended_at = now_at
                self.current_quiz().save()

                Test.objects.filter(pk=self.current_quiz().test.pk).update(completed_count=(F("completed_count") + 1))

            cache.delete("test-progress-%s-%s" % (self.quiz_set().student_id, self.current_quiz().test.section_id))
            cache.delete("test-average-score-%s" % self.current_quiz().test.section_id)

            self.reset_current_quiz()
            if self.current_status(now_at) == "queued":
                return TightJsonResponse(self.queued_response())
            elif self.current_status(now_at) == "concluded":
                self.quiz_set().is_current = None
                self.quiz_set().save()
                return TightJsonResponse(self.concluded_response())
        except ConcurrentUpdate:
            pass
        return TightJsonResponse({
            "success": False,
            "error_msg": f'ExamEndView.post: missed all conditions',
        })


class ExamReportView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, ExamMixin, View):
    def post(self, request, *args, **kwargs):
        now_at = now()
        if self.current_status(now_at) != "started":
            return TightJsonResponse({
                "success": False,
                "error_msg": 'ExamReportView.post: self.current_status(now_at) != "started"',
            })

        response = {}
        try:
            with atomic(savepoint=False):
                self.quiz_set().save()
                form = ExamReportForm(self.current_quiz().test, data=request.POST, instance=self.current_quiz())
                if not form.is_valid():
                    response.update({
                        "errors": loads(form.errors.as_json()),
                    })
                    raise ValueError("Incorrect report")
                form.save()
            return TightJsonResponse({
                "success": True,
            })
        except ConcurrentUpdate as e:
            response.update({
                "success": False,
                "error_msg": f"ExamReportView.post: ConcurrentUpdate error. {e}\n" + tight_dumps(response.get("errors", {})),
            })
        except ValueError as e:
            response.update({
                "success": False,
                "error_msg": f"ExamReportView.post: ValueError failed. {e}\n" + tight_dumps(response.get("errors", {})),
            })
        
        return TightJsonResponse(response)
