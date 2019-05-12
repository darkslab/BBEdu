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
    url = "https://tstmpay.beeline.kz/merchant-api/v1/get-products"
    data = tight_dumps({
        "is_active": True,
    })
    hasher.update(bytes(data, encoding="utf8"))
    kwargs["headers"]["Signature"] = hasher.hexdigest()
    kwargs["headers"]["Api-Name"] = "tstbbminds"
    response = post(url, data=data, **kwargs)
    if response.status_code != 200 or response.json()["status"] != "ok":
        raise ValueError("Unsuccessful payment")

    print(response.json())
except (RequestException, ValueError, KeyError) as error:
    print(error)
