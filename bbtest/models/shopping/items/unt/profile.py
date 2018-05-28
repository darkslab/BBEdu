from django.utils.translation import pgettext
from decimal import Decimal
from .base import UNTItem
from ...exceptions import ItemError


class ProfileUNTItem(UNTItem):
    pass


class MathematicsProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "Mathematics Profile UNT Test is required."))

    def description(self):
        return "Mathematics Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class PhysicsProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "Physics Profile UNT Test is required."))

    def description(self):
        return "Physics Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class ChemistryProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "Chemistry Profile UNT Test is required."))

    def description(self):
        return "Chemistry Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class BiologyProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "Biology Profile UNT Test is required."))

    def description(self):
        return "Biology Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class GeographyProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "Geography Profile UNT Test is required."))

    def description(self):
        return "Geography Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class HistoryProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "History Profile UNT Test is required."))

    def description(self):
        return "History Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class EnglishLanguageProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "English Language Profile UNT Test is required."))

    def description(self):
        return "English Language Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class FrenchLanguageProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "French Language Profile UNT Test is required."))

    def description(self):
        return "French Language Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class GermanLanguageProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "German Language Profile UNT Test is required."))

    def description(self):
        return "German Language Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class KazakhLanguageAndLiteratureProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "Kazakh Language and Literature Profile UNT Test is required."))

    def description(self):
        return "Kazakh Language and Literature Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class RussianLanguageAndLiteratureProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "Russian Language and Literature Profile UNT Test is required."))

    def description(self):
        return "Russian Language and Literature Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")


class HumanSocietyRightProfileUNTItem(ProfileUNTItem):
    def assert_test_and_student(self, test, student):
        super().assert_test_and_student(test, student)
        if test.section_id != 0:
            raise ItemError(pgettext("Item error", "Human. Society. Right Profile UNT Test is required."))

    def description(self):
        return "Human. Society. Right Profile UNT Test"

    def price(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")

    def discount(self):
        # DARK_TODO  implement this!
        return Decimal("0.00")
