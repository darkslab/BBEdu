from django.template import loader
from django.core.mail import EmailMessage
from django.conf import settings


def send_mail(subject, template_path, from_email, to_email):
    email = EmailMessage(
        subject=subject,
        body=loader.render_to_string(template_path, {
            "base_url": settings.BB_BASE_URL,
        }),
        from_email=from_email,
        to=to_email,
    )
    email.content_subtype = "html"
    email.send()
