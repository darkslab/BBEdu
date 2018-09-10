from django.db.models import (
    Model, OneToOneField, CASCADE,
    PositiveSmallIntegerField, DateTimeField, CharField, GenericIPAddressField,
)
from django.contrib.auth import get_user_model
from django.utils.translation import pgettext_lazy


class DeveloperAcknowledgement(Model):
    PLAN_A  = 0x0001
    PLAN_C  = 0x0003
    PLANS = (
        ( PLAN_A, pgettext_lazy("Developer acknowledgement plan", "Immediate")   ),
        ( PLAN_C, pgettext_lazy("Developer acknowledgement plan", "Profitable")  ),
    )
    AGREEMENT_CODES_FOR_PLANS = {
        PLAN_A: "928d4499e9f1e6b90111710ecf607795",
        PLAN_C: "61011ada89570a6d41140a656fbbbd37",
    }
    AGREEMENT_CODES = []
    AGREEMENT_CODES.append((AGREEMENT_CODES_FOR_PLANS[PLAN_A], AGREEMENT_CODES_FOR_PLANS[PLAN_A]))
    AGREEMENT_CODES.append((AGREEMENT_CODES_FOR_PLANS[PLAN_C], AGREEMENT_CODES_FOR_PLANS[PLAN_C]))

    developer  = OneToOneField  ( get_user_model(), on_delete=CASCADE, related_name="acknowledgement", )

    plan             = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "plan"),                                           choices=PLANS,           db_index=True, )
    agreement_code   = CharField                  ( pgettext_lazy("Model field", "agreement code"),  max_length=32,                 choices=AGREEMENT_CODES, db_index=True, )
    signature        = CharField                  ( pgettext_lazy("Model field", "signature"),       max_length=200,                                                        )
    acknowledged_at  = DateTimeField              ( pgettext_lazy("Model field", "acknowledged at"), auto_now_add=True,                                                     )
    ip_address       = GenericIPAddressField      ( pgettext_lazy("Model field", "ip address"),      protocol="IPv4",                                                       )
    user_agent       = CharField                  ( pgettext_lazy("Model field", "user agent"),      max_length=200,    blank=True,                                         )

    class Meta:
        default_permissions = ()

    def __str__(self):
        if self.pk:
            return "DeveloperAcknowledgement #%d" % self.pk
        return "New DeveloperAcknowledgement"
