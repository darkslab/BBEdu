import datetime

from django.forms import (
    CharField,
    ChoiceField,
    DateField,
    DateInput,
    DateTimeField,
    Form,
    IntegerField,
    ModelChoiceField,
    MultipleChoiceField,
)
from django.utils.translation import pgettext, pgettext_lazy

from bbtest.models import Test, TestDomain, TestSection, TestPackageRusKazPair


class GiveCreditsForm(Form):
    credit_type = ChoiceField(
        label="Credit Type",
        error_messages={
            "required": "Please provide a credit type.",
            "invalid_choice": "Credit type is invalid.",
        },
        choices=(
            ("Cash", "Cash Payment (ex.: Offline Kaspii Bank payment)"),
            ("Promo-Credits", "Promo Credits (ex.: Promotional stuff)"),
            (
                "Correction-Credits",
                "Correction Credits (ex.: Payment error correction)",
            ),
        ),
    )
    amount = IntegerField(
        label="Amount",
        error_messages={
            "required": "Please provide an amount.",
            "invalid": "Amount is invalid.",
            "max_value": "Amount cannot be more than %(limit_value)s.",
            "min_value": "Amount has to be at least %(limit_value)s.",
        },
        max_value=10000,
        min_value=1,
    )
    description = CharField(
        label="Description",
        error_messages={
            "required": "Please provide a description.",
            "max_length": "Description cannot be more than %(limit_value)s characters long.",
            "min_length": "Description has to be at least %(limit_value)s characters long.",
        },
        max_length=1000,
        min_length=5,
    )


class CreateStudentsForm(Form):
    name = CharField(
        label=pgettext("CreateStudentsForm", "Login prefix"),
        error_messages={"required": "Student will be generated with this name."},
        initial="IAC_2023",
        min_length=1,
        max_length=30,
    )
    # prefix = CharField(label="Email Pefix", error_messages={
    #     "required": "Student's email will be generated with this prefix."
    # }, max_length=30, initial="bb")
    domain = ModelChoiceField(
        queryset=TestDomain.objects.all(),
        empty_label=pgettext("CreateStudentsForm", "Select Test Domain"),
    )

    amount = IntegerField(
        label=pgettext("CreateStudentsForm", "Amount"),
        initial=10,
        error_messages={
            "required": "Please provide an amount.",
            "invalid": "Amount is invalid.",
            "max_value": "Amount cannot be more than %(limit_value)s.",
            "min_value": "Amount has to be at least %(limit_value)s.",
        },
        max_value=100000,
        min_value=1,
    )

    # def __init__(self, *args, **kwargs):
    #     super(CreateStudentsForm, self).__init__(*args, **kwargs)
    #     self.fields['section'].choices = [(1,1),(2,2),(3,3)]
    #     print("asd", self.data)

    # CATEGORY_CHOICES = (
    #     ('Debt', (
    #         (11, 'Credit Card'),
    #         (12, 'Student Loans'),
    #         (13, 'Taxes'),
    #     )),
    #     ('Entertainment', (
    #         (21, 'Books'),
    #         (22, 'Games'),
    #     )),
    #     ('Everyday', (
    #         (31, 'Groceries'),
    #         (32, 'Restaurants'),
    #     )),
    # )

    # section = ChoiceField(choices=CATEGORY_CHOICES, required=False)


class CreatePackageForm(Form):
    name = CharField(
        label=pgettext("CreatePackageForm", "Login prefix"),
        error_messages={"required": "Package will be generated with this name."},
        initial="Pilot_test",
        # help_text="Pilot_test",
        # empty_value="Pilot_test",
        min_length=1,
        max_length=100,
    )

    domain = ModelChoiceField(
        label=pgettext("CreatePackageForm", "Domain"),
        queryset=TestDomain.objects.all(),
        empty_label=pgettext("CreatePackageForm", "Select Test Domain"),
    )

class Buy_B2BTeacher_PackageForm(Form):
    

    test_package_pair = ModelChoiceField(
        label=pgettext("Buy_B2BTeacher_PackageForm", "TestPackage"),
        queryset=TestPackageRusKazPair.objects.all(),
        empty_label=pgettext("Buy_B2BTeacher_PackageForm", "Select TestPackage"),
    )

    number_of_students = IntegerField(
        label=pgettext("Buy_B2BTeacher_PackageForm", "Number of Students"),
        error_messages={
            "required": "Select Number of Students",
            # "invalid_choice": "Invalid choice.",
        },
        # choices=(
        #     (5, "5 (5000 KZT)"),
        #     (25, "25 (10000 KZT)"),
        #     (50, "50 (19000 KZT)"),
        #     (100, "100 (35000 KZT)"),
        # ),
    )

    # comment = CharField(
    #     label=pgettext("Buy_B2BTeacher_PackageForm", "Comment"),
    #     error_messages={"required": "Package will be generated with this name."},
    #     initial="",
    #     # help_text="Pilot_test",
    #     # empty_value="Pilot_test",
    #     min_length=1,
    #     max_length=100,
    # )


