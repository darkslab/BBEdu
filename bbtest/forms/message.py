from django.forms import ModelForm
from django.utils.translation import pgettext_lazy, pgettext
from bbtest.models import Message
from bbtest.emails.message import send_mail


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ("name", "phone", "email", "message")
        error_messages = {
            "name": {
                "max_length": pgettext_lazy("Validation error", "Name is too long."),
            },
            "phone": {
                "max_length": pgettext_lazy("Validation error", "Phone is too long."),
            },
            "email": {
                "max_length": pgettext_lazy("Validation error", "Email is too long."),
            },
            "message": {
                "required": pgettext_lazy("Validation error", "Please enter the message."),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["message"].widget.attrs["placeholder"] = pgettext("/contact_us/", "Hello...")
        self.fields["message"].widget.attrs["rows"] = "6"

    def save(self, request, commit=True):
        message = super().save(commit=False)

        if commit:
            send_mail()
            message.save()

        return message
