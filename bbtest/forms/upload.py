from django.forms import ModelForm, Form
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now
from datetime import timedelta
from uuid import uuid4
from bbtest.models import Upload
from .fields import JSONField
import bbtest.upload_starters


class UploadStartForm(ModelForm):
    error_messages = {
        "incorrect": pgettext_lazy("Validation error", "Incorrect upload starter data."),
    }

    upload_starter = JSONField(label=pgettext_lazy("Form label", "Upload starter"), error_messages={
        "required": pgettext_lazy("Validation error", "Please provide upload starter data."),
    })

    class Meta:
        model = Upload
        fields = ("file_name", "file_size", "file_type")
        error_messages = {
            "file_name": {
                "required": pgettext_lazy("Validation error", "Please provide file name."),
                "max_length": pgettext_lazy("Validation error", "File name is too long."),
            },
            "file_size": {
                "required": pgettext_lazy("Validation error", "Please provide file size."),
                "invalid": pgettext_lazy("Validation error", "Incorrect file size value."),
            },
            "file_type": {
                "max_length": pgettext_lazy("Validation error", "File content type value is too long."),
            },
        }

    def __init__(self, origin, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._origin = origin
        self._upload_starter = None
        self._upload_starter_kwargs = {}

    def clean_file_size(self):
        file_size = self.cleaned_data["file_size"]
        if file_size <= 0:
            raise ValidationError(
                self._meta.error_messages["file_size"]["invalid"],
                code="invalid",
            )
        return file_size

    def clean_upload_starter(self):
        upload_starter = self.cleaned_data["upload_starter"]

        try:
            if not isinstance(upload_starter, dict):
                raise ValueError("Incorrect upload_starter")
            if not isinstance(upload_starter["name"], str):
                raise ValueError("Incorrect upload_starter")
            self._upload_starter = getattr(bbtest.upload_starters, upload_starter["name"])

            if "kwargs" in upload_starter:
                if not isinstance(upload_starter["kwargs"], dict):
                    raise ValueError("Incorrect upload_starter")
                for key, value in upload_starter["kwargs"].items():
                    if not isinstance(value, str):
                        raise ValueError("Incorrect upload_starter")
                    self._upload_starter_kwargs[key] = value

        except (KeyError, ValueError, AttributeError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return upload_starter

    def save(self, commit=True):
        upload = super().save(commit=False)

        if not upload.uuid:
            while True:
                upload.uuid = uuid4().hex
                if not Upload.objects.filter(uuid=upload.uuid).exists():
                    break
        upload.expire_at = now() + timedelta(days=7)
        upload.upload_url = upload.generate_upload_url(self._origin)

        if commit:
            upload.save()
        return upload

    def upload_starter_function(self):
        return self._upload_starter

    def upload_starter_kwargs(self):
        return self._upload_starter_kwargs


class UploadAdoptForm(Form):
    error_messages = {
        "incorrect": pgettext_lazy("Validation error", "Incorrect data."),
    }

    data = JSONField(label=pgettext_lazy("Form label", "Data"), error_messages={
        "required": pgettext_lazy("Validation error", "Please provide data."),
    })

    def clean_data(self):
        data = self.cleaned_data["data"]
        try:
            if not isinstance(data, dict):
                raise ValueError("Incorrect data")
            for key, value in data.items():
                if not isinstance(value, str):
                    raise ValueError("Incorrect data")

        except ValueError:
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return data