class CreateStudentGroupForm(Form):
    name = CharField(
        label=pgettext("/build/packages/PACKAGE_CODE/ (CreateStudentGroupForm)", "Student Group name"),
        error_messages={"required": "Student Group will be created with this name."},
        # initial = "Test day n",
        # empty_value=pgettext("CreateStudentGroupForm", "Test day 001"),
        min_length=1,
        max_length=100,
    )

    # domain = ModelChoiceField(
    #     queryset = TestDomain.objects.all(),
    #     empty_label = pgettext("CreatePackageForm", "Select Test Domain")
    # )


class ManagePackageStudentsForm(Form):

    amount = IntegerField(
        label=pgettext("/build/packages/PACKAGE_CODE/GROUP_NUMBER (ManagePackageStudentsForm)", "Amount"),
        initial=1,
        error_messages={
            "required": "Please provide an amount.",
            "invalid": "Amount is invalid.",
            "max_value": "Amount cannot be more than %(limit_value)s.",
            "min_value": "Amount has to be at least %(limit_value)s.",
        },
        max_value=100000,
        min_value=1,
    )

    prefix = CharField(
        label=pgettext("/build/packages/PACKAGE_CODE/GROUP_NUMBER (ManagePackageStudentsForm)", "Optional Prefix"),
        # error_messages={"required": "Student's email will be generated with this prefix."},
        max_length=30,
        required=False,
        initial="",
    )


class ManagePackageTestForm(Form):
    # This form field options are created later in runtime
    test = ChoiceField(
        label=pgettext("/build/packages/PACKAGE_CODE/ (ManagePackageTestForm)", "Select Test") , 
        choices=[]
    )  # queryset=Test.objects.none()

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices", [])
        super(Form, self).__init__(*args, **kwargs)
        self.fields["test"].choices = choices


class ExportDataForm(Form):
    start_date = DateField(
        label="Start Date",
        error_messages={"required": "Specify start date."},
        initial=datetime.datetime.now() - datetime.timedelta(days=0),
        widget=DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    end_date = DateField(
        label="End Date",
        error_messages={"required": "Specify end date."},
        initial=datetime.datetime.now(),
        widget=DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    klass_domain = ChoiceField(
        label="Domain",
        error_messages={
            "required": "Select Domain",
            "invalid_choice": "Invalid choice.",
        },
        choices=(
            ("Klass_4", "Класс 4"),
            ("Klass_9", "Класс 9"),
            ("Teacher", "Учителя"),
            ("Parent", "Родители"),
        ),
    )


class ChangeUserPassManualForm(Form):
    pass1 = CharField(
        label="Password", error_messages={"required": "Reset password"}, max_length=30
    )
    pass2 = CharField(
        label="Password Repeat",
        error_messages={"required": "Reset password."},
        max_length=30,
    )


class CreateCustomTestSelectionForm(Form):
    # This form field options are created later in runtime
    section = ChoiceField(
        label=pgettext("/build/test_assemble/ (CreateCustomTestSelectionForm)", "Select section") , 
        choices=[]
    ) 
    question_count = IntegerField(
        label=pgettext("/build/test_assemble/ (CreateCustomTestSelectionForm)", "question_count"),
        initial=10,
        error_messages={
            "required": "Please provide an amount.",
            "invalid": "Amount is invalid.",
            "max_value": "Amount cannot be more than %(limit_value)s.",
            "min_value": "Amount has to be at least %(limit_value)s.",
        },
        max_value=1000,
        min_value=1,
    )
    test_duration = IntegerField(
        label=pgettext("/build/test_assemble/ (CreateCustomTestSelectionForm)", "test_duration"),
        initial=60,
        error_messages={
            "required": "Please provide an amount.",
            "invalid": "Amount is invalid.",
            "max_value": "Amount cannot be more than %(limit_value)s.",
            "min_value": "Amount has to be at least %(limit_value)s.",
        },
        max_value=10000000,
        min_value=1,
    )

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices", [])
        super(Form, self).__init__(*args, **kwargs)
        self.fields["section"].choices = choices


class CreateStandaloneQuestionForm(Form):
    # This form field options are created later in runtime
    section = ChoiceField(
        label=pgettext("/build/question_standalone_create/ (CreateStandaloneQuestionForm)", "Select section") , 
        choices=[]
    ) 


    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices", [])
        super(Form, self).__init__(*args, **kwargs)
        self.fields["section"].choices = choices
