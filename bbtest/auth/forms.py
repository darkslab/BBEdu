from django.forms import ValidationError, Form, ModelForm, CharField, PasswordInput
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import pgettext as _
from uuid import uuid4


User = get_user_model()

class AuthenticationForm(Form):
    username = CharField(label=_("Form label", "Email"), error_messages={
        "required": _("Form field error", "Please enter email"),
    })
    password = CharField(label=_("Form label", "Password"), error_messages={
        "required": _("Form field error", "Please enter password"),
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
                    _("Authentication failed error", "Please enter a correct email and password."),
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
    password1 = CharField(label=_("Form label", "New password"), error_messages={
        "required": _("Form field error", "Please enter password"),
    }, widget=PasswordInput, strip=False)
    password2 = CharField(label=_("Form label", "Confirm password"), error_messages={
        "required": _("Form field error", "Please enter password confirmation"),
    }, widget=PasswordInput, strip=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        error_messages = {
            "first_name": {
                "required": _("Form field error", "Please enter first name"),
                "max_length": _("Form field error", "First name is too long"),
            },
            "last_name": {
                "required": _("Form field error", "Please enter last name"),
                "max_length": _("Form field error", "Last name is too long"),
            },
            "email": {
                "required": _("Form field error", "Please enter email"),
                "invalid": _("Form field error", "Incorrect email"),
                "max_length": _("Form field error", "Email is too long"),
                "unique": _("Form field error", "This email is already taken"),
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
                _("Form validation error", "Passwords do not match"),
                code="password_mismatch",
            )
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
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
