from django.forms.fields import CharField
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext
from json import loads


class JSONField(CharField):
    def to_python(self, value):
        value = super().to_python(value)
        if value in self.empty_values:
            return None
        try:
            value = loads(value)
        except (ValueError, TypeError):
            raise ValidationError(
                pgettext("Validation error", "Invalid JSON format"),
                code="invalid",
            )
        return value
