from django.db.models import (
    Manager, Q,
    Model, ForeignKey, CASCADE, ManyToManyField, OneToOneField,
    CharField, PositiveSmallIntegerField, BooleanField, DateTimeField, PositiveIntegerField,
)
from django.utils.translation import pgettext_lazy
from django.contrib.auth import get_user_model
from .fields import JSONField
from bbtest.utils.colors import GOOGLE_COLORS, GOOGLE_COLORS_BLEACHED


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

    class Meta:
        default_permissions = ()
        ordering = ("order",)

    def __str__(self):
        return self.name

    def is_nis(self):
        # return self.pk in range(9540, 9559)
        return self.domain.pk in (7911, 7912, 7913, 7914)
        # return True

    def fg_color(self):
        return GOOGLE_COLORS[(self.pk - 9540) % len(GOOGLE_COLORS)]

    def bg_color(self):
        return GOOGLE_COLORS_BLEACHED[(self.pk - 9540) % len(GOOGLE_COLORS_BLEACHED)]

    def can_measure_topics(self):
        return False
        # return self.pk in (9540, 9544, 9547, 9545) or self.pk in range(9548, 9560) or self.pk in range(9560, 9564) or self.pk == 9565


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


class TestSubTopic(Model):
    sections  = ManyToManyField  ( TestSection, through="TestSubTopicSection", related_name="subtopics", )

    name  = CharField  ( pgettext_lazy("Model field", "name"),  max_length=200, unique=True, )

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.name

class TestSubTopicSection(Model):
    section  = ForeignKey  ( TestSection, on_delete=CASCADE,                         )
    subtopic    = ForeignKey  ( TestSubTopic,   on_delete=CASCADE, related_name="through", )

    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"), db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)
        unique_together = ("section", "subtopic")


class TestEducationGoal(Model):
    sections  = ManyToManyField  ( TestSection, through="TestEducationGoalSection", related_name="goals", )

    name  = CharField  ( pgettext_lazy("Model field", "name"),  max_length=1000, unique=False, )

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.name

class TestEducationGoalSection(Model):
    section  = ForeignKey  ( TestSection, on_delete=CASCADE,                         )
    goal    = ForeignKey  ( TestEducationGoal,   on_delete=CASCADE, related_name="through", )

    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"), db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)
        unique_together = ("section", "goal")


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

class PreProductionTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__lte=Test.STATUS_APPROVED)
    
class ProductionTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__lt=Test.STATUS_ARCHIVED)

class ActiveTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Test.STATUS_ACTIVE)

class ArchivedTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Test.STATUS_ARCHIVED)
    
class RedoTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Test.STATUS_REDO)

class InDevelopmentTestManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__lte=Test.STATUS_REDO)

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
    STATUS_REDO      = 0x01
    STATUS_PENDING   = 0x10
    STATUS_APPROVED  = 0x20
    STATUS_ACTIVE    = 0x30
    
    STATUS_ARCHIVED  = 0xFF

    STATUSES = (
        ( STATUS_DRAFT,    pgettext_lazy("Test status", "Draft")    ),
        ( STATUS_PENDING,  pgettext_lazy("Test status", "Pending")  ),
        ( STATUS_APPROVED, pgettext_lazy("Test status", "Approved") ),
        ( STATUS_ACTIVE,   pgettext_lazy("Test status", "Active")   ),
        ( STATUS_REDO,     pgettext_lazy("Test status", "Redo")     ),
        ( STATUS_ARCHIVED, pgettext_lazy("Test status", "Archived") ),
    )

    section    = ForeignKey  ( TestSection, on_delete=CASCADE, related_name="tests", )
    developer  = ForeignKey  ( User,        on_delete=CASCADE, related_name="tests", )

    code             = CharField                  ( pgettext_lazy("Model field", "code of the test"),     max_length=6,                                               unique=True,   )
    language         = CharField                  ( pgettext_lazy("Model field", "language of the test"), max_length=2,      choices=LANGUAGES,                       db_index=True, )
    status           = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "status"),                                  choices=STATUSES,  default=STATUS_DRAFT, db_index=True, )
    is_free          = BooleanField               ( pgettext_lazy("Model field", "is free?"),                                                   default=True,         db_index=True, )
    sales_count      = PositiveIntegerField       ( pgettext_lazy("Model field", "sales count"),                                                default=0,                           )
    completed_count  = PositiveIntegerField       ( pgettext_lazy("Model field", "completed count"),                                            default=0,                           )
    created_at       = DateTimeField              ( pgettext_lazy("Model field", "created at"),           auto_now_add=True,                                                         )

    objects = Manager()
    draft_tests = DraftTestManager()
    pending_tests = PendingTestManager()
    worked_tests = WorkedTestManager()
    approved_tests = ApprovedTestManager()
    preproduction_tests = PreProductionTestManager()
    production_tests = ProductionTestManager()
    active_tests = ActiveTestManager()
    archived_tests = ArchivedTestManager()
    redo_tests = RedoTestManager()
    in_development_tests = InDevelopmentTestManager()

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
    
    def is_redo(self):
        return self.status == self.STATUS_REDO
    
    def is_active(self):
        return self.status == self.STATUS_ACTIVE

    def max_score(self, question_ids=None):
        score = 0
        for question in self.questions.all():
            if question_ids is not None and question.pk not in question_ids:
                continue
            score += question.weight
        if self.section_id == 9544:
            score = round(score / 2)
        return score

    def topic_branches(self):
        branches = []
        topics = {}
        if not self.section.can_measure_topics():
            return branches
        for question in self.questions.all():
            if question.topic_id is None:
                continue
            index = topics.get(question.topic_id)
            if index is None:
                branches.append({
                    "topic_id": question.topic_id,
                    "question_ids": [],
                })
                index = len(branches) - 1
                topics[question.topic_id] = index
            branches[index]["question_ids"].append(question.pk)
        return branches


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
    DIFFICULTY_NONE    = 0x00
    DIFFICULTIES = (
        ( DIFFICULTY_HIGH,   pgettext_lazy("Question difficulty", "High")   ),
        ( DIFFICULTY_NORMAL, pgettext_lazy("Question difficulty", "Normal") ),
        ( DIFFICULTY_LOW,    pgettext_lazy("Question difficulty", "Low")    ),
        ( DIFFICULTY_NONE,   pgettext_lazy("Question difficulty", "Unspecified")),
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
    subtopic   = ForeignKey  ( TestSubTopic,        on_delete=CASCADE, related_name="questions", null=True, blank=True, )
    goal       = ForeignKey  ( TestEducationGoal,   on_delete=CASCADE, related_name="questions", null=True, blank=True, )
    developer  = ForeignKey  ( User,         on_delete=CASCADE, related_name="questions",                        )

    answer_class  = CharField                  ( pgettext_lazy("Model field", "answer class"),       max_length=100,    choices=ANSWER_CLASSES,                                           )
    meta_data     = JSONField                  ( pgettext_lazy("Model field", "meta data"),                                                                                               )
    difficulty    = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "difficulty"),                            choices=DIFFICULTIES,   default=DIFFICULTY_NONE  , db_index=True, )
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
        # if test_section.is_nis():
        #     return 1
        return 1


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



####### 

class TestPackage(Model):
    name        = CharField   ( pgettext_lazy("Model field", "package name"),  max_length=100, unique=False, )
    code        = CharField   ( pgettext_lazy("Model field", "package code"),  max_length=10, unique=True, db_index=True, )
    assessible  = BooleanField( pgettext_lazy("Model field", "is assessible?"), default=False)

    tests       = ManyToManyField  ( Test, through="TestPackageRelation", related_name="tests", )
    students    = ManyToManyField  ( User,                                related_name="package_students", db_index=True)

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.code


class TestPackageRelation(Model):
    test        = ForeignKey  ( Test,        on_delete=CASCADE,                         )
    package     = ForeignKey  ( TestPackage, on_delete=CASCADE, related_name="through", )

    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"), db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)
        unique_together = ("package", "test")


# class PackageForStudent(Model):
#     student      = OneToOneField ( User,         on_delete=CASCADE, related_name="package_field", )
#     package      = ForeignKey    ( TestPackage,  on_delete=CASCADE,                       )

#     class Meta:
#         default_permissions = ()

#     def __str__(self):
#         return self.package + " " + self.student.get_short_name()



class DomainForStudent(Model):
    student     = OneToOneField ( User,         on_delete=CASCADE, related_name="student_domain", db_index=True)
    domain      = ForeignKey    ( TestDomain,   on_delete=CASCADE, related_name="domains"   )

    class Meta:
        default_permissions = ()

    def __str__(self):
        # self.domain.name
        return "{} | {}".format(self.domain.name, self.student.get_short_name())