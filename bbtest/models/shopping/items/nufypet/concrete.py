from django.utils.translation import pgettext
from decimal import Decimal
from .base import NUFYPETItem
from ...exceptions import ItemError


class MathematicsNUFYPETItem(NUFYPETItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9560:
            raise ItemError(pgettext("Item error", "Mathematics NUFYPET Test is required."))

    # def price(self):
    #     if self.test().is_free:
    #         return Decimal("0.00")
    #     return Decimal("16.00") * self.test().section.question_count


class PhysicsNUFYPETItem(NUFYPETItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9561:
            raise ItemError(pgettext("Item error", "Physics NUFYPET Test is required."))

    # def price(self):
    #     if self.test().is_free:
    #         return Decimal("0.00")
    #     return Decimal("16.00") * self.test().section.question_count


class BiologyChemistryNUFYPETItem(NUFYPETItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9562:
            raise ItemError(pgettext("Item error", "Biology/Chemistry NUFYPET Test is required."))

    # def price(self):
    #     if self.test().is_free:
    #         return Decimal("0.00")
    #     return Decimal("16.00") * self.test().section.question_count


class ThinkingSkillsNUFYPETItem(NUFYPETItem):
    def assert_init_args(self, test, student, language):
        super().assert_init_args(test, student, language)
        if test.section_id != 9563:
            raise ItemError(pgettext("Item error", "Thinking skills NUFYPET Test is required."))

    # def price(self):
    #     if self.test().is_free:
    #         return Decimal("0.00")
    #     return Decimal("16.00") * self.test().section.question_count
