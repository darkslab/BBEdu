from bbtest.models import BalanceAccount


def create_balance_account(sender, **kwargs):
    if not kwargs["created"]:
        return
    BalanceAccount.objects.create_equity_account(kwargs["instance"].balance_account_name())
