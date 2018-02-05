from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _, pgettext, get_language
from django.urls import reverse, reverse_lazy
from django.contrib.messages import success
from django.db.models import Prefetch
from json import loads
from bbtest.auth.mixins import DeveloperLoginRequiredMixin
from bbtest.views.generic import View, TemplateView, FormView
from bbtest.models import TestQuestion, TestDomain, Test, TestParagraph
from bbtest.models.upload import expiring_url
from bbtest.forms.test import TestQuestionForm, TestParagraphsContainerForm, TestForm, TestSendForm
from bbtest.utils.json import tight_dumps
from bbtest.http import TightJsonResponse
from .mixins import DeveloperAcknowledgementRequiredMixin


class TestsView(DeveloperLoginRequiredMixin, DeveloperAcknowledgementRequiredMixin, FormView):
    template_name = "developer/tests.html"
    form_class = TestForm
    unaccepted_acknowledgement_redirect_urlpattern = "bbtest:developer_acknowledgement"

    def get_context_data(self, **kwargs):
        kwargs["empty_language_code"] = Test.LANGUAGE_XX

        kwargs["nis"] = get_object_or_404(TestDomain.objects.prefetch_related("sections"), pk=7911)
        kwargs["nis_data"] = []
        for section in kwargs["nis"].sections.all():
            data = {
                "section": section,
                "language": None,
                "specification": {},
            }

            if section.id in (9540, 9544):
                data["language"] = {
                    "title": pgettext("/developer/tests/", "Choose test language"),
                    "choices": [],
                }
                for language in Test.LANGUAGES:
                    if language[0] == Test.LANGUAGE_XX:
                        continue
                    data["language"]["choices"].append(language)
                    data["specification"][language[0]] = section.specification[language[0]][get_language()]

            elif section.id == 9541:
                data["language"] = {
                    "title": pgettext("/developer/tests/", "Choose type"),
                    "choices": [
                        (Test.LANGUAGE_KK, pgettext("Test language", "Kazakh 1")),
                        (Test.LANGUAGE_RU, pgettext("Test language", "Kazakh 2")),
                    ],
                }
                data["specification"][Test.LANGUAGE_KK] = section.specification[Test.LANGUAGE_KK][get_language()]
                data["specification"][Test.LANGUAGE_RU] = section.specification[Test.LANGUAGE_RU][get_language()]

            elif section.id == 9542:
                data["language"] = {
                    "title": pgettext("/developer/tests/", "Choose type"),
                    "choices": [
                        (Test.LANGUAGE_RU, pgettext("Test language", "Russian 1")),
                        (Test.LANGUAGE_KK, pgettext("Test language", "Russian 2")),
                    ],
                }
                data["specification"][Test.LANGUAGE_RU] = section.specification[Test.LANGUAGE_RU][get_language()]
                data["specification"][Test.LANGUAGE_KK] = section.specification[Test.LANGUAGE_KK][get_language()]

            elif section.id == 9543:
                data["specification"][Test.LANGUAGE_XX] = section.specification[Test.LANGUAGE_XX][get_language()]

            kwargs["nis_data"].append(data)

        kwargs["unt"] = get_object_or_404(TestDomain.objects, pk=7912)

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self._test = form.create_test_suite(self.request.user)
        success(self.request, pgettext("Success alert message", "You have created a new Test."))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("bbtest:developer_test", kwargs={ "code": self._test.code })


class TestView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/test.html"

    def get_context_data(self, **kwargs):
        test = get_object_or_404(
            self.request.user.tests(manager="draft_tests").select_related("section"),
            code=self.kwargs["code"],
        )

        kwargs["code"] = self.kwargs["code"]
        kwargs["section_name"] = _(test.section.name)
        kwargs["specification"] = test.section.specification[test.language][get_language()]
        question_ids = []
        for data in test.questions.values("id").order_by("order"):
            question_ids.append(data["id"])
        kwargs["question_ids"] = tight_dumps(question_ids)
        return super().get_context_data(**kwargs)


