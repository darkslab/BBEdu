from django.db.models import Model, TextField, BinaryField, DateTimeField
from django.utils.translation import pgettext_lazy


class Email(Model):
    from_email = TextField(pgettext_lazy("Model field", "from email"), editable=False)
    recipients = TextField(pgettext_lazy("Model field", "recipients"), editable=False)
    subject = TextField(pgettext_lazy("Model field", "subject"), blank=True, editable=False)
    mime_data = BinaryField(pgettext_lazy("Model field", "mime data"), editable=False)
    created_at = DateTimeField(pgettext_lazy("Model field", "created at"), auto_now_add=True, db_index=True, editable=False)
    sent_at = DateTimeField(pgettext_lazy("Model field", "sent at"), null=True, blank=True, db_index=True, editable=False)

    class Meta:
        default_permissions = ()

    def __str__(self):
        subject = self.subject
        if len(subject) > 50:
            subject = "%s..." % subject[:47]
        elif not subject:
            subject = "(no subject)"
        return subject
