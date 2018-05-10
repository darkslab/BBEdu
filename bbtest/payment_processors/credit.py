from django.contrib.auth import get_user_model
from .base import PaymentProcessor
from .exceptions import PaymentProcessorError, MerchantError


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, amount, user, captured=False):
        super().__init__(amount)
        self.__user = user
        self.__account = self.__user.balance_account()
        self.__authorized = captured
        self.__captured = captured

    @classmethod
    def instantiate_from_meta_data(cls, amount, meta_data):
        try:
            kwargs = {}
            kwargs["user"] = get_user_model().objects.get(pk=meta_data["user_id"])
            kwargs["captured"] = meta_data["captured"]
            return cls(amount, **kwargs)
        except KeyError:
            raise PaymentProcessorError("Incorrect meta data")

    def authorize(self):
        if self.__authorized:
            raise PaymentProcessorError("Cannot authorize funds")
        if self.__account.balance() < self.amount():
            raise MerchantError("Insufficient funds")
        self.__authorized = True

    def capture(self):
        if not self.__authorized:
            raise PaymentProcessorError("Cannot capture funds, please authorize first")
        if self.__captured:
            raise PaymentProcessorError("Cannot capture funds")
        self.__captured = True

    def void(self):
        if not self.__authorized:
            raise PaymentProcessorError("Cannot void funds, please authorize first")
        if self.__captured:
            raise PaymentProcessorError("Cannot void funds")

    def refund(self):
        if not self.__captured:
            raise PaymentProcessorError("Cannot refund funds, please capture first")

    def meta_data(self):
        return {
            "user_id": self.__user.pk,
            "captured": self.__captured,
        }

    def funds(self):
        return []
