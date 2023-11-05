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
        print("BuildPackageView", kwargs, code)


        # obj = TestPackage.objects.get(code=code)
        package_obj = get_object_or_404(TestPackage.objects, code=code)
        kwargs["package"] = package_obj

        # form_add_test = ManagePackageTestForm()
        # form.fields['domain'].queryset = TestSection.objects.filter(domain=package_obj.domain)
        section_set = TestSection.objects.filter(domain=package_obj.domain)

        CATEGORY_CHOICES = []
        for section_obj in section_set:
            options = []
            tests = section_obj.tests.all()
            for test_obj in tests:
                options.append((str(test_obj.code), test_obj.code))
            if len(tests) > 0:
                CATEGORY_CHOICES.append((section_obj.name, tuple(options)))
                
        # form_add_test.fields['test'].choices = tuple(CATEGORY_CHOICES)
        # form_add_test.fields['test'].initial = CATEGORY_CHOICES[0][1]
        form_add_test = ManagePackageTestForm(choices = CATEGORY_CHOICES)
        kwargs["add_tests_form"] = form_add_test

        kwargs["tests"] = package_obj.tests.all()
        print("BuildPackageView", kwargs["tests"])
        # print(form_add_test)

        form_add_students = ManagePackageStudentsForm()
        kwargs["add_students_form"] = form_add_students
        # print(form_add_students)

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

        form.fields['test'].choices = [(test_code, test_code)]
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
        form = ManagePackageStudentsForm(data=request.POST)
        print("ManagePackageStudentsForm", form.is_valid())
        if form.is_valid():

            domain = form.cleaned_data["domain"]
            name = form.cleaned_data["name"]

            # obj = TestPackage.objects.create(
            #     name = name,
            #     code = "{}{}".format(datetime.now().strftime("%y%m%d"), "%04x" % randint(0x0000, 0xffff) ),
            #     assessible = False,
            #     # tests 
            #     # students
            #     domain = domain,
            # )
            # print("CreatePackageFormView", obj)

        else:
            error(request, "Could not create package! %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))

        return redirect("bbtest:build_package", code)