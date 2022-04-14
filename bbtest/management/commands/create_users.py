from django.core.management.base import BaseCommand
from bbtest.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from bbtest.models import Account

User.objects.all()

# User.objects.create(username="student_01",
#                     email="student_01@example.com",
#                     first_name="Dimon",
#                     last_name="Electric")


def create_students():
    user = User.objects.create_user(username="student_02", email="student_02@example.com", password="monkeymonkey")
    user.first_name = "Dimon"
    user.last_name = "Electric"
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="student", content_type=content_type))
    user.user_permissions.set(permissions)
    return user


# username = CharField(pgettext_lazy("Model field", "username"), max_length=100, unique=True)
# email = EmailField(pgettext_lazy("Model field", "email"), max_length=100, null=True, blank=True, unique=True)
# first_name = CharField(pgettext_lazy("Model field", "first name"), max_length=100, blank=True)
# last_name = CharField(pgettext_lazy("Model field", "last name"), max_length=100, blank=True)
# phone = CharField(pgettext_lazy("Model field", "phone"), max_length=100, blank=True)
# meta_data = JSONField(pgettext_lazy("Model field", "meta_data"), null=True, blank=True)
# joined_at = DateTimeField(pgettext_lazy("Model field", "joined at"), auto_now_add=True, db_index=True)
# is_active = BooleanField(pgettext_lazy("Model field", "active?"), db_index=True, default=True)


def create_developer():
    user = User.objects.create_user(username="dev_02", email="dev_02@example.com", password="monkeymonkey")
    user.first_name = "Dimon"
    user.last_name = "Dev"
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="developer", content_type=content_type))
    user.user_permissions.set(permissions)
    Account.objects.create_liability_account("Developer-%s" % user.pk)
    return user


