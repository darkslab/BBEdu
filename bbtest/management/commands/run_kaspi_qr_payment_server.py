from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from decimal import Decimal
from bbtest.models import Transaction, Entry
from bbtest.models.accounting import squash_funds, Debit
from bbtest.models.shopping.handle import CartHandle
from bbtest.payment_processors.kaspi_qr import order_status
from django.utils.timezone import now
from datetime import datetime, timedelta
import logging

# run script every 1 minutes
# crontab -e
# */1 * * * * /usr/local/bin/python3 ~/BBEdu/manage.py run_kaspi_qr_payment_server

BASE_DIR_PATH = settings.BASE_DIR_PATH

# Set up logging configuration
LOG_FILE = BASE_DIR_PATH.parent / 'kaspi_qr.log'
LOG_FILE = LOG_FILE.name

logging.basicConfig(
    level=logging.INFO,  # Adjust to DEBUG if you need more detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Optional: Also log to console
    ]
)

def now_str():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Command(BaseCommand):
    help = 'Runs Kaspi QR payment email service'

    def handle(self, *args, **kwargs):
        logging.info('Starting Kaspi QR payment server.')

        one_hour_ago = now() - timedelta(hours=1)

        try:
            pending_transactions = Transaction.objects.filter(
                is_complete=False,
                payment_processor_class="KaspiQRPaymentProcessor",
                created_at__gte=one_hour_ago
            )
            logging.info('Found {} pending transactions.'.format(pending_transactions.count()))

            for transaction in pending_transactions:
                order_id = transaction.meta_data["order_id"]
                logging.debug('Processing transaction with order ID: {}'.format(order_id))

                status = order_status(order_id)
                logging.debug('Status for order {}: {}'.format(order_id, status))

                if status['status'] == 'payment processed':
                    cart_handle = CartHandle(transaction.document)
                    payment_processor_funds = [Debit("Cash", cart_handle.total())]
                    post_funds = squash_funds(payment_processor_funds + cart_handle.funds())
                    post_funds.sort(key=lambda fund: fund.account().pk)

                    with atomic(savepoint=False):
                        completed_cart = cart_handle.checkout()
                        logging.info('Cart {} checked out successfully.'.format(completed_cart))

                        Entry.objects.post(
                            "Cart checkout ({})".format(cart_handle.total()), 
                            post_funds, 
                            document=completed_cart
                        )

                        transaction.document = completed_cart
                        transaction.is_complete = True
                        transaction.save()

                        logging.info('Transaction {} marked as complete.'.format(transaction.id))

        except Exception as e:
            logging.error('An error occurred: {}'.format(e), exc_info=True)
        finally:
            logging.info('Kaspi QR payment server finished.')
