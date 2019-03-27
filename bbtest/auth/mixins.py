from django.contrib.auth.mixins import AccessMixin, PermissionRequiredMixin as _PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.conf import settings
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied, ImproperlyConfigured


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


class PermissionRequiredMixin(_PermissionRequiredMixin):
    def base_permission(self):
        raise NotImplementedError("%s has to implement 'base_permission' method" % type(self).__name__)

    def get_permission_required(self):
        permissions = set()
        permissions.add(self.base_permission())
        if self.permission_required is None:
            return permissions
        try:
            if isinstance(self.permission_required, str):
                self.permission_required = (self.permission_required,)
            permissions |= set(self.permission_required)
        except TypeError:
            raise ImproperlyConfigured("Incorrect permission_required attribute value. Only iterable objects are allowed.")
        return permissions


class SuperPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Super access required"

    def base_permission(self):
        return "bbtest.super"


class AdminPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Admin access required"

    def base_permission(self):
        return "bbtest.admin"


class DeveloperPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Developer access required"

    def base_permission(self):
        return "bbtest.developer"


class StudentPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Student access required"

    def base_permission(self):
        return "bbtest.student"
