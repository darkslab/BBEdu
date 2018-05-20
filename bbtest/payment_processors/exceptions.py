class PaymentProcessorError(Exception):
    pass


class MerchantError(PaymentProcessorError):
    pass
