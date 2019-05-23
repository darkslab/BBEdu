from django.db.transaction import atomic
from .exceptions import ChargeError
from bbtest.models.accounting import squash_funds
from bbtest.models import Account, Entry, Transaction
from bbtest.payment_processors import PaymentProcessorError
from bbtest.emails.manager import send_mail


def charge(payment_processor, cart_handle):
    if payment_processor.amount() != cart_handle.total():
        raise ChargeError("Amounts mismatch")

    payment_processor.authorize()

    try:
        post_funds = squash_funds(payment_processor.funds() + cart_handle.funds())
        post_funds.sort(key=lambda fund: fund.account().pk)

        with atomic(savepoint=False):
            for fund in post_funds:
                if not fund.should_lock_account():
                    continue
                Account.objects.select_for_update().get(pk=fund.account().pk)
                if fund.account().balance() < fund.amount():
                    raise ChargeError("Insufficient funds")

            completed_cart = cart_handle.checkout()
            Entry.objects.post("Cart checkout (%s)" % cart_handle.total(), post_funds, document=completed_cart)
            transaction = Transaction.objects.create(
                document=completed_cart,
                payment_processor_class=type(payment_processor).__name__,
                meta_data=payment_processor.meta_data(),
                amount=payment_processor.amount(),
                is_complete=False,
            )

    except Exception:
        try:
            payment_processor.void()
        except PaymentProcessorError as error:
            send_mail("Payment processor failed void", "\n".join([
                "Payment processor failed void for %s (%s)" % (type(payment_processor).__name__, payment_processor.amount()),
                "",
                "Error: %s" % str(error),
            ]))
        raise

    try:
        payment_processor.capture()
        transaction.is_complete = True
        transaction.meta_data = payment_processor.meta_data()
        transaction.save()
    except PaymentProcessorError as error:
        send_mail("Payment processor failed capture", "\n".join([
            "Payment processor failed capture for %s (%s)" % (type(payment_processor).__name__, payment_processor.amount()),
            str(completed_cart),
            "",
            "Error: %s" % str(error),
        ]))
        raise


def refund():
    # DARK_TODO  Someday we'll be able to do the refunds too!
    pass
