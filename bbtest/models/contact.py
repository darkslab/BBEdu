from django.db.models import Model, EmailField, DateTimeField, TextField
from django.utils.translation import pgettext_lazy


class Contact(Model):
    name       = TextField     ( pgettext_lazy("Model field", "name"),      max_length=100,    )
    email       = EmailField     ( pgettext_lazy("Model field", "email"),      max_length=200,    )
    phone       = EmailField     ( pgettext_lazy("Model field", "phone"),      max_length=15,    )
    message       = EmailField     ( pgettext_lazy("Model field", "message"),      max_length=1000,    )
    created_at  = DateTimeField  ( pgettext_lazy("Model field", "created at"), auto_now_add=True, )

    class Meta:
        default_permissions = ()

    def __str__(self):
        if self.pk:
            return "Contact #%d" % self.pk
        return "New Contact"
