from django.db.models import (
    Manager,
    Model, ForeignKey, CASCADE, ManyToManyField,
    CharField, PositiveSmallIntegerField, BooleanField, DateTimeField, PositiveIntegerField,
)
from django.utils.translation import pgettext_lazy
from django.contrib.auth import get_user_model
from .fields import JSONField


User = get_user_model()


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

    name             = CharField                  ( pgettext_lazy("Model field", "name"),                max_length=100,                )
    duration         = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "duration in seconds"),                                )
    question_count   = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "question count"),                                     )
    order            = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                               db_index=True, )
    specification    = JSONField                  ( pgettext_lazy("Model field", "specification"),                                      )

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
        unique_together = ("section", "taxonomy")


class TestTopic(Model):
    sections  = ManyToManyField  ( TestSection, through="TestTopicSection", related_name="topics", )

    name  = CharField  ( pgettext_lazy("Model field", "name"),  max_length=200, unique=True, )

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
        unique_together = ("section", "topic")


class DraftTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Test.STATUS_DRAFT)

class PendingTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Test.STATUS_PENDING)

class WorkedTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__lt=Test.STATUS_APPROVED)

class ApprovedTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Test.STATUS_APPROVED)

class ActiveTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__lt=Test.STATUS_ARCHIVED)

class ArchivedTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Test.STATUS_ARCHIVED)

class Test(Model):
    LANGUAGE_XX  = "xx"
    LANGUAGE_KK  = "kk"
    LANGUAGE_RU  = "ru"
    LANGUAGES = (
        ( LANGUAGE_XX, pgettext_lazy("Test language", "N/A")     ),
        ( LANGUAGE_KK, pgettext_lazy("Test language", "Kazakh")  ),
        ( LANGUAGE_RU, pgettext_lazy("Test language", "Russian") ),
    )

    STATUS_DRAFT     = 0x00
    STATUS_PENDING   = 0x01
    STATUS_APPROVED  = 0x02
    STATUS_ARCHIVED  = 0x03
    STATUSES = (
        ( STATUS_DRAFT,    pgettext_lazy("Test status", "Draft")    ),
        ( STATUS_PENDING,  pgettext_lazy("Test status", "Pending")  ),
        ( STATUS_APPROVED, pgettext_lazy("Test status", "Approved") ),
        ( STATUS_ARCHIVED, pgettext_lazy("Test status", "Archived") ),
    )

    section    = ForeignKey  ( TestSection, on_delete=CASCADE, related_name="tests", )
    developer  = ForeignKey  ( User,        on_delete=CASCADE, related_name="tests", )

    code             = CharField                  ( pgettext_lazy("Model field", "code of the test"),     max_length=6,                                               unique=True,   )
    language         = CharField                  ( pgettext_lazy("Model field", "language of the test"), max_length=2,      choices=LANGUAGES,                       db_index=True, )
    status           = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "status"),                                  choices=STATUSES,  default=STATUS_DRAFT, db_index=True, )
    is_free          = BooleanField               ( pgettext_lazy("Model field", "is free?"),                                                   default=False,        db_index=True, )
    sales_count      = PositiveIntegerField       ( pgettext_lazy("Model field", "sales count"),                                                default=0,                           )
    completed_count  = PositiveIntegerField       ( pgettext_lazy("Model field", "completed count"),                                            default=0,                           )
    created_at       = DateTimeField              ( pgettext_lazy("Model field", "created at"),           auto_now_add=True,                                                         )

    objects = Manager()
    draft_tests = DraftTestManager()
    pending_tests = PendingTestManager()
    worked_tests = WorkedTestManager()
    approved_tests = ApprovedTestManager()
    active_tests = ActiveTestManager()
    archived_tests = ArchivedTestManager()

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.code

    def is_draft(self):
        return self.status == self.STATUS_DRAFT

    def is_pending(self):
        return self.status == self.STATUS_PENDING

    def is_approved(self):
        return self.status == self.STATUS_APPROVED

    def is_archived(self):
        return self.status == self.STATUS_ARCHIVED


