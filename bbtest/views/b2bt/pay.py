from django.shortcuts import resolve_url, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.conf import settings
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.messages import success
from django.utils.translation import pgettext
from django.core.cache import cache
from decimal import Decimal
from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.views.base import is_cart_with_credits
from bbtest.views.generic import FormView, RedirectView, TemplateView, View
from bbtest.views.common import UserContextMixin
from bbtest.forms.base import BuyCreditsForm
from bbtest.forms.message import MessageForm
from bbtest.payment_processors import PaymentProcessorError
from bbtest.payment_processors.kaspi_qr import order_create as kaspi_qr_order_create
from bbtest.models.shopping.handle import CartHandleAccessMixin, CartHandle
from bbtest.models.shopping.items import CreditItem
from bbtest.models.shopping.items.credit import MIN_CREDIT_AMOUNT
from bbtest.models.shopping.operate import charge
from bbtest.models import Cart, TestDomain, Account, Entry, Transaction
from bbtest.http import TightJsonResponse
import qrcode
from io import BytesIO
import base64
from PIL import Image


class BuyCreditsKaspiView(LoginRequiredMixin, CartHandleAccessMixin, UserContextMixin, TemplateView):
    template_name = "base/buy_credits_kaspi_qr.html"

    def get(self, request, *args, **kwargs):
        if not is_cart_with_credits(self.cart_handle()):
            return redirect("bbtest:buy_credits")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        kwargs["cart_rounded_total"] = round(self.cart_handle().total())

        order = kaspi_qr_order_create(kwargs["cart_rounded_total"])
        if order["status"] != "ok":
            raise PaymentProcessorError(str(order))
        

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(order["payment_url"])
        qr.make(fit=True)

        # Create an image for the QR code
        img = qr.make_image().convert("RGB")

        # Load the logo image
        logo = Image.open(settings.BASE_DIR_PATH / "logo/qr_logo_center.png")  # Replace with the actual path to the logo
        logo = logo.convert("RGB")

        # Resize the logo to fit in the QR code (adjust as needed)
        logo_size = 75  # You can adjust this size
        logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

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
        kwargs['qr_code_base64'] = qr_code_base64
        
        kwargs["kaspi_qr_form"] = {
            "order_id": order["order_id"],
            "payment_url": order["payment_url"],
            'status': order["status"],
            # 'order_id': 47734761,
            # 'payment_url': 'https://kaspi.kz/pay/Smartvend?service_id=4680&7363=payprint-47734761',
            # 'status': "ok",
        }

        current_cart = self.cart_handle().get_cart()
        transaction = Transaction.objects.create(
            document=current_cart,
            payment_processor_class="KaspiQRPaymentProcessor",
            meta_data=kwargs["kaspi_qr_form"],
            amount=kwargs["cart_rounded_total"],
            is_complete=False,
        )
        return super().get_context_data(**kwargs)