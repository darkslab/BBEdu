import logging
import time
from datetime import datetime, timedelta
from decimal import Decimal

from django.db.transaction import atomic
from django.utils.timezone import now
from django_rq import job

from bbtest.models import Account, Entry, Transaction
from bbtest.models.accounting import Debit, squash_funds
from bbtest.models.shopping.handle import CartHandle
from bbtest.models.test import (
    TestPackageRusKazQuiz,
)
from bbtest.payment_processors.kaspi_qr import order_status

# run script every 1 minutes
# crontab -e
# */1 * * * * /usr/local/bin/python3 ~/BBEdu/manage.py run_kaspi_qr_payment_server
logger = logging.getLogger("bbtest.payment")


@job("high", timeout=10*60)
def kaspi_qr_payment_job(transaction: Transaction, order_id: int, time_step = 5, timeout=10*60):
    logger.debug('Starting kaspi_qr_payment_job.')

    package_pair_quiz_obj: TestPackageRusKazQuiz = transaction.document
    if package_pair_quiz_obj.payed:
        logger.debug('Already payed TestPackageRusKazQuiz -> pk:{package_pair_quiz_obj.pk}')

    
    for i in range(timeout // time_step):
        time.sleep(time_step)

        try:
            status = order_status(order_id)
            logger.debug('Status for order {}: {}'.format(order_id, status))

            if status['status'] == 'payment processed':
                # cart_handle = CartHandle(transaction.document)
                total = 1

                payment_processor_funds = [Debit("Cash", Decimal(total))]
                post_funds = squash_funds(payment_processor_funds)
                post_funds.sort(key=lambda fund: fund.account().pk)

                with atomic(savepoint=False):
                    # completed_cart = cart_handle.checkout()
                    # logger.info('Cart {} checked out successfully.'.format(completed_cart))

                    Entry.objects.post(
                        "Cart checkout ({})".format(total),
                        post_funds,
                        document=package_pair_quiz_obj
                    )

                    transaction.document = package_pair_quiz_obj
                    transaction.is_complete = True
                    transaction.save()

                    logger.info('Transaction {} marked as complete.'.format(transaction.id))
                
                    package_pair_quiz_obj.payed = True
                    package_pair_quiz_obj.save()

        except Exception as e:
            logger.error('An error occurred: {}'.format(e), exc_info=True)
        finally:
            logger.info('Kaspi QR payment server finished.')