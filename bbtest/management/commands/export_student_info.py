from django.core.management.base import BaseCommand
from bbtest.models import User
from datetime import datetime
import pytz



class Command(BaseCommand):
    help = 'export student info (phone, email, etc.)' 


    def handle(self, *args, **kwargs):

        users = User.objects.all()
        # сентября 2021 года
        from_date = datetime(2021, 8, 31, 0, 0, 0, tzinfo=pytz.timezone('Asia/Almaty'))
        out = ""
        for usr in users:
            if usr.joined_at > from_date:
                out += "{:%Y-%m-%d},{},{}\n".format(usr.joined_at, usr.email, usr.phone)
        
        print(out)


    def handle_2(self, *args, **kwargs):

        users = User.objects.all()
        # 1 февраля 2022 года
        from_date = datetime(2022, 1, 31, 0, 0, 0, tzinfo=pytz.timezone('Asia/Almaty'))
        out = ""
        for usr in users:
            if usr.joined_at > from_date:
                finished_some_tests = len(usr.obtained_test_ids()) > 0
                out += "{:%Y-%m-%d},{},{},{}\n".format(usr.joined_at, usr.email, usr.phone, finished_some_tests)

        print(out)
