from django.contrib.auth.mixins import LoginRequiredMixin as _LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings


class LoginRequiredMixin(_LoginRequiredMixin):
    login_url = reverse_lazy("bbtest:login")
    permission_denied_message = "Please login."
    redirect_field_name = settings.BB_REDIRECT_FIELDNAME
