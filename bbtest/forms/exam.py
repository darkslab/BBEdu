from django.forms import ModelForm
from django.utils.translation import pgettext_lazy
from django.core.exceptions import ValidationError
from bbtest.models import Quiz, TestQuestion
from bbtest.utils.json import tight_dumps


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
                raise ValueError(f"Incorrect report, place 01|{report}")
            if not isinstance(report["answers"], list):
                raise ValueError(f'Incorrect report, place 02|{report}')

            for i, question in enumerate(self.__test.questions.order_by("testtoquestionrelation").all()):
                answer_report = {}
                if not isinstance(report["answers"][i], dict):
                    raise ValueError(f'Incorrect report, place 03|{report}')

                answer_report["answer"] = None
                if report["answers"][i]["answer"] is not None:
                    if not isinstance(report["answers"][i]["answer"], dict):
                        raise ValueError(f'Incorrect report, place 04|{report}')

                    answer = {}
                    if question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                        answer = {
                            "correct_id": int(report["answers"][i]["answer"]["correct_id"]),
                        }
                        if answer["correct_id"] not in [ choice["id"] for choice in question.meta_data["choices"] ]:
                            raise ValueError(f'Incorrect report, place 05|{report}')

                    elif question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI:
                        if not isinstance(report["answers"][i]["answer"]["correct_ids"], list):
                            raise ValueError(f'Incorrect report, place 06|{report}')
                        answer = {
                            "correct_ids": list(set([ int(correct_id) for correct_id in report["answers"][i]["answer"]["correct_ids"] ])),
                        }
                        if not len(answer["correct_ids"]):
                            raise ValueError(f'Incorrect report, place 07|{report}')
                        if len(set(answer["correct_ids"]) - set([ choice["id"] for choice in question.meta_data["choices"] ])):
                            raise ValueError(f'Incorrect report, place 08|{report}')

                    else:
                        raise ValueError('Incorrect report, wrong TestQuestion.ANSWER_CLASS')
                    answer_report["answer"] = answer

                answer_report["observation"] = self.__clean_answer_observation(report["answers"][i]["observation"])
                cleaned_report["answers"].append(answer_report)

            cleaned_report["observation"] = self.__clean_report_observation(report["observation"])

        except (KeyError, IndexError, ValueError, TypeError) as e:
            raise ValidationError(
                str(e),  # self.error_messages["incorrect"] + 
                code="incorrect",
            ) from e
        return cleaned_report

    def __clean_report_observation(self, observation):
        try:
            if not isinstance(observation, dict):
                raise ValueError('Incorrect report, __clean_report_observation')
            if len(observation):
                raise ValueError('Incorrect report, __clean_report_observation')

        except ValueError:
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return observation

    def __clean_answer_observation(self, observation):
        try:
            if not isinstance(observation, dict):
                raise ValueError('Incorrect report, __clean_answer_observation, isinstance')
            if len(observation):
                raise ValueError('Incorrect report, __clean_answer_observation, len')

        except ValueError:
            raise ValidationError(
                self.error_messages["incorrect"],
                code="incorrect",
            )
        return observation
