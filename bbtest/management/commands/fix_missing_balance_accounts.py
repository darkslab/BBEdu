from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from bbtest.models import BalanceAccount

class Command(BaseCommand):
    help = "Creates missing balance accounts for all users."

    def handle(self, *args, **options):
        User = get_user_model()
        users_without_balance_account = []
        created_count = 0

        # Identify users who don't have an associated BalanceAccount
        for user in User.objects.all():
            q = BalanceAccount.objects.filter(name=user.balance_account_name())
            print(q)
            if not q:
                # Prepare a new BalanceAccount instance for each user without one
                balance_obj = BalanceAccount(
                    name=user.balance_account_name(), 
                    type=BalanceAccount.TYPE_EQUITY, 
                    is_contra=False
                )
                users_without_balance_account.append(balance_obj)
                created_count += 1

        # Bulk create all missing BalanceAccounts at once
        if users_without_balance_account:
            BalanceAccount.objects.bulk_create(users_without_balance_account)
            self.stdout.write(self.style.SUCCESS(f"Successfully created {created_count} missing balance accounts."))
        else:
            self.stdout.write(self.style.SUCCESS("No missing balance accounts found."))
