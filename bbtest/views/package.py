from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.messages import warning, success, error
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.utils.translation import pgettext
from django.db.models import Q, F
from django.utils.timezone import now
from django.http import Http404
from django.http import HttpResponse
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.forms.super import  CreatePackageForm, ManagePackageStudentsForm, ManagePackageTestForm
from bbtest.models.test import TestDomain, Test, TestPackage, TestSection, TestPackageRelation
from bbtest.http import TightJsonResponse
import uuid
from random import randint
import csv
from bbtest.models import User
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, AdminPermissionRequiredMixin, CreateStudentRequiredMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin
from django.core.exceptions import ValidationError
# User = get_user_model()
from datetime import datetime
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View


class BuildPackagesView(AdminPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "package/create_package.html"

    def get_context_data(self, **kwargs):
        packages = TestPackage.objects.all().order_by("-created_at") # .prefetch_related("domain_name")
        kwargs["q"] = ""
        try:
            packages = packages.filter(
                Q(name__icontains=self.request.GET["q"])
                |
                Q(code__icontains=self.request.GET["q"])
                # |
                # Q(domain_name__icontains=self.request.GET["q"])
            )
            kwargs["q"] = self.request.GET["q"]
        except KeyError:
            pass

        paginator = Paginator(packages, 25)
        try:
            kwargs["packages"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["packages"] = paginator.page(1)
        except EmptyPage:
            kwargs["packages"] = paginator.page(paginator.num_pages)
        paginator.page_indexes = self.page_indexes(kwargs["packages"], 5)

        # for user in kwargs["packages"]:
        #     for permission in user.user_permissions.all():
        #         if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("admin", "expert", "developer", "student"):
        #             user.role = permission.codename
        #             break

        kwargs["create_package_form"] = CreatePackageForm()

        return super().get_context_data(**kwargs)



class CreatePackageFormView(CreateStudentRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = CreatePackageForm(data=request.POST)
        print("CreatePackageFormView", form.is_valid())
        if form.is_valid():

            domain = form.cleaned_data["domain"]
            name = form.cleaned_data["name"]

            obj = TestPackage.objects.create(
                name = name,
                code = "{}{}".format(datetime.now().strftime("%y%m%d"), "%04x" % randint(0x0000, 0xffff) ),
                assessible = False,
                # tests 
                # students
                domain = domain,
            )
            print("CreatePackageFormView", obj)

        else:
            error(request, "Could not create package! %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))

        return redirect("bbtest:build_packages")


class BuildPackageView(AdminPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateResponseMixin, ContextMixin, View):
    template_name = "package/manage_package.html"
    # form_class = ManagePackageTestForm
    
    def get(self, request, code, *args, **kwargs):
        # print("BuildPackageView", args, kwargs, self.get_context_data())
        # print("BuildPackageView", self.request)
        # print("BuildPackageView", kwargs, code)


        # obj = TestPackage.objects.get(code=code)
        package_obj = get_object_or_404(TestPackage.objects, code=code)
        kwargs["package"] = package_obj
        kwargs["tests"] = package_obj.tests.all()
        kwargs["users"] = package_obj.students.all()

        section_set = TestSection.objects.filter(domain=package_obj.domain).prefetch_related("tests")

        CATEGORY_CHOICES = [(None, "-----")]
        for section_obj in section_set:
            options = []
            tests = section_obj.tests.filter(status=Test.STATUS_ACTIVE).all()
            for test_obj in tests:
                if test_obj not in kwargs["tests"]:
                    options.append((str(test_obj.code), test_obj.code))

            if len(options) > 0:
                CATEGORY_CHOICES.append((section_obj.name, tuple(options)))
        
        kwargs["add_tests_form"] = ManagePackageTestForm(choices = CATEGORY_CHOICES)

        
        # print("BuildPackageView", kwargs["tests"])

        kwargs["add_students_form"] = ManagePackageStudentsForm()

        return self.render_to_response(super().get_context_data(**kwargs))
    

class ManagePackageTestFormView(CreateStudentRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        package_code = code
        # print("ManagePackageTestFormView", request.POST)
        form = ManagePackageTestForm(data=request.POST)
        # print("ManagePackageTestFormView", form)
        test_code = request.POST.get('test')
        test_obj = Test.objects.get(code=test_code)
        if not test_obj:
            error(request, "not valid test code %s" % test_code)

        form.fields['test'].choices = [(test_code, test_code)]  # this hack is needed because choices are generated dynamically
        print("ManagePackageTestFormView", form.is_valid())
        # print("ManagePackageTestFormView", form)
        if form.is_valid():
            # test = form.cleaned_data["test"]
            package_obj = TestPackage.objects.get(code = package_code)

            TestPackageRelation.objects.create(
                test = test_obj,
                package = package_obj,
                order = 0
            )

            # print(test_obj, type(test_obj))
            # package_obj.tests.add(test_obj)
            # print(package_obj, package_obj.tests)

            
            # name = form.cleaned_data["name"]

        else:
            error(request, "Could not create package! %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))

        return redirect("bbtest:build_package", code)

class ManagePackageStudentsFormView(CreateStudentRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        package_code = code
        form = ManagePackageStudentsForm(data=request.POST)
        print("ManagePackageStudentsForm", form.is_valid())
        if form.is_valid():
            # initialize csv table response
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'
            writer = csv.writer(response)

            amount = int(form.cleaned_data["amount"])
            package_obj = TestPackage.objects.get(code = package_code)
            student_count = package_obj.students.count()  # package_students

            package_name = package_obj.name
            print("ManagePackageStudentsFormView", package_name, student_count)
            
            order_of_magnitude = amount // 10 + 2
            
            for i in range(student_count + 1, student_count + amount + 1):
                username = "{}_{:0{}}".format(package_name, i, order_of_magnitude)
                login_email =  None
                # if len(prefix) > 0:
                #     login_email = "{}_{}@modo.edu.kz".format(prefix, uuid.uuid4().hex[:10])
                # else:
                #     login_email = "{}@modo.edu.kz".format(uuid.uuid4().hex)
                gen_pass = "{:05}".format(randint(1, 99999))
                
                try:
                    student = self.create_students(username, login_email, gen_pass)
                    
                    package_obj.students.add(student)

                    writer.writerow([username, login_email, gen_pass])
                except ValidationError:
                    writer.writerow([username, login_email, "already_exist"])

            # success(request, "Created %s students." % form.cleaned_data["amount"])
            return response
        else:
            error(request, "Could not create package! %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))

        return redirect("bbtest:build_package", code)

    def create_students(self, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = username
        # user.last_name = "Electric"
        user.save()
        content_type = ContentType.objects.get_for_model(type(user))
        permissions = []
        permissions.append(Permission.objects.get(codename="student", content_type=content_type))
        user.user_permissions.set(permissions)
        return user


class RemoveTestFromPackageView(AdminPermissionRequiredMixin, View): # DeveloperPermissionRequiredMixin,
    def post(self, request, package_code, test_code, *args, **kwargs):
        print("RemoveTestFromPackageView", package_code, test_code)
        package_obj = get_object_or_404(TestPackage.objects, code=package_code)
        test_obj = get_object_or_404(Test.objects, code=test_code)
        
        obj = TestPackageRelation.objects.get(test = test_obj, package = package_obj)
        obj.delete()

        success(request, pgettext("Success alert message", "Test is removed from package."))
        return redirect("bbtest:build_package", package_code)