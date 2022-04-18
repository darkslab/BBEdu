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
from .shopping.base import Cart, LineItem


class QuizSet(VersionedMixin, Model):
    test_domain  = ForeignKey  ( TestDomain,       on_delete=CASCADE, related_name="quiz_sets", )
    student      = ForeignKey  ( get_user_model(), on_delete=CASCADE, related_name="quiz_sets", )
    cart         = ForeignKey  ( Cart,             on_delete=CASCADE, related_name="quiz_sets", )

    lock_version  = VersionField      ( pgettext_lazy("Model field", "lock version"),                                                 default=0, )
    is_current    = NullBooleanField  ( pgettext_lazy("Model field", "is current?"),                     default=True, db_index=True,            )
    created_at    = DateTimeField     ( pgettext_lazy("Model field", "created at"),   auto_now_add=True,                                         )
    updated_at    = DateTimeField     ( pgettext_lazy("Model field", "updated at"),   auto_now=True,                                             )

    class Meta:
        db_table = "quiz_sets"
        default_permissions = ()
        unique_together = ("student", "is_current")


class Quiz(Model):
    quiz_set   = ForeignKey  ( QuizSet,  on_delete=CASCADE, related_name="quizzes", )
    test       = ForeignKey  ( Test,     on_delete=CASCADE, related_name="quizzes", )
    line_item  = ForeignKey  ( LineItem, on_delete=CASCADE, related_name="quizzes", )

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

    def score(self, question_ids=None, correct_question_ids_bucket=None):
        bucket = []
        if correct_question_ids_bucket is not None:
            bucket = correct_question_ids_bucket
        score = 0
        if self.report is None:
            return score

        if self.test.section.is_nis():
            if self.test.section.pk == 9544:
                score = self.__calculate_nis_quantitative(question_ids, bucket)
            else:
                score = self.__calculate_straightforward(question_ids, bucket)
        elif self.test.section.is_unt_compulsory():
            score = self.__calculate_straightforward(question_ids, bucket)
        elif self.test.section.is_unt_profile():
            score = self.__calculate_unt_profile(question_ids, bucket)
        elif self.test.section.is_nufypet():
            score = self.__calculate_straightforward(question_ids, bucket)
        elif self.test.section.is_law():
            score = self.__calculate_straightforward(question_ids, bucket)

        return score

    def __calculate_simple_multichoice_one_answer(self, answer, test_question):
        score = 0
        if test_question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
            if (
                test_question.meta_data["correct_id"] is not None
                and answer["answer"] is not None
                and test_question.meta_data["correct_id"] == answer["answer"]["correct_id"]
            ):
                score += test_question.weight
        return score

    def __calculate_straightforward(self, question_ids, bucket):
        score = 0
        for i, question in enumerate(self.test.questions.all()):
            if question_ids is not None and question.pk not in question_ids:
                continue
            before_score = score
            score += self.__calculate_simple_multichoice_one_answer(self.report["answers"][i], question)
            if before_score != score:
                bucket.append(question.pk)
        return score

    def __calculate_nis_quantitative(self, question_ids, bucket):
        score = 0
        for i, question in enumerate(self.test.questions.all()):
            if question_ids is not None and question.pk not in question_ids:
                continue
            before_score = score
            score += self.__calculate_simple_multichoice_one_answer(self.report["answers"][i], question)
            if before_score != score:
                bucket.append(question.pk)
        return round(score / 2)

    def __calculate_unt_profile(self, question_ids, bucket):
        score = 0
        for i, question in enumerate(self.test.questions.all()):
            if question_ids is not None and question.pk not in question_ids:
                continue
            before_score = score
            if question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                score += self.__calculate_simple_multichoice_one_answer(self.report["answers"][i], question)
            elif question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI:
                answer = self.report["answers"][i]
                if (
                    len(question.meta_data["correct_ids"]) > 0
                    and len(question.meta_data["correct_ids"]) <= 3
                    and answer["answer"] is not None
                ):
                    correct_answers = set(question.meta_data["correct_ids"])
                    report_answers = set(answer["answer"]["correct_ids"])
                    if not len(correct_answers ^ report_answers):
                        score += question.weight
                    elif len(correct_answers & report_answers) >= ceil(len(correct_answers) / 2):
                        if len(report_answers - correct_answers) <= 1:
                            score += round(question.weight / 2)
            if before_score != score:
                bucket.append(question.pk)
        return score

    def get_student_answers(self):
        def dif_None(a, b):
            try:
                return a - b + 1
            except TypeError:
                return None
        answer_a_offsets = self.get_a_offset()
        user_answers = self.get_answers_ids()
        normalized_answers = [dif_None(ans, a_offset) for ans, a_offset in zip(user_answers, answer_a_offsets)]
        return normalized_answers

    def get_correct_answers(self):
        questions = self.test.questions.all()
        ret = []
        for q in questions:
            a_offset = min([option["id"] for option in q.meta_data['choices']])
            correct_id = q.meta_data["correct_id"]
            if correct_id is not None:
                ret.append(correct_id-a_offset)
            else:
                ret.append(None)
        return ret

    def get_a_offset(self):
        questions = self.test.questions.all()
        a_id = []
        for q in questions:
            a_id.append(min([option["id"] for option in q.meta_data['choices']]))
        return a_id
        
    def get_answers_ids(self):
        if self.report is not None:
            ret = []
            for ans_meta in self.report["answers"]:
                try:
                    ret.append(ans_meta["answer"]["correct_id"] + 1)
                except TypeError:
                    ret.append(None)
            return ret
        else:
            return [None for _ in range(self.test.section.question_count)]