from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.translation import ugettext as _
from json import dumps
from bbtest.auth.mixins import DeveloperLoginRequiredMixin
from bbtest.models import TestQuestion


def get_test_or_404(user, code):
    return get_object_or_404(user.tests.select_related("section"), code=code)


class DashboardView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/dashboard.html"


class TestView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/test.html"

    def get_context_data(self, **kwargs):
        kwargs["test"] = get_test_or_404(self.request.user, kwargs.get("code"))
        kwargs["section_name"] = _(kwargs["test"].section.name)
        return super().get_context_data(**kwargs)


class IndexedQuestionView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/indexed_question.txt"
    content_type = "application/json"

    def get_context_data(self, **kwargs):
        test = get_test_or_404(self.request.user, kwargs.get("code"))
        question_index = 0
        if kwargs["question_index"] is not None:
            question_index = int(kwargs["question_index"])
            if question_index < 0 or question_index >= test.section.question_count:
                question_index = 0
        try:
            question = test.questions.all()[question_index]
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
            kwargs["question_data"] = dumps(question_data, separators=(",", ":"))
        except IndexError:
            raise Http404("Could not find test question")

        return super().get_context_data(**kwargs)


class AttributesView(DeveloperLoginRequiredMixin, TemplateView):
    template_name = "developer/attributes.txt"
    content_type = "application/json"

    def get_context_data(self, **kwargs):
        test = get_test_or_404(self.request.user, kwargs.get("code"))
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

        kwargs["attributes_data"] = dumps(attributes_data, separators=(",", ":"))
        return super().get_context_data(**kwargs)
