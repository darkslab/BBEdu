from django.forms import Form
from django.utils.translation import pgettext_lazy
from django.core.exceptions import ValidationError
from bbtest.forms.fields import JSONField
from bbtest.models import Test


class BuyTestsCartForm(Form):
    error_messages = {
        "incorrect": pgettext_lazy("Validation error", "Incorrect data."),
    }

    data = JSONField(label=pgettext_lazy("Form label", "Data"), error_messages={
        "required": pgettext_lazy("Validation error", "Please provide data."),
    })

    def __init__(self, student, test_domain, *args, **kwargs):
        self.__student = student
        self.__test_domain = test_domain
        super().__init__(*args, **kwargs)

    def clean_data(self):
        data = self.cleaned_data["data"]
        clean_data = {}
        try:
            if not isinstance(data, dict):
                raise ValueError("Incorrect data")

            if self.__test_domain.pk == 7913:
                data["language"] = Test.LANGUAGE_XX
            else:
                if data["language"] not in [ test_language[0] for test_language in Test.LANGUAGES if test_language[0] != Test.LANGUAGE_XX ]:
                    raise ValueError("Incorrect data")
            clean_data["language"] = data["language"]

            clean_data["sections"] = []
            if not isinstance(data["sections"], list):
                raise ValueError("Incorrect data")
            available_tests = self.__student.next_tests(self.__test_domain, clean_data["language"])
            available_test_section_ids = [ test.section_id for test in available_tests ]
            for section in data["sections"]:
                if section not in available_test_section_ids:
                    raise ValueError("Incorrect data")
                if section in clean_data["sections"]:
                    continue
                clean_data["sections"].append(section)
            clean_data["selected_bundle_pk"] = data.get("selected_bundle_pk", -1)

        except (KeyError, ValueError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return clean_data
