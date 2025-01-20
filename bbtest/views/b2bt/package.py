from __future__ import annotations

import io
import json
import re
import uuid
from datetime import datetime, timedelta
from random import randint
from typing import TYPE_CHECKING, List

import xlsxwriter
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages import error, success, warning
from django.core.exceptions import ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.transaction import atomic
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now
from django.utils.translation import pgettext, get_language
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View

from bbtest.auth.mixins import (
    CreateStudentRequiredMixin,
    PermissionRequiredMixinFactory,
)
from bbtest.auth.models import User
from bbtest.forms.super import (
    Buy_B2BTeacher_PackageForm,
    CreateStudentGroupForm,
    ManagePackageStudentsForm,
    ManagePackageTestForm,
)
from bbtest.http import TightJsonResponse
from bbtest.jobs.create_student_in_package import (
    activate_package,
    hash_users_passwords,
    populate_package_student_group,
)
from bbtest.models.accounting import Account, BalanceAccount
from bbtest.models.quiz import Quiz, QuizSet
from bbtest.models.test import (
    StudentGroup,
    StudentProfile,
    Test,
    TestDomain,
    TestPackage,
    TestPackageRelation,
    TestPackageRusKazPair,
    TestPackageRusKazQuiz,
    TestSection,
    UserTestPackageProfile,
)
from bbtest.views.common import PaginationMixin, UserContextMixin
from bbtest.views.generic import TemplateView, View

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.db.models import QuerySet

    from bbtest.auth.models import User


User_model = get_user_model()

def col_to_letter(col):
    """Convert a column number (1-based) to a letter (A1-style)."""
    result = ""
    while col > 0:
        col, remainder = divmod(col - 1, 26)
        result = chr(65 + remainder) + result
    return result

def row_col_to_a1(row, col):
    """Convert 1-based row and column numbers to A1-style notation."""
    col_letter = col_to_letter(col + 1)
    return f"{col_letter}{row + 1}"