class TestPreviewView(DeveloperLoginRequiredMixin, FormView):
    template_name = "developer/test_preview.html"
    form_class = TestSendForm
    success_url = reverse_lazy("bbtest:developer_dashboard")

    def get(self, request, *args, **kwargs):
        self._test = get_object_or_404(
            self.request.user.tests(manager="active_tests").select_related("section"),
            code=self.kwargs["code"],
        )
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self._test = get_object_or_404(
            self.request.user.tests(manager="draft_tests").select_related("section"),
            code=self.kwargs["code"],
        )
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["test"] = self._test
        kwargs["questions_count"] = self._test.questions.count()
        kwargs["code"] = self.kwargs["code"]
        kwargs["section_name"] = _(self._test.section.name)
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self._test
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TestPreviewDataView(DeveloperLoginRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        test = get_object_or_404(request.user.tests(manager="active_tests").select_related("section"), code=code)
        data = {
            "seconds_left": test.section.duration,
            "questions": [],
            "answer_submission": {
                "answers": [],
                "observation": {},
            },
        }

        for question in test.questions.prefetch_related(
            Prefetch("paragraphs", queryset=TestParagraph.objects.order_by("through").all()),
        ).all():
            _question = {
                "answer_class": question.answer_class,
                "meta_data": question.meta_data,
                "paragraphs": [],
            }
            for paragraph in question.paragraphs.all():
                if paragraph.paragraph_class == TestParagraph.PARAGRAPH_CLASS_IMAGE:
                    paragraph.meta_data["asset_url"] = expiring_url(paragraph.meta_data["asset_object_name"], expire_in=test.section.duration)

                _paragraph = {
                    "paragraph_class": paragraph.paragraph_class,
                    "meta_data": paragraph.meta_data,
                }
                _question["paragraphs"].append(_paragraph)
            data["questions"].append(_question)

            _answer = {
                "answer": None,
                "observation": {},
            }
            if question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
                if question.meta_data["correct_id"]:
                    _answer["answer"] = {
                        "correct_id": question.meta_data["correct_id"],
                    }
            data["answer_submission"]["answers"].append(_answer)

        return TightJsonResponse(data)


class TestDeleteView(DeveloperLoginRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        test = get_object_or_404(
            request.user.tests(manager="draft_tests").prefetch_related("questions__paragraphs"),
            code=code,
        )
        paragraph_ids = []
        for question in test.questions.all():
            for paragraph in question.paragraphs.all():
                paragraph_ids.append(paragraph.id)
        # DARK_TODO  schedule jobs to delete assets
        TestParagraph.objects.filter(pk__in=paragraph_ids).delete()
        test.delete()

        success(request, pgettext("Success alert message", "You have deleted a Test."))
        return redirect("bbtest:developer_dashboard")


class QuestionView(DeveloperLoginRequiredMixin, View):
    def get(self, request, code, question_id, *args, **kwargs):
        question = self.__question(request, code, question_id)

        question_data = {
            "id": question.id,
            "data": {
                "answer_class": question.answer_class,
                "meta_data": question.meta_data,
                "difficulty": question.difficulty,
                "taxonomy": question.taxonomy_id,
                "topic": question.topic_id,
            },
            "paragraphs": [],
        }
        for paragraph in question.paragraphs.prefetch_related("through").order_by("through"):
            if paragraph.paragraph_class == TestParagraph.PARAGRAPH_CLASS_IMAGE:
                paragraph.meta_data["asset_url"] = expiring_url(paragraph.meta_data["asset_object_name"])

            paragraph_data = {
                "id": paragraph.id,
                "data": {
                    "paragraph_class": paragraph.paragraph_class,
                    "meta_data": paragraph.meta_data,
                },
                "question_ids": []
            }
            for through in paragraph.through.all():
                if through.question_id != question.id:
                    paragraph_data["question_ids"].append(through.question_id)
            question_data["paragraphs"].append(paragraph_data)

        return TightJsonResponse(question_data)

    def post(self, request, code, question_id, *args, **kwargs):
        question = self.__question(request, code, question_id)

        form = TestQuestionForm(data=request.POST, instance=question)
        if not form.is_valid():
            return TightJsonResponse({
                "success": False,
                "errors": loads(form.errors.as_json()),
            }, status=400)

        form.save()
        return TightJsonResponse({"success": True})

    def __question(self, request, code, question_id):
        test = get_object_or_404(request.user.tests(manager="draft_tests"), code=code)
        return get_object_or_404(test.questions, pk=question_id)


class ParagraphsView(DeveloperLoginRequiredMixin, View):
    def post(self, request, code, question_id, *args, **kwargs):
        test = get_object_or_404(request.user.tests(manager="draft_tests"), code=code)
        question = get_object_or_404(test.questions, pk=question_id)

        form = TestParagraphsContainerForm(question, data=request.POST)
        if not form.is_valid():
            return TightJsonResponse({
                "success": False,
                "errors": loads(form.errors.as_json()),
            }, status=400)

        paragraph_morphs = form.save_paragraphs()
        return TightJsonResponse({
            "success": True,
            "update": paragraph_morphs,
        })


class AttributesView(DeveloperLoginRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        test = get_object_or_404(request.user.tests(manager="draft_tests").select_related("section"), code=code)
        attributes_data = {
            "difficulties": [],
            "taxonomies": [],
            "topics": [],
        }

        for difficulty in TestQuestion.DIFFICULTIES:
            attributes_data["difficulties"].append({
                "value": difficulty[0],
                "caption": str(difficulty[1]),
            })
        for taxonomy in test.section.taxonomies.order_by("through"):
            attributes_data["taxonomies"].append({
                "value": taxonomy.id,
                "caption": str(_(str(taxonomy))),
            })
        for topic in test.section.topics.order_by("through"):
            attributes_data["topics"].append({
                "value": topic.id,
                "caption": str(_(str(topic))),
            })

        return TightJsonResponse(attributes_data)
