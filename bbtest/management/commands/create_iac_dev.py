from random import randint

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from bbtest.models import Account, User

# 4 Класс
# Казахский язык (с казахским языком обучения)	    Абзалбек Лаура Сапаркызы	            L.Abzalbek@iac.kz
# Русский язык (с русским языком обучения)	        Акульбекова Нурбакыт Заркешевна	        nurbahytakulbekova@gmail.com
# Математика	                                    Баймаханбетов Мухит Абилкасымович	    mukhit.baimakhanbetov@iac.kz
# Естествознание	                                Раш Шахеризада Мухтаровна	            shakhierizada.rash@mail.ru

# Казахский язык (с казахским языком обучения)	    Абзалбек Лаура Сапарқызы	            L.Abzalbek@iac.kz
# Русский язык (с русским языком обучения)	        Акульбекова Нурбакыт Заркешевна	        nurbahytakulbekova@gmail.com
# Математика	                                    Баймаханбетов Мухит Абилкасымович	    mukhit.baimakhanbetov@iac.kz
# Математика                                        Аймжанова Агилаш Адигановна	            a.aimzhanova@iac.kz
# Физика	                                        Каратаева Назым Касымовна	            nazym.karatayeva@quantum.edu.kz
# Химия	                                            Райсханова Гульжанат Советовна	        rgsovet@gmail.com
# География	                                        Тукенова Жаркын Казбековна	            zharkyn-1975@mail.ru
# Биология	                                        Тумарбавева Кызылгуль Кабылкановна	    red_flower29@mail.ru
		


# ["Казахский"        , "Абзалбек Лаура Сапаркызы",	            "L.Abzalbek@iac.kz"]
# ["Русский"          , "Акульбекова Нурбакыт Заркешевна",	    "nurbahytakulbekova@gmail.com"]
# ["Математика"       , "Баймаханбетов Мухит Абилкасымович",	    "mukhit.baimakhanbetov@iac.kz"]
# ["Естествознание"   , "Раш Шахеризада Мухтаровна",	            "shakhierizada.rash@mail.ru"]
# ["Казахский"        , "Абзалбек Лаура Сапарқызы",	            "L.Abzalbek@iac.kz"]
# ["Русский"          , "Акульбекова Нурбакыт Заркешевна",	    "nurbahytakulbekova@gmail.com"]
# ["Математика"       , "Баймаханбетов Мухит Абилкасымович",	    "mukhit.baimakhanbetov@iac.kz"]
# ["Математика"       , "Аймжанова Агилаш Адигановна",	        "a.aimzhanova@iac.kz"]
# ["Физика"           , "Каратаева Назым Касымовна",	            "nazym.karatayeva@quantum.edu.kz"]
# ["Химия"            , "Райсханова Гульжанат Советовна",	        "rgsovet@gmail.com"]
# ["География"        , "Тукенова Жаркын Казбековна",	            "zharkyn-1975@mail.ru"]
# ["Биология"         , "Тумарбавева Кызылгуль Кабылкановна",	    "red_flower29@mail.ru"]


def create_students():
    user = User.objects.create_user(username="student_02", email="student_02@example.com", password="m")
    user.first_name = "Dimon"
    user.last_name = "Electric"
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

def create_admin():
    user = User.objects.create_user(username="Admin", email=None, password="m")
    user.first_name = "Admin"
    user.last_name = ""
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="admin", content_type=content_type))
    user.user_permissions.set(permissions)
    Account.objects.create_liability_account("Admin-%s" % user.pk)
    return user

def create_expert():
    user = User.objects.create_user(username="Expert", email=None, password="m")
    user.first_name = "Expert"
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
        # user = create_students()
        # print(user)
        table = ""
        for i, (subject, name, email) in enumerate([
            ["Казахский"        , "Абзалбек Лаура Сапаркызы",	            "L.Abzalbek@iac.kz"],
            ["Русский"          , "Акульбекова Нурбакыт Заркешевна",	    "nurbahytakulbekova@gmail.com"],
            ["Математика"       , "Баймаханбетов Мухит Абилкасымович",	    "mukhit.baimakhanbetov@iac.kz"],
            ["Естествознание"   , "Раш Шахеризада Мухтаровна",	            "shakhierizada.rash@mail.ru"],
            # ["Казахский"        , "Абзалбек Лаура Сапарқызы",	            "L.Abzalbek@iac.kz"],

            # ["Русский"          , "Акульбекова Нурбакыт Заркешевна",	    "nurbahytakulbekova@gmail.com"],
            # ["Математика"       , "Баймаханбетов Мухит Абилкасымович",	    "mukhit.baimakhanbetov@iac.kz"],
            ["Математика"       , "Аймжанова Агилаш Адигановна",	        "a.aimzhanova@iac.kz"],
            ["Физика"           , "Каратаева Назым Касымовна",	            "nazym.karatayeva@quantum.edu.kz"],
            ["Химия"            , "Райсханова Гульжанат Советовна",	        "rgsovet@gmail.com"],
            ["География"        , "Тукенова Жаркын Казбековна",	            "zharkyn-1975@mail.ru"],
            ["Биология"         , "Тумарбавева Кызылгуль Кабылкановна",	    "red_flower29@mail.ru"]
            ]):
            password = str(randint(100000000, 1000000000))
            username = "Dev-{}".format(i + 8333)
            user = create_developer(password, username=username, email=email, first_name = name, last_name = "[{}]".format(subject))
            table += "{} {} {} {}\t{}\n".format(username, password, subject, name, email)

        print(table)


# username = CharField(pgettext_lazy("Model field", "username"), max_length=100, unique=True)
# email = EmailField(pgettext_lazy("Model field", "email"), max_length=100, null=True, blank=True, unique=True)
# first_name = CharField(pgettext_lazy("Model field", "first name"), max_length=100, blank=True)
# last_name = CharField(pgettext_lazy("Model field", "last name"), max_length=100, blank=True)
# phone = CharField(pgettext_lazy("Model field", "phone"), max_length=100, blank=True)
# meta_data = JSONField(pgettext_lazy("Model field", "meta_data"), null=True, blank=True)
# joined_at = DateTimeField(pgettext_lazy("Model field", "joined at"), auto_now_add=True, db_index=True)
# is_active = BooleanField(pgettext_lazy("Model field", "active?"), db_index=True, default=True)





