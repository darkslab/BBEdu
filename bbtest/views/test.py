from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _, pgettext, get_language
from django.urls import reverse_lazy, reverse
from django.contrib.messages import success, error
from django.db.models import Prefetch
from django.http import Http404
from json import loads
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, SuperPermissionRequiredMixin, ExpertPermissionRequiredMixin, StaffPermissionRequiredMixin, AdminPermissionRequiredMixin
from .generic import View, TemplateView, FormView, RedirectView
from .common import UserContextMixin, inject_questions_and_report_into_started_response, inject_standalone_question_and_report_into_started_response
from bbtest.utils.json import tight_dumps
from bbtest.models.upload import expiring_url
from bbtest.models import TestQuestion, Test, TestParagraph
from bbtest.http import TightJsonResponse
from bbtest.forms.test import TestQuestionForm, TestParagraphsContainerForm, TestSendForm, TestCheckForm, QuestionSendForm
from bbtest.jobs.upload import image_paragraph_destroyer
from bbtest.texts import inject_texts_into_response, test_specification, inject_texts_into_question_response


def get_test_for_edit_or_404(request, code, include_section=False, include_paragraphs=False):
    if request.user.has_perm("bbtest.super") or request.user.has_perm("bbtest.expert"):
        tests = Test.worked_tests.select_related("developer")
    elif request.user.has_perm("bbtest.developer"): 
        tests = request.user.tests(manager="in_development_tests") 
    else:
        raise Http404("You do not have permission to edit tests")
    
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
        
    if request.user.has_perm("bbtest.expert"):
        if not test.developer.has_perm("bbtest.expert") and not test.is_pending():
            raise Http404("Experts can only edit tests of other developers that are in pending status")
        if test.developer.has_perm("bbtest.super") and not test.is_draft():
            raise Http404("Experts can only edit tests of other experts (and their own) that are in draft status")
    return test

def get_test_for_preview_or_404(request, code):
    if request.user.has_perm("bbtest.super") or request.user.has_perm("bbtest.expert") or request.user.has_perm("bbtest.admin"):
        tests = Test.objects
    elif request.user.has_perm("bbtest.developer"):
        tests = request.user.tests(manager="production_tests")
    else:
        raise Http404("You do not have permission to preview tests")
    tests = tests.select_related("section")
    return get_object_or_404(
        tests,
        code=code,
    )


def get_question_for_edit_or_404(request, code, include_section=False, include_paragraphs=False):
    if request.user.has_perm("bbtest.super") or request.user.has_perm("bbtest.expert"):
        questions = TestQuestion.select_related("developer")
    elif request.user.has_perm("bbtest.developer"): 
        questions = request.user.questions.filter(status__lt=TestQuestion.STATUS_APPROVED)
    else:
        raise Http404("You do not have permission to edit tests")
    
    if include_section:
        questions = questions.select_related("section")
    if include_paragraphs:
        questions = questions.prefetch_related("questions__paragraphs")
    question = get_object_or_404(
        questions,
        code=code,
    )
    if request.user.has_perm("bbtest.super"):
        if not question.developer.has_perm("bbtest.super") and not question.is_pending():
            raise Http404("Superusers can only edit questions of other developers that are in pending status")
        if question.developer.has_perm("bbtest.super") and not question.is_draft():
            raise Http404("Superusers can only edit questions of other superusers (and their own) that are in draft status")
        
    if request.user.has_perm("bbtest.expert"):
        if not question.developer.has_perm("bbtest.expert") and not question.is_pending():
            raise Http404("Experts can only edit questions of other developers that are in pending status")
        if question.developer.has_perm("bbtest.super") and not question.is_draft():
            raise Http404("Experts can only edit questions of other experts (and their own) that are in draft status")
    return question

def get_question_for_preview_or_404(request, code):
    if request.user.has_perm("bbtest.super") or request.user.has_perm("bbtest.expert") or request.user.has_perm("bbtest.admin"):
        questions = TestQuestion.objects
    elif request.user.has_perm("bbtest.developer"):
        # tests = request.user.tests(manager="production_tests")
        questions = TestQuestion.objects
    else:
        raise Http404("You do not have permission to preview tests")
    questions = questions.select_related("section")
    return get_object_or_404(
        questions,
        code=code,   # TODO: create code field
    )

def get_test_for_check_or_404(request, code):
    if request.user.has_perm("bbtest.super") or request.user.has_perm("bbtest.expert"):
        tests = Test.worked_tests
    else:
        tests = request.user.tests(manager="in_development_tests")
    return get_object_or_404(tests, code=code)


