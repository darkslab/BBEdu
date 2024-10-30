import base64
from io import BytesIO

import qrcode
import requests
from django.conf import settings
from PIL import Image


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


def generate_QR_base64(url):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image for the QR code
    img = qr.make_image().convert("RGB")

    # Load the logo image
    logo = Image.open(settings.BASE_DIR_PATH / "logo/qr_logo_center.png")  # Replace with the actual path to the logo
    logo = logo.convert("RGB")

    # Resize the logo to fit in the QR code (adjust as needed)
    logo_size = 75  # You can adjust this size
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calculate the position to paste the logo (center of the QR code)
    qr_width, qr_height = img.size
    logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Paste the logo on the QR code image
    img.paste(logo, logo_position)
    
    # Convert the image to a byte stream
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_code_image = buffer.getvalue()

    # Encode the image in base64 so it can be rendered in an <img> tag
    qr_code_base64 = base64.b64encode(qr_code_image).decode('utf-8')
    return qr_code_base64