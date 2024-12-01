from django.contrib.auth.models import ContentType, Permission
from django.core.management.base import BaseCommand

from bbtest.auth.models import User
from bbtest.models.test import StudentProfile


class Command(BaseCommand):
    help = 'Add bird game for every student' 

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(codename="student", content_type=content_type)

        objects = User.objects.filter(
            user_permissions  = permission,
        )
        for user in objects:
            StudentProfile.objects.create(
                student = user,
                games = "bird",
            )