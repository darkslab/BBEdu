from django.utils.translation import pgettext
from decimal import Decimal
from .base import CompulsoryUNTItem
from ...exceptions import ItemError


class MathematicalLiteracyCompulsoryUNTItem(CompulsoryUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9547:
            raise ItemError(pgettext("Item error", "Mathematical Literacy Compulsory UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class ReadingLiteracyCompulsoryUNTItem(CompulsoryUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9546:
            raise ItemError(pgettext("Item error", "Reading Literacy Compulsory UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class HistoryOfKazakhstanCompulsoryUNTItem(CompulsoryUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9545:
            raise ItemError(pgettext("Item error", "History of Kazakhstan Compulsory UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count
