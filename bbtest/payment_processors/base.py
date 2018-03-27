class PaymentProcessor:
    def __init__(self, test=False):
        self.__test = test

    def set_test(self):
        self.__test = True

    def is_test(self):
        return self.__test

    def authorize(self):
        raise NotImplementedError("%s has to implement 'authorize' method" % type(self).__name__)

    def capture(self):
        raise NotImplementedError("%s has to implement 'capture' method" % type(self).__name__)

    def void(self):
        raise NotImplementedError("%s has to implement 'void' method" % type(self).__name__)

    def refund(self):
        raise NotImplementedError("%s has to implement 'refund' method" % type(self).__name__)
