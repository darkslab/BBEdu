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
from bbtest.models.test import TestDomain, Test
from bbtest.http import TightJsonResponse
import uuid
from random import randint
import csv
from bbtest.models import User
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, AdminPermissionRequiredMixin, CreateStudentRequiredMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin
from django.core.exceptions import ValidationError
# User = get_user_model()


class CreatePackageView(AdminPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "super/create_package.html"

    def get_context_data(self, **kwargs):
        users = User.objects.filter(is_superuser=False).order_by("-joined_at").prefetch_related("user_permissions__content_type")
        kwargs["q"] = ""
        try:
            users = users.filter(
                Q(first_name__icontains=self.request.GET["q"])
                |
                Q(last_name__icontains=self.request.GET["q"])
                |
                Q(email__icontains=self.request.GET["q"])
            )
            kwargs["q"] = self.request.GET["q"]
        except KeyError:
            pass

        paginator = Paginator(users, 25)
        try:
            kwargs["users"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["users"] = paginator.page(1)
        except EmptyPage:
            kwargs["users"] = paginator.page(paginator.num_pages)
        paginator.page_indexes = self.page_indexes(kwargs["users"], 5)

        for user in kwargs["users"]:
            for permission in user.user_permissions.all():
                if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("admin", "expert", "developer", "student"):
                    user.role = permission.codename
                    break

        kwargs["create_package_form"] = CreatePackageForm()

        return super().get_context_data(**kwargs)



class CreatePackageFormView(CreateStudentRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = CreatePackageForm(data=request.POST)

        if form.is_valid():
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'
            writer = csv.writer(response)

            amount = int(form.cleaned_data["amount"])
            order_of_magnitude = amount // 10 + 2
            name = form.cleaned_data["name"] 
            # prefix = form.cleaned_data["prefix"]
            prefix = "bb"
            for i in range(1, amount+1):
                username = "{}_{:0{}}".format(name, i, order_of_magnitude)
                login_email =  None
                # if len(prefix) > 0:
                #     login_email = "{}_{}@modo.edu.kz".format(prefix, uuid.uuid4().hex[:10])
                # else:
                #     login_email = "{}@modo.edu.kz".format(uuid.uuid4().hex)
                gen_pass = "{:05}".format(randint(1, 99999))
                
                domain = form.cleaned_data["domain"]
                try:
                    student = self.create_students(username, login_email, gen_pass)
                    domain_for_student_obj = DomainForStudent.objects.create(student = student, domain = domain)

                    quiz_set = student.quiz_sets.create(test_domain=domain, cart=None)
                    for quiz_order, test in enumerate(
                        Test.objects.filter(
                            Q(section__domain=domain) & 
                            Q(status=Test.STATUS_ACTIVE)
                        ).order_by('section__order')):
                        
                        quiz_set.quizzes.create(test=test, order=quiz_order, line_item=None)
                        # test.update(sales_count=(F("sales_count") + 1))

                    writer.writerow([username, login_email, gen_pass])
                except ValidationError:
                    writer.writerow([username, login_email, "already_exist"])

            # success(request, "Created %s students." % form.cleaned_data["amount"])
            return response

        else:
            error(request, "Could not create students! %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))

        return redirect("bbtest:super_create_students")