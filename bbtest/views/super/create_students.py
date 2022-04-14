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
from bbtest.forms.super import CreateStudentsForm
from bbtest.http import TightJsonResponse
import uuid
import csv
from bbtest.models import User
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin

# User = get_user_model()

class CreateStudentsView(DeveloperPermissionRequiredMixin, DeveloperAcknowledgementRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "super/create_students.html"

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
                if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("admin", "developer", "student"):
                    user.role = permission.codename
                    break

        kwargs["create_students_form"] = CreateStudentsForm()

        return super().get_context_data(**kwargs)



class CreateStudentsFormView(DeveloperPermissionRequiredMixin, DeveloperAcknowledgementRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = CreateStudentsForm(data=request.POST)

        if form.is_valid():
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'
            writer = csv.writer(response)

            amount = int(form.cleaned_data["amount"])
            name = form.cleaned_data["name"] 
            prefix = form.cleaned_data["prefix"]
            for i in range(amount):
                username = name + uuid.uuid4().hex[:5]
                if len(prefix) > 0:
                    login = "{}_{}@iqanat.bbtest.kz".format(prefix, uuid.uuid4().hex)
                else:
                    login = "{}@iqanat.bbtest.kz".format(uuid.uuid4().hex)
                gen_pass = uuid.uuid4().hex[:5]

                self.create_students(username, login, gen_pass)

                writer.writerow([login, gen_pass])

            # success(request, "Created %s students." % form.cleaned_data["amount"])
            return response

        else:
            error(request, "Could not add credits! %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))

        return redirect("bbtest:super_create_students")

        # data = {
        #     "success": True,
        # }
        # return TightJsonResponse(data)


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