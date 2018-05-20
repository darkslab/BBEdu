from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element


"""
<document>
    <merchant id="92061103"> 
        <command type="complete" />
        <payment reference="180326030450" approval_code="030450" orderid="888888888888004" amount="100.00" currency_code="398" />
        <reason>Only for reverse/refund</reason>
    </merchant>
    <merchant_sign type="RSA" cert_id="00c183d70b">
        p25i1rUH7StnhOfnkHSOHguuPMePaGXtiPGEOrJE4bof1gFVH19mhDyHjfWa6OeJ80fidyvVf1X4
        ewyP0yG4GxJSl0VyXz7+PNLsbs1lJe42d1fixvozhJSSYN6fAxMN8hhDht6S81YK3GbDTE7GH498
        pU9HGuGAoDVjB+NtrHk=
    </merchant_sign>
</document>
"""

document = Element("document")
merchant = Element("merchant", {
    "id": "92061103",
})
merchant.append(Element("command", {
    "type": "complete",
}))
merchant.append(Element("payment", {
    "reference": "180326030450",
    "approval_code": "030450",
    "orderid": "888888888888004",
    "amount": "100.00",
    "currency_code": "398",
}))
document.append(merchant)




from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from base64 import b64encode

test_private_key = "-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,D7EAB35213AF0278\n\nkNBrP8tIJOygO25g/R0ZocgY+WUPHE/xvVomhPf8hnD4X7ldn/NGYRXjsVJ5WPhB\n4l0p95RNveQW2nlTyyRiqpymAD7iqM7ztpktTghh0Bjwl0Qk1zluxycCtZW3/HzW\nvXdfOuQmftDh6gZsTQ5jx67YXZABqjTUV5RCAwwx4mklDC2TYpJd1pdVgdXjPCcP\nLnREinm4QjFC7Ph27vbLc/no0PwJFgzzf4/UrYv0TFx90mwQCaz/gJg5h1nXolaG\n3nTBXnND5jX99IdMOF1igGzGDAL8oLqclsP6d8Cq3/bHyENzPnAhXoro/oOH6q6F\n3E+JY9ILIw6LCZr8JbE13XzCbbpds2kn+xTViGgbbgpTNx0q6AKwQtiwZsqcT7cu\nmRoH4V8QdMEUO8AQV8LCH5xpw1qYbbfAFo2hM3le9lUqD5aOl8Dd19l0Im7rXC6/\nQKGsweSqs+ysGjExP/xI9noH3kiE2vXlbiRmwUgoqYU5TSAV4t1RVsjm1zb8CtvY\nB67OMPJx6ATN+bJs8mq54nz1Cpz6Nk7n2gUi+NWKleaxTcb1FOXTN3Zty5OM5LDs\nWZqvaVawyaePaubVGGEcYB3Pq6MyJuxjROgneaU5Oxx3b+FyLoc197rELYsz+N1A\nLpbJsnf+aXpKeLqDX5Nk0b9ZB4tOu+lWxfmUYZXAcvym32NhApXR5olkyqNVKSJi\nGZZRtK+9gXPlKecB6/XZXm+H1hc6jw4gIesaEJ8b8YyYF3s6iJTGdba4D17kghQ7\nXwXfhSxUBnkgI/RULCwnf8ZFjI7H92+qiiG/jW8JLMA=\n-----END RSA PRIVATE KEY-----\n"
test_private_pass = "1q2w3e4r"

signing_key = load_pem_private_key(
    bytes(test_private_key, encoding="UTF-8"),
    password=bytes(test_private_pass, encoding="UTF-8"),
    backend=default_backend(),
)
binary_signature = signing_key.sign(
    ET.tostring(merchant),
    PKCS1v15(),
    SHA1(),
)
signature = str(b64encode(binary_signature[::-1]), encoding="UTF-8")


merchant_sign = Element("merchant_sign", {
    "type": "RSA",
    "cert_id": "00c183d70b",
})
merchant_sign.text = signature
document.append(merchant_sign)




from requests import get
from requests.exceptions import RequestException


try:
    response = get("https://testpay.kkb.kz/jsp/remote/control.jsp", params=str(ET.tostring(document), encoding="UTF-8"), headers={
        "User-Agent": "bbTest.kz",
    }, timeout=8)
except RequestException as error:
    print("Something happened: %s" % str(error))


"""

<?xml version="1.0" encoding="UTF-8"?>
<document>
    <bank name="Kazkommertsbank JSC">
        <merchant id="92061103">
            <command type="complete"/>
            <payment amount="100.00" approval_code="030450" currency_code="398" orderid="888888888888004" reference="180326030450"/>
        </merchant>
        <merchant_sign cert_id="00c183d70b" type="RSA">VOaxxtcz9g/hXjhNrK2BzEGJmxhpIp9g8lGx189EhFHPx0BLnsSqHK65eTAUcRbowaJtlk0zenl9TSGAgnRLq1J2/GsZgvV5/bLZIP1Cb3V0XZFBQhC2m7aXiqybkkhY6eL1njWemupop3ncB7zMuKjUB7l52OWbNV5ISwCYwQM=</merchant_sign>
        <response code="00" message="Approved" SessionID="51B52E2F45556256D5740E4CF820135B"/>
    </bank>
    <bank_sign type="RSA" cert_id="00c183d690">cinMWMGs+xEFpSV2wtMsSw4Q/464aRCaDTMNhIIymbtUol1tdrMNEgfyi8jwFbYZM3+2/UdhEXxFNoNDAWgNRBnCU9xetqYwSTfQ2zugg/60JCLaVjtaGHtMr5DwqZWhSWg9C8EzFf3SWdKDvP24QbLyyuTgpKS0qJRxaMoflXk=</bank_sign>
</document>

"""
