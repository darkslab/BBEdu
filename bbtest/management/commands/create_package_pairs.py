from datetime import datetime

import pytz
from django.core.management.base import BaseCommand

from bbtest.models import TestPackageRusKazPair, TestPackage


class Command(BaseCommand):
    help = '' 

    def handle(self, *args, **kwargs):

        package_ru = TestPackage.objects.get(
            code = "2404122712",
            # name = "МОДО PS 9 кл Буклет 8 рус",
        )
        package_kz = TestPackage.objects.get(
            code = "240412213d",
            # name = "МОДО PS 9 кл Буклет 8 kaz",
        )

        TestPackageRusKazPair.objects.create(
            name = "МОДО PS 9 кл Буклет 8",
            test_package_ru = package_ru,
            test_package_kz = package_kz,
        )





