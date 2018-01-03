from django.views.generic import View, TemplateView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _, pgettext, get_language
from django.urls import reverse
from django.contrib.messages import success
from json import loads
from bbtest.auth.mixins import DeveloperLoginRequiredMixin
from bbtest.models import TestQuestion, TestDomain, Test, DeveloperAcknowledgement, TestParagraph
from bbtest.forms.test import TestQuestionForm, TestParagraphsContainerForm, TestForm
from bbtest.utils.json import tight_dumps
from bbtest.http import TightJsonResponse


def get_test_or_404(user, code):
    return get_object_or_404(user.tests.select_related("section"), code=code)


class TestsView(DeveloperLoginRequiredMixin, FormView):
    template_name = "developer/tests.html"
    form_class = TestForm

    def get(self, request, *args, **kwargs):
        if not self.__is_acknowledgement_accepted():
            return redirect("bbtest:developer_acknowledgement")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.__is_acknowledgement_accepted():
            return redirect("bbtest:developer_acknowledgement")
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["empty_language_code"] = Test.LANGUAGE_XX

        kwargs["nis"] = get_object_or_404(TestDomain.objects.prefetch_related("sections"), pk=7911)
        kwargs["nis_data"] = []
        for section in kwargs["nis"].sections.all():
            data = {
                "section": section,
                "specification": None,
                "languages_title": None,
                "languages": [],
            }

            if section.id in (9540, 9544):
                data["languages_title"] = pgettext("/developer/tests/", "Choose test language")
                for language in Test.LANGUAGES:
                    if language[0] == Test.LANGUAGE_XX:
                        continue
                    data["languages"].append(language)
            elif section.id == 9541:
                data["languages_title"] = pgettext("/developer/tests/", "Choose type")
                data["languages"].append((Test.LANGUAGE_KK, pgettext("Test language", "Kazakh 1")))
                data["languages"].append((Test.LANGUAGE_RU, pgettext("Test language", "Kazakh 2")))
            elif section.id == 9542:
                data["languages_title"] = pgettext("/developer/tests/", "Choose type")
                data["languages"].append((Test.LANGUAGE_RU, pgettext("Test language", "Russian 1")))
                data["languages"].append((Test.LANGUAGE_KK, pgettext("Test language", "Russian 2")))

            if section.specification and get_language() in section.specification:
                data["specification"] = section.specification[get_language()]

            kwargs["nis_data"].append(data)

        kwargs["unt"] = get_object_or_404(TestDomain.objects, pk=7912)

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self._test = form.create_test_suite(self.request.user)
        success(self.request, pgettext("Success alert message", "You have created a new Test."))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("bbtest:developer_test", kwargs={ "code": self._test.code })

    def __is_acknowledgement_accepted(self):
        return DeveloperAcknowledgement.objects.filter(developer=self.request.user).exists()


class TestView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/test.html"

    def get_context_data(self, **kwargs):
        kwargs["test"] = get_test_or_404(self.request.user, kwargs.get("code"))
        kwargs["section_name"] = _(kwargs["test"].section.name)
        question_ids = []
        for data in kwargs["test"].questions.values("id").order_by("order"):
            question_ids.append(data["id"])
        kwargs["question_ids"] = tight_dumps(question_ids)
        return super().get_context_data(**kwargs)


class TestDeleteView(DeveloperLoginRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        test = get_object_or_404(request.user.tests(manager="drafts").prefetch_related("questions__paragraphs"), code=code)
        paragraph_ids = []
        for question in test.questions.all():
            for paragraph in question.paragraphs.all():
                paragraph_ids.append(paragraph.id)
        TestParagraph.objects.filter(pk__in=paragraph_ids).delete()
        test.delete()

        success(request, pgettext("Success alert message", "You have deleted a Test."))
        return redirect("bbtest:developer_dashboard")


class QuestionView(DeveloperLoginRequiredMixin, View):
    def get(self, request, code, question_id, *args, **kwargs):
        test = get_object_or_404(request.user.tests, code=code)
        question = get_object_or_404(test.questions, pk=question_id)

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
        test = get_object_or_404(request.user.tests, code=code)
        question = get_object_or_404(test.questions, pk=question_id)

        form = TestQuestionForm(data=request.POST, instance=question)
        if form.is_valid():
            form.save()
            return TightJsonResponse({"success": True})

        return TightJsonResponse({
            "success": False,
            "errors": loads(form.errors.as_json()),
        }, status=400)


class ParagraphsView(DeveloperLoginRequiredMixin, View):
    def post(self, request, code, question_id, *args, **kwargs):
        test = get_object_or_404(request.user.tests, code=code)
        question = get_object_or_404(test.questions, pk=question_id)

        form = TestParagraphsContainerForm(question, data=request.POST)
        if form.is_valid():
            form.save_paragraphs()
            return TightJsonResponse({"success": True})

        return TightJsonResponse({
            "success": False,
            "errors": loads(form.errors.as_json()),
        }, status=400)


class AttributesView(DeveloperLoginRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        test = get_test_or_404(request.user, code)
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
