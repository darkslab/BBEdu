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
from django.db.models import Q

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

        # print(start_date, end_date)

        if form.is_valid() and end_date >= start_date:

            quizes = Quiz.objects.filter(
                                        Q(ended_at__lte=end_date) & Q(ended_at__gte=start_date)
                                    ).order_by("-ended_at") #.prefetch_related("user_permissions__content_type")
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'
            writer = csv.writer(response)

            answer_report_columns = [ "s_{}".format(i+1) for i in range(60)]  #+ [ "c_{}".format(i+1) for i in range(60)] 
            # writer.writerow(["student", "student_email", "ended", "test_name", "score", "max_score"] + answer_report_columns)
            table_tests_all = {}
            test_names_and_count = {}
            for quiz in quizes:
                student = quiz.quiz_set.student.username
                # student_email = quiz.quiz_set.student.email
                ended = quiz.ended_at
                test_name = quiz.test.section.name
                score = quiz.score()
                max_score = quiz.test.max_score()
                
                # print(student, ended, test_name, score, max_score)
                
                if test_names_and_count.get(test_name, None) is None: test_names_and_count[test_name] = quiz.test.section.question_count
                table_tests_all[student] = table_tests_all.get(student, {})
                table_tests_all[student][test_name]  = [ended, score, max_score] + quiz.get_student_answers()

            test_names_sorted = sorted(test_names_and_count.keys())  # fix sort order

            # create table header
            header = ["student"]
            for k in test_names_sorted:
                header += ["{}_ended".format(k), "{}_score".format(k), "{}_max_score".format(k)] + ["{}_{:03}".format(k, i+1) for i in range(test_names_and_count[k])]
            writer.writerow(header)
            # fill table
            for student, tests in table_tests_all.items():
                table_row = [student]
                for test in test_names_sorted:
                    test_report = tests.get(test, None)
                    if test_report is not None:
                        table_row += test_report
                writer.writerow(table_row)

            success(request, "Export from {} to {}.".format(start_date, end_date))
            # print("arra", test_names_and_count, header, table_tests_all)
            # return redirect("bbtest:super_export_data")
            return response
            # return HttpResponseRedirect(self.request.path_info)
        else:
            error(request, "Errors %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))

        return redirect("bbtest:super_export_data")

        # data = {
        #     "success": True,
        # }
        # return TightJsonResponse(data)


