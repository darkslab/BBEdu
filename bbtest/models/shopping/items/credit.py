from django.utils.translation import pgettext
from django.contrib.auth import get_user_model
from decimal import Decimal, ROUND_HALF_UP
from .base import Item
from ..exceptions import ItemError


User = get_user_model()


class CreditItem(Item):
    def __init__(self, handle, amount, user):
        super().__init__(handle)

        self.__amount = Decimal("0.00")
        self.set_amount(amount)
        if not isinstance(user, User):
            raise ItemError(pgettext("Item error", "User is required."))
        self.__user = user
        self.__account = self.__user.balance_account()

        self.handle().add_item(self)

    def set_amount(self, amount):
        if not isinstance(amount, Decimal) or amount <= 0:
            raise ItemError(pgettext("Item error", "Incorrect amount value."))
        self.__amount = amount.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)

    def account(self):
        return self.__account

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
        return "Credits: %s" % self.__amount

    def price(self):
        return self.__amount

    def __eq__(self, other):
        return type(self) == type(other) and self.account() == other.account()

    def __hash__(self):
        return self.account().pk
