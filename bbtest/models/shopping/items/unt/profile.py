from django.utils.translation import pgettext
from decimal import Decimal
from .base import ProfileUNTItem
from ...exceptions import ItemError


class MathematicsProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9548:
            raise ItemError(pgettext("Item error", "Mathematics Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class PhysicsProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9549:
            raise ItemError(pgettext("Item error", "Physics Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class ChemistryProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9550:
            raise ItemError(pgettext("Item error", "Chemistry Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class BiologyProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9551:
            raise ItemError(pgettext("Item error", "Biology Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class GeographyProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9552:
            raise ItemError(pgettext("Item error", "Geography Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class HistoryProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9553:
            raise ItemError(pgettext("Item error", "History Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class EnglishLanguageProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9554:
            raise ItemError(pgettext("Item error", "English Language Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class FrenchLanguageProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9555:
            raise ItemError(pgettext("Item error", "French Language Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class GermanLanguageProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9556:
            raise ItemError(pgettext("Item error", "German Language Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class KazakhLanguageAndLiteratureProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9557:
            raise ItemError(pgettext("Item error", "Kazakh Language and Literature Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class RussianLanguageAndLiteratureProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9558:
            raise ItemError(pgettext("Item error", "Russian Language and Literature Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count


class HumanSocietyRightProfileUNTItem(ProfileUNTItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9559:
            raise ItemError(pgettext("Item error", "Human. Society. Right Profile UNT Test is required."))

    def price(self):
        if self.test().is_free:
            return Decimal("0.00")
        return Decimal("6.00") * self.test().section.question_count

    def discount(self):
        if self.price().is_zero():
            return Decimal("0.00")
        return self.question_discount() * self.test().section.question_count
