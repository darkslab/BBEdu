from django.db.models import TextField
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy
from json import loads, dumps
from bbtest.forms.fields import JSONField as JSONFormField


class JSONField(TextField):
    empty_strings_allowed = False
    default_error_messages = {
        "invalid": pgettext_lazy("Validation error", "Invalid JSON format"),
    }
    description = pgettext_lazy("Field class description", "JSON")

    def __init__(self, *args, **kwargs):
        if "max_length" in kwargs:
            del kwargs["max_length"]
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if "max_length" in kwargs:
            del kwargs["max_length"]
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return None
        try:
            value = loads(value)
        except ValueError:
            return None
        return value

    def to_python(self, value):
        if value is None:
            return None
        try:
            if isinstance(value, str):
                value = loads(value)
            else:
                dumps(value, separators=(",", ":"))
        except (ValueError, TypeError):
            raise ValidationError(
                self.error_messages["invalid"],
                code="invalid",
            )
        return value

    def get_prep_value(self, value):
        if value is None and self.null:
            return None
        try:
            value = dumps(value, separators=(",", ":"))
        except TypeError:
            if self.null:
                return None
            return dumps(None)
        return value

    def formfield(self, **kwargs):
        defaults = {
            "form_class": JSONFormField,
        }
        defaults.update(**kwargs)
        return super().formfield(**defaults)
