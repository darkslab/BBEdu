import csv
import datetime
import uuid

# from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages import error, success, warning
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now
from django.utils.translation import pgettext


from bbtest.auth.mixins import (
    AdminPermissionRequiredMixin,
    DeveloperPermissionRequiredMixin,
    SuperPermissionRequiredMixin,
)
from bbtest.forms.super import ExportDataForm
from bbtest.http import TightJsonResponse
from bbtest.models import Quiz, TestSection
from bbtest.views.common import PaginationMixin, UserContextMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin
from bbtest.views.generic import TemplateView, View


class ExportDataView(AdminPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "super/export_data.html"

    def get_context_data(self, **kwargs):
        kwargs["active_nav_item"] = "export_data"

        kwargs["export_data_form"] = ExportDataForm()

        return super().get_context_data(**kwargs)



class ExportDataFormView(AdminPermissionRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        print("TODO: TestSection.objects.get(name=section_name).question_count is probably depreciated")
        form = ExportDataForm(data=request.POST)
        valid = form.is_valid()    # is_valid should be called before form.cleaned_data could be accessed
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"] 

        if valid and end_date >= start_date:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'
            writer = csv.writer(response)

            # get all quizes
            table_tests_all = self.get_quizes_in_range(start_date, end_date)  # [student][(quiz.language, test_name)]

            test_names_sorted = sorted(test_names_and_count.keys())  # fix sort order
            # test_names_sorted = ["Critical Thinking", "Quantitative", "Spatial Thinking", "English Language"]  # hardcode order and subjects
            
            # test_names_sorted = [("ru", "Critical Thinking"), ("ru", "Quantitative"), ("ru", "Spatial Thinking"), 
            #                      ("kk", "Critical Thinking"), ("kk", "Quantitative"), ("kk", "Spatial Thinking"), 
            #                      ("xx", "English Language")]  # hardcode order and subjects
            test_names_and_count = {section_name: TestSection.objects.get(name=section_name).question_count for section_name in test_names_sorted}

            # create table header
            header = self.create_table_header(test_names_sorted, test_names_and_count)
            # print(positions) , positions 
            
            writer.writerow(header)
            # fill table
            self.write_response_csv(writer, table_tests_all, test_names_sorted, test_names_and_count)

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

    def get_quizes_in_range(self, start_date, end_date):
        quizes = Quiz.objects.filter(
                                    Q(started_at__lte=end_date) & Q(started_at__gte=start_date)
                                ).order_by("-started_at") #.prefetch_related("user_permissions__content_type")
        table_tests_all = {}
        for quiz in quizes:
            student = (quiz.quiz_set.student.username, quiz.test.language)
            # student_email = quiz.quiz_set.student.email
            started = quiz.started_at
            test_name = quiz.test.section.name
            score = quiz.score()
            max_score = quiz.test.max_score()
            
            # print(student, ended, test_name, score, max_score)
            if student[1] != "xx":
                table_tests_all[student] = table_tests_all.get(student, {})
                table_tests_all[student][test_name]  = [started, score, max_score] + quiz.get_student_answers()
            else:
                for lang in ["ru", "kk"]:
                    student = (student[0], lang)
                    table_tests_all[student] = table_tests_all.get(student, {})
                    table_tests_all[student][test_name]  = [started, score, max_score] + quiz.get_student_answers()
        
        students_all = {s[0] for s in table_tests_all.keys()}
        for sname in students_all:
            count_ru = len(table_tests_all.get((sname, "ru"), {}).keys())
            count_kk = len(table_tests_all.get((sname, "kk"), {}).keys())
            if count_ru == count_kk and count_ru == 1 and "English Language" in table_tests_all.get((sname, "ru"), {}).keys() and "English Language" in table_tests_all.get((sname, "kk"), {}).keys():
                table_tests_all.pop((sname, "kk"), None)
            elif count_ru > count_kk:
                table_tests_all.pop((sname, "kk"), None)
            elif count_ru < count_kk:
                table_tests_all.pop((sname, "ru"), None)
        return table_tests_all

    def create_table_header(self, test_names_sorted, test_names_and_count):
        header = ["student", "lang"]
        # positions = {name: None for name in test_names_sorted}
        for k in test_names_sorted:
            # positions[k] = len(header) 
            header += ["{}_started".format(k), "{}_score".format(k), "{}_max_score".format(k)] + ["{}_{:03}".format(k, i+1) for i in range(test_names_and_count[k])]
            # positions[k]["end"] = len(header)

        
        header.append("Total_score")
        return header #, positions

    def write_response_csv(self, writer, table_tests_all, test_names_sorted, test_names_and_count):
        # table = []
        for student, tests in table_tests_all.items():  # [(quiz.language, student)][test_name]
            table_row = [student[0], student[1]]   # name, lang
            total_score = 0
            for test_name in test_names_sorted:
                test_report = tests.get(test_name, None)
                if test_report is not None:     # if student attended this test
                    table_row += test_report
                    total_score += test_report[1]  # [1] -> score
                else:                           # if not attended generate empty 
                    table_row += [None for _ in range(test_names_and_count[test_name]+3)]
            writer.writerow(table_row + [total_score])
            # table.append(table_row + [total_score])

        # table = sorted(table, key=lambda tup: (tup[0],tup[1]) )
        # for row in table:
        #     writer.writerow(row)
