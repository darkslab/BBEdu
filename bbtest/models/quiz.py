from django.db.models import (
    Model, ForeignKey, CASCADE,
    NullBooleanField, DateTimeField, PositiveSmallIntegerField, BooleanField,
)
from django.contrib.auth import get_user_model
from django.utils.translation import pgettext_lazy
from .test import TestDomain, Test
from .fields import JSONField


class QuizSet(Model):
    test_domain  = ForeignKey  ( TestDomain,       on_delete=CASCADE, related_name="quiz_sets", )
    student      = ForeignKey  ( get_user_model(), on_delete=CASCADE, related_name="quiz_sets", )

    is_current  = NullBooleanField  ( pgettext_lazy("Model field", "is current?"),                    default=True, db_index=True, )
    created_at  = DateTimeField     ( pgettext_lazy("Model field", "created at"),  auto_now_add=True,                              )
    updated_at  = DateTimeField     ( pgettext_lazy("Model field", "updated at"),  auto_now=True,                                  )

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
