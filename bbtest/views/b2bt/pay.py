
from decimal import Decimal
from django.conf import settings
from django.contrib.messages import success
from django.core.cache import cache
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, redirect, resolve_url
from django.urls import reverse, reverse_lazy
from django.utils.translation import get_language, pgettext

from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.forms.message import MessageForm
from bbtest.http import TightJsonResponse
from bbtest.jobs.kaspi_process_payment import kaspi_qr_payment_job
from bbtest.models import Account, Entry, TestDomain, Transaction
from bbtest.models.shopping.items import CreditItem
from bbtest.models.test import (
    TestPackageRusKazQuiz,
)
from bbtest.payment_processors import PaymentProcessorError
from bbtest.payment_processors.kaspi_qr import generate_QR_base64
from bbtest.payment_processors.kaspi_qr import order_create as kaspi_qr_order_create
from bbtest.views.common import UserContextMixin
from bbtest.views.generic import TemplateView, View


class BuyCreditsKaspiView(LoginRequiredMixin, UserContextMixin, TemplateView):
    template_name = "base/buy_credits_kaspi_qr.html"

    def get(self, request: WSGIRequest, package_pair_quiz_id, *args, **kwargs):
        package_pair_quiz_obj = get_object_or_404(TestPackageRusKazQuiz.objects, user=request.user, pk=package_pair_quiz_id)
        # if transaction is payed redirect to pakage quiz control
        if package_pair_quiz_obj.payed:
            return redirect("bbtest:b2bt_build_package_pair_quiz", package_pair_quiz_obj.pk)
        
        # caches kaspi payment url for five minutes
        order_key = f"package_pair_quiz_obj-{package_pair_quiz_obj.pk}"
        order = cache.get(order_key)
        cache_hit = order is not None
        kwargs["cart_rounded_total"] = 1

        if not cache_hit:
            order = kaspi_qr_order_create(kwargs["cart_rounded_total"])
            if order["status"] != "ok":
                raise PaymentProcessorError(str(order))
            cache.set(order_key, order, 60 * 5)

        
        kwargs['qr_code_base64'] = generate_QR_base64(order["payment_url"])
        kwargs["kaspi_qr_form"] = {
            "order_id": order["order_id"],
            "payment_url": order["payment_url"],
            'status': order["status"],
            # 'order_id': 47734761,
            # 'payment_url': 'https://kaspi.kz/pay/Smartvend?service_id=4680&7363=payprint-47734761',
            # 'status': "ok",
        }

        if not cache_hit:
            transaction = Transaction.objects.create(
                document=package_pair_quiz_obj,
                payment_processor_class="KaspiQRPaymentProcessor",
                meta_data=kwargs["kaspi_qr_form"],
                amount=kwargs["cart_rounded_total"],
                is_complete=False,
            )

        # kaspi_qr_payment_job.delay(transaction, order["order_id"])

        return self.render_to_response(super().get_context_data(**kwargs)) # super().get(request, *args, **kwargs)
