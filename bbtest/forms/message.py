from django.forms import ModelForm
from django.utils.translation import pgettext_lazy, pgettext, ugettext_lazy
from django.core.exceptions import ValidationError
from django.conf import settings
from requests import post
from requests.exceptions import RequestException
from bbtest.models import Message
from bbtest.emails.message import send_mail


class MessageForm(ModelForm):
    error_messages = {
        "recaptcha": ugettext_lazy("_common.validation.message_form.recaptcha"),
    }

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

    def save(self, commit=True):
        message = super().save(commit=False)

        if commit:
            message.save()
            send_mail(message)

        return message

    def clean(self):
        kwargs = {
            "headers": {
                "User-Agent": settings.BB_USER_AGENT,
            },
            "timeout": 8,
        }

        try:
            response = post(settings.RECAPTCHA_URL, data={
                "secret": settings.SECRETS["RECAPTCHA_SECRET_KEY"],
                "response": self.data["g-recaptcha-response"],
            }, **kwargs)
            if response.status_code != 200 or not response.json()["success"]:
                raise ValueError("Incorrect reCAPTCHA")
        except (RequestException, ValueError, KeyError):
            raise ValidationError(
                self.error_messages["recaptcha"],
                code="recaptcha",
            )

        return self.cleaned_data
