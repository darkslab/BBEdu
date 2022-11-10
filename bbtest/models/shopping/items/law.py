from django.utils.translation import pgettext
from decimal import Decimal
from .test import TestItem
from ..exceptions import ItemError
from bbtest.models import Account, Test


class LawItem(TestItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section.domain.pk != 7915 or test.section_id != 9565:
            raise ItemError(pgettext("Item error", "Law Test is required."))

    def revenue_account(self):
        return Account.objects.get(name="Tests-LAW")

    def merge_into_items(self, items):
        new_items = []
        for item in items:
            if not isinstance(item, LawItem) or item.student() != self.student() or item.test().section.pk == self.test().section.pk:
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

    # def price(self):
    #     if self.test().is_free:
    #         return Decimal("0.00")
    #     return Decimal("200.00")

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal(self.test().section.question_price * self.test().section.question_count)
