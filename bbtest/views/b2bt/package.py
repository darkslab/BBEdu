import csv
import io
import json
import uuid
from datetime import datetime
from random import randint

import xlsxwriter
from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages import error, success, warning
from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import F, Q
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now
from django.utils.translation import pgettext
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View

from bbtest.auth.mixins import (
    CreateStudentRequiredMixin,
    PermissionRequiredMixinFactory,
)
from bbtest.forms.super import (
    Buy_B2BTeacher_PackageForm,
    CreateStudentGroupForm,
    ManagePackageStudentsForm,
    ManagePackageTestForm,
)
from bbtest.http import TightJsonResponse
from bbtest.jobs.create_student_in_package import (
    activate_package,
    populate_package_student_group,
)
from bbtest.auth.models import User
from bbtest.models.quiz import Quiz, QuizSet
from bbtest.models.test import (
    StudentGroup,
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

# User = get_user_model()


class BuildPackagesView(
    PermissionRequiredMixinFactory(["B2BTeacher"]), UserContextMixin, PaginationMixin, TemplateView
):
    template_name = "b2bt/create_package.html"

    def get_context_data(self, **kwargs):
        kwargs["active_nav_item"] = "buy_packages"

        package_pair_quiz_set: TestPackageRusKazQuiz = TestPackageRusKazQuiz.objects.filter(
            user = self.request.user
        ).order_by(
            "-created_at"
        ).prefetch_related("TestPackagePair")
        

        # kwargs["q"] = ""
        # try:
        #     package_pair_quiz_set = package_pair_quiz_set.filter(
        #         Q(name__icontains=self.request.GET["q"])
        #         | Q(code__icontains=self.request.GET["q"])
        #         # |
        #         # Q(domain_name__icontains=self.request.GET["q"])
        #     )
        #     kwargs["q"] = self.request.GET["q"]
        # except KeyError:
        #     pass

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


class BuildStudentGroupView(
    PermissionRequiredMixinFactory(["B2BTeacher"]),
    UserContextMixin,
    PaginationMixin,
    TemplateResponseMixin,
    ContextMixin,
    View,
):
    template_name = "b2bt/manage_student_group.html"
    # form_class = ManagePackageTestForm

    def get(self, request, package_code, student_group_id, *args, **kwargs):
        package_obj = get_object_or_404(TestPackage.objects, code=package_code)
        group_obj = get_object_or_404(StudentGroup.objects, pk=student_group_id)

        kwargs["package"] = package_obj
        kwargs["student_group"] = group_obj

        test_profiles = group_obj.students.prefetch_related("student").all()
        kwargs["users"] = [p.student for p in test_profiles]

        print(kwargs["users"])

        kwargs["add_student_form"] = ManagePackageStudentsForm()

        return self.render_to_response(super().get_context_data(**kwargs))


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
        kwargs["active_nav_item"] = "buy_packages"

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

        student_table = []
        for i in range(int(number_of_students)):
            passwrd = "{:05}".format(randint(10000, 99999))
            user: User = self.create_students(passwrd)
            student_table.append([user.username, "first", "last", "rus", passwrd])

        package_quiz_obj = TestPackageRusKazQuiz.objects.create(
            # name = name,
            user=request.user,
            TestPackagePair=test_package_pair,
            number_of_students=number_of_students,
            student_table = student_table,
        )
        print("AddPackagePairFormView", package_quiz_obj)

        return redirect("bbtest:b2bt_build_package_pair_quiz", package_quiz_obj.id)
    

    def create_students(self, password, is_active = False):
        temp_username = uuid.uuid4().hex
        temp_email = f"{temp_username}@b2b.bbtest.kz"

        user: User = User.objects.create_user(
            username=temp_username, email=temp_email, password=password
        )

        user.username = f"std{user.pk}"
        user.email = f"{user.username}@b2b.bbtest.kz"
        user.first_name = "first"
        user.last_name = "last"
        user.is_active = is_active
        user.save()

        content_type = ContentType.objects.get_for_model(type(user))
        permissions = []
        permissions.append(
            Permission.objects.get(codename="student", content_type=content_type)
        )
        user.user_permissions.set(permissions)
        return user

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
        print("ExportStudentExcelView", "end")
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
            lang = row[3]

            domain = domain_ru if lang == "rus" else domain_kz
            test_set = test_set_ru if lang == "rus" else test_set_kz

            student: User = User.objects.get(username = username)

            quiz_set = student.quiz_sets.create(test_domain=domain, cart=None)
            for quiz_order, test in enumerate(test_set):
                quiz_set.quizzes.create(test=test, order=quiz_order, line_item=None)

            student.is_active = True
            student.save()

        success(request, pgettext("Success alert message", "Test is started."))
        return redirect("bbtest:b2bt_build_package_pair_quiz", package_pair_quiz_id)


class ManagePackageCreateStudentGroupFormView(CreateStudentRequiredMixin, View):
    def post(self, request: WSGIRequest, package_code, *args, **kwargs):
        form = CreateStudentGroupForm(data=request.POST)

        UserTestPackageProfile, StudentGroup

        if form.is_valid():
            package_obj = TestPackage.objects.get(code=package_code)

            group_obj = StudentGroup.objects.create(
                name=form.cleaned_data["name"],
                package=package_obj,
            )
            print(group_obj)
        else:
            error(
                request,
                "Could not create StudentGroup! %s"
                % " ".join([" ".join(errors) for key, errors in form.errors.items()]),
            )

        return redirect("bbtest:build_package", package_code)


class ManagePackageStudentsFormView(CreateStudentRequiredMixin, View):
    def post(self, request: WSGIRequest, package_code, student_group_id, *args, **kwargs):
        form = ManagePackageStudentsForm(data=request.POST)
        print("ManagePackageStudentsForm", form.is_valid())
        if not form.is_valid():
            error(
                request,
                "Could not create package! %s"
                % " ".join([" ".join(errors) for key, errors in form.errors.items()]),
            )
            return redirect("bbtest:build_package", package_code)

        group_obj = get_object_or_404(StudentGroup.objects, pk=student_group_id)
        package_obj = get_object_or_404(TestPackage.objects, code=package_code)

        amount = int(form.cleaned_data["amount"])
        prefix = form.cleaned_data["prefix"]

        populate_package_student_group.delay(
            package_code, group_obj.name, prefix, amount
        )

        success(
            request,
            f"Работа по созданию {amount} учеников начата на фоне, на данный момент визуализации нету.",
        )
        return redirect("bbtest:build_package", package_code)

    def create_students(self, username, email, password, is_active):
        user: User = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.first_name = username
        user.is_active = is_active
        # user.last_name = "Electric"
        user.save()
        content_type = ContentType.objects.get_for_model(type(user))
        permissions = []
        permissions.append(
            Permission.objects.get(codename="student", content_type=content_type)
        )
        user.user_permissions.set(permissions)
        return user


class FinalizePackageView(PermissionRequiredMixinFactory(["B2BTeacher"]), View):
    def post(self, request: WSGIRequest, package_code, *args, **kwargs):
        print("ActivatePackageView", package_code)
        package_obj = get_object_or_404(TestPackage.objects, code=package_code)
        package_obj.finalized = True

        student_set = []
        student_groups = package_obj.student_groups.all()
        for group in student_groups:
            for student_test_profile_obj in group.students.all():
                student_set.append(student_test_profile_obj.student)

        test_set = package_obj.tests.order_by("section__order").all()

        # student_set = package_obj.students.all()
        domain = package_obj.domain
        # print(test_set)
        # print(student_set)

        for student in student_set:
            # Quiz
            quiz_set = student.quiz_sets.create(test_domain=domain, cart=None)
            for quiz_order, test in enumerate(test_set):
                quiz_set.quizzes.create(test=test, order=quiz_order, line_item=None)
                # test.update(sales_count=(F("sales_count") + 1))
            # student.is_active = True
            # student.save()

        package_obj.save()

        success(request, pgettext("Success alert message", "Package is finalized."))
        return redirect("bbtest:build_packages")


class ActivateStudentGroupToggleView(PermissionRequiredMixinFactory(["B2BTeacher"]), View):
    def post(self, request: WSGIRequest, package_code, student_group_id, *args, **kwargs):
        print("ActivateStudentGroupView", package_code)
        # package_obj = get_object_or_404(TestPackage.objects, code=package_code)
        group_obj = get_object_or_404(StudentGroup.objects, pk=student_group_id)
        is_active = group_obj.is_active

        for student_test_profile_obj in group_obj.students.all():
            student_test_profile_obj.student.is_active = not is_active
            student_test_profile_obj.student.save()

        group_obj.is_active = not is_active
        group_obj.save()

        return redirect("bbtest:build_package", package_code)


class ActivateStudentTurnON(PermissionRequiredMixinFactory(["B2BTeacher"]), View):
    def post(self, request: WSGIRequest, package_code, student_group_id, *args, **kwargs):
        print("ActivateStudentTurnON", package_code)
        group_obj = get_object_or_404(StudentGroup.objects, pk=student_group_id)
        if settings.DEBUG:
            # group_obj.students.update(student__is_active=True)
            # User.objects.filter(student_test_profile=group_obj).count()
            User.objects.filter(
                student_test_profile__isnull=False,
                student_test_profile__student_group=group_obj,
            ).update(is_active=True)
            group_obj.is_active = True
            group_obj.save()
        else:
            activate_package.delay(group_obj, True)

        success(request, "Открытие доступа...")
        return redirect("bbtest:build_package", package_code)


class ActivateStudentTurnOFF(PermissionRequiredMixinFactory(["B2BTeacher"]), View):
    def post(self, request: WSGIRequest, package_code, student_group_id, *args, **kwargs):
        print("ActivateStudentTurnOFF", package_code)
        group_obj: StudentGroup = get_object_or_404(
            StudentGroup.objects, pk=student_group_id
        )
        if settings.DEBUG:
            User.objects.filter(
                student_test_profile__isnull=False,
                student_test_profile__student_group=group_obj,
            ).update(is_active=False)
            group_obj.is_active = False
            group_obj.save()
        else:
            activate_package.delay(group_obj, False)

        success(request, "Закрытие доступа...")
        return redirect("bbtest:build_package", package_code)
