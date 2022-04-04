from django.forms import Form, ChoiceField, IntegerField, CharField


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

class ChangeUserPassManualForm(Form):
    pass1 = CharField(label="Password", 
        error_messages={"required": "Reset password" }, 
        max_length=30)
    pass2 = CharField(label="Password Repeat", 
        error_messages={"required": "Reset password." }, 
        max_length=30)