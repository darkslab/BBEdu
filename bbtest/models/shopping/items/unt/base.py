from django.utils.translation import pgettext
from ..test import TestItem
from ...exceptions import ItemError
from bbtest.models import Account


class UNTItem(TestItem):
    def assert_test_and_student(self, test, student):
        if test.section.domain.name != "UNT":
            raise ItemError(pgettext("Item error", "UNT Test is required."))

    def revenue_account(self):
        return Account.objects.get(name="Tests-UNT")

    def merge_into_items(self, items):
        new_items = []
        for item in items:
            if not isinstance(item, UNTItem) or item.student() != self.student():
                continue
            new_item = item
            if item == self:
                new_item = self
            new_items.append(new_item)
        if self not in new_items:
            new_items.append(self)
        new_items.sort(key=lambda new_item: new_item.test().section.order)
        return new_items
