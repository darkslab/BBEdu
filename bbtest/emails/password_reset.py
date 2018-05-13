from django.template import loader
from django.core.mail import EmailMessage
from django.utils.translation import pgettext
from django.urls import reverse
from django.conf import settings


def send_mail(to_email, context):
    reset_url = "%s%s" % (
        settings.BB_BASE_URL,
        reverse("bbtest:password_reset_confirm", kwargs={ "uidb64": context["uid"], "token": context["token"] }),
    )
    email = EmailMessage(
        subject=pgettext("Email subject", "Password reset"),
        body=loader.render_to_string("emails/password_reset.html", {
            "base_url": settings.BB_BASE_URL,
            "user": context["user"],
            "reset_url": reset_url,
        }),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[ to_email ],
    )
    email.content_subtype = "html"
    email.send()
