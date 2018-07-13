from django.forms import ModelForm
from django.utils.translation import pgettext_lazy
from django.core.exceptions import ValidationError
from bbtest.models import Quiz, TestQuestion


class ExamReportForm(ModelForm):
    error_messages = {
        "incorrect": pgettext_lazy("Validation error", "Incorrect report."),
    }

    class Meta:
        model = Quiz
        fields = ("report",)
        error_messages = {
            "report": {
                "required": pgettext_lazy("Validation error", "Please provide report."),
            },
        }

    def __init__(self, test, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__test = test
        self.fields["report"].required = True

    def clean_report(self):
        report = self.cleaned_data["report"]
        cleaned_report = {
            "answers": [],
        }
        try:
            if not isinstance(report, dict):
                raise ValueError("Incorrect report")
            if not isinstance(report["answers"], list):
                raise ValueError("Incorrect report")

            for i, question in enumerate(self.__test.questions.all()):
                answer_report = {}
                if not isinstance(report["answers"][i], dict):
                    raise ValueError("Incorrect report")

                answer_report["answer"] = None
                if report["answers"][i]["answer"] is not None:
                    if not isinstance(report["answers"][i]["answer"], dict):
                        raise ValueError("Incorrect report")

                    answer = {}
                    if question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                        answer = {
                            "correct_id": int(report["answers"][i]["answer"]["correct_id"]),
                        }
                        if answer["correct_id"] not in [ choice["id"] for choice in question.meta_data["choices"] ]:
                            raise ValueError("Incorrect report")

                    elif question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI:
                        if not isinstance(report["answers"][i]["answer"]["correct_ids"], list):
                            raise ValueError("Incorrect report")
                        answer = {
                            "correct_ids": list(set([ int(correct_id) for correct_id in report["answers"][i]["answer"]["correct_ids"] ])),
                        }
                        if len(set(answer["correct_ids"]) - set([ choice["id"] for choice in question.meta_data["choices"] ])):
                            raise ValueError("Incorrect report")

                    else:
                        raise ValueError("Incorrect report")
                    answer_report["answer"] = answer

                answer_report["observation"] = self.__clean_answer_observation(report["answers"][i]["observation"])
                cleaned_report["answers"].append(answer_report)

            cleaned_report["observation"] = self.__clean_report_observation(report["observation"])

        except (KeyError, IndexError, ValueError, TypeError):
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return cleaned_report

    def __clean_report_observation(self, observation):
        try:
            if not isinstance(observation, dict):
                raise ValueError("Incorrect report")
            if len(observation):
                raise ValueError("Incorrect report")

        except ValueError:
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return observation

    def __clean_answer_observation(self, observation):
        try:
            if not isinstance(observation, dict):
                raise ValueError("Incorrect report")
            if len(observation):
                raise ValueError("Incorrect report")

        except ValueError:
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return observation
