from __future__ import annotations

from typing import TYPE_CHECKING

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import (
    LoginView as _LoginView,
)
from django.contrib.auth.views import (
    LogoutView as _LogoutView,
)
from django.contrib.auth.views import (
    PasswordResetConfirmView as _PasswordResetConfirmView,
)
from django.contrib.auth.views import (
    PasswordResetView as _PasswordResetView,
)
from django.contrib.messages import success
from django.shortcuts import resolve_url
from django.urls import reverse, reverse_lazy
from django.utils.translation import pgettext

from bbtest.jobs.create_student_in_package import populate_demouser_test
from bbtest.models import QuizSet, TestPackage
from bbtest.views.generic import FormView

from .forms import (
    AuthenticationForm,
    DemoUserCreationForm,
    ExtendedUserCreationForm,
    PasswordResetForm,
    SetPasswordForm,
    UserCreationForm,
)
from .mixins import LogoutRequiredMixin

if TYPE_CHECKING:
    from bbtest.auth.models import User


class LoginView(_LoginView):
    template_name = "base/login.html"
    redirect_field_name = settings.BB_REDIRECT_FIELDNAME
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(self.request.user)


class LogoutView(_LogoutView):
    def get_next_page(self):
        return reverse_lazy("bbtest:home")


class RegisterView(LogoutRequiredMixin, FormView):
    form_class = ExtendedUserCreationForm
    success_url = reverse_lazy("bbtest:student_dashboard")
    template_name = "base/register.html"

    def form_valid(self, form):
        login(self.request, form.save(self._group()))
        self.request.session["ga_events"] = self.request.session.get(
            "ga_events", []
        ) + [["registration", {"event_category": self._group()}]]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs["group"] = self._group()
        return super().get_context_data(**kwargs)

    def _group(self):
        return "student"


class RegisterDeveloperView(RegisterView):
    form_class = UserCreationForm
    success_url = reverse_lazy("bbtest:developer_dashboard")

    def _group(self):
        return "developer"


class RegisterB2BTeacherView(RegisterView):
    form_class = UserCreationForm
    success_url = reverse_lazy("bbtest:b2bt_dashboard")

    def _group(self):
        return "B2BTeacher"


class RegisterDemoUserView(RegisterView):
    form_class = DemoUserCreationForm
    success_url = reverse_lazy("bbtest:demo_dashboard")
    template_name = "base/register_demo.html"

    def form_valid(self, form: DemoUserCreationForm):
        user: User = form.save(self._group())
        # print("logging in")
        login(self.request, user)

        populate_demouser_test.delay(user)
        self.request.session["ga_events"] = self.request.session.get(
            "ga_events", []
        ) + [["registration", {"event_category": self._group()}]]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs["group"] = self._group()
        return super().get_context_data(**kwargs)

    def _group(self):
        return "demouser"


class Logout_and_Register_DemoUserView(_LogoutView):
    success_url = reverse_lazy("bbtest:register_b2bt")
    next_page = reverse_lazy("bbtest:register_b2bt")

    def get_next_page(self):
        return reverse_lazy("bbtest:register_b2bt")


class PasswordResetView(LogoutRequiredMixin, _PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy("bbtest:login")
    template_name = "base/password_reset.html"


class PasswordResetConfirmView(LogoutRequiredMixin, _PasswordResetConfirmView):
    form_class = SetPasswordForm
    post_reset_login = True
    success_url = reverse_lazy("bbtest:dashboard")
    template_name = "base/password_reset_confirm.html"

    def form_valid(self, form):
        success(
            self.request,
            pgettext("Success alert message", "Password was reset successfully."),
        )
        return super().form_valid(form)
