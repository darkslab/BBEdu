from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from django.utils.translation import pgettext_lazy
from bbtest.models import DeveloperAcknowledgement
from bbtest.utils import remote_ip


class DeveloperAcknowledgementForm(ModelForm):
    class Meta:
        model = DeveloperAcknowledgement
        fields = ("plan",)
        widgets = {
            "plan": HiddenInput,
        }
        error_messages = {
            "plan": {
                "required": pgettext_lazy("Validation error", "Please select plan."),
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect plan value."),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # DARK_TODO  remove this when more developer plans are available
        self.fields["plan"].choices = [ DeveloperAcknowledgement.PLANS[0] ]

    def make_acknowledgement(self, request):
        acknowledgement = self.save(commit=False)
        acknowledgement.signature = "(signed)"
        acknowledgement.ip_address = remote_ip(request)
        acknowledgement.user_agent = request.META.get("HTTP_USER_AGENT")
        acknowledgement.developer = request.user
        acknowledgement.save()
        return acknowledgement
