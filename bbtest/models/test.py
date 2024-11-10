from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    Manager,
    ManyToManyField,
    Model,
    OneToOneField,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    Q,
)
from django.utils.translation import pgettext_lazy

from bbtest.utils.colors import GOOGLE_COLORS, GOOGLE_COLORS_BLEACHED

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
    code             = CharField                  ( pgettext_lazy("Model field", "code"),                max_length=6,                  )
    duration         = PositiveIntegerField       ( pgettext_lazy("Model field", "duration in seconds"),                                )
    question_count   = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "question count"),                                     )
    order            = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),                               db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)

    def __str__(self):
        return self.name

    def is_nis(self):
        domain_id_list = (7911, 7912, 7913, 7914, 7915, 7916, 7919, 7920)
        return self.domain.pk in domain_id_list 
        # return True

    def fg_color(self):
        return GOOGLE_COLORS[(self.pk - 9540) % len(GOOGLE_COLORS)]

    def bg_color(self):
        return GOOGLE_COLORS_BLEACHED[(self.pk - 9540) % len(GOOGLE_COLORS_BLEACHED)]

    def can_measure_topics(self):
        return False
        # return self.pk in (9540, 9544, 9547, 9545) or self.pk in range(9548, 9560) or self.pk in range(9560, 9564) or self.pk == 9565
    
    def get_lang(self):
        if "ru" in self.name:
            return Test.LANGUAGE_RU
        if "kz" in self.name:
            return Test.LANGUAGE_KK
        return Test.LANGUAGE_XX


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

class TestTopicToSubtopicRelation(Model):
    topic  = ForeignKey  ( TestTopic, on_delete=CASCADE,                         )
    subtopic    = ForeignKey  ( TestSubTopic,   on_delete=CASCADE,  )
    
    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"), db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)
        unique_together = ("topic", "subtopic")


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

    STATUSES_DICT = {s[0]: s[1] for s in STATUSES}

    section    = ForeignKey  ( TestSection, on_delete=CASCADE, related_name="tests", )
    developer  = ForeignKey  ( User,        on_delete=CASCADE, related_name="tests", )

    code             = CharField                  ( pgettext_lazy("Model field", "code of the test"),     max_length=6,                                               unique=True,   )
    language         = CharField                  ( pgettext_lazy("Model field", "language of the test"), max_length=2,      choices=LANGUAGES,                       db_index=True, )
    question_count   = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "question count"),                                     )
    duration         = PositiveIntegerField       ( pgettext_lazy("Model field", "duration in seconds"),                                )

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

    @property
    def actual_question_count(self):
        return self.questions.count()

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



class DraftQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TestQuestion.STATUS_DRAFT)

class PendingQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TestQuestion.STATUS_PENDING)

class WorkedQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__lt=TestQuestion.STATUS_APPROVED)

class ApprovedQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TestQuestion.STATUS_APPROVED)

class FinishedQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(status=TestQuestion.STATUS_APPROVED) | Q(status=TestQuestion.STATUS_ACTIVE))

class PreProductionQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__lte=TestQuestion.STATUS_APPROVED)
    
class ProductionQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__lt=TestQuestion.STATUS_ARCHIVED)

class ActiveQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TestQuestion.STATUS_ACTIVE)

class ArchivedQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TestQuestion.STATUS_ARCHIVED)
    
class RedoQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TestQuestion.STATUS_REDO)

class InDevelopmentQuestionManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__lte=TestQuestion.STATUS_REDO)


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

    # test       = ForeignKey  ( Test,         on_delete=CASCADE, related_name="questions",                        )  # TODO: remove
    test  = ManyToManyField  ( Test,                       related_name="questions", through="TestToQuestionRelation",)
    section    = ForeignKey  ( TestSection,  on_delete=CASCADE, related_name="questions",                        )
    taxonomy   = ForeignKey  ( TestTaxonomy, on_delete=CASCADE, related_name="questions", null=True, blank=True, )
    topic      = ForeignKey  ( TestTopic,    on_delete=CASCADE, related_name="questions", null=True, blank=True, )
    subtopic   = ForeignKey  ( TestSubTopic,        on_delete=CASCADE, related_name="questions", null=True, blank=True, )
    goal       = ForeignKey  ( TestEducationGoal,   on_delete=CASCADE, related_name="questions", null=True, blank=True, )
    developer  = ForeignKey  ( User,         on_delete=CASCADE, related_name="questions",                        )

    status         = PositiveSmallIntegerField ( pgettext_lazy("Model field", "status"),                                choices=STATUSES,       default=STATUS_DRAFT,      db_index=True, )
    code           = CharField                 ( pgettext_lazy("Model field", "code of the question"),     max_length=15,                       unique=True,               db_index=True, )
    answer_class  = CharField                  ( pgettext_lazy("Model field", "answer class"),       max_length=100,    choices=ANSWER_CLASSES,                                           )
    meta_data     = JSONField                  ( pgettext_lazy("Model field", "meta data"),                                                                                               )
    difficulty    = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "difficulty"),                            choices=DIFFICULTIES,   default=DIFFICULTY_NONE  , db_index=True, )
    weight        = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "weight of question"),                                                                       db_index=True, )
    # order         = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"),    db_index=True, ) # TODO: remove
    created_at    = DateTimeField              ( pgettext_lazy("Model field", "created at"),         auto_now_add=True,                                                                   )
    updated_at    = DateTimeField              ( pgettext_lazy("Model field", "updated at"),         auto_now=True,                                                                       )
    last_comment_at    = DateTimeField         ( pgettext_lazy("Model field", "last_comment at"),    default=None,     null=True, blank=True                                              )
    has_periodic_table   = BooleanField        ( pgettext_lazy("Model field", "has periodic table"), default=False)
    has_calculator       = BooleanField        ( pgettext_lazy("Model field", "has calculator"),     default=False)

    objects = Manager()
    draft_questions = DraftQuestionManager()
    pending_questions = PendingQuestionManager()
    worked_questions = WorkedQuestionManager()
    approved_questions = ApprovedQuestionManager()
    preproduction_questions = PreProductionQuestionManager()
    production_questions = ProductionQuestionManager()
    finished_questions = FinishedQuestionManager()
    active_questions = ActiveQuestionManager()
    archived_questions = ArchivedQuestionManager()
    redo_questions = RedoQuestionManager()
    in_development_questions = InDevelopmentQuestionManager()


    class Meta:
        default_permissions = ()
        # ordering = ("order",)

    def __str__(self):
        if self.id:
            return "TestQuestion #%d code%s" % (self.id, self.code)
        return "New TestQuestion"

    @classmethod
    def calculate_weight(cls, test_question):
        # if test_section.is_nis():
        #     return 1
        return 1
    
    def is_draft(self) -> bool:
        return self.status == self.STATUS_DRAFT

    def is_pending(self) -> bool:
        return self.status == self.STATUS_PENDING

    def is_approved(self) -> bool:
        return self.status == self.STATUS_APPROVED

    def is_archived(self) -> bool:
        return self.status == self.STATUS_ARCHIVED
    
    def is_redo(self) -> bool:
        return self.status == self.STATUS_REDO
    
    def is_active(self) -> bool:
        return self.status == self.STATUS_ACTIVE
    
    def get_lang(self) -> str:
        domain_name = self.section.domain.name
        if "ru" in domain_name:
            return Test.LANGUAGE_RU
        if "kz" in domain_name:
            return Test.LANGUAGE_KK
        return Test.LANGUAGE_XX


