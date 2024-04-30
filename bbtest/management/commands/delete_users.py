from datetime import datetime, timedelta
from pprint import pprint

import pytz
from django.core.management.base import BaseCommand

from bbtest.models import User
from bbtest.models.quiz import Quiz, QuizSet
from bbtest.models.test import (
    StudentGroup,
    Test,
    TestPackage,
    TestParagraph,
    TestQuestion,
)


class Command(BaseCommand):
    help = 'export test info' 


    def handle(self, *args, **kwargs):
        for username in user_list:
            del_user(username)


def del_user(username):    
    try:
        u = User.objects.get(username = username)
        u.delete()

    except User.DoesNotExist:
        print(username, "was already deleted")

user_list = []

