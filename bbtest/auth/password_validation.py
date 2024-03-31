import os
import gzip
from re import split
from difflib import SequenceMatcher
from django.utils.encoding import force_str
from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.contrib.auth import password_validation
from django.utils.translation import pgettext, pgettext_lazy
from django.contrib.auth.password_validation import password_validators_help_texts
from django.utils.html import format_html
from django.utils.six import text_type
from django.utils.functional import lazy


class BadPasswordValidator:
    def __init__(self):
        self.min_length = 8
        self.secure_length = 16

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                pgettext("Validation error", "The password has to be at least %(min_length)d characters."),
                code="password_too_short",
                params={
                    "min_length": self.min_length
                },
            )
        if len(password) < self.secure_length:
            if password.lower() == password:
                raise ValidationError(
                    pgettext("Validation error", "If the password is less than %(secure_length)d characters, it has to contain at least one uppercase character."),
                    code="password_bad",
                    params={
                        "secure_length": self.secure_length
                    },
                )
            if password.upper() == password:
                raise ValidationError(
                    pgettext("Validation error", "If the password is less than %(secure_length)d characters, it has to contain at least one lowercase character."),
                    code="password_bad",
                    params={
                        "secure_length": self.secure_length
                    },
                )
            has_numeric = False
            for c in password:
                if c.isnumeric():
                    has_numeric = True
                    break
            if not has_numeric:
                raise ValidationError(
                    pgettext("Validation error", "If the password is less than %(secure_length)d characters, it has to contain at least one numeric character."),
                    code="password_bad",
                    params={
                        "secure_length": self.secure_length
                    },
                )
            if password.isalnum():
                raise ValidationError(
                    pgettext("Validation error", "If the password is less than %(secure_length)d characters, it has to contain at least one symbol character."),
                    code="password_bad",
                    params={
                        "secure_length": self.secure_length
                    },
                )

    def get_help_text(self):
        return str(pgettext_lazy(
            "Password validation help text",
            "If the password is less than %(secure_length)d characters, it has to be at least %(min_length)d characters and contain uppercase, lowercase, numeric and a symbol character.",
        ) % {
            "secure_length": self.secure_length,
            "min_length": self.min_length,
        })


class MinLengthPasswordValidator:
    def __init__(self):
        self.min_length = 10

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                pgettext("Validation error", "The password has to be at least %(min_length)d characters."),
                code="password_too_short",
                params={
                    "min_length": self.min_length
                },
            )

    def get_help_text(self):
        return str(pgettext_lazy(
            "Password validation help text",
            "The password has to be at least %(min_length)d characters long.",
        ) % {
            "min_length": self.min_length,
        })


class UserAttributeSimilarityValidator:
    def __init__(self):
        self.user_attributes = ("first_name", "last_name", "email")
        self.special_user_attribute = "username"
        self.max_similarity = 0.7

    def validate(self, password, user=None):
        if not user:
            return

        user_attributes = []
        for attribute_name in self.user_attributes:
            user_attributes.append(attribute_name)
        if not user.email:
            user_attributes.append(self.special_user_attribute)

        for attribute_name in user_attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue
            value_parts = split(r"\W+", value) + [value]
            for value_part in value_parts:
                if SequenceMatcher(a=password.lower(), b=value_part.lower()).quick_ratio() >= self.max_similarity:
                    try:
                        verbose_name = force_str(user._meta.get_field(attribute_name).verbose_name)
                    except FieldDoesNotExist:
                        verbose_name = attribute_name
                    raise ValidationError(
                        pgettext("Validation error", "The password is too similar to the %(verbose_name)s."),
                        code="password_too_similar",
                        params={
                            "verbose_name": verbose_name
                        },
                    )

    def get_help_text(self):
        return str(pgettext_lazy("Password validation help text", "The password can't be too similar to your other personal information."))


class CommonPasswordValidator:
    DEFAULT_PASSWORD_LIST_PATH = os.path.join(
        os.path.dirname(os.path.realpath(password_validation.__file__)),
        "common-passwords.txt.gz",
    )

    def __init__(self):
        try:
            with gzip.open(self.DEFAULT_PASSWORD_LIST_PATH) as f:
                common_passwords_lines = f.read().decode("utf-8").splitlines()
        except IOError:
            with open(self.DEFAULT_PASSWORD_LIST_PATH) as f:
                common_passwords_lines = f.readlines()

        self.passwords = {p.strip() for p in common_passwords_lines}

    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                pgettext("Validation error", "The password is too common."),
                code="password_too_common",
            )

    def get_help_text(self):
        return str(pgettext_lazy("Password validation help text", "The password can't be a commonly used password."))


def _password_validators_help_text_html(password_validators=None):
    help_texts = password_validators_help_texts(password_validators)
    help_items = [format_html("<li>{}</li>", help_text) for help_text in help_texts]
    return "<ul class=\"list-narrow\">%s</ul>" % "".join(help_items) if help_items else ""
password_validators_help_text_html = lazy(_password_validators_help_text_html, text_type)
