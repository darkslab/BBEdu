from django.forms import ModelForm
from bbtest.models import Subscription
from django.utils.translation import pgettext_lazy


class SubscriptionForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "phone", "message")
        error_messages = {
            "name": {
                "required": pgettext_lazy("Validation error", "Please enter name."),
                "invalid": pgettext_lazy("Validation error", "Incorrect name."),
                "max_length": pgettext_lazy("Validation error", "Name is too long."),
            },
            "email": {
                "required": pgettext_lazy("Validation error", "Please enter email."),
                "invalid": pgettext_lazy("Validation error", "Incorrect email."),
                "max_length": pgettext_lazy("Validation error", "Email is too long."),
            },
            "phone": {
                "required": pgettext_lazy("Validation error", "Please enter phone."),
                "invalid": pgettext_lazy("Validation error", "Incorrect phone."),
                "max_length": pgettext_lazy("Validation error", "Phone is too long."),
            },
            "message": {
                "required": pgettext_lazy("Validation error", "Please enter message."),
                "invalid": pgettext_lazy("Validation error", "Incorrect message."),
                "max_length": pgettext_lazy("Validation error", "Message is too long."),
            },

        }
