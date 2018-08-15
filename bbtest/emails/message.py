from django.template import loader
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def send_mail(message):
    subject = "New message from a user"
    if message.name:
        subject = "New message from %s" % message.name
    reply_to_emails = []
    try:
        validate_email(message.email.strip())
        reply_to_emails.append(message.email.strip())
    except ValidationError:
        pass

    email = EmailMessage(
        subject=subject,
        body=loader.render_to_string("emails/message.html", {
            "base_url": settings.BB_BASE_URL,
            "name": message.name,
            "phone": message.phone,
            "email": message.email,
            "message": message.message,
        }),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=settings.BB_MANAGERS,
        reply_to=reply_to_emails,
    )
    email.content_subtype = "html"
    email.send()
