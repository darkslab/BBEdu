from django.forms import ValidationError, CharField, PasswordInput
from django.utils.translation import pgettext_lazy, pgettext
from .base import BaseUserForm


class SettingsForm(BaseUserForm):
    require_password = False

    old_password = CharField(label=pgettext_lazy("Form label", "Old password"), error_messages={
        "required": pgettext_lazy("Validation error", "Please enter old password."),
    }, widget=PasswordInput, strip=False, required=False)

    field_order = [
        "first_name",
        "last_name",
        "email",
        "old_password",
        "password1",
        "password2",
    ]

    def clean(self):
        super().clean()
        if self.cleaned_data["password1"] or self.cleaned_data["password2"]:
            if not self.instance.check_password(self.cleaned_data["old_password"]):
                self.add_error("old_password", ValidationError(
                    pgettext("Validation error", "Incorrect old password."),
                    code="password_incorrect",
                ))
