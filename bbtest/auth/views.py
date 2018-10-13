from django.contrib.auth.views import (
    LoginView as _LoginView,
    LogoutView as _LogoutView,
    PasswordResetView as _PasswordResetView,
    PasswordResetConfirmView as _PasswordResetConfirmView,
)
from django.shortcuts import resolve_url
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.messages import success
from django.utils.translation import pgettext
from django.contrib.auth import login
from .forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
from .mixins import LogoutRequiredMixin
from bbtest.views.generic import FormView


class LoginView(_LoginView):
    template_name = "base/login.html"
    redirect_field_name = settings.BB_REDIRECT_FIELDNAME
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(self.request.user)


class LogoutView(_LogoutView):
    redirect_field_name=settings.BB_REDIRECT_FIELDNAME


class RegisterView(LogoutRequiredMixin, FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy("bbtest:dashboard")
    template_name = "base/register.html"

    def dispatch(self, request, group, *args, **kwargs):
        self._group = group or "student"
        assert self._group in ("developer", "student")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.save(self._group))
        self.request.session["ga_events"] = self.request.session.get("ga_events", []) + [
            "registration",
            self._group,
        ]
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs["group"] = self._group
        return super().get_context_data(**kwargs)


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
        success(self.request, pgettext("Success alert message", "Password was reset successfully."))
        return super().form_valid(form)