class TestQuestion(Model):
    # DIFFICULTY_RESERVED  = 0x0f
    # DIFFICULTY_RESERVED  = 0x0e
    # DIFFICULTY_HIGH      = 0x0d
    # DIFFICULTY_RESERVED  = 0x0c
    # DIFFICULTY_RESERVED  = 0x0b
    # DIFFICULTY_RESERVED  = 0x0a
    # DIFFICULTY_RESERVED  = 0x09
    # DIFFICULTY_NORMAL    = 0x08
    # DIFFICULTY_RESERVED  = 0x07
    # DIFFICULTY_RESERVED  = 0x06
    # DIFFICULTY_RESERVED  = 0x05
    # DIFFICULTY_RESERVED  = 0x04
    # DIFFICULTY_LOW       = 0x03
    # DIFFICULTY_RESERVED  = 0x02
    # DIFFICULTY_RESERVED  = 0x01
    # DIFFICULTY_NONE      = 0x00

    DIFFICULTY_HIGH    = 0x0d
    DIFFICULTY_NORMAL  = 0x08
    DIFFICULTY_LOW     = 0x03
    DIFFICULTIES = (
        ( DIFFICULTY_HIGH,   pgettext_lazy("Question difficulty", "High")   ),
        ( DIFFICULTY_NORMAL, pgettext_lazy("Question difficulty", "Normal") ),
        ( DIFFICULTY_LOW,    pgettext_lazy("Question difficulty", "Low")    ),
    )

    ANSWER_CLASS_MULTICHOICE_ONE    = "MultichoiceOneAnswer"
    ANSWER_CLASS_MULTICHOICE_MULTI  = "MultichoiceMultiAnswer"
    ANSWER_CLASS_FREEFORM           = "FreeformAnswer"
    ANSWER_CLASSES = (
        ( ANSWER_CLASS_MULTICHOICE_ONE,   ANSWER_CLASS_MULTICHOICE_ONE ),
        ( ANSWER_CLASS_MULTICHOICE_MULTI, ANSWER_CLASS_MULTICHOICE_MULTI ),
    )

    test       = ForeignKey  ( Test,         on_delete=CASCADE, related_name="questions",                        )
    taxonomy   = ForeignKey  ( TestTaxonomy, on_delete=CASCADE, related_name="questions", null=True, blank=True, )
    topic      = ForeignKey  ( TestTopic,    on_delete=CASCADE, related_name="questions", null=True, blank=True, )
    developer  = ForeignKey  ( User,         on_delete=CASCADE, related_name="questions",                        )

    answer_class  = CharField                  ( pgettext_lazy("Model field", "answer class"),       max_length=100,    choices=ANSWER_CLASSES,                                           )
    meta_data     = JSONField                  ( pgettext_lazy("Model field", "meta data"),                                                                                               )
    difficulty    = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "difficulty"),                            choices=DIFFICULTIES,   default=DIFFICULTY_NORMAL, db_index=True, )
    weight        = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "weight of question"),                                                                       db_index=True, )
    order         = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                                                                                    db_index=True, )
    created_at    = DateTimeField              ( pgettext_lazy("Model field", "created at"),         auto_now_add=True,                                                                   )
    updated_at    = DateTimeField              ( pgettext_lazy("Model field", "updated at"),         auto_now=True,                                                                       )

    class Meta:
        default_permissions = ()
        ordering = ("order",)

    def __str__(self):
        if self.id:
            return "TestQuestion #%d" % self.id
        return "New TestQuestion"

    @classmethod
    def calculate_weight(cls, test_question, test_section):
        if test_section.pk in (9540, 9541, 9542, 9543, 9544):
            return 10
        elif test_section.pk in (9545, 9546, 9547):
            return 1
        elif test_section.pk in (9548, 9549, 9550, 9551, 9552, 9553, 9554, 9555, 9556, 9557, 9558, 9559):
            if test_question.answer_class == cls.ANSWER_CLASS_MULTICHOICE_ONE:
                return 1
            elif test_question.answer_class == cls.ANSWER_CLASS_MULTICHOICE_MULTI:
                return 2
        return None


class TestParagraph(Model):
    PARAGRAPH_CLASS_TEXT        = "TextParagraph"
    PARAGRAPH_CLASS_SPLIT_TEXT  = "SplitTextParagraph"
    PARAGRAPH_CLASS_IMAGE       = "ImageParagraph"
    PARAGRAPH_CLASS_AUDIO       = "AudioParagraph"
    PARAGRAPH_CLASSES = (
        ( PARAGRAPH_CLASS_TEXT,       PARAGRAPH_CLASS_TEXT       ),
        ( PARAGRAPH_CLASS_SPLIT_TEXT, PARAGRAPH_CLASS_SPLIT_TEXT ),
        ( PARAGRAPH_CLASS_IMAGE,      PARAGRAPH_CLASS_IMAGE      ),
    )

    questions  = ManyToManyField  ( TestQuestion, through="TestParagraphQuestion", related_name="paragraphs", )

    paragraph_class  = CharField      ( pgettext_lazy("Model field", "paragraph class"), max_length=100,    choices=PARAGRAPH_CLASSES, )
    meta_data        = JSONField      ( pgettext_lazy("Model field", "meta data"),                                                     )
    created_at       = DateTimeField  ( pgettext_lazy("Model field", "created at"),      auto_now_add=True,                            )
    updated_at       = DateTimeField  ( pgettext_lazy("Model field", "updated at"),      auto_now=True,                                )

    class Meta:
        default_permissions = ()

    def __str__(self):
        if self.id:
            return "TestParagraph #%d" % self.id
        return "New TestParagraph"


class TestParagraphQuestion(Model):
    question   = ForeignKey  ( TestQuestion,  on_delete=CASCADE,                         )
    paragraph  = ForeignKey  ( TestParagraph, on_delete=CASCADE, related_name="through", )

    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"), db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)
        unique_together = ("question", "paragraph")
