from django.core.management.base import BaseCommand
from bbtest.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from bbtest.models import Account


def create_students(password, first_name = "Саке", username="student_01", email="student_01@example.com"):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = ""
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="student", content_type=content_type))
    user.user_permissions.set(permissions)
    return user


def create_developer(password, username="Dev", email=None, first_name = "Dev", last_name = ""):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="developer", content_type=content_type))
    user.user_permissions.set(permissions)
    Account.objects.create_liability_account("Developer-%s" % user.pk)
    return user

    # Account: Developer-3972 Iqanat

def create_admin(password, first_name = "Admin", username="Admin", email=None):
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

def create_expert(password, username="Expert", email=None, first_name = "Ethernal", last_name = "Secret Expert"):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
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
        # user = create_students()
        # print(user)
        user = create_developer("shmonkey_dev", username="Dev-007", first_name = "Ethernal", last_name = "Secret Expert")
        print(user)
        # user = create_admin()
        # print(user)
        user = create_expert("shmonkey_expert", username="Expert-007", first_name = "Ethernal", last_name = "Secret Expert")
        print(user)

# username = CharField(pgettext_lazy("Model field", "username"), max_length=100, unique=True)
# email = EmailField(pgettext_lazy("Model field", "email"), max_length=100, null=True, blank=True, unique=True)
# first_name = CharField(pgettext_lazy("Model field", "first name"), max_length=100, blank=True)
# last_name = CharField(pgettext_lazy("Model field", "last name"), max_length=100, blank=True)
# phone = CharField(pgettext_lazy("Model field", "phone"), max_length=100, blank=True)
# meta_data = JSONField(pgettext_lazy("Model field", "meta_data"), null=True, blank=True)
# joined_at = DateTimeField(pgettext_lazy("Model field", "joined at"), auto_now_add=True, db_index=True)
# is_active = BooleanField(pgettext_lazy("Model field", "active?"), db_index=True, default=True)





