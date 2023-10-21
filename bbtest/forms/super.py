from django.forms import Form, ChoiceField, IntegerField, CharField, DateField, DateTimeField
from django.utils.translation import pgettext_lazy, pgettext
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
    name =CharField(label = pgettext("CreateStudentsForm", "Login prefix"), 
        error_messages = {"required": "Student will be generated with this name." }, 
        initial = "IAC_2023",
        min_length = 1,
        max_length = 30)
    # prefix = CharField(label="Email Pefix", error_messages={
    #     "required": "Student's email will be generated with this prefix."
    # }, max_length=30, initial="bb")
    amount = IntegerField(label=pgettext("CreateStudentsForm", "Amount"),
        initial=10, 
        error_messages={
            "required": "Please provide an amount.",
            "invalid": "Amount is invalid.",
            "max_value": "Amount cannot be more than %(limit_value)s.",
            "min_value": "Amount has to be at least %(limit_value)s.",
        }, max_value=1000, min_value=1)


class ExportDataForm(Form):
    start_date = DateField(label="Start Date", 
                           error_messages={"required": "Specify start date." }, 
                           initial=datetime.datetime.now() - datetime.timedelta(days = 7))

    end_date = DateField(label="End Date", 
                         error_messages={"required": "Specify start date."}, 
                         initial=datetime.datetime.now())