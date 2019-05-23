from django.conf import settings
from requests import post
from requests.exceptions import RequestException
import hmac
from decimal import Decimal
from .base import PaymentProcessor
from .exceptions import PaymentProcessorError, MerchantError
from bbtest.utils.json import tight_dumps
from bbtest.models.accounting import Debit


class BeelinePaymentProcessor(PaymentProcessor):
    def __init__(self, amount, payment_id, otp=None, captured=False):
        super().__init__(amount)
        self.__payment_id = payment_id
        self.__otp = otp
        self.__meta_data = {}
        self.__captured = captured and self.__payment_id is not None and self.__otp is None

    @classmethod
    def instantiate_from_meta_data(cls, amount, meta_data):
        return cls(amount, **{
            "payment_id": meta_data["receipts"]["paymentReceipt"]["paymentTransactionId"],
            "captured": True,
        })

    def authorize(self):
        if self.__payment_id is None or self.__otp is None:
            raise PaymentProcessorError("Cannot authorize funds")
        response = self.__request("/merchant-api/v1/confirm-payment", {
            "paymentId": self.__payment_id,
            "otp": self.__otp,
        }, test=self.is_test())
        self.__meta_data = response

    def capture(self):
        if self.__payment_id is None or self.__otp is None or not self.__meta_data or self.__captured:
            raise PaymentProcessorError("Cannot capture funds, please authorize first")
        self.__otp = None
        self.__captured = True

    def void(self):
        if self.__payment_id is None or self.__otp is None or not self.__meta_data or self.__captured:
            raise PaymentProcessorError("Cannot void funds, please authorize first")
        self.__refund_payment()
        self.__otp = None

    def refund(self):
        if not self.__captured:
            raise PaymentProcessorError("Cannot refund funds, please capture first")
        self.__meta_data = self.__refund_payment()
        self.__captured = False

    def meta_data(self):
        return self.__meta_data

    def funds(self):
        if not self.__meta_data:
            raise NotImplementedError("Currently it is not implemented")
        result = [
            Debit("Cash", Decimal(str(self.__meta_data["receipts"]["paymentReceipt"]["amount"]))),
        ]
        fees = Decimal(str(self.__meta_data["receipts"]["paymentReceipt"]["commission"]))
        if not fees.is_zero():
            result.append(Debit("MerchantFees-Beeline", fees))
        return result

    @classmethod
    def create_payment(cls, cart_handle, number, test=False):
        cart_id = cart_handle.cart_id(force=True)

        response = cls.__request("/merchant-api/v1/create-payment", {
            "productId": cls.product_id(),
            "amount": str(cart_handle.total()),
            "productReceiver": number,
            "payerPhone": number,
            "sellerId": cls.seller_id(),
            "merchantOrderId": cart_id,
            "description": "Cart #%s" % cart_id,
        }, test=test)

        if Decimal(str(response["paymentDetails"]["totalAmount"])) != cart_handle.total():
            raise MerchantError("Created payment fund amount does not match")

        return response["paymentDetails"]

    @classmethod
    def resend_otp(cls, payment_id, test=False):
        response = cls.__request("/merchant-api/v1/resend-otp", {
            "paymentId": payment_id,
        }, test=test)
        return response["canResend"]

    @classmethod
    def private_key(cls):
        raise NotImplementedError("%s has to implement 'private_key' class method" % cls.__name__)

    @classmethod
    def api_name(cls):
        raise NotImplementedError("%s has to implement 'api_name' class method" % cls.__name__)

    @classmethod
    def service_base_url(cls):
        raise NotImplementedError("%s has to implement 'service_base_url' class method" % cls.__name__)

    @classmethod
    def seller_id(cls):
        raise NotImplementedError("%s has to implement 'seller_id' class method" % cls.__name__)

    @classmethod
    def product_id(cls):
        raise NotImplementedError("%s has to implement 'product_id' class method" % cls.__name__)

    @classmethod
    def __request(cls, uri, data, test=False):
        try:
            post_data = tight_dumps(data)

            hasher = hmac.new(bytes(cls.private_key(), encoding="utf8"), digestmod="sha256")
            hasher.update(bytes(post_data, encoding="utf8"))

            response = post("%s%s" % (
                cls.service_base_url(),
                uri,
            ), data=post_data, **{
                "headers": {
                    "User-Agent": settings.BB_USER_AGENT,
                    "Content-Type": "application/json",
                    "Api-Name": cls.api_name(),
                    "Signature": hasher.hexdigest(),
                },
                "timeout": 8,
                "verify": False,
            })

            if response.status_code != 200 or response.json()["status"] != "ok":
                raise ValueError("Unsuccessful payment")

            return response.json()

        except (RequestException, ValueError, KeyError, TypeError) as error:
            raise PaymentProcessorError("Request failed")

    def __refund_payment(self):
        return self.__request("/merchant-api/v1/refund-payment", {
            "paymentId": self.__payment_id,
        }, test=self.is_test())


class FirstBeelinePaymentProcessor(BeelinePaymentProcessor):
    @classmethod
    def private_key(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_BEELINE_PAYMENT_PROCESSOR"]["PRIVATE_KEY"]

    @classmethod
    def api_name(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_BEELINE_PAYMENT_PROCESSOR"]["API_NAME"]

    @classmethod
    def service_base_url(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_BEELINE_PAYMENT_PROCESSOR"]["SERVICE_BASE_URL"]

    @classmethod
    def seller_id(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_BEELINE_PAYMENT_PROCESSOR"]["SELLER_ID"]

    @classmethod
    def product_id(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_BEELINE_PAYMENT_PROCESSOR"]["PRODUCT_ID"]
