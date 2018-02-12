from django.db.models import (
    Manager,
    Model, ForeignKey, CASCADE, ManyToManyField,
    CharField, PositiveSmallIntegerField, BooleanField, DateTimeField, IntegerField, DecimalField,
)
from django.db.transaction import atomic
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
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


class EntryManager(Manager):
    def post(self, description, debits=[], credits=[], document=None):
        if not isinstance(description, str) or not len(description):
            raise RuntimeError("Please provide correct description")
        if document is not None and not isinstance(document, Model):
            raise RuntimeError("Please provide correct document")

        _debits = []
        _credits = []
        unique_accounts = []
        try:
            for index, entries in enumerate((debits, credits)):
                if not index:
                    _entries = _debits
                else:
                    _entries = _credits
                for entry in entries:
                    account = entry.get("account", None)
                    if account is None:
                        account = Account.objects.get(name=entry["account_name"])
                    if not isinstance(account, Account):
                        raise TypeError("Incorrect account type")
                    if account in unique_accounts:
                        raise TypeError("Reusing the same account")
                    unique_accounts.append(account)
                    if not isinstance(entry["amount"], Decimal) or entry["amount"] <= 0:
                        raise TypeError("Incorrect amount type")
                    _entries.append((account, entry["amount"]))
                if not len(_entries):
                    raise TypeError("Incorrect entries")
        except (TypeError, AttributeError, KeyError, Account.DoesNotExist):
            raise RuntimeError("Please provide correct debits and credits")

        if sum([debit[1] for debit in _debits]) != sum([credit[1] for credit in _credits]):
            raise RuntimeError("The sum of debit amounts does not match the sum of credit amounts")

        balance = Decimal("0.00")
        for index, entries in enumerate((_debits, _credits)):
            for entry in entries:
                if not index:
                    amount = entry[1]
                else:
                    amount = -entry[1]
                if entry[0].is_debit_account():
                    balance += amount
                else:
                    balance -= amount
        if not balance.is_zero():
            raise RuntimeError("Debit and credit amounts do not balance")

        with atomic(savepoint=False):
            entry = Entry.objects.create(description=description, document=document)
            for index, entries in enumerate((_debits, _credits)):
                for _entry in entries:
                    if not index:
                        is_debit = True
                    else:
                        is_debit = False
                    entry.amounts.create(account=_entry[0], is_debit=is_debit, amount=_entry[1])

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
