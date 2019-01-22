from django.utils.translation import pgettext
from decimal import Decimal
from ..test import TestItem
from ...exceptions import ItemError
from bbtest.models import Account


class UNTItem(TestItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section.domain.pk != 7912:
            raise ItemError(pgettext("Item error", "UNT Test is required."))

    def revenue_account(self):
        return Account.objects.get(name="Tests-UNT")

    def merge_into_items(self, items):
        new_items = []
        for item in items:
            if not isinstance(item, UNTItem) or item.student() != self.student() or item.language() != self.language() or item.test().section.pk == self.test().section.pk:
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


class CompulsoryUNTItem(UNTItem):
    def question_discount(self):
        compulsory_items_count = 0
        profile_items_count = 0
        for item in self.handle():
            if isinstance(item, CompulsoryUNTItem) and not item.test().is_free:
                compulsory_items_count += 1
            elif isinstance(item, ProfileUNTItem) and not item.test().is_free:
                profile_items_count += 1
        if compulsory_items_count < 3:
            return Decimal("0.00")
        if profile_items_count >= 2:
            return Decimal("2.00")
        return Decimal("1.00")


class ProfileUNTItem(UNTItem):
    def question_discount(self):
        compulsory_items_count = 0
        profile_items_count = 0
        self_index = None
        for i, item in enumerate(self.handle()):
            if isinstance(item, CompulsoryUNTItem) and not item.test().is_free:
                compulsory_items_count += 1
            elif isinstance(item, ProfileUNTItem) and not item.test().is_free:
                profile_items_count += 1
                if item == self:
                    self_index = i - compulsory_items_count
        if self_index is None:
            raise RuntimeError("Something is not right")
        if self_index not in range((profile_items_count // 2) * 2):
            return Decimal("0.00")
        if compulsory_items_count >= 3 and self_index in range(2):
            return Decimal("2.00")
        return Decimal("1.00")
