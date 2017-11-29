from django.db.models import (
    Model, ForeignKey, CASCADE, ManyToManyField,
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
    duration           = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "duration in seconds"),                                       )
    question_count     = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "question count"),                                            )
    question_weight    = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "question weight by default"),                                )
    order              = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                                      db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)

    def __str__(self):
        return self.name


class TestTaxonomy(Model):
    sections  = ManyToManyField  ( TestSection, through="TestTaxonomySection", related_name="taxonomies", )

    name  = CharField  ( pgettext_lazy("Model field", "name"), max_length=100, unique=True, )

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.name


class TestTaxonomySection(Model):
    section   = ForeignKey  ( TestSection,  on_delete=CASCADE,                         )
    taxonomy  = ForeignKey  ( TestTaxonomy, on_delete=CASCADE, related_name="through", )

    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"), db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)


class TestTopic(Model):
    sections  = ManyToManyField  ( TestSection, through="TestTopicSection", related_name="topics", )

    name  = CharField  ( pgettext_lazy("Model field", "name"),  max_length=100, unique=True, )

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.name


class TestTopicSection(Model):
    section  = ForeignKey  ( TestSection, on_delete=CASCADE,                         )
    topic    = ForeignKey  ( TestTopic,   on_delete=CASCADE, related_name="through", )

    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"), db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)


class Test(Model):
    LANGUAGE_KK = "kk"
    LANGUAGE_RU = "ru"
    LANGUAGES = (
        ( LANGUAGE_KK, pgettext_lazy("Test language", "Kazakh")  ),
        ( LANGUAGE_RU, pgettext_lazy("Test language", "Russian") ),
    )

    section    = ForeignKey  ( TestSection,      on_delete=CASCADE, related_name="tests", )
    developer  = ForeignKey  ( get_user_model(), on_delete=CASCADE, related_name="tests", )

    code         = CharField      ( pgettext_lazy("Model field", "code of the test"),     max_length=6,                                        unique=True,   )
    language     = CharField      ( pgettext_lazy("Model field", "language of the test"), max_length=2,      choices=LANGUAGES,                db_index=True, )
    is_active    = BooleanField   ( pgettext_lazy("Model field", "is active?"),                                                 default=True,  db_index=True, )
    is_approved  = BooleanField   ( pgettext_lazy("Model field", "is approved?"),                                               default=False, db_index=True, )
    created_at   = DateTimeField  ( pgettext_lazy("Model field", "created at"),           auto_now_add=True,                                                  )

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.code


class TestQuestion(Model):
    DIFFICULTY_HIGH    = 2
    DIFFICULTY_NORMAL  = 1
    DIFFICULTY_LOW     = 0
    DIFFICULTIES = (
        ( DIFFICULTY_HIGH,   pgettext_lazy("Question difficulty", "High")   ),
        ( DIFFICULTY_NORMAL, pgettext_lazy("Question difficulty", "Normal") ),
        ( DIFFICULTY_LOW,    pgettext_lazy("Question difficulty", "Low")    ),
    )

    test      = ForeignKey  ( Test,         on_delete=CASCADE, related_name="questions",                        )
    taxonomy  = ForeignKey  ( TestTaxonomy, on_delete=CASCADE, related_name="questions", null=True, blank=True, )
    topic     = ForeignKey  ( TestTopic,    on_delete=CASCADE, related_name="questions", null=True, blank=True, )

    answer_class     = CharField                  ( pgettext_lazy("Model field", "answer class"),       max_length=100,                                                                    )
    meta_data        = JSONField                  ( pgettext_lazy("Model field", "meta data"),                                                                                             )
    paragraph_order  = JSONField                  ( pgettext_lazy("Model field", "paragraph order"),                                                                                       )
    difficulty       = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "difficulty"),                            choices=DIFFICULTIES, default=DIFFICULTY_NORMAL, db_index=True, )
    weight           = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "weight of question"),                                                                     db_index=True, )
    order            = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                                                                                  db_index=True, )
    created_at       = DateTimeField              ( pgettext_lazy("Model field", "created at"),         auto_now_add=True,                                                                 )
    updated_at       = DateTimeField              ( pgettext_lazy("Model field", "updated at"),         auto_now=True,                                                                     )

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
