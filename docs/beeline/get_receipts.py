from django.conf import settings
from requests import post
from requests.exceptions import RequestException
import hmac
from bbtest.utils.json import tight_dumps

secret_api_name = "tstbbminds"
secret_private_key = "rqv66G0RWoluxx5h272R"
secret_domain = "https://tstmpay.beeline.kz"

kwargs = {
    "headers": {
        "User-Agent": settings.BB_USER_AGENT,
        "Content-Type": "application/json",
    },
    "timeout": 8,
    "verify": False,
}
hasher = hmac.new(bytes(secret_private_key, encoding="utf8"), digestmod="sha256")

try:
    url = "%s/merchant-api/v1/get-receipts" % secret_domain
    data = tight_dumps({
        "paymentId": 19294,
    })
    hasher.update(bytes(data, encoding="utf8"))
    kwargs["headers"]["Signature"] = hasher.hexdigest()
    kwargs["headers"]["Api-Name"] = secret_api_name
    response = post(url, data=data, **kwargs)
    if response.status_code != 200 or response.json()["status"] != "ok":
        raise ValueError("Unsuccessful payment")

    print(response.json())

    # {
    #     "status": "ok",
    #     "categories": [
    #         {
    #             "categoryId": 22,
    #             "categoryName": "Мобильные операторы",
    #             "parentId": "None"
    #         },
    #         {
    #             "categoryId": 23,
    #             "categoryName": "Билеты",
    #             "parentId": "None"
    #         },
    #         {
    #             "categoryId": 24,
    #             "categoryName": "Финансовые услуги",
    #             "parentId": "None"
    #         },
    #         {
    #             "categoryId": 25,
    #             "categoryName": "Букмекеры",
    #             "parentId": "None"
    #         }
    #     ],
    #     "products": [
    #         {
    #             "id": 34,
    #             "categoryId": 22,
    #             "is_own_product": false,
    #             "name": "Интернет Дома"
    #         },
    #         {
    #             "id": 33,
    #             "categoryId": 22,
    #             "is_own_product": false,
    #             "name": "Мобильный перевод Sim2Sim"
    #         },
    #         {
    #             "id": 42,
    #             "categoryId": 24,
    #             "is_own_product": true,
    #             "name": "bbtest.kz"
    #         }
    #     ]
    # }

except (RequestException, ValueError, KeyError) as error:
    print(error)
