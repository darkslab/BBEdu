from django.db.models import Model, CharField, TextField, DateTimeField
from django.utils.translation import pgettext_lazy


class Message(Model):
    name        = CharField      ( pgettext_lazy("Model field", "name"),       max_length=200,    blank=True,                )
    phone       = CharField      ( pgettext_lazy("Model field", "phone"),      max_length=200,    blank=True,                )
    email       = CharField      ( pgettext_lazy("Model field", "email"),      max_length=200,    blank=True,                )
    message     = TextField      ( pgettext_lazy("Model field", "message"),                                                  )
    created_at  = DateTimeField  ( pgettext_lazy("Model field", "created at"), auto_now_add=True,             db_index=True, )

    class Meta:
        db_table = "messages"
        default_permissions = ()

    def __str__(self):
        if self.pk:
            return "Message #%d" % self.pk
        return "New Message"
