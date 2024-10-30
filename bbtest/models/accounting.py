from decimal import ROUND_HALF_UP, Decimal
from typing import List

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    IntegerField,
    Manager,
    ManyToManyField,
    Model,
    PositiveSmallIntegerField,
    Q,
    Sum,
)
from django.db.transaction import atomic
from django.utils.translation import pgettext_lazy


class AccountManager(Manager):
    def create_asset_account(self, name, is_contra=False):
        return self.create(name=name, type=Account.TYPE_ASSET, is_contra=is_contra)

    def create_expense_account(self, name, is_contra=False):
        return self.create(name=name, type=Account.TYPE_EXPENSE, is_contra=is_contra)

    def create_dividend_account(self, name, is_contra=False):
        return self.create(name=name, type=Account.TYPE_DIVIDEND, is_contra=is_contra)

    def create_liability_account(self, name, is_contra=False):
        return self.create(name=name, type=Account.TYPE_LIABILITY, is_contra=is_contra)

    def create_equity_account(self, name, is_contra=False):
        return self.create(name=name, type=Account.TYPE_EQUITY, is_contra=is_contra)

    def create_revenue_account(self, name, is_contra=False):
        return self.create(name=name, type=Account.TYPE_REVENUE, is_contra=is_contra)

    def has_errors(self):
        debit_balance = Decimal("0.00")
        debit_balance += Amount.objects.filter(is_debit=True).filter(
            Q(account__type__lt=0x10, account__is_contra=False) | Q(account__type__gt=0x0f, account__is_contra=True),
        ).aggregate(balance=Sum("amount"))["balance"] or Decimal("0.00")
        debit_balance -= Amount.objects.filter(is_debit=False).filter(
            Q(account__type__lt=0x10, account__is_contra=False) | Q(account__type__gt=0x0f, account__is_contra=True),
        ).aggregate(balance=Sum("amount"))["balance"] or Decimal("0.00")

        credit_balance = Decimal("0.00")
        credit_balance += Amount.objects.filter(is_debit=False).filter(
            Q(account__type__gt=0x0f, account__is_contra=False) | Q(account__type__lt=0x10, account__is_contra=True),
        ).aggregate(balance=Sum("amount"))["balance"] or Decimal("0.00")
        credit_balance -= Amount.objects.filter(is_debit=True).filter(
            Q(account__type__gt=0x0f, account__is_contra=False) | Q(account__type__lt=0x10, account__is_contra=True),
        ).aggregate(balance=Sum("amount"))["balance"] or Decimal("0.00")

        return not (debit_balance - credit_balance).is_zero()

class Account(Model):
    TYPE_ASSET      = 0x00
    TYPE_EXPENSE    = 0x01
    TYPE_DIVIDEND   = 0x02
    TYPE_LIABILITY  = 0x10
    TYPE_EQUITY     = 0x11
    TYPE_REVENUE    = 0x12
    TYPES = (
        ( TYPE_ASSET,     pgettext_lazy("Account type", "Asset")     ),
        ( TYPE_EXPENSE,   pgettext_lazy("Account type", "Expense")   ),
        ( TYPE_DIVIDEND,  pgettext_lazy("Account type", "Dividend")  ),
        ( TYPE_LIABILITY, pgettext_lazy("Account type", "Liability") ),
        ( TYPE_EQUITY,    pgettext_lazy("Account type", "Equity")    ),
        ( TYPE_REVENUE,   pgettext_lazy("Account type", "Revenue")   ),
    )

    name        = CharField                  ( pgettext_lazy("Model field", "name"),               max_length=100,                                  unique=True,   )
    type        = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "type"),                                  choices=TYPES,                db_index=True, )
    is_contra   = BooleanField               ( pgettext_lazy("Model field", "is contra account?"),                                   default=False, db_index=True, )
    created_at  = DateTimeField              ( pgettext_lazy("Model field", "created at"),         auto_now_add=True,                                              )

    objects = AccountManager()

    class Meta:
        db_table = "accounting_accounts"
        default_permissions = ()

    def __str__(self):
        if self.name:
            return self.name
        if self.pk:
            return "Account #%s" % self.pk
        return "New Account"

    def is_debit_account(self):
        if self.type is None:
            raise RuntimeError("Unknown account type")
        is_debit = True
        if self.type > 0x0f:
            is_debit = False
        if self.is_contra:
            is_debit = not is_debit
        return is_debit

    def is_credit_account(self):
        if self.type is None:
            raise RuntimeError("Unknown account type")
        is_credit = True
        if self.type < 0x10:
            is_credit = False
        if self.is_contra:
            is_credit = not is_credit
        return is_credit

    def balance(self):
        is_debit = True
        if self.is_credit_account():
            is_debit = False
        balance = Decimal("0.00")
        balance += self.amounts.filter(is_debit=is_debit).aggregate(balance=Sum("amount"))["balance"] or Decimal("0.00")
        balance -= self.amounts.exclude(is_debit=is_debit).aggregate(balance=Sum("amount"))["balance"] or Decimal("0.00")
        return balance

    def is_balance_account(self):
        return False

