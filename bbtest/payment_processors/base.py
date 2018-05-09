from decimal import Decimal, ROUND_HALF_UP
from .exceptions import PaymentProcessorError


class PaymentProcessor:
    def __init__(self, amount, test=False):
        if not isinstance(amount, Decimal) or amount <= self.min_amount():
            raise PaymentProcessorError("Incorrect amount")
        self.__amount = amount.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)
        self.__test = bool(test)

    def amount(self):
        return self.__amount

    def min_amount(self):
        return Decimal("0.00")

    def set_test(self):
        self.__test = True

    def is_test(self):
        return self.__test

    @classmethod
    def instantiate_from_meta_data(cls, meta_data):
        raise NotImplementedError("%s has to implement 'instantiate_from_meta_data' class method" % cls.__name__)

    def authorize(self):
        raise NotImplementedError("%s has to implement 'authorize' method" % type(self).__name__)

    def capture(self):
        raise NotImplementedError("%s has to implement 'capture' method" % type(self).__name__)

    def void(self):
        raise NotImplementedError("%s has to implement 'void' method" % type(self).__name__)

    def refund(self):
        raise NotImplementedError("%s has to implement 'refund' method" % type(self).__name__)

    def meta_data(self):
        raise NotImplementedError("%s has to implement 'meta_data' method" % type(self).__name__)

    def funds(self):
        raise NotImplementedError("%s has to implement 'funds' method" % type(self).__name__)
