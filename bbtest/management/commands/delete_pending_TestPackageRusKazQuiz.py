from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils.timezone import get_current_timezone
from bbtest.models.test import (
    TestPackageRusKazQuiz,
)

class Command(BaseCommand):
    help = 'Delete old and not yet payed TestPackageRusKazQuiz'

    def handle(self, *args, **kwargs):
        objects = TestPackageRusKazQuiz.objects.filter(
            created_at__lte = datetime.now(tz=get_current_timezone()) - timedelta(hours=6),
            payed  = False,
        )
        objects.delete()

