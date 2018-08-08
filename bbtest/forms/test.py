from django.forms import ModelForm, Form
from django.forms.widgets import HiddenInput
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy, pgettext, ugettext as _, npgettext_lazy
from random import randint
from bbtest.models import TestQuestion, TestParagraph, TestParagraphQuestion, Test, Asset
from bbtest.forms.fields import JSONField
from bbtest.utils.json import tight_dumps
from bbtest.models.asset_classes import ImageParagraphAsset
from bbtest.jobs.upload import image_paragraph_destroyer


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
        elif answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI:
            clean_meta_data = self.__clean_multichoice_multi_answer_meta_data(meta_data)

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

    def __clean_multichoice_multi_answer_meta_data(self, meta_data):
        clean_meta_data = {
            "choices": [],
            "correct_ids": []
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

            choice_ids = set([])
            for choice in clean_meta_data["choices"]:
                choice_ids.add(choice["id"])
            if len(choice_ids) != len(clean_meta_data["choices"]):
                raise ValueError("Incorrect meta_data")

            if not isinstance(meta_data["correct_ids"], list):
                raise ValueError("Incorrect meta_data")
            correct_ids = set([])
            for correct_id in meta_data["correct_ids"]:
                correct_id = int(correct_id)
                if correct_id not in choice_ids:
                    raise ValueError("Incorrect meta_data")
                correct_ids.add(correct_id)
            if len(correct_ids) != len(meta_data["correct_ids"]):
                raise ValueError("Incorrect meta_data")
            clean_meta_data["correct_ids"] = list(correct_ids)

        except (KeyError, ValueError, TypeError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return clean_meta_data

    def __clean_multichoice_text_choice_meta_data(self, meta_data):
        clean_meta_data = {}
        try:
            if not isinstance(meta_data, dict):
                raise ValueError("Incorrect meta_data")
            if not isinstance(meta_data["text"], str):
                raise ValueError("Incorrect meta_data")
            clean_meta_data["text"] = meta_data["text"]
            if "has_formulas" in meta_data:
                if not isinstance(meta_data["has_formulas"], bool) or not meta_data["has_formulas"]:
                    raise ValueError("Incorrect meta_data")
                clean_meta_data["has_formulas"] = meta_data["has_formulas"]
        except (KeyError, ValueError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return clean_meta_data


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
        elif paragraph_class == TestParagraph.PARAGRAPH_CLASS_IMAGE:
            return self.__clean_image_paragraph_meta_data(meta_data)

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
            if "has_formulas" in meta_data:
                if not isinstance(meta_data["has_formulas"], bool) or not meta_data["has_formulas"]:
                    raise ValueError("Incorrect meta_data")
                clean_meta_data["has_formulas"] = meta_data["has_formulas"]
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

            if "has_formulas" in meta_data:
                if not isinstance(meta_data["has_formulas"], bool) or not meta_data["has_formulas"]:
                    raise ValueError("Incorrect meta_data")
                clean_meta_data["has_formulas"] = meta_data["has_formulas"]

        except (KeyError, ValueError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return clean_meta_data

    def __clean_image_paragraph_meta_data(self, meta_data):
        clean_meta_data = {
            "asset_uuid": None,
            "asset_object_name": None,
        }
        try:
            if not isinstance(meta_data, dict):
                raise ValueError("Incorrect meta_data")
            if not isinstance(meta_data["asset_uuid"], str):
                raise ValueError("Incorrect meta_data")

            asset = Asset.objects.get(uuid=meta_data["asset_uuid"])
            if not asset.is_adopted() or not isinstance(asset.asset_object(), ImageParagraphAsset):
                raise ValueError("Incorrect meta_data")

            clean_meta_data["asset_uuid"] = asset.uuid
            clean_meta_data["asset_object_name"] = asset.asset_object().object_name()

        except (KeyError, ValueError, Asset.DoesNotExist):
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
        self._form_data = []
        self._removed_paragraphs = []
        super().__init__(*args, **kwargs)

    def clean_data(self):
        data = self.cleaned_data["data"]
        clean_data = []
        try:
            if not isinstance(data, list):
                raise ValueError("Incorrect data")

            new_paragraph_ids = []
            old_paragraph_ids = []
            for _data in data:
                _clean_data = {}
                if not isinstance(_data, dict):
                    raise ValueError("Incorrect data")
                _clean_data["id"] = int(_data["id"])
                if not isinstance(_data["is_new"], bool):
                    raise ValueError("Incorrect data")
                _clean_data["is_new"] = _data["is_new"]
                if _clean_data["is_new"]:
                    if _clean_data["id"] in new_paragraph_ids:
                        raise ValueError("Incorrect data")
                    new_paragraph_ids.append(_clean_data["id"])
                else:
                    if _clean_data["id"] in old_paragraph_ids:
                        raise ValueError("Incorrect data")
                    old_paragraph_ids.append(_clean_data["id"])
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
            if data["is_new"]:
                self._form_data.append({
                    "form": TestParagraphForm(data=data["data"]),
                    "old": data["id"],
                })
            else:
                if data["id"] not in paragraph_ids:
                    raise ValidationError({
                        "data": ValidationError(
                            self.error_messages["incorrect"],
                            code="incorrect",
                        ),
                    })
                paragraph_index = paragraph_ids.index(data["id"])
                self._form_data.append({
                    "form": TestParagraphForm(
                        data=data["data"],
                        instance=paragraphs.pop(paragraph_index),
                    ),
                })
                paragraph_ids.pop(paragraph_index)

        for form_datum in self._form_data:
            if not form_datum["form"].is_valid():
                _error_messages = []
                for key, validation_errors in form_datum["form"].errors.as_data().items():
                    for validation_error in validation_errors:
                        _error_messages.append(str(validation_error.message))
                raise ValidationError({
                    "data": ValidationError(
                        " ".join(_error_messages),
                        code="incorrect",
                    ),
                })

        self._removed_paragraphs = paragraphs
        return self.cleaned_data

    def save_paragraphs(self):
        paragraph_morphs = []

        try:
            while True:
                paragraph = self._removed_paragraphs.pop()
                if paragraph.paragraph_class == TestParagraph.PARAGRAPH_CLASS_IMAGE:
                    image_paragraph_destroyer.delay(paragraph.meta_data["asset_uuid"])
                paragraph.delete()
        except IndexError:
            pass

        paragraphs = []
        paragraph_ids = []
        self._form_data.reverse()
        try:
            while True:
                paragraph_morph = None
                form_datum = self._form_data.pop()
                if "old" in form_datum:
                    paragraph_morph = {
                        "old": form_datum["old"],
                    }
                paragraph = form_datum["form"].save()
                if paragraph_morph is not None:
                    paragraph_morph["new"] = paragraph.id
                    paragraph_morphs.append(paragraph_morph)
                paragraphs.append(paragraph)
                paragraph_ids.append(paragraph.id)
        except IndexError:
            pass

        for paragraph_question in self._question.testparagraphquestion_set.all():
            if paragraph_question.paragraph_id not in paragraph_ids:
                continue
            paragraph_index = paragraph_ids.index(paragraph_question.paragraph_id)
            if paragraph_question.order != paragraph_index:
                paragraph_question.order = paragraph_index
                paragraph_question.save()
            paragraphs[paragraph_index] = None

        paragraphs.reverse()
        try:
            while True:
                paragraph = paragraphs.pop()
                if paragraph is None:
                    continue
                paragraph_index = paragraph_ids.index(paragraph.id)
                TestParagraphQuestion.objects.create(
                    question=self._question,
                    paragraph=paragraph,
                    order=paragraph_index,
                )
        except IndexError:
            pass

        return paragraph_morphs


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ("section", "language")
        widgets = {
            "section": HiddenInput,
            "language": HiddenInput,
        }
        error_messages = {
            "section": {
                "required": pgettext_lazy("Validation error", "Please select test section."),
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect test section value."),
            },
            "language": {
                "required": pgettext_lazy("Validation error", "Please select test language."),
                "invalid_choice": pgettext_lazy("Validation error", "Incorrect test language value."),
            },
        }

    # def clean(self):
    #     # DARK_TODO  clean language by section, i.e. only certain languages for certain sections
    #     pass

    def create_test_suite(self, developer):
        test = self.save(developer)

        # NIS sections
        if test.section.is_nis():
            shared_paragraph = None
            for i in range(test.section.question_count):
                choice_id = randint(0x0000, 0xffff)
                meta_data = {
                    "choices": [
                        {"id": choice_id + 0, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
                        {"id": choice_id + 1, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
                        {"id": choice_id + 2, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
                        {"id": choice_id + 3, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
                    ],
                    "correct_id": None,
                }
                if test.section.id == 9544:
                    meta_data["choices"][0]["meta_data"]["text"] = str(
                        pgettext("NIS Quantitative section answer", "Quantity A is greater."))
                    meta_data["choices"][1]["meta_data"]["text"] = str(
                        pgettext("NIS Quantitative section answer", "Quantity B is greater."))
                    meta_data["choices"][2]["meta_data"]["text"] = str(
                        pgettext("NIS Quantitative section answer", "The two quantities are equal."))
                    meta_data["choices"][3]["meta_data"]["text"] = str(pgettext("NIS Quantitative section answer",
                                                                                "The relationship cannot be determined from the information given."))

                question = test.questions.create(
                    answer_class=TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE,
                    meta_data=meta_data,
                    weight=0,
                    order=i,
                    developer=test.developer,
                )
                question.weight = TestQuestion.calculate_weight(question, test.section)
                question.save()

                if test.section.id == 9540:
                    paragraph = TestParagraph.objects.create(
                        paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                        meta_data={"text": ""},
                    )
                    TestParagraphQuestion.objects.create(
                        question=question,
                        paragraph=paragraph,
                        order=0,
                    )
                elif test.section.id in (9541, 9542, 9543):
                    if i < 6:
                        TestParagraphQuestion.objects.create(
                            question=question,
                            paragraph=TestParagraph.objects.create(
                                paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                                meta_data={"text": ""},
                            ),
                            order=0,
                        )
                    elif i in (6, 9, 12, 15):
                        shared_paragraph = TestParagraph.objects.create(
                            paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                            meta_data={"text": ""},
                        )
                        TestParagraphQuestion.objects.create(
                            question=question,
                            paragraph=shared_paragraph,
                            order=0,
                        )
                        TestParagraphQuestion.objects.create(
                            question=question,
                            paragraph=TestParagraph.objects.create(
                                paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                                meta_data={"text": ""},
                            ),
                            order=1,
                        )
                    else:
                        TestParagraphQuestion.objects.create(
                            question=question,
                            paragraph=shared_paragraph,
                            order=0,
                        )
                        TestParagraphQuestion.objects.create(
                            question=question,
                            paragraph=TestParagraph.objects.create(
                                paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                                meta_data={"text": ""},
                            ),
                            order=1,
                        )
                elif test.section.id == 9544:
                    paragraph = TestParagraph.objects.create(
                        paragraph_class=TestParagraph.PARAGRAPH_CLASS_SPLIT_TEXT,
                        meta_data={"right": {"text": ""}, "left": {"text": ""}},
                    )
                    TestParagraphQuestion.objects.create(
                        question=question,
                        paragraph=paragraph,
                        order=0,
                    )
        # UNT core sections
        elif test.section.is_unt_compulsory():
            shared_paragraph = None
            for i in range(test.section.question_count):
                choice_id = randint(0x0000, 0xffff)
                meta_data = {
                    "choices": [
                        {"id": choice_id + 0, "choice_class": "MultichoiceTextChoice",
                         "meta_data": {"text": ""}},
                        {"id": choice_id + 1, "choice_class": "MultichoiceTextChoice",
                         "meta_data": {"text": ""}},
                        {"id": choice_id + 2, "choice_class": "MultichoiceTextChoice",
                         "meta_data": {"text": ""}},
                        {"id": choice_id + 3, "choice_class": "MultichoiceTextChoice",
                         "meta_data": {"text": ""}},
                        {"id": choice_id + 4, "choice_class": "MultichoiceTextChoice",
                         "meta_data": {"text": ""}},
                    ],
                    "correct_id": None,
                }

                question = test.questions.create(
                    answer_class=TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE,
                    meta_data=meta_data,
                    weight=0,
                    order=i,
                    developer=test.developer,
                )
                question.weight = TestQuestion.calculate_weight(question, test.section)
                question.save()

                if test.section.id == 9546:
                    if i in (0, 2, 6, 12):
                        shared_paragraph = TestParagraph.objects.create(
                            paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                            meta_data={"text": ""},
                        )
                        TestParagraphQuestion.objects.create(
                            question=question,
                            paragraph=shared_paragraph,
                            order=0,
                        )
                        TestParagraphQuestion.objects.create(
                            question=question,
                            paragraph=TestParagraph.objects.create(
                                paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                                meta_data={"text": ""},
                            ),
                            order=1,
                        )
                    else:
                        TestParagraphQuestion.objects.create(
                            question=question,
                            paragraph=shared_paragraph,
                            order=0,
                        )
                        TestParagraphQuestion.objects.create(
                            question=question,
                            paragraph=TestParagraph.objects.create(
                                paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                                meta_data={"text": ""},
                            ),
                            order=1,
                        )
                else:
                    paragraph = TestParagraph.objects.create(
                        paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                        meta_data={"text": ""},
                    )
                    TestParagraphQuestion.objects.create(
                        question=question,
                        paragraph=paragraph,
                        order=0,
                    )

        # UNT spec sections
        elif test.section.is_unt_profile():
            for i in range(test.section.question_count):
                choice_id = randint(0x0000, 0xffff)
                if i in range(20):
                    answer_class = TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE
                    meta_data = {
                        "choices": [
                            {"id": choice_id + 0, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                            {"id": choice_id + 1, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                            {"id": choice_id + 2, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                            {"id": choice_id + 3, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                            {"id": choice_id + 4, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                        ],
                        "correct_id": None,
                    }
                else:
                    answer_class = TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI
                    meta_data = {
                        "choices": [
                            {"id": choice_id + 0, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                            {"id": choice_id + 1, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                            {"id": choice_id + 2, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                            {"id": choice_id + 3, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                            {"id": choice_id + 4, "choice_class": "MultichoiceTextChoice",
                             "meta_data": {"text": ""}},
                        ],
                        "correct_ids": [],
                    }

                question = test.questions.create(
                    answer_class=answer_class,
                    meta_data=meta_data,
                    weight=0,
                    order=i,
                    developer=test.developer,
                )
                question.weight = TestQuestion.calculate_weight(question, test.section)
                question.save()

                paragraph = TestParagraph.objects.create(
                    paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
                    meta_data={"text": ""},
                )
                TestParagraphQuestion.objects.create(
                    question=question,
                    paragraph=paragraph,
                    order=0,
                )

        return test

    def save(self, developer, commit=True):
        test = super().save(commit=False)
        test.developer = developer

        while True:
            test.code = "%04x" % randint(0x0000, 0xffff)
            if not Test.objects.filter(code=test.code).exists():
                break

        if commit:
            test.save()
        return test


class TestSendForm(ModelForm):
    class Meta:
        model = Test
        fields = ()

    def save(self, commit=True):
        test = super().save(commit=False)
        test.status = Test.STATUS_PENDING
        if commit:
            test.save()
        return test


class TestCheckForm(ModelForm):
    error_messages = {
        "nis_answer_class":             pgettext_lazy("Validation error", "Answer types should only be Multichoice with one answer."),
        "unt_compulsory_answer_class":  pgettext_lazy("Validation error", "Answer types should only be Multichoice with one answer."),
        "unt_profile_answer_class":     pgettext_lazy("Validation error", "There should be 20 answers of type Multichoice with one answer and 10 answers of type Multichoice with one or more answers."),
        "taxonomy":                     npgettext_lazy(
                                            "Validation error",
                                            "There has to be %(count)s question in taxonomy: %(taxonomy)s.",
                                            "There has to be %(count)s questions in taxonomy: %(taxonomy)s.",
                                            "count",
                                        ),
        "topic":                        npgettext_lazy(
                                            "Validation error",
                                            "There has to be %(count)s question in topic: %(topic)s.",
                                            "There has to be %(count)s questions in topic: %(topic)s.",
                                            "count",
                                        ),
        "difficulty": {
            TestQuestion.DIFFICULTY_HIGH:    npgettext_lazy(
                                                 "Validation error",
                                                 "There has to be %(count)s high difficulty question.",
                                                 "There has to be %(count)s high difficulty questions.",
                                                 "count",
                                             ),
            TestQuestion.DIFFICULTY_NORMAL:  npgettext_lazy(
                                                 "Validation error",
                                                 "There has to be %(count)s normal difficulty question.",
                                                 "There has to be %(count)s normal difficulty questions.",
                                                 "count",
                                             ),
            TestQuestion.DIFFICULTY_LOW:     npgettext_lazy(
                                                 "Validation error",
                                                 "There has to be %(count)s low difficulty question.",
                                                 "There has to be %(count)s low difficulty questions.",
                                                 "count",
                                             ),
        },
    }

    class Meta:
        model = Test
        fields = ()

    def save(self, commit=True):
        return self.instance

    def clean(self):
        questions_queryset = self.instance.questions.select_related("taxonomy", "topic")
        if self.instance.section.is_nis():
            if self.instance.section.pk == 9540:
                self.__clean_nis_mathematics(questions_queryset)
            elif self.instance.section.pk in (9541, 9542, 9543):
                self.__clean_nis_language(questions_queryset)
            elif self.instance.section.pk == 9544:
                self.__clean_nis_quantitative(questions_queryset)
        elif self.instance.section.is_unt_compulsory() or self.instance.section.is_unt_profile():
            if self.instance.section.is_unt_compulsory():
                self.__clean_unt_compulsory(questions_queryset)
            elif self.instance.section.is_unt_profile():
                self.__clean_unt_profile(questions_queryset)
        return self.cleaned_data

    def __clean_nis_mathematics(self, questions_queryset):
        questions_queryset = questions_queryset.all()

        for question in questions_queryset:
            if question.answer_class != TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                self.add_error(None, ValidationError(
                    self.error_messages["nis_answer_class"],
                    code="incomplete",
                ))
                break

        taxonomy_counts = {}
        for taxonomy in self.instance.section.taxonomies.order_by("through"):
            if taxonomy.pk == 3529:
                taxonomy_counts[taxonomy] = { "required": 24, "count": 0 }
            elif taxonomy.pk == 3530:
                taxonomy_counts[taxonomy] = { "required": 16, "count": 0 }
        topic_counts = {}
        for topic in self.instance.section.topics.order_by("through"):
            if topic.pk in (5156, 5158, 5160, 5161):
                topic_counts[topic] = { "required": 6, "count": 0 }
            elif topic.pk in (5157, 5159, 5162, 5163):
                topic_counts[topic] = { "required": 4, "count": 0 }
        difficulty_counts = {
            TestQuestion.DIFFICULTY_HIGH:    { "required": 10, "count": 0 },
            TestQuestion.DIFFICULTY_NORMAL:  { "required": 20, "count": 0 },
            TestQuestion.DIFFICULTY_LOW:     { "required": 10, "count": 0 },
        }
        for question in questions_queryset:
            if question.taxonomy is not None:
                taxonomy_counts[question.taxonomy]["count"] += 1
            if question.topic is not None:
                topic_counts[question.topic]["count"] += 1
            difficulty_counts[question.difficulty]["count"] += 1
        for taxonomy, stats in taxonomy_counts.items():
            if stats["required"] != stats["count"]:
                self.add_error(None, ValidationError(
                    self.error_messages["taxonomy"],
                    code="incomplete",
                    params={ "taxonomy": _(taxonomy.name), "count": stats["required"] },
                ))
        for topic, stats in topic_counts.items():
            if stats["required"] != stats["count"]:
                self.add_error(None, ValidationError(
                    self.error_messages["topic"],
                    code="incomplete",
                    params={ "topic": _(topic.name), "count": stats["required"] },
                ))
        for difficulty, stats in difficulty_counts.items():
            if stats["required"] != stats["count"]:
                self.add_error(None, ValidationError(
                    self.error_messages["difficulty"][difficulty],
                    code="incomplete",
                    params={ "count": stats["required"] },
                ))

    def __clean_nis_language(self, questions_queryset):
        questions_queryset = questions_queryset.prefetch_related("paragraphs").all()

        for question in questions_queryset:
            if question.answer_class != TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                self.add_error(None, ValidationError(
                    self.error_messages["nis_answer_class"],
                    code="incomplete",
                ))
                break

        # DARK_TODO  we also have to somehow check for shared texts
        taxonomy_counts = {}
        for taxonomy in self.instance.section.taxonomies.order_by("through"):
            if taxonomy.pk == 3531:
                taxonomy_counts[taxonomy] = { "required": 13, "count": 0 }
            elif taxonomy.pk == 3532:
                taxonomy_counts[taxonomy] = { "required": 5, "count": 0 }
            elif taxonomy.pk == 3533:
                taxonomy_counts[taxonomy] = { "required": 2, "count": 0 }
        difficulty_counts = {
            TestQuestion.DIFFICULTY_HIGH:    { "required": 5, "count": 0 },
            TestQuestion.DIFFICULTY_NORMAL:  { "required": 10, "count": 0 },
            TestQuestion.DIFFICULTY_LOW:     { "required": 5, "count": 0 },
        }
        for question in questions_queryset:
            if question.taxonomy is not None:
                taxonomy_counts[question.taxonomy]["count"] += 1
            difficulty_counts[question.difficulty]["count"] += 1
        for taxonomy, stats in taxonomy_counts.items():
            if stats["required"] != stats["count"]:
                self.add_error(None, ValidationError(
                    self.error_messages["taxonomy"],
                    code="incomplete",
                    params={ "taxonomy": _(taxonomy.name), "count": stats["required"] },
                ))
        for difficulty, stats in difficulty_counts.items():
            if stats["required"] != stats["count"]:
                self.add_error(None, ValidationError(
                    self.error_messages["difficulty"][difficulty],
                    code="incomplete",
                    params={ "count": stats["required"] },
                ))

    def __clean_nis_quantitative(self, questions_queryset):
        questions_queryset = questions_queryset.all()

        for question in questions_queryset:
            if question.answer_class != TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                self.add_error(None, ValidationError(
                    self.error_messages["nis_answer_class"],
                    code="incomplete",
                ))
                break

        topic_counts = {}
        for topic in self.instance.section.topics.order_by("through"):
            if topic.pk in (5164, 5165, 5166, 5167):
                topic_counts[topic] = { "required": 5, "count": 0 }
            elif topic.pk in (5163, 5171, 5172, 5173):
                topic_counts[topic] = { "required": 4, "count": 0 }
            elif topic.pk in (5174, 5175):
                topic_counts[topic] = { "required": 2, "count": 0 }
        difficulty_counts = {
            TestQuestion.DIFFICULTY_HIGH:    { "required": 15, "count": 0 },
            TestQuestion.DIFFICULTY_NORMAL:  { "required": 30, "count": 0 },
            TestQuestion.DIFFICULTY_LOW:     { "required": 15, "count": 0 },
        }
        for question in questions_queryset:
            if question.topic is not None:
                topic_counts[question.topic]["count"] += 1
            difficulty_counts[question.difficulty]["count"] += 1
        for topic, stats in taxonomy_counts.items():
            if stats["required"] != stats["count"]:
                self.add_error(None, ValidationError(
                    self.error_messages["topic"],
                    code="incomplete",
                    params={ "topic": _(topic.name), "count": stats["required"] },
                ))
        for difficulty, stats in difficulty_counts.items():
            if stats["required"] != stats["count"]:
                self.add_error(None, ValidationError(
                    self.error_messages["difficulty"][difficulty],
                    code="incomplete",
                    params={ "count": stats["required"] },
                ))

    def __clean_unt_compulsory(self, questions_queryset):
        questions_queryset = questions_queryset.all()

        for question in questions_queryset:
            if question.answer_class != TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                self.add_error(None, ValidationError(
                    self.error_messages["unt_compulsory_answer_class"],
                    code="incomplete",
                ))
                break

        difficulty_counts = {
            TestQuestion.DIFFICULTY_HIGH:    { "required": 5, "count": 0 },
            TestQuestion.DIFFICULTY_NORMAL:  { "required": 5, "count": 0 },
            TestQuestion.DIFFICULTY_LOW:     { "required": 10, "count": 0 },
        }
        for question in questions_queryset:
            difficulty_counts[question.difficulty]["count"] += 1
        for difficulty, stats in difficulty_counts.items():
            if stats["required"] != stats["count"]:
                self.add_error(None, ValidationError(
                    self.error_messages["difficulty"][difficulty],
                    code="incomplete",
                    params={ "count": stats["required"] },
                ))

    def __clean_unt_profile(self, questions_queryset):
        questions_queryset = questions_queryset.all()

        multichoice_one = 20
        multichoice_multi = 10
        for question in questions_queryset:
            is_found = False
            if question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                is_found = True
                multichoice_one -= 1
            elif question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI:
                is_found = True
                multichoice_multi -= 1
            if not is_found or multichoice_one < 0 or multichoice_multi < 0:
                self.add_error(None, ValidationError(
                    self.error_messages["unt_profile_answer_class"],
                    code="incomplete",
                ))
                break

        difficulty_counts = {
            TestQuestion.DIFFICULTY_HIGH:    { "required": 7, "count": 0 },
            TestQuestion.DIFFICULTY_NORMAL:  { "required": 8, "count": 0 },
            TestQuestion.DIFFICULTY_LOW:     { "required": 15, "count": 0 },
        }
        for question in questions_queryset:
            difficulty_counts[question.difficulty]["count"] += 1
        for difficulty, stats in difficulty_counts.items():
            if stats["required"] != stats["count"]:
                self.add_error(None, ValidationError(
                    self.error_messages["difficulty"][difficulty],
                    code="incomplete",
                    params={ "count": stats["required"] },
                ))
