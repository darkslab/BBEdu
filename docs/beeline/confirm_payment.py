from django.conf import settings
from requests import post
from requests.exceptions import RequestException
import hmac
from bbtest.utils.json import tight_dumps

kwargs = {
    "headers": {
        "User-Agent": settings.BB_USER_AGENT,
        "Content-Type": "application/json",
    },
    "timeout": 8,
    "verify": False,
}
hasher = hmac.new(bytes("rqv66G0RWoluxx5h272R", encoding="utf8"), digestmod="sha256")

try:
    url = "https://tstmpay.beeline.kz/merchant-api/v1/confirm-payment"
    data = tight_dumps({
        "paymentId": 2055,
        "otp": 240873,
    })
    hasher.update(bytes(data, encoding="utf8"))
    kwargs["headers"]["Signature"] = hasher.hexdigest()
    kwargs["headers"]["Api-Name"] = "tstbbminds"
    response = post(url, data=data, **kwargs)
    if response.status_code != 200 or response.json()["status"] != "ok":
        raise ValueError("Unsuccessful payment")

    print(response.json())

    # {
    #     "receipts": {
    #         "emoneyReceipt": {
    #             "agentAddress": "address",
    #             "operatorName": "ТОО КАЗЕВРОМОБАЙЛ",
    #             "agentName": "Каумбаев Жамбыл Оразбаевич",
    #             "emoneyTransactionId": 2055,
    #             "totalAmount": 5,
    #             "operatorBin": "070940019233",
    #             "transactionType": "Покупка ЭД",
    #             "emoneyTransactionTimestamp": 1556892487,
    #             "walletNumber": 182,
    #             "operatorAddress": "Республика Казахстан, г. Алматы, 050040, Бостандыкский район, микрорайон Коктем-2, д.22.",
    #             "agentBin": "920114301585",
    #             "commission": 0
    #         },
    #         "paymentReceipt": {
    #             "merchantAddress": "Республика Казахстан, г. Нур-Султан (Астана), пр. Кабанбай батыра 43а, п.м. 67",
    #             "commission": 0,
    #             "operatorName": "ТОО КАЗЕВРОМОБАЙЛ",
    #             "payerPhone": "77052036767",
    #             "merchantBin": "171040002110",
    #             "merchantName": "Товарищество с ограниченной ответственностью «BBMINDS»",
    #             "amount": 5,
    #             "paymentTransactionTimestamp": 1556892487,
    #             "walletNumber": 182,
    #             "operatorBin": "070940019233",
    #             "transactionType": "Оплата продукта",
    #             "paymentTransactionId": 2055,
    #             "operatorAddress": "Республика Казахстан, г. Алматы, 050040, Бостандыкский район, микрорайон Коктем-2, д.22.",
    #             "totalAmount": 5
    #         }
    #     },
    #     "isSmsSent": true,
    #     "status": "ok"
    # }

except (RequestException, ValueError, KeyError) as error:
    print(error)
