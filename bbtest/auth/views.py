from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.contrib.auth.views import (
    LoginView as _LoginView,
    LogoutView as _LogoutView,
    PasswordResetView as _PasswordResetView,
    PasswordResetConfirmView as _PasswordResetConfirmView,
)
from django.shortcuts import redirect, resolve_url
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.urls import reverse_lazy
from .forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from .mixins import LogoutRequiredMixin


class LoginView(_LoginView):
    template_name="login.html"
    redirect_field_name=settings.BB_REDIRECT_FIELDNAME
    authentication_form=AuthenticationForm
    redirect_authenticated_user=True

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(self.request.user)


class LogoutView(_LogoutView):
    redirect_field_name=settings.BB_REDIRECT_FIELDNAME


class RegisterView(LogoutRequiredMixin, TemplateView):
    template_name = "register.html"

    def dispatch(self, request, group, *args, **kwargs):
        self._group = group or "student"
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        if self._group == "developer":
            kwargs["form_url"] = resolve_url("bbtest:register", "developer")
        else:
            kwargs["form_url"] = resolve_url("bbtest:register")
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context["form"] = UserCreationForm(self._group)

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context["form"] = UserCreationForm(self._group, data=request.POST)
        if context["form"].is_valid():
            user = context["form"].save()

            content_type = ContentType.objects.get_for_model(type(user))
            permissions = []
            if self._group in ("developer", "student"):
                permissions.append(Permission.objects.get(codename=self._group, content_type=content_type))
            user.user_permissions.set(permissions)

            login(request, user)
            return redirect(user)

        return self.render_to_response(context)


class PasswordResetView(_PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy("bbtest:login")
    template_name = "password_reset.html"


class PasswordResetConfirmView(_PasswordResetConfirmView):
    # DARK_TODO
    # form_class = 
    post_reset_login = True
    success_url = reverse_lazy("bbtest:login")
    template_name = "password_reset_confirm.html"
