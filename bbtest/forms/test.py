from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy
from bbtest.models import TestQuestion


class TestQuestionForm(ModelForm):
    error_messages = {
        "incorrect": pgettext_lazy("Form validation error", "Incorrect meta data."),
    }

    class Meta:
        model = TestQuestion
        fields = ("difficulty", "taxonomy", "topic", "answer_class", "meta_data")
        error_messages = {
            "difficulty": {
                "required": pgettext_lazy("Form field error", "Please select difficulty."),
                "invalid_choice": pgettext_lazy("Form field error", "Incorrect difficulty value."),
            },
            "taxonomy": {
                "invalid_choice": pgettext_lazy("Form field error", "Incorrect taxonomy value."),
            },
            "topic": {
                "invalid_choice": pgettext_lazy("Form field error", "Incorrect topic value."),
            },
            "answer_class": {
                "invalid_choice": pgettext_lazy("Form field error", "Incorrect answer class."),
            },
            "meta_data": {
                "invalid": pgettext_lazy("Form field error", "Please provide meta data in JSON format."),
                "incorrect": pgettext_lazy("Form field error", "Incorrect meta data value."),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["answer_class"].required = False
        self.fields["meta_data"].required = False

    def clean_meta_data(self):
        answer_class = self.cleaned_data.get("answer_class", "")
        meta_data = self.cleaned_data["meta_data"]
        clean_meta_data = None

        if answer_class == "MultichoiceOneAnswer":
            clean_meta_data = self.__clean_multichoice_one_answer_meta_data(meta_data)

        return clean_meta_data

    def __clean_multichoice_one_answer_meta_data(self, meta_data):
        clean_meta_data = {
            "choices": [],
            "correct_id": None
        }
        if meta_data is None:
            return clean_meta_data

        try:
            if not isinstance(meta_data, dict):
                raise ValueError("Incorrect meta_data")
            if not isinstance(meta_data["choices"], list):
                raise ValueError("Incorrect meta_data")

            for choice in meta_data["choices"]:
                clean_choice = {}
                if not isinstance(choice, dict):
                    raise ValueError("Incorrect meta_data")

                clean_choice["id"] = int(choice["id"])
                if clean_choice["id"] < 0 or clean_choice["id"] > 0xffff + 8:
                    raise ValueError("Incorrect meta_data")

                clean_choice["choice_class"] = choice["choice_class"]
                if clean_choice["choice_class"] not in (
                    "MultichoiceTextChoice",
                ):
                    raise ValueError("Incorrect meta_data")

                if clean_choice["choice_class"] == "MultichoiceTextChoice":
                    clean_choice["meta_data"] = self.__clean_multichoice_text_choice_meta_data(choice["meta_data"])

                clean_meta_data["choices"].append(clean_choice)

            if meta_data["correct_id"] is not None:
                clean_meta_data["correct_id"] = int(meta_data["correct_id"])
                found = False
                for choice in clean_meta_data["choices"]:
                    if choice["id"] == clean_meta_data["correct_id"]:
                        found = True
                        break
                if not found:
                    raise ValueError("Incorrect meta_data")

            choice_ids = set([])
            for choice in clean_meta_data["choices"]:
                choice_ids.add(choice["id"])
            if len(choice_ids) != len(clean_meta_data["choices"]):
                raise ValueError("Incorrect meta_data")

        except (KeyError, ValueError, TypeError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return clean_meta_data

    def __clean_multichoice_text_choice_meta_data(self, meta_data):
        try:
            if not isinstance(meta_data, dict):
                raise ValueError("Incorrect meta_data")
            if not isinstance(meta_data["text"], str):
                raise ValueError("Incorrect meta_data")
            return {
                "text": meta_data["text"]
            }
        except (KeyError, ValueError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