class TestToQuestionRelation(Model):
    question   = ForeignKey  ( TestQuestion,  on_delete=CASCADE,                         )
    test  = ForeignKey  ( Test, on_delete=CASCADE, related_name="through", )

    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"), db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)
        unique_together = ("test", "question")

    def __str__(self):
        return "({}: {} {})".format(self.order, self.test, self.question)

class TestParagraph(Model):
    PARAGRAPH_CLASS_TEXT           = "TextParagraph"
    PARAGRAPH_CLASS_SPLIT_TEXT     = "SplitTextParagraph"
    PARAGRAPH_CLASS_IMAGE          = "ImageParagraph"
    PARAGRAPH_CLASS_AUDIO          = "AudioParagraph"
    PARAGRAPH_CLASS_PERIODIC_TABLE = "PeriodicTableParagraph"
    PARAGRAPH_CLASS_CALCULATOR     = "CalculatorParagraph"
    PARAGRAPH_CLASS_SOLUTION_TEXT  = "SolutionTextParagraph"
    PARAGRAPH_CLASS_SOLUTION_IMAGE = "SolutionImageParagraph"

    PARAGRAPH_CLASSES = (
        ( PARAGRAPH_CLASS_TEXT,           PARAGRAPH_CLASS_TEXT              ),
        ( PARAGRAPH_CLASS_SPLIT_TEXT,     PARAGRAPH_CLASS_SPLIT_TEXT        ),
        ( PARAGRAPH_CLASS_IMAGE,          PARAGRAPH_CLASS_IMAGE             ),
        ( PARAGRAPH_CLASS_PERIODIC_TABLE, PARAGRAPH_CLASS_PERIODIC_TABLE    ),
        ( PARAGRAPH_CLASS_CALCULATOR,     PARAGRAPH_CLASS_CALCULATOR        ),
        ( PARAGRAPH_CLASS_SOLUTION_TEXT,  PARAGRAPH_CLASS_SOLUTION_TEXT     ),
        ( PARAGRAPH_CLASS_SOLUTION_IMAGE, PARAGRAPH_CLASS_SOLUTION_IMAGE    ),
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
    name        = CharField        ( pgettext_lazy("Model field", "package name"),  max_length=100, unique=False, )
    code        = CharField        ( pgettext_lazy("Model field", "package code"),  max_length=10, unique=True, db_index=True, )
    finalized   = BooleanField     ( pgettext_lazy("Model field", "is finalized"),  default=False)
    created_at  = DateTimeField    ( pgettext_lazy("Model field", "created at"), auto_now_add=True, )

    tests       = ManyToManyField  ( Test, through="TestPackageRelation", related_name="test_packages", )
    # students    = ManyToManyField  ( User,                                related_name="package_students", db_index=True)
    domain      = ForeignKey       ( TestDomain,   on_delete=CASCADE,     related_name="test_packages"   )


    # student_group = ForeignKey     ( StudentGroup,   on_delete=CASCADE,     related_name="test_packages"   )

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.code

class StudentGroup(Model):
    name          = CharField                  ( pgettext_lazy("Model field", "student group name"),  max_length=100, unique=True, )
    package       = ForeignKey                 ( TestPackage,   on_delete=CASCADE,     related_name="student_groups"   )
    student_count = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "student count"), default=0)
    is_active     =     BooleanField           ( pgettext_lazy("Model field", "is active?"),  default=False)

    class Meta:
        default_permissions = ()
        # unique_together = ('name', 'package')
    
    def __str__(self):
        return "{}|{}|{}|{}".format(self.package.pk, self.name, self.student_count, self.is_active)


class TestPackageRelation(Model):
    test        = ForeignKey  ( Test,        on_delete=CASCADE,                         )
    package     = ForeignKey  ( TestPackage, on_delete=CASCADE, related_name="through", )

    order  = PositiveSmallIntegerField  ( pgettext_lazy("Model field", "order"), db_index=True, )

    class Meta:
        default_permissions = ()
        ordering = ("order",)
        unique_together = ("package", "test")



