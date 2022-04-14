from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.messages import warning, success, error
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.utils.translation import pgettext
from django.db.models import Q
from django.utils.timezone import now
from django.http import Http404
from django.http import HttpResponse
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.forms.super import ExportDataForm
from bbtest.http import TightJsonResponse
import uuid
import csv
from bbtest.models import User, quiz
from bbtest.models import Quiz
import datetime

from bbtest.auth.mixins import DeveloperPermissionRequiredMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin


class ExportDataView(DeveloperPermissionRequiredMixin, DeveloperAcknowledgementRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "super/export_data.html"

    def get_context_data(self, **kwargs):

        kwargs["export_data_form"] = ExportDataForm()

        return super().get_context_data(**kwargs)



class ExportDataFormView(DeveloperPermissionRequiredMixin, DeveloperAcknowledgementRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = ExportDataForm(data=request.POST)
        valid = form.is_valid()
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"] 

        print(start_date, end_date)

        if form.is_valid() and end_date > start_date:
            quizes = Quiz.objects.filter(ended_at__lte=end_date).order_by("-ended_at") #.prefetch_related("user_permissions__content_type")
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'
            writer = csv.writer(response)
            writer.writerow(["student", "student_email", "ended", "test_name", "score", "max_score"])
            for quiz in quizes:
                student = quiz.quiz_set.student.username
                student_email = quiz.quiz_set.student.email
                ended = quiz.ended_at
                test_name = quiz.test.section.name
                score = quiz.score()
                max_score = quiz.test.max_score()
                print(student, student_email, ended, test_name, score, max_score)


                
                writer.writerow([student, student_email, ended, test_name, score, max_score])

            success(request, "Export from {} to {}.".format(start_date, end_date))
            # return redirect("bbtest:super_export_data", response)
            return response
            # return HttpResponseRedirect(self.request.path_info)
        else:
            error(request, "Errors %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))

        return redirect("bbtest:super_export_data")

        # data = {
        #     "success": True,
        # }
        # return TightJsonResponse(data)

    def proftest_score(self):
        def dif_None(a, b):
            try:
                return a - b
            except TypeError:
                return None
        answer_a_offsets = self.get_a_offset()
        user_answers = self.get_answers_ids()
        normalized_answers = [dif_None(ans, a_offset) for ans, a_offset in zip(user_answers, answer_a_offsets)]

    def get_a_offset(self):
        questions = self.test.questions.all()
        a_id = []
        for q in questions:
            a_id.append(min([option["id"] for option in q.meta_data['choices']]))
        return a_id
    
    def get_answers_ids(self):
        if self.report is not None:
            ret = []
            for ans_meta in self.report["answers"]:
                try:
                    ret.append(ans_meta["answer"]["correct_id"])
                except TypeError:
                    ret.append(None)
            return ret
        else:
            return [None for _ in range(self.test.section.question_count)]

