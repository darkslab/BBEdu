from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models import CharField, EmailField, DateTimeField, BooleanField
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, email=None):
        user = self.__create_unsaved_user(username, password, email)
        user.save()
        return user

    def create_superuser(self, username, password, email=None):
        user = self.__create_unsaved_user(username, password, email)
        user.is_superuser = True
        user.save()
        return user

    def __create_unsaved_user(self, username, password=None, email=None):
        try:
            if len(username) < self.model.USERNAME_LENGTH_MIN:
                raise ValueError("Username has to be at least %s characters" % self.model.USERNAME_LENGTH_MIN)
            user = self.model(username=username)
            if email is not None:
                user.email = self.normalize_email(email)
            user.set_password(password)
            user.full_clean()
        except ValidationError:
            raise ValueError("Please provide correct user data")
        return user

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_LENGTH_MAX = 200
    USERNAME_LENGTH_MIN = 5

    username = CharField(max_length=USERNAME_LENGTH_MAX, unique=True)
    email = EmailField(max_length=USERNAME_LENGTH_MAX, null=True, blank=True, unique=True)
    first_name = CharField(max_length=100, blank=True)
    last_name = CharField(max_length=100, blank=True)
    joined_at = DateTimeField(auto_now_add=True)
    is_active = BooleanField(default=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        default_permissions = ()
        permissions = (
            ("admin", "Can act as an Admin"),
            ("developer", "Can act as a Developer"),
            ("student", "Can act as a Student"),
        )

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        full_name = " ".join([
            self.first_name,
            self.last_name,
        ])
        if full_name != " ":
            return full_name
        return self.username

    def get_short_name(self):
        if len(self.first_name):
            return self.first_name
        return self.username