class TestPackageRusKazPair(Model):
    name = CharField(
        pgettext_lazy("Model field", "package name"),
        max_length=100,
        unique=False,
    )
    # organizator = ForeignKey(User, on_delete=CASCADE, related_name="test_packages_ruskaz_pairs")
    created_at = DateTimeField(
        pgettext_lazy("Model field", "created at"),
        auto_now_add=True,
    )
    test_package_ru = ForeignKey(
        TestPackage, on_delete=CASCADE, related_name="test_package_ru_pairs"
    )
    test_package_kz = ForeignKey(
        TestPackage, on_delete=CASCADE, related_name="test_package_kz_pairs"
    )
    
    @property
    def code(self):
        return f"{self.test_package_ru.code}{self.test_package_kz.code}"

    class Meta:
        default_permissions = ()
        unique_together = ("test_package_ru", "test_package_kz")

    def __str__(self):
        return f"{self.name} ({self.code})"
    

class TestPackageRusKazQuiz(Model):
    user = ForeignKey(
        get_user_model(),
        on_delete=CASCADE,
        related_name="test_package_pair_quiz_sets",
    )
    # name = CharField(
    #     pgettext_lazy("Model field", "package name"),
    #     max_length=100,
    #     unique=False,
    # )
    TestPackagePair = ForeignKey(
        TestPackageRusKazPair,
        on_delete=CASCADE,
        related_name="test_package_pair_quiz_sets",
    )
    payed = BooleanField(
        pgettext_lazy("Model field", "is payed?"),
        default=False,
        db_index=True,
        null=False,
    )
    started = BooleanField(
        pgettext_lazy("Model field", "is started?"),
        default=False,
        db_index=True,
        null=False,
    )
    number_of_students = PositiveIntegerField(
        pgettext_lazy("Model field", "number of students in package quiz"),
    )
    student_table = JSONField(
        pgettext_lazy("Model field", "Student Json Table"), default="[]"
    )

    created_at = DateTimeField(
        pgettext_lazy("Model field", "created at"),
        auto_now_add=True,
    )

    class Meta:
        default_permissions = ()

# -------------------------------------------- User Profile --------------------------------------------

class UserTestPackageProfile(Model):
    student = OneToOneField ( User,         on_delete=CASCADE, related_name="student_test_profile")

    student_group = ForeignKey       ( StudentGroup,   on_delete=CASCADE,     related_name="students"   )


class ExpertProfile(Model):
    expert = OneToOneField ( User,         on_delete=CASCADE, related_name="expert_profile")

    section = ManyToManyField  ( TestSection, related_name="expert_section_list", )

    permission_all = BooleanField( default=False, db_index=True, )

    def __str__(self):
        return "{}: {}".format(self.expert.username, self.section.all())


class DeveloperProfile(Model):
    developer = OneToOneField ( User,         on_delete=CASCADE, related_name="developer_profile")

    section = ManyToManyField  ( TestSection, related_name="developer_section_list", )
    
    permission_all = BooleanField( default=False, db_index=True, )

    def __str__(self):
        return "{}: {}".format(self.developer.username, self.section.all())


# class B2BTeacherProfile(Model):
#     B2BTeacher = OneToOneField(
#         User, on_delete=CASCADE, related_name="B2BTeacher_profile"
#     )
#     TestPackagePair = ForeignKey(
#         TestPackageRusKazPair, on_delete=CASCADE, related_name="test_package_pairs"
#     )


# -------------------------------------------- Simple chat --------------------------------------------
    
class QuestionComments(Model):
    sender = ForeignKey(User, on_delete=CASCADE)
    question = ForeignKey(TestQuestion, on_delete=CASCADE, related_name='comments')
    content = CharField( pgettext_lazy("Model field", "content"),  max_length=1000, unique=False, )
    created_at  = DateTimeField( pgettext_lazy("Model field", "created at"), auto_now_add=True, )