class BuildPackagesView(
    PermissionRequiredMixinFactory(["B2BTeacher"]), UserContextMixin, TemplateView, PaginationMixin
):
    template_name = "b2bt/package_table.html"

    def get_context_data(self, **kwargs):
        kwargs["active_nav_item"] = "manage_students"

        package_pair_quiz_set: TestPackageRusKazQuiz = TestPackageRusKazQuiz.objects.filter(
            user = self.request.user
        ).order_by(
            "-created_at"
        ).prefetch_related("TestPackagePair")
        

        paginator = Paginator(package_pair_quiz_set, 25)
        try:
            kwargs["package_pair_quiz_set"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["package_pair_quiz_set"] = paginator.page(1)
        except EmptyPage:
            kwargs["package_pair_quiz_set"] = paginator.page(paginator.num_pages)
        paginator.page_indexes = self.page_indexes(kwargs["package_pair_quiz_set"], 5)


        kwargs["add_package_pair_form"] = Buy_B2BTeacher_PackageForm()

        return super().get_context_data(**kwargs)


class BuildPackagesListView(
    PermissionRequiredMixinFactory(["B2BTeacher"]), UserContextMixin, TemplateView
):
    template_name = "b2bt/package_variant_list.html"

    def get_context_data(self, **kwargs):
        kwargs["active_nav_item"] = "manage_variants"

        
        package_pair_list: QuerySet[TestPackageRusKazPair] = TestPackageRusKazPair.objects.filter(
            test_package_pair_quiz_sets__user = self.request.user
        ).distinct().order_by(
            "id"
        ).all()

        kwargs["package_pair_list"] = package_pair_list
        
        print(package_pair_list)

        for test_package_pair_obj in package_pair_list:

            package_ru = test_package_pair_obj.test_package_ru
            package_kz = test_package_pair_obj.test_package_kz


            tests_ru: QuerySet[Test] = package_ru.tests.order_by("section__order").all()
            tests_kz: QuerySet[Test] = package_kz.tests.order_by("section__order").all()


            # test_package_pair_obj.tests_list = [{"test": ts, "lang": "rus"} for ts in tests_ru]
            # test_package_pair_obj.tests_list.extend([{"test": ts, "lang": "kaz"} for ts in tests_kz])
            test_package_pair_obj.tests_list = [[ts, "rus"] for ts in tests_ru]
            test_package_pair_obj.tests_list.extend([[ts, "kaz"] for ts in tests_kz])


        return super().get_context_data(**kwargs)


class BuildPackageView(
    PermissionRequiredMixinFactory(["B2BTeacher"]),
    UserContextMixin,
    PaginationMixin,
    TemplateResponseMixin,
    ContextMixin,
    View,
):
    template_name = "b2bt/manage_package.html"
    # form_class = ManagePackageTestForm

    def get(self, request: WSGIRequest, package_pair_quiz_id, *args, **kwargs):
        # print("BuildPackageView", args, kwargs, self.get_context_data())
        # print("BuildPackageView", self.request)
        # print("BuildPackageView", kwargs, code)
        kwargs["active_nav_item"] = "manage_students"

        package_pair_quiz_obj: TestPackageRusKazQuiz = get_object_or_404(TestPackageRusKazQuiz.objects, pk=package_pair_quiz_id)

        if not package_pair_quiz_obj.payed:
            return redirect("bbtest:b2bt_build_packages_buy_kaspi", package_pair_quiz_obj.pk)

        kwargs["package_pair_quiz_obj"] = package_pair_quiz_obj

        kwargs["package_ru"] = package_pair_quiz_obj.TestPackagePair.test_package_ru
        kwargs["package_kz"] = package_pair_quiz_obj.TestPackagePair.test_package_kz

        kwargs["tests_ru"] = kwargs["package_ru"].tests.order_by("section__order").all()
        kwargs["tests_kz"] = kwargs["package_kz"].tests.order_by("section__order").all()

        # kwargs["student_group_list"] = package_pair_quiz_obj.student_groups.all()

        kwargs["student_table"] = package_pair_quiz_obj.student_table

        return self.render_to_response(super().get_context_data(**kwargs))
    
    def post(self, request: WSGIRequest, package_pair_quiz_id, *args, **kwargs):
        print(request.POST.dict())
        tableData = request.POST.get("tableData", [])
        print(tableData)
        
        if not tableData:
            return TightJsonResponse({"success": False})
        
        package_pair_quiz_obj: TestPackageRusKazQuiz = get_object_or_404(TestPackageRusKazQuiz.objects, pk=package_pair_quiz_id)
        package_pair_quiz_obj.student_table = json.loads(tableData)
        package_pair_quiz_obj.save()

        response = {
            "success": True,
        }
        return TightJsonResponse(response)


class AddPackagePairFormView(PermissionRequiredMixinFactory(["B2BTeacher"]), View):
    def post(self, request: WSGIRequest, *args, **kwargs):
        form = Buy_B2BTeacher_PackageForm(data=request.POST)
        print("AddPackagePairFormView", form.is_valid())
        if not form.is_valid():
            error(
                request,
                "Could not create TestPackageRusKazQuizSet! %s"
                % " ".join([" ".join(errors) for key, errors in form.errors.items()]),
            )
            return redirect("bbtest:b2bt_build_packages")
        
        test_package_pair: TestPackageRusKazPair = form.cleaned_data["test_package_pair"]
        # comment = form.cleaned_data["comment"]
        number_of_students = form.cleaned_data["number_of_students"]

        package_quiz_obj = TestPackageRusKazQuiz.objects.create(
            user=request.user,
            TestPackagePair=test_package_pair,
            number_of_students=number_of_students,
            student_table = [],
        )

        # create_package_pair_quiz_users.delay(package_quiz_obj)
        initialized_users = self.create_package_pair_quiz_users_helper(package_quiz_obj)
        # hashing passwords takes a lot if time, there lets put into separete job queue
        hash_users_passwords.delay(initialized_users)

        # print("AddPackagePairFormView", package_quiz_obj)

        return redirect("bbtest:b2bt_build_package_pair_quiz", package_quiz_obj.id)
    

    def create_package_pair_quiz_users_helper(self, package_quiz_obj: TestPackageRusKazQuiz):
        student_table = [] # package_quiz_obj.student_table
        number_of_students = package_quiz_obj.number_of_students 
        
        
        bulk_create_user: List[User] = []
        for i in range(int(number_of_students)):
            temp_username = uuid.uuid4().hex
            temp_email = f"{temp_username}@b2b.bbtest.kz"
            passwrd = "{:05}".format(randint(10000, 99999))
            temp_user = User_model(
                    username=temp_username,
                    email=temp_email,
                    password=passwrd,
                    is_active=False,
                    first_name = f"Имя {i+1}",
                    last_name = f"Фамилия {i+1}",
                )
            bulk_create_user.append(temp_user)
            student_table.append(["user.username", f"Имя {i+1}", f"Фамилия {i+1}", "rus", passwrd])

        content_type = ContentType.objects.get_for_model(User_model)
        permissions = [Permission.objects.get(codename="student", content_type=content_type)]

        with atomic(savepoint=False):
            created_users: List[User] = User_model.objects.bulk_create(bulk_create_user)

        # balance account is not created in bulk creation because post_save is not triggered
        balance_acount_list = []
        initialized_users: List[User] = []

        for i, std_user in enumerate(created_users):
            user = User_model.objects.get(username = std_user.username)
            user.user_permissions.set(permissions)
            user.username = f"std{user.pk}"  # "std" + F("id") 
            # bulk_refetch_users.append(user)
            user.save()
            student_table[i][0] = f"std{user.pk}"

            balance_obj = BalanceAccount(
                name=user.balance_account_name(), 
                type=Account.TYPE_EQUITY, 
                is_contra=False
            )

            initialized_users.append(user)
            balance_acount_list.append(balance_obj)

            StudentProfile.objects.create(
                student = user,
                teacher = package_quiz_obj.user,
                games = "bird",
            )

        # BalanceAccount.objects.create_equity_account(kwargs["instance"].balance_account_name())
        with atomic(savepoint=False):
            account_list: List[BalanceAccount] = BalanceAccount.objects.bulk_create(balance_acount_list)
        
        package_quiz_obj.student_table = student_table
        package_quiz_obj.save()

        return initialized_users


    # def create_students(self, password, is_active = False):
        # temp_username = uuid.uuid4().hex
        # temp_email = f"{temp_username}@b2b.bbtest.kz"

        # user: User = User_model.objects.create_user(
        #     username=temp_username, email=temp_email, password=password
        # )

        # user.username = f"std{user.pk}"
        # user.email = f"{user.username}@b2b.bbtest.kz"
        # user.first_name = "first"
        # user.last_name = "last"
        # user.is_active = is_active
        # user.save()

        # content_type = ContentType.objects.get_for_model(type(user))
        # permissions = [Permission.objects.get(codename="student", content_type=content_type)]
        # user.user_permissions.set(permissions)
        # return user

class ExportStudentExcelView(PermissionRequiredMixinFactory(["B2BTeacher"]), View):

    def post(self, request: WSGIRequest, package_pair_quiz_id, *args, **kwargs):
        # Parse the JSON table data from the request
        print("ExportStudentExcelView", request.POST)
        try:
            table_data = json.loads(request.POST.get('tableData'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # package_pair_quiz_obj: TestPackageRusKazQuiz = get_object_or_404(TestPackageRusKazQuiz.objects, pk=package_pair_quiz_id)
        # table_data = package_pair_quiz_obj.student_table

        # Create an in-memory output stream for the Excel file
        output = io.BytesIO()

        # Create a new Excel workbook and add a worksheet
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()
        print("ExportStudentExcelView", "worksheet")
        # Define Excel headers
        headers = ['Login', 'First Name', 'Last Name', 'Language', 'Password']

        # Write the headers to the first row of the worksheet
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header)

        print("ExportStudentExcelView", "header")
        # Write table data to the worksheet (starting from row 1)
        for row_num, row_data in enumerate(table_data, start=1):
            worksheet.write(row_num, 0, row_data[0])
            worksheet.write(row_num, 1, row_data[1])
            worksheet.write(row_num, 2, row_data[2])
            worksheet.write(row_num, 3, row_data[3])
            worksheet.write(row_num, 4, row_data[4])

        # Close the workbook to finalize the output stream
        workbook.close()
        print("ExportStudentExcelView", "close")
        # Rewind the output stream to the beginning
        output.seek(0)

        # Create an HTTP response with the Excel file
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="students.xlsx"'
        # print("ExportStudentExcelView", "end")
        return response


class B2BStudentStartExamView(PermissionRequiredMixinFactory(["B2BTeacher"]), View):

    def post(self, request: WSGIRequest, package_pair_quiz_id, *args, **kwargs):
        package_pair_quiz_obj: TestPackageRusKazQuiz = get_object_or_404(TestPackageRusKazQuiz.objects, pk=package_pair_quiz_id)

        package_obj_ru: TestPackage = package_pair_quiz_obj.TestPackagePair.test_package_ru
        package_obj_kz: TestPackage = package_pair_quiz_obj.TestPackagePair.test_package_kz

        test_set_ru = package_obj_ru.tests.order_by("section__order").all()
        test_set_kz = package_obj_kz.tests.order_by("section__order").all()

        domain_ru = package_obj_ru.domain
        domain_kz = package_obj_kz.domain

        for row in package_pair_quiz_obj.student_table:
            username = row[0]
            first_name = row[1]
            last_name = row[2]
            lang = row[3]
            pwd = row[4]

            domain = domain_ru if lang == "rus" else domain_kz
            test_set = test_set_ru if lang == "rus" else test_set_kz

            student: User = User_model.objects.get(username = username)

            quiz_set = student.quiz_sets.create(test_domain=domain, cart=None)
            for quiz_order, test in enumerate(test_set):
                quiz_set.quizzes.create(test=test, order=quiz_order, line_item=None)

            student.is_active = True
            student.first_name = first_name
            student.last_name = last_name
            student.save()
        
        package_pair_quiz_obj.started = True
        package_pair_quiz_obj.save()

        success(request, pgettext("Success alert message", "Test is started."))
        return redirect("bbtest:b2bt_build_package_pair_quiz", package_pair_quiz_id)



class BuyPackageView(
    PermissionRequiredMixinFactory(["B2BTeacher"]), 
    UserContextMixin, 
    TemplateView
):
    template_name = "b2bt/buy_package.html"

    def get_context_data(self, **kwargs):
        kwargs["active_nav_item"] = "buy_packages"
        kwargs["language"] = get_language()

        kwargs["card_data"] = [
            {
                'title': 'Пакет "Классный"',
                'subtitle': 'Предоставление доступа к одному варианту симуляционного теста PISA 2025 для',
                'features': [
                    'Читательская грамотность',
                    'Математическая грамотность',
                    'Естественнонаучная грамотность',
                ],
                'footer': 'Автоматическое формирование аналитики по всему классу и каждому ученику',
                'techsupport': 'Предоставление технической поддержки',
                'price': '15 000 тг',
                'number_of_students': 25,
            },
            {
                'title': 'Пакет "Школьный"',
                'subtitle': 'Предоставление доступа к одному варианту симуляционного теста PISA 2025 для',
                'features': [
                    'Читательская грамотность',
                    'Математическая грамотность',
                    'Естественнонаучная грамотность',
                ],
                'footer': 'Автоматическое формирование аналитики по всему классу и каждому ученику',
                'techsupport': 'Предоставление технической поддержки',
                'price': '45 000 тг',
                'number_of_students': 150,
            },
        ] if get_language() == "ru" else [
            {
                'title': 'Пакет "Сынып"',
                'subtitle': 'PISA 2025 симуляциялық тестінің бір нұсқасына қолжетімділік беру',
                'features': [
                    'Оқу сауаттылығы',
                    'Математикалық сауаттылық',
                    'Жаратылыстану-ғылыми сауаттылық',
                ],
                'footer': 'Толық сынып және әр оқушы бойынша аналитиканы автоматты түрде қалыптастыру',
                'techsupport': 'Техникалық қолдау көрсету',
                'price': '15 000 тг',
                'number_of_students': 25,
            },
            {
                'title': 'Пакет "Мектептік"',
                'subtitle': 'PISA 2025 симуляциялық тестінің бір нұсқасына қолжетімділік беру',
                'features': [
                    'Оқу сауаттылығы',
                    'Математикалық сауаттылық',
                    'Жаратылыстану-ғылыми сауаттылық',
                ],
                'footer': 'Толық сыныптар және әр оқушы бойынша аналитиканы автоматты түрде қалыптастыру',
                'techsupport': 'Техникалық қолдау көрсету',
                'price': '45 000 тг',
                'number_of_students': 150,
            },
        ]

        if settings.DEBUG:
            kwargs["card_data"].append({
                'title': 'Пакет "Для Разработчиков"',
                'subtitle': 'Предоставление доступа к одному варианту симуляционного теста PISA 2025 для',
                'features': [
                    'Читательская грамотность',
                    'Математическая грамотность',
                    'Естественнонаучная грамотность',
                ],
                'footer': 'Автоматическое формирование аналитики по всему классу и каждому ученику',
                'techsupport': 'Предоставление технической поддержки',
                'price': '1 тг',
                'number_of_students': 5,
            })

        variant_list: QuerySet[TestPackageRusKazPair] = TestPackageRusKazPair.objects.all()

        
        kwargs["variant_list"] = variant_list
        # kwargs["add_package_pair_form"] = Buy_B2BTeacher_PackageForm()

        return super().get_context_data(**kwargs)
    


class ExportTestResultView(PermissionRequiredMixinFactory(["B2BTeacher"]), View):

    def post(self, request: WSGIRequest, package_pair_quiz_id, *args, **kwargs):
        package_pair_quiz_obj: TestPackageRusKazQuiz = get_object_or_404(TestPackageRusKazQuiz.objects, pk=package_pair_quiz_id)

        if not package_pair_quiz_obj.payed or not package_pair_quiz_obj.started:
            return JsonResponse({'error': 'Test is not started or not payed'}, status=400)

        # # correct time zone offset
        # dt = timedelta(hours=5)  

        # Create an in-memory output stream for the Excel file
        output = io.BytesIO()
        # Create a new Excel workbook and add a worksheet
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()


        header_row = ["Логин", "Имя", "Фамилия", "Общий балл"]
        domain_obj: TestDomain = package_pair_quiz_obj.TestPackagePair.test_package_ru.domain
        for section_obj in domain_obj.sections.order_by("order").all():
            section_obj: TestSection = section_obj
            print(section_obj, section_obj.question_count)

            header_row += ["предмет", f"балл по {section_obj.name}"] + [f"вопрос {i + 1}" for i in range(section_obj.question_count)]

        for i_col, cell_data in enumerate(header_row):
                worksheet.write(0, i_col, cell_data)

        total_index = [index for index, value in enumerate(header_row) if re.match("^балл по.+", value)]
        def total_subject_index(row):
            cells = [row_col_to_a1(row, index) for index in total_index]
            return "=" + "+".join(cells)
        
        # total_sum_formula = "=" + "+".join(total_subject_index)

        for i_row, row in enumerate(package_pair_quiz_obj.student_table, start=1):
            username = row[0]
            first_name = row[1]
            last_name = row[2]
            lang = row[3]
            # pwd = row[4]
            student: User = User_model.objects.get(username = username)

            quiz_set_list: QuerySet[QuizSet] = student.quiz_sets.all()
            if len(quiz_set_list) < 1:
                continue

            # email = student.email if student.email else ""
            
            for quiz_set in quiz_set_list:
                row = [student.username, first_name, last_name, total_subject_index(i_row)] 
                quiz_list: QuerySet[Quiz] = quiz_set.quizzes.order_by("test__section__order", "order").all()

                for quiz in quiz_list:
                    test: Test = quiz.test
                    answers = [""] * test.question_count

                    for i, ans in enumerate(quiz.get_answers_letters()):
                        if ans is not None:
                            answers[i] = str(ans)

                    # started_at = str((quiz.started_at + dt).strftime("%Y.%m.%d %H:%M:%S")) if quiz.started_at else ""
                    # due_at = str((quiz.due_at + dt).strftime("%Y.%m.%d %H:%M:%S")) if quiz.due_at else ""
                    # ended_at = str((quiz.ended_at + dt).strftime("%Y.%m.%d %H:%M:%S")) if quiz.ended_at else due_at
                    row = row + [f"{test.section.name} {lang}", str(quiz.calc_score())] + answers

                # row.append(total_sum_formula)
                for i_col, cell_data in enumerate(row, start=0):
                    worksheet.write(i_row, i_col, cell_data)


        # Close the workbook to finalize the output stream
        workbook.close()
        print("ExportTestResultView", "close")
        # Rewind the output stream to the beginning
        output.seek(0)
        # Create an HTTP response with the Excel file
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="students_result.xlsx"'
        return response
