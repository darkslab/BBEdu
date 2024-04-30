from django.db.models import DateTimeField, EmailField, Model
from django.utils.translation import pgettext_lazy


class Subscription(Model):
    email       = EmailField     ( pgettext_lazy("Model field", "email"),      max_length=200,    )
    created_at  = DateTimeField  ( pgettext_lazy("Model field", "created at"), auto_now_add=True, )

    class Meta:
        default_permissions = ()

    def __str__(self):
        if self.pk:
            return "Subscription #%d" % self.pk
        return "New Subscription"
