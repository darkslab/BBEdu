from django.contrib.auth.management.commands.createsuperuser import (
    Command as CreateSuperUserCommand,
)
from django.core.exceptions import ValidationError


class Command(CreateSuperUserCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel.REQUIRED_FIELDS = [self.UserModel.EMAIL_FIELD]

    def get_input_data(self, field, message, default=None):
        if field.name != "email":
            return super().get_input_data(field, message, default)

        raw_value = input(message)
        if raw_value == "":
            raw_value = None
        if default and raw_value is None:
            raw_value = default
        try:
            val = field.clean(raw_value, None)
            if val is None:
                self.stderr.write("Error: Email is required.")
            elif self.UserModel._default_manager.filter(email=val).exists():
                self.stderr.write("Error: That email is already taken.")
                val = None
        except ValidationError as error:
            self.stderr.write("Error: %s" % "; ".join(error.messages))
            val = None

        return val
