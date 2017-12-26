from django.forms import ModelForm, Form
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy
from bbtest.models import TestQuestion, TestParagraph, TestParagraphQuestion
from bbtest.forms.fields import JSONField
from bbtest.utils.json import tight_dumps


class TestQuestionForm(ModelForm):
    error_messages = {
        "incorrect": pgettext_lazy("Validation error", "Incorrect data."),
    }

    class Meta:
        model = TestQuestion
        fields = ("difficulty", "taxonomy", "topic", "answer_class", "meta_data")
        error_messages = {
            "difficulty": {
                "required": pgettext_lazy("Validation error", "Please select difficulty."),
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect difficulty value."),
            },
            "taxonomy": {
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect taxonomy value."),
            },
            "topic": {
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect topic value."),
            },
            "answer_class": {
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect answer class."),
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

        if answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
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


class TestParagraphForm(ModelForm):
    error_messages = {
        "incorrect": pgettext_lazy("Validation error", "Incorrect data."),
    }

    class Meta:
        model = TestParagraph
        fields = ("paragraph_class", "meta_data")
        error_messages = {
            "paragraph_class": {
                "required": pgettext_lazy("Validation error", "Please provide paragraph class."),
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect paragraph class."),
            },
            "meta_data": {
                "required": pgettext_lazy("Validation error", "Please provide meta data."),
            },
        }

    def clean_meta_data(self):
        paragraph_class = self.cleaned_data.get("paragraph_class", None)
        meta_data = self.cleaned_data["meta_data"]
        if paragraph_class is None:
            return meta_data

        if paragraph_class == TestParagraph.PARAGRAPH_CLASS_TEXT:
            return self.__clean_text_paragraph_meta_data(meta_data)
        elif paragraph_class == TestParagraph.PARAGRAPH_CLASS_SPLIT_TEXT:
            return self.__clean_split_text_paragraph_meta_data(meta_data)

        raise ValidationError(
            self.error_messages["incorrect"],
            code="incorrect",
        )

    def __clean_text_paragraph_meta_data(self, meta_data):
        clean_meta_data = {
            "text": "",
        }
        try:
            if not isinstance(meta_data, dict):
                raise ValueError("Incorrect meta_data")
            if not isinstance(meta_data["text"], str):
                raise ValueError("Incorrect meta_data")
            clean_meta_data["text"] = meta_data["text"]
        except (KeyError, ValueError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return clean_meta_data

    def __clean_split_text_paragraph_meta_data(self, meta_data):
        clean_meta_data = {
            "right": {
                "text": "",
            },
            "left": {
                "text": "",
            },
        }
        try:
            if not isinstance(meta_data, dict):
                raise ValueError("Incorrect meta_data")

            if not isinstance(meta_data["right"], dict):
                raise ValueError("Incorrect meta_data")
            if not isinstance(meta_data["right"]["text"], str):
                raise ValueError("Incorrect meta_data")
            clean_meta_data["right"]["text"] = meta_data["right"]["text"]

            if not isinstance(meta_data["left"], dict):
                raise ValueError("Incorrect meta_data")
            if not isinstance(meta_data["left"]["text"], str):
                raise ValueError("Incorrect meta_data")
            clean_meta_data["left"]["text"] = meta_data["left"]["text"]

        except (KeyError, ValueError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return clean_meta_data


class TestParagraphsContainerForm(Form):
    error_messages = {
        "incorrect": pgettext_lazy("Validation error", "Incorrect data."),
    }

    data = JSONField(label=pgettext_lazy("Form label", "Data"), required=False)

    def __init__(self, question, *args, **kwargs):
        self._question = question
        self._forms = []
        self._removed_paragraphs = []
        super().__init__(*args, **kwargs)

    def clean_data(self):
        data = self.cleaned_data["data"]
        clean_data = []
        try:
            if not isinstance(data, list):
                raise ValueError("Incorrect data")

            for _data in data:
                _clean_data = {}
                if not isinstance(_data, dict):
                    raise ValueError("Incorrect data")
                if not isinstance(_data["is_new"], bool):
                    raise ValueError("Incorrect data")
                if not _data["is_new"]:
                    _clean_data["id"] = int(_data["id"])
                if not isinstance(_data["data"], dict):
                    raise ValueError("Incorrect data")
                _clean_data["data"] = {
                    "paragraph_class": _data["data"]["paragraph_class"],
                    "meta_data": tight_dumps(_data["data"]["meta_data"]),
                }
                clean_data.append(_clean_data)

        except (KeyError, ValueError, TypeError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return clean_data

    def clean(self):
        if self.cleaned_data.get("data", None) is None:
            return self.cleaned_data

        paragraphs = list(self._question.paragraphs.all())
        paragraph_ids = []
        for paragraph in paragraphs:
            paragraph_ids.append(paragraph.id)

        for data in self.cleaned_data["data"]:
            if "id" in data and data["id"] not in paragraph_ids:
                raise ValidationError({
                    "data": ValidationError(
                        self.error_messages["incorrect"],
                        code="incorrect",
                    ),
                })
            if "id" in data:
                paragraph_index = paragraph_ids.index(data["id"])
                self._forms.append(
                    TestParagraphForm(
                        data=data["data"],
                        instance=paragraphs.pop(paragraph_index),
                    )
                )
                paragraph_ids.pop(paragraph_index)
            else:
                self._forms.append(
                    TestParagraphForm(data=data["data"])
                )

        for form in self._forms:
            if not form.is_valid():
                _error_messages = []
                for key, validation_errors in form.errors.as_data().items():
                    for validation_error in validation_errors:
                        _error_messages.append(validation_error.message)
                raise ValidationError({
                    "data": ValidationError(
                        " ".join(_error_messages),
                        code="incorrect",
                    ),
                })

        self._removed_paragraphs = paragraphs
        return self.cleaned_data

    def save_paragraphs(self):
        try:
            while True:
                self._removed_paragraphs.pop().delete()
        except IndexError:
            pass

        paragraphs = []
        paragraph_ids = []
        self._forms.reverse()
        try:
            while True:
                paragraph = self._forms.pop().save()
                paragraphs.append(paragraph)
                paragraph_ids.append(paragraph.id)
        except IndexError:
            pass

        for paragraph_question in self._question.testparagraphquestion_set.all():
            paragraph_index = paragraph_ids.index(paragraph_question.paragraph_id)
            if paragraph_question.order != paragraph_index:
                paragraph_question.order = paragraph_index
                paragraph_question.save()
            paragraphs.pop(paragraph_index)
            paragraph_ids.pop(paragraph_index)

        paragraphs.reverse()
        try:
            while True:
                paragraph = paragraphs.pop()
                paragraph_index = paragraph_ids.index(paragraph.id)
                TestParagraphQuestion.objects.create(
                    question=self._question,
                    paragraph=paragraph,
                    order=paragraph_index,
                )
        except IndexError:
            pass
