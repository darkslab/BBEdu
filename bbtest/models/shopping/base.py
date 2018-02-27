from django.db.models import (
    Model, ForeignKey, CASCADE,
    PositiveIntegerField, DecimalField, DateTimeField, NullBooleanField, IntegerField, CharField,
)
from django.contrib.auth import get_user_model
from django.utils.translation import pgettext_lazy
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from bbtest.models.fields import JSONField


class Cart(Model):
    buyer  = ForeignKey  ( get_user_model(), on_delete=CASCADE, related_name="carts", )

    lock_version  = PositiveIntegerField  ( pgettext_lazy("Model field", "lock version"),                                                                        default=0,     )
    discount      = DecimalField          ( pgettext_lazy("Model field", "discount"),     max_digits=16, decimal_places=2,                                                      )
    created_at    = DateTimeField         ( pgettext_lazy("Model field", "created at"),   auto_now_add=True,                                      db_index=True,                )
    updated_at    = DateTimeField         ( pgettext_lazy("Model field", "updated at"),   auto_now=True,                                          db_index=True,                )
    content_type  = ForeignKey            ( ContentType, on_delete=CASCADE, null=True, blank=True, )
    object_id     = IntegerField          ( pgettext_lazy("Model field", "object ID"),                                     null=True, blank=True, db_index=True,                )
    transaction   = GenericForeignKey     ()
    is_current    = NullBooleanField      ( pgettext_lazy("Model field", "is current?"),                                                          db_index=True,                )
    completed_at  = DateTimeField         ( pgettext_lazy("Model field", "completed at"),                                  null=True, blank=True, db_index=True,                )

    class Meta:
        db_table = "shopping_carts"
        default_permissions = ()
        unique_together = ("buyer", "is_current")

    def __str__(self):
        description = "completed"
        if self.is_current:
            description = "not completed"
        if self.pk:
            return "Cart #%s (%s)" % (self.pk, description)
        return "New Cart (%s)" % description


class LineItem(Model):
    cart  = ForeignKey  ( Cart, on_delete=CASCADE, related_name="line_items", )

    item_class   = CharField      ( pgettext_lazy("Model field", "item class"),  max_length=100,                  db_index=True, )
    meta_data    = JSONField      ( pgettext_lazy("Model field", "meta data"),                                                   )
    description  = CharField      ( pgettext_lazy("Model field", "description"), max_length=1000,                                )
    price        = DecimalField   ( pgettext_lazy("Model field", "price"),       max_digits=16, decimal_places=2,                )
    discount     = DecimalField   ( pgettext_lazy("Model field", "discount"),    max_digits=16, decimal_places=2,                )
    refunded     = DecimalField   ( pgettext_lazy("Model field", "refunded"),    max_digits=16, decimal_places=2,                )
    created_at   = DateTimeField  ( pgettext_lazy("Model field", "created at"),  auto_now_add=True,               db_index=True, )
    updated_at   = DateTimeField  ( pgettext_lazy("Model field", "updated at"),  auto_now=True,                   db_index=True, )

    class Meta:
        db_table = "shopping_line_items"
        default_permissions = ()

    def __str__(self):
        description = "not in cart"
        if self.cart_id:
            description = "in Cart #%s" % self.cart_id
        if self.pk:
            return "LineItem #%s (%s)" % (self.pk, description)
        return "New LineItem (%s)" % description
