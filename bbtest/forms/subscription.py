from django.forms import ModelForm
from bbtest.models import Subscription
from django.utils.translation import pgettext_lazy


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ("email",)
        error_messages = {
            "email": {
                "required": pgettext_lazy("Validation error", "Please enter email."),
                "invalid": pgettext_lazy("Validation error", "Incorrect email."),
                "max_length": pgettext_lazy("Validation error", "Email is too long."),
            }
        }
