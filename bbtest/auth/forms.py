from django.forms import ValidationError, Form, ModelForm, CharField, EmailField, PasswordInput
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password, password_validators_help_texts
from django.contrib.auth.forms import (
    PasswordResetForm as _PasswordResetForm,
    SetPasswordForm as _SetPasswordForm,
)
from django.utils.translation import pgettext_lazy, pgettext
from django.contrib.messages import success
from uuid import uuid4
from bbtest.emails.password_reset import send_mail


User = get_user_model()


class AuthenticationForm(Form):
    username = CharField(label=pgettext_lazy("Form label", "Email"), error_messages={
        "required": pgettext_lazy("Form field error", "Please enter email."),
    })
    password = CharField(label=pgettext_lazy("Form label", "Password"), error_messages={
        "required": pgettext_lazy("Form field error", "Please enter password."),
    }, widget=PasswordInput, strip=False)

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self._user = None

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self._user = authenticate(self.request, username=username, password=password)
            if self._user is None:
                raise ValidationError(
                    pgettext("Authentication failed error", "Please enter a correct email and password."),
                    code="invalid_login",
                )

        return self.cleaned_data

    def get_user_id(self):
        if self._user:
            return self._user.id
        return None

    def get_user(self):
        return self._user


class UserCreationForm(ModelForm):
    password1 = CharField(label=pgettext_lazy("Form label", "Password"), error_messages={
        "required": pgettext_lazy("Form field error", "Please enter password."),
    }, widget=PasswordInput, strip=False, help_text=password_validators_help_texts())
    password2 = CharField(label=pgettext_lazy("Form label", "Confirm password"), error_messages={
        "required": pgettext_lazy("Form field error", "Please enter password confirmation."),
    }, widget=PasswordInput, strip=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        error_messages = {
            "first_name": {
                "required": pgettext_lazy("Form field error", "Please enter first name."),
                "max_length": pgettext_lazy("Form field error", "First name is too long."),
            },
            "last_name": {
                "required": pgettext_lazy("Form field error", "Please enter last name."),
                "max_length": pgettext_lazy("Form field error", "Last name is too long."),
            },
            "email": {
                "required": pgettext_lazy("Form field error", "Please enter email."),
                "invalid": pgettext_lazy("Form field error", "Incorrect email."),
                "max_length": pgettext_lazy("Form field error", "Email is too long."),
                "unique": pgettext_lazy("Form field error", "This email is already taken."),
            },
        }

    def __init__(self, group="student", *args, **kwargs):
        super().__init__(*args, **kwargs)
        if group not in ("admin", "developer", "student"):
            raise ValueError("%s is not a valid group" % group)
        self._group = group
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True
        self.fields["email"].empty_value = ""

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                pgettext("Form validation error", "Passwords do not match."),
                code="password_mismatch",
            )
        user_attributes = { key: self.cleaned_data.get(key) for key in self._meta.fields }
        validate_password(password2, User(**user_attributes))
        return password2

    def clean(self):
        super().clean()
        while True:
            self.instance.username = "%s_%s" % (self._group, uuid4().hex)
            if not User.objects.filter(username=self.instance.username).exists():
                break
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        if commit:
            user.save()
        return user


class PasswordResetForm(_PasswordResetForm):
    email = EmailField(label=pgettext_lazy("Form label", "Email"), error_messages={
        "required": pgettext_lazy("Form field error", "Please enter email."),
        "invalid": pgettext_lazy("Form field error", "Incorrect email."),
    })

    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        send_mail(to_email, context)

    def save(self, **kwargs):
        if "request" in kwargs:
            success(kwargs["request"], pgettext("Success alert message", "Please follow password reset instructions in the sent email."))
        super().save(**kwargs)


class SetPasswordForm(_SetPasswordForm):
    error_messages = {
        "password_mismatch": pgettext_lazy("Form validation error", "Passwords do not match."),
    }
    new_password1 = CharField(label=pgettext_lazy("Form label", "New password"), error_messages={
        "required": pgettext_lazy("Form field error", "Please enter new password."),
    }, widget=PasswordInput, strip=False, help_text=password_validators_help_texts())
    new_password2 = CharField(label=pgettext_lazy("Form label", "Confirm new password"), error_messages={
        "required": pgettext_lazy("Form field error", "Please enter new password confirmation."),
    }, widget=PasswordInput, strip=False)
