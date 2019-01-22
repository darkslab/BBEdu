from django.utils.translation import pgettext
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_noop
from decimal import Decimal, ROUND_HALF_UP
from .base import Item
from ..exceptions import ItemError
from bbtest.models.accounting import Account, Credit


User = get_user_model()


MAX_CREDIT_AMOUNT = Decimal("1000000.00")
MIN_CREDIT_AMOUNT = Decimal("200.00")

class CreditItem(Item):
    def __init__(self, handle, amount, user):
        super().__init__(handle)

        self.__amount = Decimal("0.00")
        if not isinstance(user, User):
            raise ItemError(pgettext("Item error", "User is required."))
        self.__user = user
        self.__accounts = {
            "balance_account": self.__user.balance_account(),
            "account": Account.objects.get(pk=self.__user.balance_account().pk),
        }
        self.set_amount(amount)

        self.handle().add_item(self)

    def set_amount(self, amount):
        try:
            if not isinstance(amount, Decimal):
                raise ValueError("Invalid amount")
            amount = amount.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)
            if amount < MIN_CREDIT_AMOUNT:
                raise ValueError("Invalid amount")
            self.__amount = amount
            self.handle().mark_modified()
        except ValueError:
            raise ItemError(pgettext("Item error", "Incorrect amount value."))

    def account(self):
        return self.__accounts["balance_account"]

    @classmethod
    def instantiate_from_meta_data(cls, handle, meta_data):
        try:
            amount = Decimal(meta_data["amount"])
            user = User.objects.get(pk=meta_data["user_id"])
            cls(handle, amount, user)
        except User.DoesNotExist:
            raise ItemError(pgettext("Item error", "User no longer exists."))

    def merge_into_items(self, items):
        new_items = []
        for item in items:
            if not isinstance(item, type(self)):
                continue
            if item == self:
                item.set_amount(item.price() + self.price())
            new_items.append(item)
        if self not in new_items:
            new_items.append(self)
        new_items.sort(key=lambda new_item: new_item.account().pk)
        return new_items

    def separate_from_items(self, items):
        items.pop(items.index(self))
        return items

    def meta_data(self):
        return {
            "amount": str(self.__amount),
            "user_id": self.__user.pk,
        }

    def description(self):
        return ugettext_noop("Credits")

    def price(self):
        return self.__amount

    def __eq__(self, other):
        return type(self) == type(other) and self.account() == other.account()

    def __hash__(self):
        return self.account().pk

    def funds(self):
        return [
            Credit(account=self.__accounts["account"], amount=self.__amount),
        ]
