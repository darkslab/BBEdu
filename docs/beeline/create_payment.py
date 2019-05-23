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
    url = "%s/merchant-api/v1/create-payment" % secret_domain
    data = tight_dumps({
        "productId": 45,
        "amount": "15.0",
        # "productReceiver": "7775713030",
        # "payerPhone": "7775713030",
        "productReceiver": "7052036767",
        "payerPhone": "7052036767",
        "sellerId": "1",
        "merchantOrderId": 5604,
        "description": "Monkey!",
    })
    hasher.update(bytes(data, encoding="utf8"))
    kwargs["headers"]["Signature"] = hasher.hexdigest()
    kwargs["headers"]["Api-Name"] = secret_api_name
    response = post(url, data=data, **kwargs)
    if response.status_code != 200 or response.json()["status"] != "ok":
        raise ValueError("Unsuccessful payment")

    print(response.json())

    # {
    #     "paymentDetails": {
    #         "paymentId": 2052,
    #         "otpConfirm": true,
    #         "totalAmount": 5,
    #         "commission": 0,
    #         "amount": 5
    #     },
    #     "status": "ok"
    # }

except (RequestException, ValueError, KeyError) as error:
    print(error)
