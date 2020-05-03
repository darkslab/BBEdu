from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models import CharField, EmailField, DateTimeField, BooleanField
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy, ugettext_lazy
from django.urls import reverse
from django.apps import apps
from django.db.models import Q
from hashlib import md5
from urllib.parse import urlencode
from bbtest.models.fields import JSONField


REGIONS = (
    ( "",          ugettext_lazy("_common.regions.select")          ),
    ( "akmola",    ugettext_lazy("_common.regions.names.akmola")    ),
    ( "aktobe",    ugettext_lazy("_common.regions.names.aktobe")    ),
    ( "almaty",    ugettext_lazy("_common.regions.names.almaty")    ),
    ( "atyrau",    ugettext_lazy("_common.regions.names.atyrau")    ),
    ( "west_kz",   ugettext_lazy("_common.regions.names.west_kz")   ),
    ( "zhambyl",   ugettext_lazy("_common.regions.names.zhambyl")   ),
    ( "karaganda", ugettext_lazy("_common.regions.names.karaganda") ),
    ( "kostanai",  ugettext_lazy("_common.regions.names.kostanai")  ),
    ( "kyzylorda", ugettext_lazy("_common.regions.names.kyzylorda") ),
    ( "magistau",  ugettext_lazy("_common.regions.names.magistau")  ),
    ( "pavlodar",  ugettext_lazy("_common.regions.names.pavlodar")  ),
    ( "north_kz",  ugettext_lazy("_common.regions.names.north_kz")  ),
    ( "turkestan", ugettext_lazy("_common.regions.names.turkestan") ),
    ( "east_kz",   ugettext_lazy("_common.regions.names.east_kz")   ),
)


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

class ActiveUsersManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class User(AbstractBaseUser, PermissionsMixin):
    username = CharField(pgettext_lazy("Model field", "username"), max_length=100, unique=True)
    email = EmailField(pgettext_lazy("Model field", "email"), max_length=100, null=True, blank=True, unique=True)
    first_name = CharField(pgettext_lazy("Model field", "first name"), max_length=100, blank=True)
    last_name = CharField(pgettext_lazy("Model field", "last name"), max_length=100, blank=True)
    phone = CharField(pgettext_lazy("Model field", "phone"), max_length=100, blank=True)
    meta_data = JSONField(pgettext_lazy("Model field", "meta_data"), null=True, blank=True)
    joined_at = DateTimeField(pgettext_lazy("Model field", "joined at"), auto_now_add=True, db_index=True)
    is_active = BooleanField(pgettext_lazy("Model field", "active?"), db_index=True, default=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    active_users = ActiveUsersManager()

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
            return reverse("bbtest:super_dashboard")
        if self.has_perm("bbtest.admin"):
            return reverse("bbtest:admin_dashboard")
        if self.has_perm("bbtest.developer"):
            return reverse("bbtest:developer_dashboard")
        if self.has_perm("bbtest.student"):
            return reverse("bbtest:student_dashboard")
        return reverse("home")

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

    def gravatar_url(self):
        gravatar_hash = ""
        if self.email:
            gravatar_hash = md5(self.email.strip().lower().encode("utf-8")).hexdigest()
        return "https://www.gravatar.com/avatar/%s?%s" % (
            gravatar_hash,
            urlencode({
                "s": "600",
                "r": "pg",
                "d": "mm",
            }),
        )

    def cart(self):
        Cart = apps.get_model("bbtest", "Cart")
        try:
            return self.carts.get(is_current=True)
        except Cart.DoesNotExist:
            return Cart(buyer=self, is_current=True)

    def balance_account_name(self):
        if not self.pk:
            return None
        return "BalanceAccount-%s" % self.pk

    def balance_account(self):
        try:
            self.__balance_account
        except AttributeError:
            self.__balance_account = apps.get_model("bbtest", "BalanceAccount").objects.get(name=self.balance_account_name())
        return self.__balance_account

    def obtained_test_ids(self):
        try:
            self.__obtained_test_ids
        except AttributeError:
            self.__obtained_test_ids = [ data[0] for data in apps.get_model("bbtest", "Quiz").objects.filter(quiz_set__student=self).order_by("quiz_set", "order").values_list("test") ]
        return self.__obtained_test_ids

    def next_tests(self, domain, language):
        try:
            self.__next_tests
        except AttributeError:
            # DARK_COMM  Maybe we can invent a system to simplify this
            Test = apps.get_model("bbtest", "Test")
            query_sets = []
            for section in domain.sections.all():
                query_sets.append(Test.approved_tests.filter(
                    Q(language=Test.LANGUAGE_XX) | Q(language=language),
                    section=section,
                ).exclude(
                    pk__in=self.obtained_test_ids(),
                ).order_by("-is_free", "sales_count")[:1])
            if not len(query_sets):
                raise RuntimeError("Cannot query for next tests")
            self.__next_tests = query_sets[0].union(*query_sets[1:], all=True)

        return self.__next_tests

    def info(self, key, raw=False):
        # DARK_TODO  maybe only limit to students?
        if key not in (
            "identification",
            "region",
            "district",
        ):
            raise KeyError("There is no info for %s" % key)
        if not self.meta_data or key not in self.meta_data:
            return ""
        if key == "region" and not raw:
            return next(region[1] for region in REGIONS if region[0] == self.meta_data[key])
        if key == "identification" and not raw:
            return str(self.meta_data[key]).zfill(12)
        return self.meta_data[key]
