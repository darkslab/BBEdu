from django.utils.translation import pgettext
from decimal import Decimal
from .base import NonLanguageNISItem, LanguageNISItem
from ...exceptions import ItemError


class MathematicsNISItem(NonLanguageNISItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9540:
            raise ItemError(pgettext("Item error", "Mathematics NIS Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("10.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class KazakhLanguageNISItem(LanguageNISItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9541:
            raise ItemError(pgettext("Item error", "Kazakh Language NIS Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("10.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class RussianLanguageNISItem(LanguageNISItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9542:
            raise ItemError(pgettext("Item error", "Russian Language NIS Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("10.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class EnglishLanguageNISItem(LanguageNISItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9543:
            raise ItemError(pgettext("Item error", "English Language NIS Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("10.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class QuantitativeNISItem(NonLanguageNISItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9544:
            raise ItemError(pgettext("Item error", "Quantitative NIS Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("10.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count
