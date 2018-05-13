from .base import PaymentProcessor
from .exceptions import PaymentProcessorError


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, amount, captured=False):
        super().__init__(amount)
        self.__authorized = captured
        self.__captured = captured

    @classmethod
    def instantiate_from_meta_data(cls, amount, meta_data):
        try:
            kwargs = {}
            kwargs["captured"] = meta_data["captured"]
            return cls(amount, **kwargs)
        except KeyError:
            raise PaymentProcessorError("Incorrect meta data")

    def authorize(self):
        if self.__authorized:
            raise PaymentProcessorError("Cannot authorize funds")
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
            "captured": self.__captured,
        }

    def funds(self):
        return []
