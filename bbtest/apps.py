from django.apps import AppConfig
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from bbtest.signals.user import create_balance_account


class BbtestConfig(AppConfig):
    name = 'bbtest'

    def ready(self):
        post_save.connect(create_balance_account, sender=get_user_model(), dispatch_uid="create_balance_account")
