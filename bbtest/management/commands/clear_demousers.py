from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils.timezone import get_current_timezone
from bbtest.auth.models import User
from django.contrib.auth.models import Permission, ContentType


class Command(BaseCommand):
    help = 'Clear demousers'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(codename="demouser", content_type=content_type)

        objects = User.objects.filter(
            joined_at__lte = datetime.now(tz=get_current_timezone()) - timedelta(hours=24),
            user_permissions  = permission,
        )
        objects.delete()

