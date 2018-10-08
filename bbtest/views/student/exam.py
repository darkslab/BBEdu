from django.utils.timezone import now
from django.db.transaction import atomic
from django.db.models import F
from django.core.cache import cache
from json import loads
from ool import ConcurrentUpdate
from datetime import timedelta
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin, inject_questions_and_report_into_started_response
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from .mixins import CurrentQuizSetRequiredMixin
from bbtest.http import TightJsonResponse
from bbtest.models import Test
from bbtest.forms.exam import ExamReportForm
from bbtest.texts import test_instructions, test_instructions_title, inject_texts_into_response


class ExamView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/exam.html"

    def get_context_data(self, **kwargs):
        kwargs["test_domain"] = self.quiz_set().test_domain
        return super().get_context_data(**kwargs)


class ExamMixin:
    def queued_response(self):
        return {
            "success": True,
            "status": "queued",
            "section": test_instructions_title(self.current_quiz().test),
            "instructions": test_instructions(self.current_quiz().test),
        }

    def started_response(self, now_at):
        response = {
            "success": True,
            "status": "started",
            "seconds": (self.current_quiz().due_at - now_at).seconds,
        }
        inject_questions_and_report_into_started_response(response, self.current_quiz().test)
        inject_texts_into_response(response, self.current_quiz().test)
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
            except ConcurrentUpdate:
                pass
        return TightJsonResponse({
            "success": False,
        })


class ExamStartView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, ExamMixin, View):
    def post(self, request, *args, **kwargs):
        now_at = now()
        if self.current_status(now_at) != "queued":
            return TightJsonResponse({
                "success": False,
            })

        try:
            with atomic(savepoint=False):
                self.quiz_set().save()
                self.current_quiz().started_at = now_at
                self.current_quiz().due_at = now_at + timedelta(seconds=self.current_quiz().test.section.duration)
                self.current_quiz().save()
        except ConcurrentUpdate:
            return TightJsonResponse({
                "success": False,
            })

        return TightJsonResponse(self.started_response(now_at))


class ExamSkipView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, ExamMixin, View):
    def post(self, request, *args, **kwargs):
        now_at = now()
        if self.current_status(now_at) != "queued":
            return TightJsonResponse({
                "success": False,
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
        except ConcurrentUpdate:
            pass
        return TightJsonResponse({
            "success": False,
        })


class ExamEndView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, ExamMixin, View):
    def post(self, request, *args, **kwargs):
        now_at = now()
        if self.current_status(now_at) not in ("started", "expired"):
            return TightJsonResponse({
                "success": False,
            })

        try:
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
        })


class ExamReportView(StudentPermissionRequiredMixin, CurrentQuizSetRequiredMixin, ExamMixin, View):
    def post(self, request, *args, **kwargs):
        now_at = now()
        if self.current_status(now_at) != "started":
            return TightJsonResponse({
                "success": False,
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
        except (ConcurrentUpdate, ValueError):
            pass
        response.update({
            "success": False,
        })
        return TightJsonResponse(response)
