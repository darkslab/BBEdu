from django.forms import CharField, EmailField, PasswordInput
from django.contrib.auth.forms import (
    AuthenticationForm as _AuthenticationForm,
    PasswordResetForm as _PasswordResetForm,
    SetPasswordForm as _SetPasswordForm,
)
from django.utils.translation import pgettext_lazy, pgettext
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages import success
from bbtest.forms.base import BaseUserForm
from bbtest.emails.password_reset import send_mail
from bbtest.auth.password_validation import password_validators_help_text_html
from bbtest.models import Account


class AuthenticationForm(_AuthenticationForm):
    username = CharField(label=pgettext_lazy("Form label", "Email"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter email."),
    })
    password = CharField(label=pgettext_lazy("Form label", "Password"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter password."),
    }, widget=PasswordInput, strip=False)
    error_messages = {
        "invalid_login": pgettext_lazy("Validation error", "Please enter a correct email and password."),
    }


class UserCreationForm(BaseUserForm):
    def save(self, group):
        user = super().save()

        content_type = ContentType.objects.get_for_model(type(user))
        permissions = []
        if group in ("developer", "student"):
            permissions.append(Permission.objects.get(codename=group, content_type=content_type))
        user.user_permissions.set(permissions)

        if group == "developer":
            Account.objects.create_liability_account("Developer-%s" % user.pk)

        return user


class PasswordResetForm(_PasswordResetForm):
    email = EmailField(label=pgettext_lazy("Form label", "Email"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter email."),
        "invalid": pgettext_lazy("Validation error", "Incorrect email."),
    })

    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        send_mail(to_email, context)

    def save(self, **kwargs):
        if "request" in kwargs:
            success(kwargs["request"], pgettext("Success alert message", "Please follow password reset instructions in the sent email."))
        super().save(**kwargs)


class SetPasswordForm(_SetPasswordForm):
    error_messages = {
        "password_mismatch": pgettext_lazy("Validation error", "Passwords do not match."),
    }
    new_password1 = CharField(label=pgettext_lazy("Form label", "New password"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter new password."),
    }, widget=PasswordInput, strip=False, help_text=password_validators_help_text_html())
    new_password2 = CharField(label=pgettext_lazy("Form label", "Confirm new password"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter new password confirmation."),
    }, widget=PasswordInput, strip=False)
