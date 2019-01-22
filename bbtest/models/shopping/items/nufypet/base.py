from django.utils.translation import pgettext
from ..test import TestItem
from ...exceptions import ItemError
from bbtest.models import Account, Test


class NUFYPETItem(TestItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section.domain.pk != 7913:
            raise ItemError(pgettext("Item error", "NUFYPET Test is required."))
        if language != Test.LANGUAGE_XX:
            raise ItemError(pgettext("Item error", "NUFYPET Test does not have test language."))

    def revenue_account(self):
        return Account.objects.get(name="Tests-NUFYPET")

    def merge_into_items(self, items):
        new_items = []
        for item in items:
            if not isinstance(item, NUFYPETItem) or item.student() != self.student() or item.test().section.pk == self.test().section.pk:
                continue
            new_item = item
            if item == self:
                new_item = self
            new_items.append(new_item)
        if self not in new_items:
            new_items.append(self)
        new_items.sort(key=lambda new_item: new_item.test().section.order)
        self.assert_price()
        return new_items
