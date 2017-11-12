from django.core.mail.backends.base import BaseEmailBackend
from bbtest.models import Email
from bbtest.jobs.amazon_ses import send_email


class EmailBackend(BaseEmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_messages(self, email_messages):
        if not email_messages:
            return
        num_sent = 0
        for email_message in email_messages:
            if not email_message.recipients():
                continue
            from_email = self.__get_address(email_message.from_email)
            recipients = [self.__get_address(addr) for addr in email_message.recipients()]

            email = Email.objects.create(
                from_email=from_email,
                recipients=", ".join(recipients),
                subject=email_message.subject,
                mime_data=email_message.message().as_bytes(linesep="\r\n"),
            )
            send_email.delay(email.id)

            num_sent += 1
        return num_sent

    def __get_address(self, address):
        if isinstance(address, tuple):
            address = "%s <%s>" % (
                address[0],
                address[1]
            )
        return address
