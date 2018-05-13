from django.template import loader
from django.core.mail import EmailMessage
from django.conf import settings


def send_mail(subject, body):
    email = EmailMessage(
        subject=subject,
        body=loader.render_to_string("emails/manager.html", {
            "base_url": settings.BB_BASE_URL,
            "body": body,
        }),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=settings.BB_MANAGERS,
    )
    email.content_subtype = "html"
    email.send()
