from django.core.management.base import BaseCommand
from bbtest.models import User
from django.contrib.auth.models import Permission

from bbtest.models.test import Test, TestQuestion, TestSection, ExpertProfile, DeveloperProfile



def assign(user, section_list):
    if user.is_superuser:
        return

    role_codename = user.user_permissions.get().codename
    if role_codename == "expert":
        section_obj_list = [TestSection.objects.get(name=section_name) for section_name in section_list]
        profile_obj, _ = ExpertProfile.objects.get_or_create(
            expert = user
        )
        profile_obj.section = section_obj_list
        profile_obj.save()

    elif role_codename == "developer":
        section_obj_list = [TestSection.objects.get(name=section_name) for section_name in section_list]
        profile_obj, _ = DeveloperProfile.objects.get_or_create(
            developer = user
        )
        profile_obj.section = section_obj_list
        profile_obj.save()

class Command(BaseCommand):
    help = 'generate NIS bundles from existing tests' 

    def handle(self, *args, **kwargs):
        for i, (section_list, username, fullname) in enumerate([
            [["Kazakh_4_kz", "Physics_9_ru"], "Dev-007", "Ethernal Secret Dev"],
            [["Kazakh_4_kz", "Russian_4_ru"], "Expert-007", "Ethernal Secret Expert"]
            ]):

            user = User.objects.get(username=username)
            assign(user, section_list)


    def handle2(self, *args, **kwargs):
        for i, (section_list, username, fullname, email) in enumerate(
            [
                [
                    ["Kazakh_4_kz"], 
                    "Dev-4421", 
                    "Абзалбек Лаура Сапаркызы", 
                    "L.Abzalbek@iac.kz"
                ],
                [
                    ["Russian_4_ru"],
                    "Dev-4422",
                    "Акульбекова Нурбакыт Заркешевна",
                    "nurbahytakulbekova@gmail.com",
                ],
                [
                    ["Math_4_kz", "Math_4_ru"],
                    "Dev-4423",
                    "Баймаханбетов Мухит Абилкасымович",
                    "mukhit.baimakhanbetov@iac.kz",
                ],
                [
                    ["NaturalScience_4_ru", "NaturalScience_4_kz"],
                    "Dev-4424",
                    "Раш Шахеризада Мухтаровна",
                    "shakhierizada.rash@mail.ru",
                ],
                [
                    ["Math_9_kz", "Math_9_ru"],
                    "Dev-4425",
                    "Аймжанова Агилаш Адигановна",
                    "a.aimzhanova@iac.kz",
                ],
                [
                    ["Physics_9_kz", "Physics_9_ru"],
                    "Dev-4426",
                    "Каратаева Назым Касымовна",
                    "nazym.karatayeva@quantum.edu.kz",
                ],
                [
                    ["Chemistry_9_kz", "Chemistry_9_ru"],
                    "Dev-4427",
                    "Райсханова Гульжанат Советовна",
                    "rgsovet@gmail.com",
                ],
                [
                    ["Geography_9_kz", "Geography_9_ru"],
                    "Dev-4428",
                    "Тукенова Жаркын Казбековна",
                    "zharkyn-1975@mail.ru",
                ],
                [
                    ["Biology_9_kz", "Biology_9_ru"],
                    "Dev-4429",
                    "Тумарбавева Кызылгуль Кабылкановна",
                    "red_flower29@mail.ru",
                ],
            ]
        ):
            print(username, fullname, email, section_list)
            user = User.objects.get(username=username)
            assign(user, section_list)

        


# username = CharField(pgettext_lazy("Model field", "username"), max_length=100, unique=True)
# email = EmailField(pgettext_lazy("Model field", "email"), max_length=100, null=True, blank=True, unique=True)
# first_name = CharField(pgettext_lazy("Model field", "first name"), max_length=100, blank=True)
# last_name = CharField(pgettext_lazy("Model field", "last name"), max_length=100, blank=True)
# phone = CharField(pgettext_lazy("Model field", "phone"), max_length=100, blank=True)
# meta_data = JSONField(pgettext_lazy("Model field", "meta_data"), null=True, blank=True)
# joined_at = DateTimeField(pgettext_lazy("Model field", "joined at"), auto_now_add=True, db_index=True)
# is_active = BooleanField(pgettext_lazy("Model field", "active?"), db_index=True, default=True)