class BalanceAccount(Account):
    class Meta:
        proxy = True
        default_permissions = ()

    def is_balance_account(self):
        return True


class EntryManager(Manager):
    def post(self, description, funds, document=None):
        if not isinstance(description, str) or not len(description):
            raise RuntimeError("Please provide correct description")
        funds = squash_funds(funds)
        try:
            unique_accounts = []
            balance = Decimal("0.00")
            for index, fund in enumerate(funds):
                if not isinstance(fund, Fund):
                    raise TypeError("Incorrect fund type")
                if fund.account() in unique_accounts:
                    raise TypeError("Reusing the same account")
                unique_accounts.append(fund.account())
                balance += fund.audit_balance()
            if not len(unique_accounts):
                raise TypeError("No funds")
            if not balance.is_zero():
                raise RuntimeError("Debit and credit funds do not balance")
        except TypeError:
            raise RuntimeError("Please provide correct debit and credit funds")
        if document is not None and not isinstance(document, Model):
            raise RuntimeError("Please provide correct document")

        with atomic(savepoint=False):
            entry = Entry.objects.create(description=description, document=document)
            for fund in funds:
                is_debit = True
                if isinstance(fund, Credit):
                    is_debit = False
                entry.amounts.create(
                    account=fund.account(),
                    is_debit=is_debit,
                    amount=fund.amount(),
                )

class Entry(Model):
    accounts  = ManyToManyField  ( Account, through="Amount", related_name="entries", )

    description   = CharField          ( pgettext_lazy("Model field", "description"), max_length=1000,                                         )
    content_type  = ForeignKey         ( ContentType, on_delete=CASCADE, null=True, blank=True, )
    object_id     = IntegerField       ( pgettext_lazy("Model field", "object ID"),                      null=True, blank=True, db_index=True, )
    document      = GenericForeignKey  ()
    created_at    = DateTimeField      ( pgettext_lazy("Model field", "created at"),  auto_now_add=True,                                       )

    objects = EntryManager()

    class Meta:
        db_table = "accounting_entries"
        default_permissions = ()

    def __str__(self):
        if self.description:
            return self.description
        if self.pk:
            return "Entry #%s" % self.pk
        return "New Entry"

class Fund:
    def __init__(self, account_name=None, amount=None, account=None):
        self.__account = account
        if self.__account is None and account_name is not None:
            try:
                self.__account = Account.objects.get(name=account_name)
            except Account.DoesNotExist:
                pass
        if not isinstance(self.__account, Account):
            raise RuntimeError("Account is required")

        try:
            if not isinstance(amount, Decimal):
                raise ValueError("Invalid amount")
            amount = amount.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)
            if amount <= 0:
                raise ValueError("Invalid amount")
            self.__amount = amount
        except ValueError:
            raise RuntimeError("Incorrect amount value")

    def account(self) -> Account:
        return self.__account

    def amount(self) -> Decimal:
        return self.__amount

    def audit_balance(self):
        raise NotImplementedError("%s has to implement 'audit_balance' method" % type(self).__name__)

    def should_lock_account(self):
        raise NotImplementedError("%s has to implement 'should_lock_account' method" % type(self).__name__)

class Debit(Fund):
    def audit_balance(self):
        return self.amount()

    def should_lock_account(self):
        if not self.account().is_balance_account():
            return False
        if self.account().is_credit_account():
            return True
        return False

class Credit(Fund):
    def audit_balance(self):
        return -self.amount()

    def should_lock_account(self):
        if not self.account().is_balance_account():
            return False
        if self.account().is_debit_account():
            return True
        return False

def squash_funds(funds: List[Fund]) -> List[Fund]:
    squashed_funds = []
    fund_balances = {}
    for fund in funds:
        if fund.account() not in fund_balances:
            fund_balances[fund.account()] = Decimal("0.00")
        fund_balances[fund.account()] += fund.audit_balance()
    for account, balance in fund_balances.items():
        fund_class = None
        if balance > 0:
            fund_class = Debit
        elif balance < 0:
            fund_class = Credit
        if fund_class is not None:
            squashed_funds.append(fund_class(account=account, amount=abs(balance)))
    return squashed_funds


class Amount(Model):
    account  = ForeignKey  ( Account, on_delete=CASCADE, related_name="amounts", )
    entry    = ForeignKey  ( Entry,   on_delete=CASCADE, related_name="amounts", )

    is_debit  = BooleanField  ( pgettext_lazy("Model field", "is debit?"),                                  db_index=True, )
    amount    = DecimalField  ( pgettext_lazy("Model field", "amount"),    max_digits=16, decimal_places=2,                )

    class Meta:
        db_table = "accounting_amounts"
        default_permissions = ()

    def __str__(self):
        if not self.amount:
            return "New Amount"
        sign, digits, exponent = self.amount.as_tuple()
        digits = [str(digit) for digit in digits]
        if exponent < 0:
            digits.insert(exponent, ".")
        digits.insert(0, "$")
        if sign:
            digits.insert(0, "-")
        return "".join(digits)
