from django.template import loader
from django.core.mail import EmailMessage
from django.utils.translation import pgettext
from django.urls import reverse


def send_mail(to_email, context):
    reset_url = "%s://%s%s" % (
        context["protocol"],
        context["domain"],
        # DARK_TODO
        reverse("bbtest:password_reset"),
    )
    email = EmailMessage(
        subject=pgettext("Email subject", "Password reset"),
        body=loader.render_to_string("emails/password_reset.html", {
            "base_url": "%s://%s" % ( context["protocol"], context["domain"] ),
            "user": context["user"],
            "reset_url": reset_url,
        }),
        from_email="bbTest.kz <accounts@bbtest.kz>",
        to=[ to_email ],
    )
    email.content_subtype = "html"
    email.send()
