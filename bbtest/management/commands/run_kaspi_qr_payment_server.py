from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from decimal import Decimal
from bbtest.models import Transaction, Entry
from bbtest.models.accounting import squash_funds, Debit
from bbtest.models.test import TestPackageRusKazQuiz
from bbtest.payment_processors.kaspi_qr import order_status
from django.utils.timezone import now
from datetime import datetime, timedelta
import logging

# run script every 1 minutes
# crontab -e
# */1 * * * * /usr/local/bin/python3 ~/BBEdu/manage.py run_kaspi_qr_payment_server
# */1 * * * * docker exec django_container python3 manage.py run_kaspi_qr_payment_server
logger = logging.getLogger("bbtest.payment")


class Command(BaseCommand):
    help = 'Runs Kaspi QR payment email service'

    def handle(self, *args, **kwargs):
        logger.debug('Starting Kaspi QR payment server.')
        print('Run.')
        one_hour_ago = now() - timedelta(hours=1)

        try:
            pending_transactions = Transaction.objects.filter(
                is_complete=False,
                payment_processor_class="KaspiQRPaymentProcessor",
                created_at__gte=one_hour_ago
            )
            logger.info(f'Found {pending_transactions.count()} pending transactions.')
            # print(f'Found {pending_transactions.count()} pending transactions.')

            for transaction in pending_transactions:
                order_id = transaction.meta_data["order_id"]
                logger.info('Processing transaction with order ID: {}'.format(order_id))

                status = order_status(order_id)
                logger.info('Status for order {}: {}'.format(order_id, status))

                if status['status'] == 'payment processed':
                    # payment_processor_funds = [Debit("Cash", Decimal("10.0"))]
                    # post_funds = squash_funds(payment_processor_funds)
                    # post_funds.sort(key=lambda fund: fund.account().pk)

                    with atomic(savepoint=False):
                        package_pair_quiz_obj: TestPackageRusKazQuiz = transaction.document
                        # Entry.objects.post(
                        #     "Купили ({})".format(package_pair_quiz_obj.pk),
                        #     post_funds,
                        #     document=package_pair_quiz_obj
                        # )

                        transaction.is_complete = True
                        transaction.save()
                        package_pair_quiz_obj.payed = True
                        package_pair_quiz_obj.save()

                        logger.info(f'Transaction {transaction.id} marked as complete for package_pair_quiz_obj {package_pair_quiz_obj.id}.')

        except Exception as e:
            logger.error('An error occurred: {}'.format(e), exc_info=True)
        finally:
            logger.debug('Kaspi QR payment server finished.')