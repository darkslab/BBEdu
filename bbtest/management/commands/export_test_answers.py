from datetime import datetime, timedelta
from pprint import pprint

import pytz
from django.core.management.base import BaseCommand
from django.db.models import Q

from bbtest.jobs.export_test import _job_export_results
from bbtest.models import User
from bbtest.models.quiz import Quiz, QuizSet


class Command(BaseCommand):
    help = 'export test info' 

    def handle(self, *args, **kwargs):
        domain_name = "Klass_4"
        # domain_name = "Klass_9"
        # domain_name = "Teacher"

        for day in [15, 16, 17]:
            from_date = datetime(2024, 4, day, 0, 0, 0, tzinfo=pytz.timezone('Asia/Almaty'))
            _job_export_results(from_date, domain_name)
