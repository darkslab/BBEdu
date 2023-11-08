from django.utils.translation import pgettext
from decimal import Decimal
from ..test import TestItem
from ...exceptions import ItemError
from bbtest.models import Account


class NISItem(TestItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section.domain.pk not in (7911, 7912, 7913, 7914, 7915, 7916):
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
        self.assert_price()
        return new_items

    def question_discount(self):
        non_language_items_count = 0
        language_items_count = 0
        for item in self.handle():
            if isinstance(item, NonLanguageNISItem) and not item.test().is_free:
                non_language_items_count += 1
            elif isinstance(item, LanguageNISItem) and not item.test().is_free:
                language_items_count += 1
        if non_language_items_count > 1:
            if language_items_count > 0:
                return Decimal("2.00")
            return Decimal("1.00")
        elif non_language_items_count > 0 and language_items_count > 0:
            return Decimal("1.00")
        return Decimal("0.00")


class NonLanguageNISItem(NISItem):
    pass


class LanguageNISItem(NISItem):
    pass
