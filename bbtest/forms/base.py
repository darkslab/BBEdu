import re
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.forms import (
    BooleanField,
    CharField,
    ChoiceField,
    Form,
    HiddenInput,
    IntegerField,
    ModelForm,
    PasswordInput,
    TextInput,
    ValidationError,
)
from django.utils.translation import pgettext, pgettext_lazy

from bbtest.auth.password_validation import password_validators_help_text_html
from bbtest.models import REGIONS
from bbtest.models.shopping.items.credit import MAX_CREDIT_AMOUNT, MIN_CREDIT_AMOUNT

User = get_user_model()


class BaseUserForm(ModelForm):
    require_password = True
    allow_weak_password = False

    password1 = CharField(
        label=pgettext_lazy("Form label", "Password"),
        error_messages={
            "required": pgettext_lazy("Validation error", "Please enter password."),
        },
        widget=PasswordInput,
        strip=False,
        help_text=password_validators_help_text_html(),
    )
    password2 = CharField(
        label=pgettext_lazy("Form label", "Confirm password"),
        error_messages={
            "required": pgettext_lazy("Validation error", "Please enter password confirmation."),
        },
        widget=PasswordInput,
        strip=False,
    )

    user_agreement = BooleanField(
        label=pgettext_lazy("Form label", "User Agreement"),
        required=False,
        # error_messages={
        #     "required": pgettext_lazy("Validation error", "Please enter password confirmation."),
        # },
    )

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
        self._meta_data = None

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
                if not self.allow_weak_password:
                    validate_password(password2, User(**user_attributes))
        return password2

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        # Regex to validate the phone number
        phone_regex = re.compile(r'^(?:\+?7|8)\(?7\d\d\)?\d{7}$')
        if not phone_regex.match(phone):
            raise ValidationError(
                pgettext("Validation error", "Wrong phone format. Acceptable formats are 87071112233, +7(707)1112233, "),
                code="phone_wrong_format",
            )

        return phone
    
    def clean_user_agreement(self):
        user_agreement = self.cleaned_data["user_agreement"]
        if not user_agreement:
            raise ValidationError(
                pgettext("Validation error", "To use site you must agree with terms."),
                code="user_agreement",
            )

        return user_agreement

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get("password1"):
            user.set_password(self.cleaned_data.get("password1"))
        if not user.username:
            while True:
                user.username = uuid4().hex
                if not User.objects.filter(username=user.username).exists():
                    break
        if self._meta_data:
            user.meta_data = self._meta_data
        if commit:
            user.save()
        return user


class ExtendedBaseUserForm(BaseUserForm):
    identification = IntegerField(label=pgettext_lazy("Form label", "ID"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter an ID."),
        "invalid": pgettext_lazy("Validation error", "Incorrect ID."),
        "max_value": pgettext_lazy("Validation error", "ID contains too many numbers."),
        "min_value": pgettext_lazy("Validation error", "ID contains too few numbers."),
    }, max_value=999999999999, min_value=10000000000, required=True)
    region = ChoiceField(label=pgettext_lazy("Form label", "Region"), error_messages={
        "required": pgettext_lazy("Validation error", "Please select a region."),
        "invalid_choice": pgettext_lazy("Validation error", "Please select a correct region."),
    }, choices=REGIONS, required=True)
    district = CharField(label=pgettext_lazy("Form label", "District"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter a district."),
        "max_length": pgettext_lazy("Validation error", "District is too long."),
    }, max_length=100, required=True)
    village = CharField(label=pgettext_lazy("Form label", "Village"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter a village."),
        "max_length": pgettext_lazy("Validation error", "Village is too long."),
    }, max_length=100, required=True)
    school = CharField(label=pgettext_lazy("Form label", "School"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter a school."),
        "max_length": pgettext_lazy("Validation error", "School is too long."),
    }, max_length=100, required=True)

    def clean(self):
        self._meta_data = {}
        if self.cleaned_data.get("identification"):
            self._meta_data["identification"] = self.cleaned_data["identification"]
        if self.cleaned_data.get("region"):
            self._meta_data["region"] = self.cleaned_data["region"]
        if self.cleaned_data.get("district"):
            self._meta_data["district"] = self.cleaned_data["district"]
        if self.cleaned_data.get("village"):
            self._meta_data["village"] = self.cleaned_data["village"]
        if self.cleaned_data.get("school"):
            self._meta_data["school"] = self.cleaned_data["school"]
        if not self._meta_data:
            self._meta_data = None
        return super().clean()


class DemoUserForm(ModelForm):
    require_password = False
    allow_weak_password = True

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
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False
        self.fields["email"].required = False
        self.fields["email"].empty_value = ""
        # if not self.require_password:
        #     self.fields["password1"].required = False
        #     self.fields["password2"].required = False
        self._meta_data = None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(uuid4().hex)
            
        if not user.username:
            while True:
                user.username = uuid4().hex
                user.email = f"{user.username}@demouser.kz"
                if not User.objects.filter(username=user.username).exists():
                    break
        
        if self._meta_data:
            user.meta_data = self._meta_data

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
        "required": pgettext_lazy("Validation error", "Please provide a payment type."),
        "invalid_choice": pgettext_lazy("Validation error", "Payment type is invalid."),
    }, widget=HiddenInput, choices=(
        ( "card", None ),
        ( "beeline", None ),
    ))
