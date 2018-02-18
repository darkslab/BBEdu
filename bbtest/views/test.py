from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _, pgettext, get_language
from django.urls import reverse_lazy
from django.contrib.messages import success
from django.db.models import Prefetch
from django.http import Http404
from json import loads
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, SuperPermissionRequiredMixin
from .generic import View, TemplateView, FormView
from bbtest.utils.json import tight_dumps
from bbtest.models.upload import expiring_url
from bbtest.models import TestQuestion, Test, TestParagraph
from bbtest.http import TightJsonResponse
from bbtest.forms.test import TestQuestionForm, TestParagraphsContainerForm, TestSendForm
from bbtest.jobs.upload import image_paragraph_destroyer


def get_test_for_edit_or_404(request, code, include_section=False, include_paragraphs=False):
    if request.user.has_perm("bbtest.super"):
        tests = Test.worked_tests.select_related("developer")
    else:
        tests = request.user.tests(manager="draft_tests")
    if include_section:
        tests = tests.select_related("section")
    if include_paragraphs:
        tests = tests.prefetch_related("questions__paragraphs")
    test = get_object_or_404(
        tests,
        code=code,
    )
    if request.user.has_perm("bbtest.super"):
        if not test.developer.has_perm("bbtest.super") and not test.is_pending():
            raise Http404("Superusers can only edit tests of other developers that are in pending status")
        if test.developer.has_perm("bbtest.super") and not test.is_draft():
            raise Http404("Superusers can only edit tests of other superusers (and their own) that are in draft status")
    return test

def get_test_for_preview_or_404(request, code):
    if request.user.has_perm("bbtest.super"):
        tests = Test.objects
    else:
        tests = request.user.tests(manager="active_tests")
    tests = tests.select_related("section")
    return get_object_or_404(
        tests,
        code=code,
    )


class TestView(DeveloperPermissionRequiredMixin, TemplateView):
    template_name = "test/test.html"

    def get_context_data(self, **kwargs):
        test = get_test_for_edit_or_404(self.request, self.kwargs["code"], include_section=True)

        kwargs["code"] = self.kwargs["code"]
        kwargs["section_name"] = _(test.section.name)
        kwargs["specification"] = test.section.specification[test.language][get_language()]
        question_ids = []
        for data in test.questions.values("id").order_by("order"):
            question_ids.append(data["id"])
        kwargs["question_ids"] = tight_dumps(question_ids)
        return super().get_context_data(**kwargs)


class TestQuestionView(DeveloperPermissionRequiredMixin, View):
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
        test = get_test_for_edit_or_404(request, code)
        return get_object_or_404(test.questions, pk=question_id)


class TestParagraphsView(DeveloperPermissionRequiredMixin, View):
    def post(self, request, code, question_id, *args, **kwargs):
        test = get_test_for_edit_or_404(request, code)
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


class TestAttributesView(DeveloperPermissionRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        test = get_test_for_edit_or_404(request, code, include_section=True)
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


class ApproveTestView(SuperPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        test = get_object_or_404(Test.worked_tests.select_related("developer"), code=code)
        if not test.developer.has_perm("bbtest.super") and test.is_draft():
            raise Http404("Superusers cannot approve draft tests of other developers")

        test.status = Test.STATUS_APPROVED
        test.save()

        success(request, pgettext("Success alert message", "You have approved a Test."))
        return redirect("bbtest:dashboard")


class RefuseTestView(SuperPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        test = get_object_or_404(Test.pending_tests.select_related("developer"), code=code)
        if test.developer.has_perm("bbtest.super"):
            raise Http404("Superusers can only refuse tests of other developers")

        test.status = Test.STATUS_DRAFT
        test.save()

        success(request, pgettext("Success alert message", "You have refused a Test."))
        return redirect("bbtest:dashboard")


class DeleteTestView(DeveloperPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        test = get_test_for_edit_or_404(request, code, include_paragraphs=True)
        if request.user.has_perm("bbtest.super"):
            if test.developer != request.user:
                raise Http404("Superusers can only delete their own tests")

        paragraph_ids = []
        for question in test.questions.all():
            for paragraph in question.paragraphs.all():
                paragraph_ids.append(paragraph.id)

                if paragraph.paragraph_class == TestParagraph.PARAGRAPH_CLASS_IMAGE:
                    image_paragraph_destroyer.delay(paragraph.meta_data["asset_uuid"])

        TestParagraph.objects.filter(pk__in=paragraph_ids).delete()
        test.delete()

        success(request, pgettext("Success alert message", "You have deleted a Test."))
        return redirect("bbtest:dashboard")


class TestPreviewView(DeveloperPermissionRequiredMixin, FormView):
    template_name = "test/test_preview.html"
    form_class = TestSendForm
    success_url = reverse_lazy("bbtest:dashboard")

    def get(self, request, *args, **kwargs):
        self._test = get_test_for_preview_or_404(request, self.kwargs["code"])
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self._test = get_test_for_preview_or_404(request, self.kwargs["code"])
        if request.user.has_perm("bbtest.super"):
            raise Http404("Superusers cannot send tests for approval")
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


class TestPreviewDataView(DeveloperPermissionRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        test = get_test_for_preview_or_404(request, code)
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
