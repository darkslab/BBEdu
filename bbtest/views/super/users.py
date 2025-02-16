from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.messages import warning, success, error
from django.utils.translation import pgettext
from django.db.models import Q
from django.utils.timezone import now
from django.http import Http404
from decimal import Decimal
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.forms.super import GiveCreditsForm, ChangeUserPassManualForm
from bbtest.models.accounting import Entry, Debit, Credit
from bbtest.models.quiz import QuizSet, Quiz

from bbtest.auth.mixins import StaffPermissionRequiredMixin, SuperPermissionRequiredMixin, AdminPermissionRequiredMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin

User = get_user_model()

class UsersView(StaffPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):  # SuperPermissionRequiredMixin
    template_name = "super/users.html"

    def get_context_data(self, **kwargs):
        users = User.objects.filter(is_superuser=False).order_by("-joined_at").prefetch_related("user_permissions__content_type")
        kwargs["q"] = self.request.GET.get("q", "")
        kwargs["filter_role"] = self.request.GET.get("filter_role", "")
        kwargs["filter_active"] = self.request.GET.get("filter_active", "")
        kwargs["role_type_list"] = ["developer", "expert", "admin", "student", "super", "demouser", "B2BTeacher", "B2BTeacher (pay)", "B2BTeacher (no pay)"]


        if kwargs["filter_active"] == "1":
            users = users.filter(is_active=True)

        if kwargs["filter_role"]:
            if kwargs["filter_role"] == "B2BTeacher (pay)":
                users = users.filter(user_permissions__codename="B2BTeacher" )
                users = users.filter(
                    test_package_pair_quiz_sets__payed=True
                ).distinct()

            elif kwargs["filter_role"] == "B2BTeacher (no pay)":
                users = users.filter(user_permissions__codename="B2BTeacher" )
                users = users.exclude(
                    test_package_pair_quiz_sets__payed=True
                ).distinct()
            else:
                users = users.filter(user_permissions__codename=kwargs["filter_role"] )
                

        if kwargs["q"]:
            users = users.filter(
                Q(first_name__icontains=self.request.GET["q"])
                |
                Q(last_name__icontains=self.request.GET["q"])
                |
                Q(email__icontains=self.request.GET["q"])
                |
                Q(username__icontains=self.request.GET["q"])
            )


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
                if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("admin", "developer", "expert", "student", "demouser", "B2BTeacher"):
                    user.role = permission.codename
                    break

        return super().get_context_data(**kwargs)


class UserView(AdminPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "super/user.html"

    def get_context_data(self, **kwargs):
        kwargs["now_at"] = now()

        user = get_object_or_404(User.objects.filter(is_superuser=False), pk=self.kwargs["user_id"])
        for permission in user.user_permissions.all():
            if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("admin", "developer", "expert", "admin", "student", "demouser", "B2BTeacher"):
                user.role = permission.codename
                break
        kwargs["user_object"] = user

        kwargs["extended_info"] = {}
        if user.role == "student":
            kwargs["extended_info"]["identification"] = user.info("identification")
            kwargs["extended_info"]["region"] = user.info("region")
            kwargs["extended_info"]["district"] = user.info("district")
            kwargs["extended_info"]["village"] = user.info("village")
            kwargs["extended_info"]["school"] = user.info("school")

        kwargs["balance_account"] = user.balance_account()
        kwargs["account_entries"] = user.balance_account().entries.order_by("created_at").prefetch_related("amounts__account")

        kwargs["give_credits_form"] = GiveCreditsForm()
        kwargs["change_pass_manual_form"] = ChangeUserPassManualForm()

        kwargs["quiz_set_list"] = []
        if user.role == "student":
            kwargs["quiz_set_list"] = QuizSet.objects.filter(student=user).prefetch_related("quizzes").all()
            kwargs["student_profile"] = user.student_profile if user.student_profile else None
        # print(kwargs["quiz_set_list"])

        return super().get_context_data(**kwargs)


class ImpersonateUserView(SuperPermissionRequiredMixin, View):
    def post(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(User.active_users.filter(is_superuser=False), pk=user_id)
        login(request, user)
        warning(request, pgettext("/super/users/", "Superuser, you are now logged in as %(name)s. PLEASE BE CAREFUL!") % { "name": user.get_full_name() })
        return redirect("bbtest:dashboard")


class GiveCreditsUserView(SuperPermissionRequiredMixin, View):
    def post(self, request, user_id, *args, **kwargs):
        is_found = False
        user = get_object_or_404(User.active_users.filter(is_superuser=False), pk=user_id)
        for permission in user.user_permissions.all():
            if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in "student":
                is_found = True
                break
        if not is_found:
            raise Http404("Credits can be given to only students")

        form = GiveCreditsForm(data=request.POST)
        if form.is_valid():
            amount = Decimal(form.cleaned_data["amount"])
            Entry.objects.post(form.cleaned_data["description"], [
                Debit(form.cleaned_data["credit_type"], amount),
                Credit(user.balance_account_name(), amount),
            ])
            success(request, "Added %s credits." % form.cleaned_data["amount"])
        else:
            error(request, "Could not add credits! %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))
        return redirect("bbtest:super_user", user_id=user.pk)


class ChangePassManualView(SuperPermissionRequiredMixin, View):
    def post(self, request, user_id, *args, **kwargs):
        is_found = False
        user = get_object_or_404(User.active_users.filter(is_superuser=False), pk=user_id)
        for permission in user.user_permissions.all():
            if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("student", "expert", "developer", "admin", "demouser", "B2BTeacher"):
                is_found = True
                break
        if not is_found:
            raise Http404("Change pass only for students, experts, developers, admins")

        form = ChangeUserPassManualForm(data=request.POST)
        is_valid = form.is_valid()
        print("asd" ,form.cleaned_data.keys())
        is_valid = form.cleaned_data["pass1"] == form.cleaned_data["pass2"] and len(form.cleaned_data["pass1"]) > 3
        if is_valid:
            user.set_password(form.cleaned_data["pass1"])
            user.save()
            success(request, "Password changed %s." % form.cleaned_data["pass1"])
        else:
            error(request, "Could not change password! %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))
        return redirect("bbtest:super_user", user_id=user.pk)


class CreateQuizSetDublicateView(AdminPermissionRequiredMixin, View):
    def post(self, request, user_id, *args, **kwargs):
        print("TODO: TestSection.objects.get(name=section_name).question_count is probably depreciated")

        user_student = get_object_or_404(User.objects.filter(is_superuser=False, student_test_profile__isnull=False), pk=user_id)
        student_group_obj = user_student.student_test_profile.student_group
        package_obj = student_group_obj.package

        if not package_obj.finalized:
            error(request, f"Package is not finilized. {package_obj.name}")
            return redirect("bbtest:super_user", user_id=user_student.pk)
        
        # mark all previous quizzes as finished
        for quiz_set_obj in user_student.quiz_sets.all():

            # for quiz_obj in quiz_set_obj.quizzes.all():
            #     quiz_obj.is_finished = True
            #     quiz_obj.save()
            
            quiz_set_obj.is_current = False
            quiz_set_obj.save()

        
        test_set = package_obj.tests.order_by('section__order').all()
        domain = package_obj.domain
        quiz_set = user_student.quiz_sets.create(test_domain=domain, cart=None)
        for quiz_order, test in enumerate(test_set):
            quiz_set.quizzes.create(test=test, order=quiz_order, line_item=None)
            # test.update(sales_count=(F("sales_count") + 1))

        success(request, f"New quiz set was create and previous have been stopped. {package_obj.name}")
        return redirect("bbtest:super_user", user_id=user_student.pk)