from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models import CharField, EmailField, DateTimeField, BooleanField
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy
from django.shortcuts import resolve_url


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        user = self.__create_unsaved_user(username, email, password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.__create_unsaved_user(username, email, password)
        user.is_superuser = True
        user.save()
        return user

    def __create_unsaved_user(self, username, email, password):
        try:
            user = self.model(username=username, email=email)
            user.set_password(password)
            user.full_clean()
        except ValidationError:
            raise ValueError("Given arguments have to be: username is required and has to be unique, email is not required but has to be unique")
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = CharField(pgettext_lazy("Model field", "username"), max_length=100, unique=True)
    email = EmailField(pgettext_lazy("Model field", "email"), max_length=100, null=True, blank=True, unique=True)
    first_name = CharField(pgettext_lazy("Model field", "first name"), max_length=100, blank=True)
    last_name = CharField(pgettext_lazy("Model field", "last name"), max_length=100, blank=True)
    joined_at = DateTimeField(pgettext_lazy("Model field", "joined at"), auto_now_add=True, db_index=True)
    is_active = BooleanField(pgettext_lazy("Model field", "active?"), db_index=True, default=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        default_permissions = ()
        permissions = (
            ("super", "Can act as a Super"),
            ("admin", "Can act as an Admin"),
            ("developer", "Can act as a Developer"),
            ("student", "Can act as a Student"),
        )

    def clean(self):
        super().clean()
        if self.email is not None:
            self.email = type(self).objects.normalize_email(self.email)

    def __str__(self):
        return self.get_full_name()
    def get_absolute_url(self):
        if self.has_perm("bbtest.super"):
            return resolve_url("bbtest:super_dashboard")
        if self.has_perm("bbtest.admin"):
            return resolve_url("bbtest:admin_dashboard")
        if self.has_perm("bbtest.developer"):
            return resolve_url("bbtest:developer_dashboard")
        if self.has_perm("bbtest.student"):
            return resolve_url("bbtest:student_dashboard")
        return resolve_url("home")

    def get_full_name(self):
        full_name_values = []
        if len(self.first_name):
            full_name_values.append(self.first_name)
        if len(self.last_name):
            full_name_values.append(self.last_name)
        if len(full_name_values):
            return " ".join(full_name_values)
        return self.username

    def get_short_name(self):
        if len(self.first_name):
            return self.first_name
        return self.username
