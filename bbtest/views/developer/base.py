from django.views.generic import View, TemplateView, FormView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.translation import ugettext as _
from json import loads
from bbtest.auth.mixins import DeveloperLoginRequiredMixin
from bbtest.models import TestQuestion, TestDomain, Test
from bbtest.forms.test import TestQuestionForm, TestParagraphsContainerForm, TestForm
from bbtest.utils.json import tight_dumps
from bbtest.http import TightJsonResponse


def get_test_or_404(user, code):
    return get_object_or_404(user.tests.select_related("section"), code=code)


class DashboardView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/dashboard.html"


class TestsView(DeveloperLoginRequiredMixin, FormView):
    template_name = "developer/tests.html"
    form_class = TestForm

    def get_context_data(self, **kwargs):
        kwargs["nis"] = get_object_or_404(TestDomain.objects.prefetch_related("sections"), pk=7911)
        kwargs["unt"] = get_object_or_404(TestDomain.objects, pk=7912)

        kwargs["languages"] = Test.LANGUAGES

        return super().get_context_data(**kwargs)


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
