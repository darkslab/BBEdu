from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy, pgettext
from bbtest.models import DeveloperAcknowledgement
from bbtest.utils import remote_ip


class DeveloperAcknowledgementForm(ModelForm):
    class Meta:
        model = DeveloperAcknowledgement
        fields = ("plan", "agreement_code")
        widgets = {
            "plan": HiddenInput,
            "agreement_code": HiddenInput,
        }
        error_messages = {
            "plan": {
                "required": pgettext_lazy("Validation error", "Please select plan."),
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect plan value."),
            },
            "agreement_code": {
                "required": pgettext_lazy("Validation error", "Please select agreement code."),
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect agreement code value."),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # DARK_TODO  remove this when more developer plans are available
        self.fields["plan"].choices = [ DeveloperAcknowledgement.PLANS[0] ]
        self.fields["agreement_code"].choices = [ DeveloperAcknowledgement.AGREEMENT_CODES[0] ]

    def clean(self):
        if self.cleaned_data.get("plan") is None or self.cleaned_data.get("agreement_code") is None:
            return self.cleaned_data

        if self.cleaned_data.get("agreement_code") != DeveloperAcknowledgement.AGREEMENT_CODES_FOR_PLANS[self.cleaned_data.get("plan")]:
            raise ValidationError(
                pgettext("Validation error", "Agreement code does not match the plan."),
                code="mismatch",
            )

        return self.cleaned_data

    def make_acknowledgement(self, request):
        acknowledgement = self.save(commit=False)
        acknowledgement.signature = "(signed)"
        acknowledgement.ip_address = remote_ip(request)
        acknowledgement.user_agent = request.META.get("HTTP_USER_AGENT")
        acknowledgement.developer = request.user
        acknowledgement.save()
        return acknowledgement
