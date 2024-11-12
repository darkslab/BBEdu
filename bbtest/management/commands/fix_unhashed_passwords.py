from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, is_password_usable


class Command(BaseCommand):
    help = "Hashes unhashed passwords for all users."

    def handle(self, *args, **options):
        User = get_user_model()
        users_to_update = []
        updated_count = 0

        # Find users with unhashed passwords
        for user in User.objects.all():
            if not is_password_usable(user.password) or len(user.password) < 10 or not user.password.startswith("pbkdf2_sha256"):
                print(user.password)
                user.password = make_password(user.password)
                users_to_update.append(user)
                updated_count += 1

        # Bulk update users in the database
        if users_to_update:
            User.objects.bulk_update(users_to_update, ["password"])
            self.stdout.write(self.style.SUCCESS(f"Successfully updated {updated_count} users with hashed passwords."))
        else:
            self.stdout.write(self.style.SUCCESS("No users with unhashed passwords found."))
