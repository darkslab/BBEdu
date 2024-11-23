from collections import defaultdict
from typing import List, Tuple
from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    BooleanField,
    DateTimeField,
    ForeignKey,
    Model,
    PositiveSmallIntegerField,
    QuerySet,
)
from django.utils.translation import pgettext_lazy
from ool import VersionedMixin, VersionField

from .fields import JSONField
from .shopping.base import Cart, LineItem
from .test import Test, TestDomain, TestQuestion, TestSubTopic, TestTopic


class QuizSet(VersionedMixin, Model):
    test_domain  = ForeignKey  ( TestDomain,       on_delete=CASCADE, related_name="quiz_sets", )
    student      = ForeignKey  ( get_user_model(), on_delete=CASCADE, related_name="quiz_sets", )
    cart         = ForeignKey  ( Cart,             on_delete=CASCADE, related_name="quiz_sets",  blank=True, null=True,)

    lock_version  = VersionField      ( pgettext_lazy("Model field", "lock version"),                                                 default=0, )
    is_current    = BooleanField      ( pgettext_lazy("Model field", "is current?"),      default=True, db_index=True, null=True,                )
    created_at    = DateTimeField     ( pgettext_lazy("Model field", "created at"),   auto_now_add=True,                                         )
    updated_at    = DateTimeField     ( pgettext_lazy("Model field", "updated at"),   auto_now=True,                                             )

    class Meta:
        db_table = "quiz_sets"
        default_permissions = ()
        unique_together = ("student", "is_current")


class Quiz(Model):
    quiz_set   = ForeignKey  ( QuizSet,  on_delete=CASCADE, related_name="quizzes", )
    test       = ForeignKey  ( Test,     on_delete=CASCADE, related_name="quizzes", )
    line_item  = ForeignKey  ( LineItem, on_delete=CASCADE, related_name="quizzes",  blank=True, null=True, )

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
                score += 1 # test_question.weight
        return score

    def __calculate_straightforward(self, question_ids, bucket):
        score = 0
        for i, question in enumerate(self.test.questions.order_by("testtoquestionrelation").all()):
            if question_ids is not None and question.pk not in question_ids:
                continue
            before_score = score
            score += self.__calculate_simple_multichoice_one_answer(self.report["answers"][i], question)
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
        questions = self.test.questions.order_by("testtoquestionrelation").all()
        ret = []
        for q in questions:
            choices = q.meta_data['choices'] # .sort(lambda x: x["id"])
            a_offset = 0
            if choices:
                a_offset = min([option["id"] for option in choices])
            correct_id = q.meta_data.get("correct_id", None)
            if correct_id is not None:
                ret.append(correct_id - a_offset + 1)
            else:
                ret.append(None)
        return ret

    def get_a_offset(self):
        questions = self.test.questions.order_by("testtoquestionrelation").all()
        a_id = []
        for q in questions:
            choices = q.meta_data['choices'] #.sort(lambda x: x["id"])
            if choices:
                a_id.append(min([option["id"] for option in choices]))
            else:
                a_id.append(0)
        return a_id
        
    def get_answers_ids(self):
        if self.report is not None:
            # print("get_answers_ids", self.report)
            ret = []
            for ans_meta in self.report["answers"]:
                try:
                    ans = ans_meta.get("answer", {})
                    if "correct_id" in ans:
                        ret.append(ans["correct_id"])
                    elif "correct_ids" in ans:
                        ret.append(ans["correct_ids"])
                    else:
                        ret.append(None)
                
                except TypeError:
                    ret.append(None)
                    
            return ret
        else:
            return [None for _ in range(self.test.question_count)]
    
    def get_answers_letters(self):
        alphabet = "ABCDEFGH"
        ret = []

        user_answer_id_list = self.get_answers_ids()
        questions = self.test.questions.order_by("testtoquestionrelation").all()

        for user_answer, question in zip(user_answer_id_list, questions):
            choices = question.meta_data.get('choices', [])
            if question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                for i, ch in enumerate(choices):
                    if user_answer == ch["id"]:
                        ret.append(alphabet[i])
                        break
                else:
                    ret.append("9")
            elif question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI:
                temp = []
                for i, ch in enumerate(choices):
                    if user_answer and ch["id"] in user_answer:
                        temp.append(alphabet[i])
                ret.append(temp)
            else:
                ret.append(None)

        return ret


    def calc_score(self) -> int:
        student_answers = self.get_student_answers()
        correct_answers = self.get_correct_answers()
        # print(student_answers)
        # print(correct_answers)

        assert len(student_answers) == len(correct_answers)
        score = 0
        for std, corr in zip(student_answers, correct_answers):
            if std is None:
                continue
            score += int(std == corr)
        return score

    def get_question_topic_subtopic(self) -> Tuple[List[TestTopic], List[TestSubTopic], List[int]]:
        questions: QuerySet[TestQuestion] = (
            self.test.questions.prefetch_related("topic", "subtopic")
            .order_by("testtoquestionrelation")
            .all()
        )

        return (
            [q.topic for q in questions],
            [q.subtopic for q in questions],
            [q.difficulty for q in questions],
        )

    def calc_score_by_topic_subtopic(self) -> tuple[int, defaultdict, defaultdict, defaultdict]:
        student_answers = self.get_student_answers()
        correct_answers = self.get_correct_answers()

        topic_list, subtopic_list, difficulty = self.get_question_topic_subtopic()
        # print(difficulty)

        assert len(student_answers) == len(correct_answers)
        assert len(topic_list) == len(correct_answers)

        score = 0
        score_topic = defaultdict(int)
        score_subtopic = defaultdict(int)
        score_difficulty = defaultdict(int)

        for std, corr, topic, subtopic, question_difficulty in zip(
            student_answers, correct_answers, topic_list, subtopic_list, difficulty
        ):
            if std is None:
                continue
            is_correct = int(std == corr)
            score_topic[topic] += is_correct
            score_subtopic[subtopic] += is_correct
            score_difficulty[question_difficulty] += is_correct
            score += is_correct

        return score, score_topic, score_subtopic, score_difficulty