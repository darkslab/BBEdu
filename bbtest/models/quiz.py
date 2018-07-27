from django.db.models import (
    Model, ForeignKey, CASCADE,
    NullBooleanField, DateTimeField, PositiveSmallIntegerField, BooleanField,
)
from django.contrib.auth import get_user_model
from django.utils.translation import pgettext_lazy
from ool import VersionField, VersionedMixin
from math import ceil
from .test import TestDomain, Test, TestQuestion
from .fields import JSONField


class QuizSet(VersionedMixin, Model):
    test_domain  = ForeignKey  ( TestDomain,       on_delete=CASCADE, related_name="quiz_sets", )
    student      = ForeignKey  ( get_user_model(), on_delete=CASCADE, related_name="quiz_sets", )

    lock_version  = VersionField      ( pgettext_lazy("Model field", "lock version"),                                                 default=0, )
    is_current    = NullBooleanField  ( pgettext_lazy("Model field", "is current?"),                     default=True, db_index=True,            )
    created_at    = DateTimeField     ( pgettext_lazy("Model field", "created at"),   auto_now_add=True,                                         )
    updated_at    = DateTimeField     ( pgettext_lazy("Model field", "updated at"),   auto_now=True,                                             )

    class Meta:
        db_table = "quiz_sets"
        default_permissions = ()
        unique_together = ("student", "is_current")


class Quiz(Model):
    quiz_set  = ForeignKey  ( QuizSet, on_delete=CASCADE, related_name="quizzes", )
    test      = ForeignKey  ( Test,    on_delete=CASCADE, related_name="quizzes", )

    report       = JSONField                  ( pgettext_lazy("Model field", "report"),                             null=True, blank=True,                               )
    order        = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                                                                    db_index=True, )
    is_finished  = BooleanField               ( pgettext_lazy("Model field", "is finished?"),                                              default=False, db_index=True, )
    started_at   = DateTimeField              ( pgettext_lazy("Model field", "quiz started at"),                    null=True, blank=True,                db_index=True, )
    due_at       = DateTimeField              ( pgettext_lazy("Model field", "quiz due at"),                        null=True, blank=True,                db_index=True, )
    ended_at     = DateTimeField              ( pgettext_lazy("Model field", "quiz ended at"),                      null=True, blank=True,                db_index=True, )
    created_at   = DateTimeField              ( pgettext_lazy("Model field", "created at"),      auto_now_add=True,                                                      )
    updated_at   = DateTimeField              ( pgettext_lazy("Model field", "updated at"),      auto_now=True,                                                          )

    class Meta:
        db_table = "quizzes"
        default_permissions = ()
        ordering = ("order",)

    def score(self, question_ids=None):
        score = 0
        if self.report is None:
            return score

        calculate_method = None
        if self.test.section.pk in (9540, 9541, 9542, 9543, 9544):
            calculate_method = self.__calculate_nis
        elif self.test.section.pk in (9545, 9546, 9547):
            calculate_method = self.__calculate_unt_compulsory
        elif self.test.section.pk in (9548, 9549, 9550, 9551, 9552, 9553, 9554, 9555, 9556, 9557, 9558, 9559):
            calculate_method = self.__calculate_unt_profile
        if calculate_method is None:
            return score

        for i, question in enumerate(self.test.questions.all()):
            if question_ids is not None and question.pk not in question_ids:
                continue
            score += calculate_method(self.report["answers"][i], question)
        return score

    def __calculate_nis(self, answer, test_question):
        score = 0
        if test_question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
            if (
                test_question.meta_data["correct_id"] is not None
                and answer["answer"] is not None
                and test_question.meta_data["correct_id"] == answer["answer"]["correct_id"]
            ):
                score += test_question.weight
        return score

    def __calculate_unt_compulsory(self, answer, test_question):
        score = 0
        if test_question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
            if (
                test_question.meta_data["correct_id"] is not None
                and answer["answer"] is not None
                and test_question.meta_data["correct_id"] == answer["answer"]["correct_id"]
            ):
                score += test_question.weight
        return score

    def __calculate_unt_profile(self, answer, test_question):
        score = 0
        if test_question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
            if (
                test_question.meta_data["correct_id"] is not None
                and answer["answer"] is not None
                and test_question.meta_data["correct_id"] == answer["answer"]["correct_id"]
            ):
                score += test_question.weight
        elif test_question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI:
            if (
                len(test_question.meta_data["correct_ids"]) > 0
                and len(test_question.meta_data["correct_ids"]) <= 3
                and answer["answer"] is not None
            ):
                correct_answers = set(test_question.meta_data["correct_ids"])
                report_answers = set(answer["answer"]["correct_ids"])
                if not len(correct_answers ^ report_answers):
                    score += test_question.weight
                elif len(correct_answers & report_answers) >= ceil(len(correct_answers) / 2):
                    if len(report_answers - correct_answers) <= 1:
                        score += test_question.weight / 2
        return score
