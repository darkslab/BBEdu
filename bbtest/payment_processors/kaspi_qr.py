from django.conf import settings
import requests

base_url = "https://partner.smartvend.kz/api/payprint/"
headers = {"Content-Type": "application/json"}


def order_create(price_to_pay: int) -> dict:
    print("price_to_pay {}".format(price_to_pay))
    print("vm_id {}".format(repr(settings.VM_ID)))
    print("vm_secret {}".format(repr(settings.VM_SECRET)))
    data = {
        "vm_id": settings.VM_ID,
        "vm_secret": settings.VM_SECRET,
        "price": price_to_pay,
    }

    response = requests.post(base_url + "order_create/", json=data, headers=headers)
    print("order_create", response.json())
    # response.json(): {'order_id': 47734761,
    #                   'payment_url': 'https://kaspi.kz/pay/Smartvend?service_id=4680&7363=payprint-47734761',
    #                   'status': 'ok'}
    return response.json()


def order_status(order_id: int) -> dict:
    data = {
        "vm_id": settings.VM_ID,
        "vm_secret": settings.VM_SECRET,
        "order_id": order_id,
    }

    response = requests.post(base_url + "order_status/", json=data, headers=headers)
    print(order_id, response.json())
    # {'status': 'payment wait'}
    # {'status': 'payment processed'}
    return response.json()


def order_result(order_id: int) -> dict:
    data = {
        "vm_id": settings.VM_ID,
        "vm_secret": settings.VM_SECRET,
        "order_id": order_id,
        "vend_status": True,
    }

    response = requests.post(base_url + "order_result/", json=data, headers=headers)
    print(response.json())
    # {'status': 'ok'}
    return response.json()
