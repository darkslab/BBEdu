from django.utils.translation import pgettext
from decimal import Decimal
from .base import UNTItem
from ...exceptions import ItemError


class CompulsoryUNTItem(UNTItem):
    pass


class MathematicalLiteracyCompulsoryUNTItem(CompulsoryUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 9547:
            raise ItemError(pgettext("Item error", "Mathematical Literacy Compulsory UNT Test is required."))

    def description(self):
        return "Mathematical Literacy Compulsory UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class ReadingLiteracyCompulsoryUNTItem(CompulsoryUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 9546:
            raise ItemError(pgettext("Item error", "Reading Literacy Compulsory UNT Test is required."))

    def description(self):
        return "Reading Literacy Compulsory UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class HistoryOfKazakhstanCompulsoryUNTItem(CompulsoryUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 9545:
            raise ItemError(pgettext("Item error", "History of Kazakhstan Compulsory UNT Test is required."))

    def description(self):
        return "History of Kazakhstan Compulsory UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")
