from django.contrib.auth.mixins import (
    LoginRequiredMixin as _LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.conf import settings


class LoginRequiredMixin(_LoginRequiredMixin):
    login_url = reverse_lazy("bbtest:login")
    redirect_field_name = settings.BB_REDIRECT_FIELDNAME

class _GroupLoginRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    raise_exception = True

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class SuperLoginRequiredMixin(_GroupLoginRequiredMixin):
    permission_denied_message = "Super access required"
    permission_required = "bbtest.super"

class AdminLoginRequiredMixin(_GroupLoginRequiredMixin):
    permission_denied_message = "Admin access required"
    permission_required = "bbtest.admin"

class DeveloperLoginRequiredMixin(_GroupLoginRequiredMixin):
    permission_denied_message = "Developer access required"
    permission_required = "bbtest.developer"

class StudentLoginRequiredMixin(_GroupLoginRequiredMixin):
    permission_denied_message = "Student access required"
    permission_required = "bbtest.student"
