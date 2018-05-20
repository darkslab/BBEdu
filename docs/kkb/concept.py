



class Payment:
    def __init__(self):
        pass

    def authorize(self):
        raise NotImplementedError("%s has to implement 'authorize' method" % type(self).__name__)

    def void(self):
        raise NotImplementedError("%s has to implement 'void' method" % type(self).__name__)

    def capture(self):
        raise NotImplementedError("%s has to implement 'capture' method" % type(self).__name__)

    def refund(self):
        raise NotImplementedError("%s has to implement 'refund' method" % type(self).__name__)


class QazkomPayment(Payment):
    def __init__(self):
        pass

    def authorize(self):
        raise NotImplementedError("%s has to implement 'authorize' method" % type(self).__name__)

    def void(self):
        raise NotImplementedError("%s has to implement 'void' method" % type(self).__name__)

    def capture(self):
        raise NotImplementedError("%s has to implement 'capture' method" % type(self).__name__)

    def refund(self):
        raise NotImplementedError("%s has to implement 'refund' method" % type(self).__name__)


class FirstQazkomPayment(QazkomPayment):
    pass




