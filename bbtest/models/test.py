from django.db.models import (
    Model, ForeignKey, CASCADE,
    CharField, PositiveSmallIntegerField, BooleanField, DateTimeField, TextField,
)
from django.utils.translation import pgettext_lazy
from django.contrib.auth import get_user_model
from .fields import JSONField


class TestDomain(Model):
    name   = CharField                  ( pgettext_lazy("Model field", "name"),  max_length=100,                )
    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                 db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)

    def __str__(self):
        return self.name


class TestSection(Model):
    domain  = ForeignKey  ( TestDomain, on_delete=CASCADE, related_name="sections", )

    name               = CharField                  ( pgettext_lazy("Model field", "name"),                       max_length=100,                )
    is_multi_language  = BooleanField               ( pgettext_lazy("Model field", "is multi language?"),                                        )
    question_count     = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "question count"),                                            )
    question_weight    = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "question weight by default"),                                )
    order              = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                                      db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)

    def __str__(self):
        return self.name


class TestCategory(Model):
    section  = ForeignKey  ( TestSection, on_delete=CASCADE, related_name="categories", )

    name     = CharField                  ( pgettext_lazy("Model field", "name"),  max_length=100,                )
    order    = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                 db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)

    def __str__(self):
        return self.name


class TestTopic(Model):
    section  = ForeignKey  ( TestSection, on_delete=CASCADE, related_name="topics", )

    name     = CharField                  ( pgettext_lazy("Model field", "name"),  max_length=100,                )
    order    = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                 db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)

    def __str__(self):
        return self.name


class Test(Model):
    section    = ForeignKey  ( TestSection,      on_delete=CASCADE, related_name="tests", )
    developer  = ForeignKey  ( get_user_model(), on_delete=CASCADE, related_name="tests", )

    language_code  = CharField      ( pgettext_lazy("Model field", "language code"),    max_length=2,      db_index=True, )
    code           = CharField      ( pgettext_lazy("Model field", "code of the test"), max_length=6,      unique=True,   )
    is_active      = BooleanField   ( pgettext_lazy("Model field", "is active?"),                          db_index=True, )
    is_approved    = BooleanField   ( pgettext_lazy("Model field", "is approved?"),                        db_index=True, )
    created_at     = DateTimeField  ( pgettext_lazy("Model field", "created at"),       auto_now_add=True,                )

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.code


class TestQuestion(Model):
    DIFFICULTY_HIGH    = 2
    DIFFICULTY_NORMAL  = 1
    DIFFICULTY_LOW     = 0
    DIFFICULTY_CHOICES = (
        ( DIFFICULTY_HIGH,   pgettext_lazy("Question difficulty", "High")   ),
        ( DIFFICULTY_NORMAL, pgettext_lazy("Question difficulty", "Normal") ),
        ( DIFFICULTY_LOW,    pgettext_lazy("Question difficulty", "Low")    ),
    )

    test      = ForeignKey  ( Test,         on_delete=CASCADE, related_name="questions", )
    category  = ForeignKey  ( TestCategory, on_delete=CASCADE, related_name="questions", )
    topic     = ForeignKey  ( TestTopic,    on_delete=CASCADE, related_name="questions", )

    answer_class     = CharField                  ( pgettext_lazy("Model field", "answer class"),       max_length=100,                                                                          )
    meta_data        = JSONField                  ( pgettext_lazy("Model field", "meta data"),                                                                                                   )
    paragraph_order  = JSONField                  ( pgettext_lazy("Model field", "paragraph order"),                                                                                             )
    difficulty       = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "difficulty"),                            choices=DIFFICULTY_CHOICES, default=DIFFICULTY_NORMAL, db_index=True, )
    weight           = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "weight of question"),                                                                           db_index=True, )
    order            = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                                                                                        db_index=True, )
    created_at       = DateTimeField              ( pgettext_lazy("Model field", "created at"),         auto_now_add=True,                                                                       )
    updated_at       = DateTimeField              ( pgettext_lazy("Model field", "updated at"),         auto_now=True,                                                                           )

    class Meta:
        default_permissions = ()
        ordering = ("order",)

    def __str__(self):
        if self.id:
            return "TestQuestion #%d" % self.id
        return "New TestQuestion"


class TestParagraph(Model):
    question  = ForeignKey  ( TestQuestion, on_delete=CASCADE, related_name="paragraphs", )

    paragraph_class  = CharField      ( pgettext_lazy("Model field", "paragraph class"), max_length=100,    )
    meta_data        = JSONField      ( pgettext_lazy("Model field", "meta data"),                          )
    created_at       = DateTimeField  ( pgettext_lazy("Model field", "created at"),      auto_now_add=True, )
    updated_at       = DateTimeField  ( pgettext_lazy("Model field", "updated at"),      auto_now=True,     )

    class Meta:
        default_permissions = ()

    def __str__(self):
        if self.id:
            return "TestParagraph #%d" % self.id
        return "New TestParagraph"
