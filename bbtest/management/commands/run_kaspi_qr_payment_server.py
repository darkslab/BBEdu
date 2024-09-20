from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from decimal import Decimal
from bbtest.models import User, Cart, TestDomain, Account, Entry, Transaction
from bbtest.models.accounting import Entry, Debit, Credit, squash_funds
from bbtest.models.shopping.handle import CartHandle
from bbtest.payment_processors.kaspi_qr import order_status, order_result
from time import sleep
from django.conf import settings
from datetime import datetime
import logging
from datetime import datetime, timedelta
from django.utils.timezone import now


# run script every 1 minutes
# crontab -e
# */1 * * * * /usr/local/bin/python3 ~/BBEdu/manage.py run_kaspi_qr_payment_server



# rfh = logging.handlers.RotatingFileHandler(
#     filename='/home/darkhan/kaspi_qr.log', 
#     mode='a',
#     maxBytes=5*1024*1024,  # 5mb maximum log file size
#     backupCount=2,
#     encoding=None,
#     delay=0
# )

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s:%(levelname)s: %(message)s',
#     handlers=[
#         rfh
#     ]
# )

def now_str():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


class Command(BaseCommand):
    help = 'runs kaspi qr payment email service' 
    
    def handle(self, *args, **kwargs):
        # Get the current time and subtract one hour
        one_hour_ago = now() - timedelta(hours=1)
        
        pending_transactions = Transaction.objects.filter(
            is_complete=False,
            payment_processor_class="KaspiQRPaymentProcessor",
            created_at__gte=one_hour_ago
        )

        # Process the transactions (example: print them)
        for transaction in pending_transactions:
            order_id = transaction.meta_data["order_id"]
            # print(transaction.meta_data)
            # print(transaction)

            status = order_status(order_id)
            # print(status)
            # res = order_result(order_id)
            # print(res)
            cart = transaction.document
            # print(cart)

            

            if status['status'] == 'payment processed':
                cart_handle = CartHandle(transaction.document)

                payment_processor_funds = [Debit("Cash", cart_handle.total())]
                post_funds = squash_funds(payment_processor_funds + cart_handle.funds())
                post_funds.sort(key=lambda fund: fund.account().pk)

                with atomic(savepoint=False):
                    
                    completed_cart = cart_handle.checkout()
                    print(completed_cart)
                    
                    Entry.objects.post("Cart checkout (%s)" % cart_handle.total(), post_funds, document=completed_cart)

                    transaction.document = completed_cart
                    transaction.is_complete = True
                    transaction.save()