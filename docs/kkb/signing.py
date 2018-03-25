from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from base64 import b64encode

message = '<merchant cert_id="00c183d70b" name="Demo Shop 3"><order order_id="000001" amount="100" currency="398"><department merchant_id="92061103" amount="100" instalment="no" /></order></merchant>'
test_private_key = "-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,D7EAB35213AF0278\n\nkNBrP8tIJOygO25g/R0ZocgY+WUPHE/xvVomhPf8hnD4X7ldn/NGYRXjsVJ5WPhB\n4l0p95RNveQW2nlTyyRiqpymAD7iqM7ztpktTghh0Bjwl0Qk1zluxycCtZW3/HzW\nvXdfOuQmftDh6gZsTQ5jx67YXZABqjTUV5RCAwwx4mklDC2TYpJd1pdVgdXjPCcP\nLnREinm4QjFC7Ph27vbLc/no0PwJFgzzf4/UrYv0TFx90mwQCaz/gJg5h1nXolaG\n3nTBXnND5jX99IdMOF1igGzGDAL8oLqclsP6d8Cq3/bHyENzPnAhXoro/oOH6q6F\n3E+JY9ILIw6LCZr8JbE13XzCbbpds2kn+xTViGgbbgpTNx0q6AKwQtiwZsqcT7cu\nmRoH4V8QdMEUO8AQV8LCH5xpw1qYbbfAFo2hM3le9lUqD5aOl8Dd19l0Im7rXC6/\nQKGsweSqs+ysGjExP/xI9noH3kiE2vXlbiRmwUgoqYU5TSAV4t1RVsjm1zb8CtvY\nB67OMPJx6ATN+bJs8mq54nz1Cpz6Nk7n2gUi+NWKleaxTcb1FOXTN3Zty5OM5LDs\nWZqvaVawyaePaubVGGEcYB3Pq6MyJuxjROgneaU5Oxx3b+FyLoc197rELYsz+N1A\nLpbJsnf+aXpKeLqDX5Nk0b9ZB4tOu+lWxfmUYZXAcvym32NhApXR5olkyqNVKSJi\nGZZRtK+9gXPlKecB6/XZXm+H1hc6jw4gIesaEJ8b8YyYF3s6iJTGdba4D17kghQ7\nXwXfhSxUBnkgI/RULCwnf8ZFjI7H92+qiiG/jW8JLMA=\n-----END RSA PRIVATE KEY-----\n"
test_private_pass = "1q2w3e4r"

signing_key = load_pem_private_key(
    bytes(test_private_key, encoding="UTF-8"),
    password=bytes(test_private_pass, encoding="UTF-8"),
    backend=default_backend(),
)
print(str(b64encode(signing_key.sign(
    bytes(message, encoding="UTF-8"),
    PKCS1v15(),
    SHA1(),
)), encoding="UTF-8"))
