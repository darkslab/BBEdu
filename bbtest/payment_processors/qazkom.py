from django.conf import settings
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.exceptions import InvalidSignature
from base64 import b64encode, b64decode
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ParseError
from re import search, I, S
from requests import get
from requests.exceptions import RequestException
from decimal import Decimal, DecimalException
from .base import PaymentProcessor
from .exceptions import PaymentProcessorError, MerchantError


class QazkomPaymentProcessor(PaymentProcessor):
    def __init__(self, amount, authorization_response=None, captured=False):
        super().__init__()
        self.__authorization_response = authorization_response
        self.__authorization_data = None
        self.__captured = captured and self.__authorization_response
        self.__meta_data = {}
        self.__request_kwargs = {
            "headers": {
                "User-Agent": settings.BB_USER_AGENT,
            },
            "timeout": 8,
        }

        try:
            if self.__authorization_response:
                self.__verify_document(self.__authorization_response)
        except MerchantError:
            pass

    @classmethod
    def instantiate_from_meta_data(cls, meta_data):
        kwargs = {}
        if "authorization_response" in meta_data:
            kwargs["authorization_response"] = meta_data["authorization_response"]
        if "capture_response" in meta_data:
            kwargs["captured"] = True
        return cls(**kwargs)

    def authorize(self):
        if not (self.__authorization_response and not self.__captured):
            raise PaymentProcessorError("Cannot authorize funds")
        self.__verify_document(self.__authorization_response)
        self.__retrieve_authorization_data()

    def capture(self):
        if not self.__authorization_data:
            raise PaymentProcessorError("Cannot capture funds, please authorize first")
        try:
            response = get(
                self.__command_url(),
                params=self.__command_string("complete"),
                **self.__request_kwargs
            )
            if response.status_code != 200:
                raise PaymentProcessorError("Incorrect response HTTP code while capturing")
            self.__verify_document(response.text)

            document = ET.fromstring(response.text)
            if document.find("bank").find("response").attrib["code"] != "00":
                raise ValueError("Unsuccessful capture response status")

            self.__meta_data["authorization_response"] = self.__authorization_response
            self.__meta_data["capture_response"] = response.text

            self.__captured = True
            self.__authorization_data = None

        except RequestException as error:
            raise PaymentProcessorError("Connection problem while capturing: %s" % str(error))
        except (AttributeError, KeyError, ValueError):
            raise MerchantError("Capturing funds was not successful")

    def void(self):
        if not self.__authorization_data:
            raise PaymentProcessorError("Cannot void funds, please authorize first")
        try:
            response = get(
                self.__command_url(),
                params=self.__command_string("reverse", "Void authorization"),
                **self.__request_kwargs
            )
            if response.status_code != 200:
                raise PaymentProcessorError("Incorrect response HTTP code while voiding")
            self.__verify_document(response.text)

            document = ET.fromstring(response.text)
            if document.find("bank").find("response").attrib["code"] != "00":
                raise ValueError("Unsuccessful void response status")

            self.__meta_data["void_response"] = response.text

            self.__authorization_response = None
            self.__authorization_data = None

        except RequestException as error:
            raise PaymentProcessorError("Connection problem while voiding: %s" % str(error))
        except (AttributeError, KeyError, ValueError):
            raise MerchantError("Voiding funds was not successful")

    def refund(self):
        if not (self.__authorization_response and self.__captured):
            raise PaymentProcessorError("Cannot void funds")
        self.__verify_document(self.__authorization_response)
        self.__retrieve_authorization_data()
        try:
            response = get(
                self.__command_url(),
                params=self.__command_string("refund", "Refund order"),
                **self.__request_kwargs
            )
            if response.status_code != 200:
                raise PaymentProcessorError("Incorrect response HTTP code while refunding")
            self.__verify_document(response.text)

            document = ET.fromstring(response.text)
            if document.find("bank").find("response").attrib["code"] != "00":
                raise ValueError("Unsuccessful refund response status")

            self.__meta_data["refund_response"] = response.text

            self.__authorization_response = None
            self.__authorization_data = None

        except RequestException as error:
            raise PaymentProcessorError("Connection problem while refunding: %s" % str(error))
        except (AttributeError, KeyError, ValueError):
            raise MerchantError("Refunding funds was not successful")

    def meta_data(self):
        return self.__meta_data

    @classmethod
    def post_url(cls, test=False):
        if test:
            return "https://testpay.kkb.kz/jsp/process/logon.jsp"
        return "https://epay.kkb.kz/jsp/process/logon.jsp"

    @classmethod
    def signature(cls, message):
        key = load_pem_private_key(
            bytes(cls.private_key(), encoding="UTF-8"),
            password=bytes(cls.private_password(), encoding="UTF-8"),
            backend=default_backend(),
        )
        data = key.sign(
            bytes(message, encoding="UTF-8"),
            PKCS1v15(),
            SHA1(),
        )
        return str(b64encode(data[::-1]), encoding="UTF-8")

    @classmethod
    def is_verifiable(cls, message, signature):
        key = load_pem_x509_certificate(
            bytes(cls.qazkom_certificate(), encoding="UTF-8"),
            backend=default_backend(),
        ).public_key()
        try:
            key.verify(
                b64decode(signature)[::-1],
                bytes(message, encoding="UTF-8"),
                PKCS1v15(),
                SHA1(),
            )
            return True
        except InvalidSignature:
            pass
        return False

    @classmethod
    def encoded_order(cls, cart_handle):
        document = Element("document")

        merchant_node = Element("merchant", {
            "cert_id": cls.merchant_cert_id(),
            "name": cls.merchant_name(),
        })
        order_node = Element("order", {
            "order_id": str(cart_handle.cart_id() or "").zfill(6),
            "amount": str(cart_handle.total()),
            "currency": "398",
        })
        order_node.append(Element("department", {
            "merchant_id": cls.merchant_id(),
            "amount": str(cart_handle.total()),
            "instalment": "no",
        }))
        merchant_node.append(order_node)

        merchant_sign_node = Element("merchant_sign", {
            "type": "RSA",
        })
        merchant_sign_node.text = cls.signature(str(ET.tostring(merchant_node), encoding="UTF-8"))

        document.append(merchant_node)
        document.append(merchant_sign_node)
        return str(b64encode(ET.tostring(document)), encoding="UTF-8")

    @classmethod
    def encoded_appendix(cls, cart_handle):
        document = Element("document")

        for index, item in enumerate(cart_handle):
            document.append(Element("item", {
                "number": str(index + 1),
                "name": item.description(),
                "quantity": "1",
                "amount": str(item.total()),
            }))

        return str(b64encode(ET.tostring(document)), encoding="UTF-8")

    @classmethod
    def private_key(cls):
        raise NotImplementedError("%s has to implement 'private_key' class method" % cls.__name__)

    @classmethod
    def private_password(cls):
        raise NotImplementedError("%s has to implement 'private_password' class method" % cls.__name__)

    @classmethod
    def qazkom_certificate(cls):
        raise NotImplementedError("%s has to implement 'qazkom_certificate' class method" % cls.__name__)

    @classmethod
    def merchant_id(cls):
        raise NotImplementedError("%s has to implement 'merchant_id' class method" % cls.__name__)

    @classmethod
    def merchant_cert_id(cls):
        raise NotImplementedError("%s has to implement 'merchant_cert_id' class method" % cls.__name__)

    @classmethod
    def merchant_name(cls):
        raise NotImplementedError("%s has to implement 'merchant_name' class method" % cls.__name__)

    def __verify_document(self, document):
        try:
            document_node = ET.fromstring(document)
            payload_match = search(r"(?P<bank><bank .+?</bank>)", document, I|S)
            if not payload_match:
                raise ValueError("Incorrect document")
            signature_node = document_node.find("bank_sign")
            if not signature_node:
                raise ValueError("Incorrect document")
            if not self.is_verifiable(payload_match.group("bank"), signature_node.text.strip()):
                raise MerchantError("Incorrect bank signature")
        except (ParseError, ValueError):
            raise PaymentProcessorError("Incorrect document")

    def __command_url(self):
        if self.is_test():
            return "https://testpay.kkb.kz/jsp/remote/control.jsp"
        return "https://epay.kkb.kz/jsp/remote/control.jsp"

    def __command_string(self, command, reason=None):
        document = Element("document")

        merchant_node = Element("merchant", {
            "id": self.merchant_id(),
        })
        merchant_node.append(Element("command", {
            "type": command,
        }))
        merchant_node.append(Element("payment", {
            "reference": self.__authorization_data["reference"],
            "approval_code": self.__authorization_data["approval_code"],
            "orderid": self.__authorization_data["order_id"],
            "amount": str(self.amount()),
            "currency_code": "398",
        }))
        if reason:
            reason_node = Element("reason")
            reason_node.text = reason
            merchant_node.append(reason_node)

        merchant_sign_node = Element("merchant_sign", {
            "type": "RSA",
            "cert_id": self.merchant_cert_id(),
        })
        merchant_sign_node.text = self.signature(str(ET.tostring(merchant_node), encoding="UTF-8"))

        document.append(merchant_node)
        document.append(merchant_sign_node)
        return str(ET.tostring(document), encoding="UTF-8")

    def __retrieve_authorization_data(self):
        document = ET.fromstring(self.__authorization_response)
        try:
            node = document.find("bank").find("results").find("payment")
            if node.attrib["merchant_id"] != self.merchant_id():
                raise MerchantError("Incorrect Merchant ID in authorization response")
            if Decimal(node.attrib["amount"]) != self.amount():
                raise MerchantError("Incorrect amount in authorization response")
            if node.attrib["response_code"] != "00":
                raise MerchantError("Authorization was not successful")
            self.__authorization_data = {
                "reference": node.attrib["reference"],
                "approval_code": node.attrib["approval_code"],
                "order_id": document.find("bank").find("customer").find("merchant").find("order").attrib["order_id"],
            }
        except (AttributeError, KeyError, DecimalException):
            raise MerchantError("Incorrect authorization response")


class FirstQazkomPaymentProcessor(QazkomPaymentProcessor):
    @classmethod
    def private_key(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_QAZKOM_PAYMENT_PROCESSOR"]["PRIVATE_KEY"]

    @classmethod
    def private_password(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_QAZKOM_PAYMENT_PROCESSOR"]["PRIVATE_KEY_PASS"]

    @classmethod
    def qazkom_certificate(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_QAZKOM_PAYMENT_PROCESSOR"]["PUBLIC_KEY"]

    @classmethod
    def merchant_id(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_QAZKOM_PAYMENT_PROCESSOR"]["MERCHANT_ID"]

    @classmethod
    def merchant_cert_id(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_QAZKOM_PAYMENT_PROCESSOR"]["MERCHANT_CERTIFICATE_ID"]

    @classmethod
    def merchant_name(cls):
        return settings.SECRETS["PAYMENT_PROCESSOR_CREDENTIALS"]["FIRST_QAZKOM_PAYMENT_PROCESSOR"]["MERCHANT_NAME"]
