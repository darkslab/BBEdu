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
from bbtest.forms.super import GiveCreditsForm
from bbtest.models.accounting import Entry, Debit, Credit

from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, ExpertPermissionRequiredMixin, StaffPermissionRequiredMixin, SuperPermissionRequiredMixin, AdminPermissionRequiredMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin

User = get_user_model()

class UsersView(StaffPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):  # SuperPermissionRequiredMixin
    template_name = "super/users.html"

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
                if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("admin", "developer", "expert", "student"):
                    user.role = permission.codename
                    break

        return super().get_context_data(**kwargs)


class UserView(AdminPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "super/user.html"

    def get_context_data(self, **kwargs):
        kwargs["now_at"] = now()

        user = get_object_or_404(User.objects.filter(is_superuser=False), pk=self.kwargs["user_id"])
        for permission in user.user_permissions.all():
            if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("admin", "developer", "expert", "admin", "student"):
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
