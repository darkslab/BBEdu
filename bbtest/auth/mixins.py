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


class AdminPermissionRequiredMixin(LoginRequiredMixin):  # PermissionRequiredMixin
    # permission_denied_message = "Admin access required"
    # permission_required = "bbtest.admin"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("bbtest.super") or request.user.has_perm("bbtest.admin"):
            return super().dispatch(request, *args, **kwargs)
        if request.is_ajax():
            raise PermissionDenied("Permission denied for AJAX call")
        return super().dispatch(request, *args, **kwargs)


class ExpertPermissionRequiredMixin(LoginRequiredMixin):
    # permission_denied_message = "Expert access required"
    # permission_required = "bbtest.expert"
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("bbtest.super") or request.user.has_perm("bbtest.expert"):
            return super().dispatch(request, *args, **kwargs)
        if request.is_ajax():
            raise PermissionDenied("Permission denied for AJAX call")
        return super().dispatch(request, *args, **kwargs)

class DeveloperPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Developer access required"
    permission_required = "bbtest.developer"


class StudentPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Student access required"
    permission_required = "bbtest.student"

class DemouserPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "Student access required"
    permission_required = "bbtest.demouser"

class StaffPermissionRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (request.user.has_perm("bbtest.super") or 
                request.user.has_perm("bbtest.expert") or 
                request.user.has_perm("bbtest.admin") or 
                request.user.has_perm("bbtest.developer")):
            return super().dispatch(request, *args, **kwargs)
        if request.is_ajax():
            raise PermissionDenied("Permission denied for AJAX call")
        # return redirect("bbtest:home")
        return super().handle_no_permission()
        # return super().dispatch(request, *args, **kwargs)


def PermissionRequiredMixinFactory(role_list: list): 

    class PermissionRequiredMixin(LoginRequiredMixin): 
        def dispatch(self, request, *args, **kwargs):
            role = request.user.get_user_role()

            if role == "super":
                return super().dispatch(request, *args, **kwargs)
            
            if role in role_list:
                return super().dispatch(request, *args, **kwargs)
                
            if request.is_ajax():
                raise PermissionDenied("Permission denied for AJAX call")
            
            return super().handle_no_permission()
            # return super().dispatch(request, *args, **kwargs)
  
    return PermissionRequiredMixin

class CreateStudentRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (request.user.has_perm("bbtest.super") or
                request.user.has_perm("bbtest.admin")):
            return super().dispatch(request, *args, **kwargs)
        if request.is_ajax():
            raise PermissionDenied("Permission denied for AJAX call")
        return super().dispatch(request, *args, **kwargs)