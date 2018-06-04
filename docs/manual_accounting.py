# Deposit money

from decimal import Decimal
from bbtest.models.accounting import Entry, Debit, Credit
Entry.objects.post("Giving out money", [
    Debit("Cash", Decimal("1000.00")),
    Credit("BalanceAccount-3088", Decimal("1000.00")),
])


# Withdraw money

from decimal import Decimal
from bbtest.models.accounting import Entry, Debit, Credit
Entry.objects.post("Taking out money", [
    Credit("Cash", Decimal("1000.00")),
    Debit("BalanceAccount-3088", Decimal("1000.00")),
])
