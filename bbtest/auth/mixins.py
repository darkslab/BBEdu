from django.contrib.auth.mixins import AccessMixin, PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.conf import settings
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


class LoginRequiredMixin(AccessMixin):
    login_url = reverse_lazy("bbtest:login")
    raise_exception = True
    redirect_field_name = settings.BB_REDIRECT_FIELDNAME

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            if request.is_ajax():
                raise PermissionDenied("Permission denied for AJAX call")
            return redirect_to_login(request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        return super().dispatch(request, *args, **kwargs)


class LogoutRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.is_ajax():
                raise PermissionDenied("Permission denied for AJAX call")
            return redirect(request.user)
        return super().dispatch(request, *args, **kwargs)


class SuperPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Super access required"
    permission_required = "bbtest.super"


class AdminPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Admin access required"
    permission_required = "bbtest.admin"


class DeveloperPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Developer access required"
    permission_required = "bbtest.developer"


class StudentPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Student access required"
    permission_required = "bbtest.student"
