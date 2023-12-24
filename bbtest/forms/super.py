from django.forms import Form, ChoiceField, IntegerField, CharField, DateField, DateTimeField, ModelChoiceField, MultipleChoiceField
from django.utils.translation import pgettext_lazy, pgettext
from bbtest.models import TestDomain, TestSection, Test
import datetime


class GiveCreditsForm(Form):
    credit_type = ChoiceField(label="Credit Type", error_messages={
        "required": "Please provide a credit type.",
        "invalid_choice": "Credit type is invalid.",
    }, choices=(
        ( "Cash", "Cash Payment (ex.: Offline Kaspii Bank payment)" ),
        ( "Promo-Credits", "Promo Credits (ex.: Promotional stuff)" ),
        ( "Correction-Credits", "Correction Credits (ex.: Payment error correction)" ),
    ))
    amount = IntegerField(label="Amount", error_messages={
        "required": "Please provide an amount.",
        "invalid": "Amount is invalid.",
        "max_value": "Amount cannot be more than %(limit_value)s.",
        "min_value": "Amount has to be at least %(limit_value)s.",
    }, max_value=10000, min_value=1)
    description = CharField(label="Description", error_messages={
        "required": "Please provide a description.",
        "max_length": "Description cannot be more than %(limit_value)s characters long.",
        "min_length": "Description has to be at least %(limit_value)s characters long.",
    }, max_length=1000, min_length=5)


class CreateStudentsForm(Form):
    name = CharField(label = pgettext("CreateStudentsForm", "Login prefix"), 
        error_messages = {"required": "Student will be generated with this name." }, 
        initial = "IAC_2023",
        min_length = 1,
        max_length = 30)
    # prefix = CharField(label="Email Pefix", error_messages={
    #     "required": "Student's email will be generated with this prefix."
    # }, max_length=30, initial="bb")
    domain = ModelChoiceField(
        queryset = TestDomain.objects.all(),
        empty_label = pgettext("CreateStudentsForm", "Select Test Domain")
    )

    amount = IntegerField(label=pgettext("CreateStudentsForm", "Amount"),
        initial=10, 
        error_messages={
            "required": "Please provide an amount.",
            "invalid": "Amount is invalid.",
            "max_value": "Amount cannot be more than %(limit_value)s.",
            "min_value": "Amount has to be at least %(limit_value)s.",
        }, max_value=1000, min_value=1)
    

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
    name = CharField(label = pgettext("CreatePackageForm", "Login prefix"), 
        error_messages = {"required": "Package will be generated with this name." }, 
        initial = "",
        empty_value = "IAC_2024",
        min_length = 1,
        max_length = 100)

    domain = ModelChoiceField(
        label = pgettext("CreatePackageForm", "Domain"),
        queryset = TestDomain.objects.all(),
        empty_label = pgettext("CreatePackageForm", "Select Test Domain")
    )

class CreateStudentGroupForm(Form):
    name = CharField(label = pgettext("CreateStudentGroupForm", "Student Group name"), 
        error_messages = {"required": "Student Group will be created with this name." }, 
        # initial = "Test day n",
        empty_value = pgettext("CreateStudentGroupForm", "Test day 001"),
        min_length = 1,
        max_length = 100)

    # domain = ModelChoiceField(
    #     queryset = TestDomain.objects.all(),
    #     empty_label = pgettext("CreatePackageForm", "Select Test Domain")
    # )


class ManagePackageStudentsForm(Form):

    amount = IntegerField(label=pgettext("ManagePackageStudentsForm", "Amount"),
        initial=1, 
        error_messages={
            "required": "Please provide an amount.",
            "invalid": "Amount is invalid.",
            "max_value": "Amount cannot be more than %(limit_value)s.",
            "min_value": "Amount has to be at least %(limit_value)s.",
        }, max_value=1000, min_value=1)
    
    prefix = CharField(
        label=pgettext("ManagePackageStudentsForm", "Optional Prefix"), 
        # error_messages={"required": "Student's email will be generated with this prefix."}, 
        max_length=30, 
        required=False,
        initial=""
    )



class ManagePackageTestForm(Form):
    # This form field options are created later in runtime
    test = ChoiceField(label="Select Test",  choices=[])  # queryset=Test.objects.none()

    def __init__(self, *args, **kwargs):
         choices = kwargs.pop('choices', [])
         super(Form, self).__init__(*args, **kwargs)
         self.fields['test'].choices = choices


class ExportDataForm(Form):
    start_date = DateField(label="Start Date", 
                           error_messages={"required": "Specify start date." }, 
                           initial=datetime.datetime.now() - datetime.timedelta(days = 7))

    end_date = DateField(label="End Date", 
                         error_messages={"required": "Specify start date."}, 
                         initial=datetime.datetime.now())
    


class ChangeUserPassManualForm(Form):
    pass1 = CharField(label="Password", 
        error_messages={"required": "Reset password" }, 
        max_length=30)
    pass2 = CharField(label="Password Repeat", 
        error_messages={"required": "Reset password." }, 
        max_length=30)