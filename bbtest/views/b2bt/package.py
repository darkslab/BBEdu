import csv
import uuid
from datetime import datetime
from random import randint

from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages import error, success, warning
from django.core.exceptions import ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import F, Q
from django.http import Http404, HttpResponse
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
from bbtest.models import User
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

    def get(self, request, package_pair_quiz_id, *args, **kwargs):
        # print("BuildPackageView", args, kwargs, self.get_context_data())
        # print("BuildPackageView", self.request)
        # print("BuildPackageView", kwargs, code)

        package_pair_quiz_obj: TestPackageRusKazQuiz = get_object_or_404(TestPackageRusKazQuiz.objects, pk=package_pair_quiz_id)

        kwargs["package_ru"] = package_pair_quiz_obj.TestPackagePair.test_package_ru
        kwargs["package_kz"] = package_pair_quiz_obj.TestPackagePair.test_package_kz

        kwargs["tests_ru"] = kwargs["package_ru"].tests.order_by("section__order").all()
        kwargs["tests_kz"] = kwargs["package_kz"].tests.order_by("section__order").all()

        # kwargs["student_group_list"] = package_pair_quiz_obj.student_groups.all()

        kwargs["student_table"] = package_pair_quiz_obj.student_table

        return self.render_to_response(super().get_context_data(**kwargs))


class AddPackagePairFormView(PermissionRequiredMixinFactory(["B2BTeacher"]), View):
    def post(self, request, *args, **kwargs):
        form = Buy_B2BTeacher_PackageForm(data=request.POST)
        print("AddPackagePairFormView", form.is_valid())
        if form.is_valid():
            test_package_pair: TestPackageRusKazPair = form.cleaned_data[
                "test_package_pair"
            ]
            # comment = form.cleaned_data["comment"]
            number_of_students = form.cleaned_data["number_of_students"]

            obj = TestPackageRusKazQuiz.objects.create(
                # name = name,
                user=request.user,
                TestPackagePair=test_package_pair,
                number_of_students=number_of_students,
                student_table = [["first", "last", "rus"] for _ in range(int(number_of_students))]
            )
            print("AddPackagePairFormView", obj)

        else:
            error(
                request,
                "Could not create TestPackageRusKazQuizSet! %s"
                % " ".join([" ".join(errors) for key, errors in form.errors.items()]),
            )

        return redirect("bbtest:b2bt_build_packages")


class ManagePackageTestFormView(CreateStudentRequiredMixin, View):
    def post(self, request, package_code, *args, **kwargs):
        # print("ManagePackageTestFormView", request.POST)
        form = ManagePackageTestForm(data=request.POST)
        # print("ManagePackageTestFormView", form)
        test_code = request.POST.get("test")
        test_obj = Test.objects.get(code=test_code)
        if not test_obj:
            error(request, "not valid test code %s" % test_code)

        form.fields["test"].choices = [
            (test_code, test_code)
        ]  # this hack is needed because choices are generated dynamically
        print("ManagePackageTestFormView", form.is_valid())
        # print("ManagePackageTestFormView", form)
        if form.is_valid():
            # test = form.cleaned_data["test"]
            package_obj = TestPackage.objects.get(code=package_code)

            TestPackageRelation.objects.create(
                test=test_obj, package=package_obj, order=0
            )

            # print(test_obj, type(test_obj))
            # package_obj.tests.add(test_obj)
            # print(package_obj, package_obj.tests)

            # name = form.cleaned_data["name"]

        else:
            error(
                request,
                "Could not create package! %s"
                % " ".join([" ".join(errors) for key, errors in form.errors.items()]),
            )

        return redirect("bbtest:build_package", package_code)


class ManagePackageCreateStudentGroupFormView(CreateStudentRequiredMixin, View):
    def post(self, request, package_code, *args, **kwargs):
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
    def post(self, request, package_code, student_group_id, *args, **kwargs):
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

    def post_old(self, request, package_code, student_group_id, *args, **kwargs):
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

        # initialize csv table response
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="export.csv"'
        writer = csv.writer(response)

        amount = int(form.cleaned_data["amount"])
        prefix = form.cleaned_data["prefix"]

        student_count = group_obj.students.count()
        student_list = []

        package_name = package_obj.name
        print(
            "ManagePackageStudentsFormView", package_name, group_obj.name, student_count
        )

        for i in range(student_count + 1, student_count + amount + 1):
            # username = "{}{}{:03}".format(package_name, group_obj.name, i)
            username = "{}{:03}".format(group_obj.name, i)
            login_email = None
            if len(prefix) > 0:
                login_email = "{}_{}@not.real.email.kz".format(
                    prefix, uuid.uuid4().hex[:12]
                )
            # else:
            #     login_email = "{}@not.real.email.kz".format(uuid.uuid4().hex[:12])
            gen_pass = "{:05}".format(randint(1, 99999))

            try:
                student_obj = self.create_students(
                    username, login_email, gen_pass, group_obj.is_active
                )
                UserTestPackageProfile.objects.create(
                    student=student_obj,
                    student_group=group_obj,
                )
                student_list.append(student_obj)
                # package_obj.students.add(student_obj)

                writer.writerow([username, login_email, gen_pass])
            except ValidationError:
                writer.writerow([username, login_email, "already_exist"])

        if package_obj.finalized:
            test_set = package_obj.tests.order_by("section__order").all()
            domain = package_obj.domain

            for student_obj in student_list:
                quiz_set = student_obj.quiz_sets.create(test_domain=domain, cart=None)
                for quiz_order, test in enumerate(test_set):
                    quiz_set.quizzes.create(test=test, order=quiz_order, line_item=None)
                    # test.update(sales_count=(F("sales_count") + 1))

        group_obj.student_count = group_obj.students.count()
        group_obj.save()

        success(request, "Created %s students." % amount)
        return response

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


class RemoveTestFromPackageView(
    PermissionRequiredMixinFactory(["B2BTeacher"]), View
):  # DeveloperPermissionRequiredMixin,
    def post(self, request, package_code, test_code, *args, **kwargs):
        print("RemoveTestFromPackageView", package_code, test_code)
        package_obj = get_object_or_404(TestPackage.objects, code=package_code)
        test_obj = get_object_or_404(Test.objects, code=test_code)

        obj = TestPackageRelation.objects.get(test=test_obj, package=package_obj)
        obj.delete()

        success(
            request, pgettext("Success alert message", "Test is removed from package.")
        )
        return redirect("bbtest:build_package", package_code)


class FinalizePackageView(PermissionRequiredMixinFactory(["B2BTeacher"]), View):
    def post(self, request, package_code, *args, **kwargs):
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
    def post(self, request, package_code, student_group_id, *args, **kwargs):
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
    def post(self, request, package_code, student_group_id, *args, **kwargs):
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
    def post(self, request, package_code, student_group_id, *args, **kwargs):
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
