from django.forms import ValidationError, ModelForm, Form, CharField, PasswordInput, IntegerField, TextInput, ChoiceField, HiddenInput
from django.utils.translation import pgettext_lazy, pgettext
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from uuid import uuid4
from bbtest.auth.password_validation import password_validators_help_text_html
from bbtest.models.shopping.items.credit import MAX_CREDIT_AMOUNT, MIN_CREDIT_AMOUNT


User = get_user_model()


class BaseUserForm(ModelForm):
    require_password = True

    password1 = CharField(label=pgettext_lazy("Form label", "Password"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter password."),
    }, widget=PasswordInput, strip=False, help_text=password_validators_help_text_html())
    password2 = CharField(label=pgettext_lazy("Form label", "Confirm password"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter password confirmation."),
    }, widget=PasswordInput, strip=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone")
        error_messages = {
            "first_name": {
                "required": pgettext_lazy("Validation error", "Please enter first name."),
                "max_length": pgettext_lazy("Validation error", "First name is too long."),
            },
            "last_name": {
                "required": pgettext_lazy("Validation error", "Please enter last name."),
                "max_length": pgettext_lazy("Validation error", "Last name is too long."),
            },
            "email": {
                "required": pgettext_lazy("Validation error", "Please enter email."),
                "invalid": pgettext_lazy("Validation error", "Incorrect email."),
                "max_length": pgettext_lazy("Validation error", "Email is too long."),
                "unique": pgettext_lazy("Validation error", "This email is already taken."),
            },
            "phone": {
                "max_length": pgettext_lazy("Validation error", "Phone is too long."),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True
        self.fields["email"].empty_value = ""
        if not self.require_password:
            self.fields["password1"].required = False
            self.fields["password2"].required = False

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 or password2:
            if password1 != password2:
                raise ValidationError(
                    pgettext("Validation error", "Passwords do not match."),
                    code="password_mismatch",
                )
            else:
                user_attributes = { key: self.cleaned_data.get(key) for key in self._meta.fields }
                validate_password(password2, User(**user_attributes))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get("password1"):
            user.set_password(self.cleaned_data.get("password1"))
        if not user.username:
            while True:
                user.username = uuid4().hex
                if not User.objects.filter(username=user.username).exists():
                    break
        if commit:
            user.save()
        return user


class BuyCreditsForm(Form):
    amount = IntegerField(label=pgettext_lazy("Form label", "Amount"), error_messages={
        "required": pgettext_lazy("Validation error", "Please provide an amount."),
        "invalid": pgettext_lazy("Validation error", "Amount is invalid."),
        "max_value": pgettext_lazy("Validation error", "Amount cannot be more than %(limit_value)s."),
        "min_value": pgettext_lazy("Validation error", "Amount has to be at least %(limit_value)s."),
    }, widget=TextInput, max_value=int(MAX_CREDIT_AMOUNT), min_value=int(MIN_CREDIT_AMOUNT))
    payment_type = ChoiceField(label=pgettext_lazy("Form label", "Payment type"), error_messages={
        "required": pgettext_lazy("Validation error", "Please provide an payment type."),
        "invalid_choice": pgettext_lazy("Validation error", "Payment type is invalid."),
    }, widget=HiddenInput, choices=(
        ( "card", None ),
        ( "beeline", None ),
    ))