class TestsView(StaffPermissionRequiredMixin, UserContextMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return reverse("bbtest:super_tests")
        return reverse("bbtest:developer_dashboard")


class TestView(StaffPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "test/test.html"

    def get_context_data(self, **kwargs):
        test = get_test_for_edit_or_404(self.request, self.kwargs["code"], include_section=True)

        kwargs["test"] = test
        kwargs["code"] = self.kwargs["code"]
        kwargs["section_name"] = _(test.section.name)
        kwargs["domain_name"] = _(test.section.domain.name)
        kwargs["language"] = None
        if test.language != Test.LANGUAGE_XX:
            kwargs["language"] = next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == test.language)
        kwargs["specification"] = test_specification(test.section, test.language, get_language())
        question_ids = []
        for data in test.questions.values("id").order_by("order"):
            question_ids.append(data["id"])
        kwargs["question_ids"] = tight_dumps(question_ids)
        return super().get_context_data(**kwargs)


class TestQuestionView(StaffPermissionRequiredMixin, View):
    def get(self, request, code, question_id, *args, **kwargs):
        test = get_test_for_edit_or_404(request, code)
        question = get_object_or_404(test.questions, pk=question_id)

        question_data = {
            "id": question.id,
            "data": {
                "answer_class": question.answer_class,
                "meta_data": question.meta_data,
                "difficulty": question.difficulty,
                "taxonomy": question.taxonomy_id,
                "topic": question.topic_id,
                "subtopic": question.subtopic_id,
                "goal": question.goal_id,
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

        inject_texts_into_response(question_data, test)

        # DARK_TODO  add "success" to response
        return TightJsonResponse(question_data)

    def post(self, request, code, question_id, *args, **kwargs):
        test = get_test_for_edit_or_404(request, code)
        question = get_object_or_404(test.questions, pk=question_id)

        form = TestQuestionForm(data=request.POST, instance=question)
        if not form.is_valid():
            return TightJsonResponse({
                "success": False,
                "errors": loads(form.errors.as_json()),
            }, status=400)

        test_question = form.save()
        new_weight = TestQuestion.calculate_weight(test_question, test_question.test.section)
        if new_weight is not None:
            test_question.weight = new_weight
            test_question.save()
        return TightJsonResponse({"success": True})


class TestParagraphsView(StaffPermissionRequiredMixin, View):
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


class TestAttributesView(StaffPermissionRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        test = get_test_for_edit_or_404(request, code, include_section=True)
        attributes_data = {
            "difficulties": [],
            "taxonomies": [],
            "topics": [],
            "subtopics": [],
            "goals": [],
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
        for subtopic in test.section.subtopics.order_by("through"):
            attributes_data["subtopics"].append({
                "value": subtopic.id,
                "caption": str(_(str(subtopic))),
            })
        
        for goal in test.section.goals.order_by("through"):
            attributes_data["goals"].append({
                "value": goal.id,
                "caption": str(_(str(goal))),
            })
        # DARK_TODO  add "success" to response
        return TightJsonResponse(attributes_data)


class ApproveTestView(ExpertPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        test = get_object_or_404(Test.worked_tests.select_related("developer"), code=code)
        if not test.developer.has_perm("bbtest.super") and test.is_draft():
            raise Http404("Superusers cannot approve draft tests of other developers")

        form = TestCheckForm(instance=test, data={})
        skip = False
        if "skip_check" in request.POST and request.POST["skip_check"] == "true":
            skip = True
        if not form.is_valid() and not skip:
            error(request, pgettext("Error alert message", "Could not approve the Test. Please check the Test for correctness."))
            return redirect("bbtest:build_test_preview", code=test.code)

        test.status = Test.STATUS_APPROVED
        test.save()

        success(request, pgettext("Success alert message", "You have approved the Test."))
        return redirect("bbtest:super_tests")


class RefuseTestView(ExpertPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        test = get_object_or_404(Test.pending_tests.select_related("developer"), code=code)
        if test.developer.has_perm("bbtest.super"):
            raise Http404("Superusers can only refuse tests of other developers")

        test.status = Test.STATUS_REDO
        test.save()

        success(request, pgettext("Success alert message", "You have refused the Test."))
        return redirect("bbtest:super_tests")


class DeleteTestView(StaffPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        test = get_test_for_edit_or_404(request, code, include_paragraphs=True)
        if request.user.has_perm("bbtest.super"):
            if test.developer != request.user:
                raise Http404("Superusers can only delete their own tests")

        # paragraph_ids = []
        # for question in test.questions.all():
        #     for paragraph in question.paragraphs.all():
        #         paragraph_ids.append(paragraph.id)

        #         if paragraph.paragraph_class == TestParagraph.PARAGRAPH_CLASS_IMAGE:
        #             image_paragraph_destroyer.delay(paragraph.meta_data["asset_uuid"])

        # TestParagraph.objects.filter(pk__in=paragraph_ids).delete()
        # test.delete()
        
        test.status = Test.STATUS_ARCHIVED
        test.save()
            

        success(request, pgettext("Success alert message", "You have deleted the Test."))
        return redirect("bbtest:build_tests")


class ReDraftTestView(ExpertPermissionRequiredMixin, View):  # DeveloperPermissionRequiredMixin, 
    def post(self, request, code, *args, **kwargs):
        print("sonic", code)
        test = get_object_or_404(Test.production_tests.select_related("developer"), code=code)
        test.status = Test.STATUS_REDO
        test.save()
        success(request, pgettext("Success alert message", "Test is now draft again."))
        return redirect("bbtest:home")


class ReApproveTestView(ExpertPermissionRequiredMixin, View): # DeveloperPermissionRequiredMixin,
    def post(self, request, code, *args, **kwargs):
        test = get_object_or_404(Test.production_tests.select_related("developer"), code=code)
        test.status = Test.STATUS_APPROVED
        test.save()
        success(request, pgettext("Success alert message", "Test is now approved again."))
        return redirect("bbtest:home")

class ActivateTestView(AdminPermissionRequiredMixin, View): # DeveloperPermissionRequiredMixin,
    def post(self, request, code, *args, **kwargs):
        test = get_object_or_404(Test.production_tests.select_related("developer"), code=code)
        test.status = Test.STATUS_ACTIVE
        test.save()
        success(request, pgettext("Success alert message", "Test is active now."))
        return redirect("bbtest:home")

class DeactivateTestView(AdminPermissionRequiredMixin, View): # DeveloperPermissionRequiredMixin,
    def post(self, request, code, *args, **kwargs):
        test = get_object_or_404(Test.active_tests.select_related("developer"), code=code)
        test.status = Test.STATUS_APPROVED
        test.save()
        success(request, pgettext("Success alert message", "Test is deactivated."))
        return redirect("bbtest:home")

class ToggleFreeTestView(SuperPermissionRequiredMixin, View):
    def post(self, request, code, free, *args, **kwargs):
        test = get_object_or_404(Test.production_tests.select_related("developer"), code=code)

        if free == "true":
            free = True
        else:
            free = False

        if free:
            test.is_free = True
        else:
            test.is_free = False
        test.save()

        if free:
            success(request, pgettext("Success alert message", "Test is now free."))
        else:
            success(request, pgettext("Success alert message", "Test is now paid."))
        if "r" in self.request.GET:
            return redirect(self.request.GET["r"])
        return redirect("bbtest:build_test_preview", code=test.code)


class CheckTestView(StaffPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        test = get_test_for_check_or_404(request, code)
        response = {
            "success": True,
        }
        form = TestCheckForm(instance=test, data=request.POST)
        if not form.is_valid():
            response["success"] = False
            response["errors"] = loads(form.errors.as_json())
        return TightJsonResponse(response)


class TestPreviewView(StaffPermissionRequiredMixin, UserContextMixin, FormView):
    template_name = "test/test_preview.html"
    form_class = TestSendForm
    success_url = reverse_lazy("bbtest:build_tests")

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
        kwargs["code"] = self.kwargs["code"]
        kwargs["section_name"] = _(self._test.section.name)
        kwargs["domain_name"] = _(self._test.section.domain.name)
        kwargs["language"] = None
        if self._test.language != Test.LANGUAGE_XX:
            kwargs["language"] = next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == self._test.language)
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self._test
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TestPreviewDataView(StaffPermissionRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        test = get_test_for_preview_or_404(request, code)
        response = {
            "success": True,
            "status": "started",
            "seconds": test.duration,
        }
        inject_questions_and_report_into_started_response(response, test)
        inject_texts_into_response(response, test)
        return TightJsonResponse(response)

    def post(self, request, code, *args, **kwargs):
        return self.get(request, code, *args, **kwargs)

