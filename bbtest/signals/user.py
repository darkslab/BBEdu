def create_balance_account(sender, **kwargs):
    if not kwargs["created"]:
        return
    from bbtest.models import BalanceAccount
    BalanceAccount.objects.create_equity_account(kwargs["instance"].balance_account_name())
