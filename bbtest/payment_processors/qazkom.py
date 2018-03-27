from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.exceptions import InvalidSignature
from base64 import b64encode, b64decode
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element
from .base import PaymentProcessor


class QazkomPaymentProcessor(PaymentProcessor):
    def __init__(self):
        pass

    def authorize(self):
        pass

    def capture(self):
        raise NotImplementedError("%s has to implement 'capture' method" % type(self).__name__)

    def void(self):
        raise NotImplementedError("%s has to implement 'void' method" % type(self).__name__)

    def refund(self):
        raise NotImplementedError("%s has to implement 'refund' method" % type(self).__name__)

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
