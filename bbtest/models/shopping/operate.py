from django.db.transaction import atomic
from .exceptions import ChargeError
from bbtest.models.accounting import squash_funds
from bbtest.models import Account
from bbtest.payment_processors import PaymentProcessorError
from bbtest.emails.manager import send_mail


def charge(payment_processor, cart_handle):
    if payment_processor.amount() != cart_handle.total():
        raise ChargeError("Amounts mismatch")

    payment_processor.authorize()

    post_funds = squash_funds(payment_processor.funds() + cart_handle.funds())
    lock_funds = []
    for fund in post_funds:
        if fund.account().is_balance_account():
            lock_funds.append(fund)
    lock_funds.sort(key=lambda fund: fund.account().pk)

    try:
        with atomic(savepoint=False):
            for fund in lock_funds:
                Account.objects.select_for_update().get(pk=fund.account().pk)
                if fund.account().balance() < fund.amount():
                    raise ChargeError("Insufficient funds")
            # DARK_TODO  create transaction
            completed_cart = cart_handle.checkout()
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
    except PaymentProcessorError as error:
        send_mail("Payment processor failed capture", "\n".join([
            "Payment processor failed capture for %s (%s)" % (type(payment_processor).__name__, payment_processor.amount()),
            completed_cart,
            "",
            "Error: %s" % str(error),
        ]))


def refund():
    # DARK_TODO  Someday we'll be able to do the refunds too!
    pass
