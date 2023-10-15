from django.core.management.base import BaseCommand
from bbtest.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from bbtest.models import Account

# User.objects.all()

# User.objects.create(username="student_01",
#                     email="student_01@example.com",
#                     first_name="Dimon",
#                     last_name="Electric")


def create_students(first_name = "Саке", username="student_01", email="student_01@example.com", password="monkey"):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = ""
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="student", content_type=content_type))
    user.user_permissions.set(permissions)
    return user


def create_developer(first_name = "Dev", username="Dev", email=None, password="monkey"):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = ""
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="developer", content_type=content_type))
    user.user_permissions.set(permissions)
    Account.objects.create_liability_account("Developer-%s" % user.pk)
    return user

    # Account: Developer-3972 Iqanat

def create_admin(first_name = "Admin", username="Admin", email=None, password="monkey"):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = ""
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="admin", content_type=content_type))
    user.user_permissions.set(permissions)
    Account.objects.create_liability_account("Admin-%s" % user.pk)
    return user

def create_expert(first_name = "Expert", username="Expert", email=None, password="monkey"):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = ""
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="expert", content_type=content_type))
    user.user_permissions.set(permissions)
    Account.objects.create_liability_account("Expert-%s" % user.pk)
    return user


class Command(BaseCommand):
    help = 'generate NIS bundles from existing tests' 


    def handle(self, *args, **kwargs):
        user = create_students(first_name = "Саке", username="student_01", email="student_01@example.com")
        user = create_students(first_name = "Баке", username="student_02", email="student_02@example.com")

        user = create_developer(first_name = "Dev-01", username="Dev-01")
        user = create_developer(first_name = "Dev-02", username="Dev-02")

        user = create_admin(first_name = "Admin-01", username="Admin-01")
        user = create_admin(first_name = "Admin-02", username="Admin-02")

        user = create_expert(first_name = "Expert-01", username="Expert-01")
        user = create_expert(first_name = "Expert-02", username="Expert-02")

# username = CharField(pgettext_lazy("Model field", "username"), max_length=100, unique=True)
# email = EmailField(pgettext_lazy("Model field", "email"), max_length=100, null=True, blank=True, unique=True)
# first_name = CharField(pgettext_lazy("Model field", "first name"), max_length=100, blank=True)
# last_name = CharField(pgettext_lazy("Model field", "last name"), max_length=100, blank=True)
# phone = CharField(pgettext_lazy("Model field", "phone"), max_length=100, blank=True)
# meta_data = JSONField(pgettext_lazy("Model field", "meta_data"), null=True, blank=True)
# joined_at = DateTimeField(pgettext_lazy("Model field", "joined at"), auto_now_add=True, db_index=True)
# is_active = BooleanField(pgettext_lazy("Model field", "active?"), db_index=True, default=True)





