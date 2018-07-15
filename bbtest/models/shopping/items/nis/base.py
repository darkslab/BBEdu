from django.utils.translation import pgettext
from ..test import TestItem
from ...exceptions import ItemError
from bbtest.models import Account


class NISItem(TestItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section.domain.name != "NIS":
            raise ItemError(pgettext("Item error", "NIS Test is required."))

    def revenue_account(self):
        return Account.objects.get(name="Tests-NIS")

    def merge_into_items(self, items):
        new_items = []
        for item in items:
            if not isinstance(item, NISItem) or item.student() != self.student() or item.language() != self.language() or item.test().section.pk == self.test().section.pk:
                continue
            new_item = item
            if item == self:
                new_item = self
            new_items.append(new_item)
        if self not in new_items:
            new_items.append(self)
        new_items.sort(key=lambda new_item: new_item.test().section.order)
        return new_items
