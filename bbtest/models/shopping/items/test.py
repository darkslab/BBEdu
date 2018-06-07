from django.utils.translation import pgettext
from django.contrib.auth import get_user_model
from decimal import Decimal, ROUND_HALF_UP
from .base import Item
from ..exceptions import ItemError
from bbtest.models import Test, DeveloperAcknowledgement, Account
from bbtest.models.accounting import Debit, Credit


User = get_user_model()


class TestItem(Item):
    def __init__(self, handle, test, student, language):
        super().__init__(handle)

        self.assert_init_args(test, student, language)
        self.__test = test
        self.__student = student
        self.__language = language

        self.__plan_c_developers = {}
        for question in self.test().questions.prefetch_related("developer__acknowledgement").all():
            if not hasattr(question.developer, "acknowledgement") or question.developer.acknowledgement.plan != DeveloperAcknowledgement.PLAN_C:
                continue
            if question.developer not in self.__plan_c_developers:
                self.__plan_c_developers[question.developer] = {
                    "account": Account.objects.get(name=("Developer-%s" % question.developer.pk)),
                    "questions": 0,
                }
            self.__plan_c_developers[question.developer]["questions"] += 1

        self.__balance_account = self.student().balance_account()
        self.__revenue_account = self.revenue_account()

        self.handle().add_item(self)

    def assert_init_args(self, test, student, language):
        if not isinstance(test, Test):
            raise ItemError(pgettext("Item error", "Test is required."))
        if not isinstance(student, User) or not student.has_perm("bbtest.student"):
            raise ItemError(pgettext("Item error", "Student is required."))
        if not test.is_approved():
            raise ItemError(pgettext("Item error", "Test has to be approved."))
        if language not in [ test_lang[0] for test_lang in Test.LANGUAGES if test_lang[0] != Test.LANGUAGE_XX ]:
            raise ItemError(pgettext("Item error", "Correct test language is required."))
        if test.language != Test.LANGUAGE_XX and test.language != language:
            raise ItemError(pgettext("Item error", "Incorrect Test language."))

    def test(self):
        return self.__test

    def student(self):
        return self.__student

    def language(self):
        return self.__language

    def revenue_account(self):
        raise NotImplementedError("%s has to implement 'revenue_account' method" % type(self).__name__)

    @classmethod
    def instantiate_from_meta_data(cls, handle, meta_data):
        try:
            cls(
                handle,
                Test.objects.select_related("section__domain").get(pk=meta_data["test_id"]),
                User.objects.get(pk=meta_data["student_id"]),
            )
        except Test.DoesNotExist:
            raise ItemError(pgettext("Item error", "Test no longer exists."))
        except User.DoesNotExist:
            raise ItemError(pgettext("Item error", "User no longer exists."))

    def separate_from_items(self, items):
        items.pop(items.index(self))
        return items

    def meta_data(self):
        return {
            "test_id": self.test().pk,
            "student_id": self.student().pk,
        }

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.test() == other.test() and self.student() == other.student()

    def __hash__(self):
        return hash((self.test().pk, self.student().pk))

    def funds(self):
        _funds = [
            Debit(account=self.__balance_account, amount=self.total()),
        ]
        question_amount = (self.total() / self.test().section.question_count).quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)
        liabilities_amount = Decimal("0.00")

        for developer, developer_data in self.__plan_c_developers.items():
            developer_amount = (question_amount * Decimal("0.5")).quantize(Decimal("1.00"), rounding=ROUND_HALF_UP) * developer_data["questions"]
            _funds.append(Credit(account=developer_data["account"], amount=developer_amount))
            liabilities_amount += developer_amount

        _funds.append(Credit(account=self.__revenue_account, amount=(self.total() - liabilities_amount)))

        return _funds
