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
from bbtest.forms.super import  CreatePackageForm
from bbtest.models.test import TestDomain, Test, TestPackage
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