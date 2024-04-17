from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext as _, pgettext, get_language
from django.urls import reverse_lazy, reverse
from django.contrib.messages import success, error
from django.db.models import Prefetch
from django.http import Http404
from json import loads
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, SuperPermissionRequiredMixin, ExpertPermissionRequiredMixin, StaffPermissionRequiredMixin, AdminPermissionRequiredMixin
from .generic import View, TemplateView, FormView, RedirectView
from .common import UserContextMixin, inject_standalone_question_and_report_into_started_response
from bbtest.utils.json import tight_dumps
from bbtest.models.upload import expiring_url
from bbtest.models import TestQuestion, Test, TestParagraph, QuestionComments
from bbtest.http import TightJsonResponse
from bbtest.forms.test import TestQuestionForm, TestParagraphsContainerForm, QuestionCheckForm, QuestionSendForm, QuestionCommentForm
from bbtest.jobs.upload import image_paragraph_destroyer
from bbtest.texts import inject_texts_into_response, test_specification, inject_texts_into_question_response


def get_question_for_edit_or_404(request, code, include_section=False, include_paragraphs=False):
    if request.user.has_perm("bbtest.super") or request.user.has_perm("bbtest.expert"):
        questions = TestQuestion.worked_questions.select_related("developer")
    elif request.user.has_perm("bbtest.developer"): 
        questions = request.user.questions.filter(status__lt=TestQuestion.STATUS_APPROVED)
    else:
        raise Http404("You do not have permission to edit questions")
    
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
        raise Http404("You do not have permission to preview questions")
    questions = questions.select_related("section")
    return get_object_or_404(
        questions,
        code=code,   # TODO: create code field
    )

def get_question_for_check_or_404(request, code):
    if request.user.has_perm("bbtest.super") or request.user.has_perm("bbtest.expert"):
        questions = TestQuestion.worked_questions
    else:
        questions = request.user.questions(manager="in_development_questions")
    return get_object_or_404(questions, code=code)


class TestsView(StaffPermissionRequiredMixin, UserContextMixin, RedirectView):  # TODO
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return reverse("bbtest:super_tests")
        return reverse("bbtest:developer_dashboard")


class StandaloneQuestionQuestionView(StaffPermissionRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        # print("StandaloneQuestionQuestionView", kwargs)
        question = get_question_for_edit_or_404(request, code)
        # question = get_object_or_404(question.questions, pk=question_id)
        # print("StandaloneQuestionQuestionView", question)
        question.meta_data["question_code"] = question.code
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

        inject_texts_into_question_response(question_data, question)

        # DARK_TODO  add "success" to response
        return TightJsonResponse(question_data)

    def post(self, request, code, *args, **kwargs):
        question = get_question_for_edit_or_404(request, code)
        # question = get_object_or_404(question.questions, pk=question_id)

        form = TestQuestionForm(data=request.POST, instance=question)
        if not form.is_valid():
            return TightJsonResponse({
                "success": False,
                "errors": loads(form.errors.as_json()),
            }, status=400)

        test_question = form.save()
        new_weight = TestQuestion.calculate_weight(test_question)
        if new_weight is not None:
            test_question.weight = new_weight
            test_question.save()
        return TightJsonResponse({"success": True})


class StandaloneQuestionParagraphsView(StaffPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        question = get_question_for_edit_or_404(request, code)

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


class StandaloneQuestionAttributesView(StaffPermissionRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        question = get_question_for_edit_or_404(request, code, include_section=True)
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
        for taxonomy in question.section.taxonomies.order_by("through"):
            attributes_data["taxonomies"].append({
                "value": taxonomy.id,
                "caption": str(_(str(taxonomy))),
            })
        for topic in question.section.topics.order_by("through"):
            attributes_data["topics"].append({
                "value": topic.id,
                "caption": str(_(str(topic))),
            })
        for subtopic in question.section.subtopics.order_by("through"):
            attributes_data["subtopics"].append({
                "value": subtopic.id,
                "caption": str(_(str(subtopic))),
            })
        
        for goal in question.section.goals.order_by("through"):
            attributes_data["goals"].append({
                "value": goal.id,
                "caption": str(_(str(goal))),
            })
        # DARK_TODO  add "success" to response
        return TightJsonResponse(attributes_data)


class ApproveQuestionView(ExpertPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        question = get_object_or_404(TestQuestion.worked_questions.select_related("developer"), code=code)
        if not question.developer.has_perm("bbtest.super") and question.is_draft():
            raise Http404("Superusers cannot approve draft questions of other developers")

        form = QuestionCheckForm(instance=question, data={})
        skip = False
        if "skip_check" in request.POST and request.POST["skip_check"] == "true":
            skip = True
        if not form.is_valid() and not skip:
            error(request, pgettext("Error alert message", "Could not approve the Question. Please check the Question for correctness."))
            return redirect("bbtest:build_standalone_question_preview", code=question.code)

        question.status = TestQuestion.STATUS_APPROVED
        question.save()

        success(request, pgettext("Success alert message", "You have approved the Question."))
        return redirect("bbtest:questions")


class RefuseQuestionView(StaffPermissionRequiredMixin, View): # TODO
    def post(self, request, code, *args, **kwargs):
        question = get_object_or_404(TestQuestion.objects.select_related("developer"), code=code)  # pending_questions
        if question.developer.has_perm("bbtest.super"):
            raise Http404("Superusers can only refuse questions of other developers")

        question.status = TestQuestion.STATUS_REDO
        question.save()

        success(request, pgettext("Success alert message", "You have refused the Question."))
        return redirect("bbtest:questions")


class DeleteQuestionView(StaffPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        question = get_question_for_edit_or_404(request, code, include_paragraphs=True)
        if request.user.has_perm("bbtest.super"):
            if question.developer != request.user:
                raise Http404("Superusers can only delete their own questions")

        # paragraph_ids = []
        # for question in test.questions.order_by("testtoquestionrelation").all():
        #     for paragraph in question.paragraphs.all():
        #         paragraph_ids.append(paragraph.id)

        #         if paragraph.paragraph_class == TestParagraph.PARAGRAPH_CLASS_IMAGE:
        #             image_paragraph_destroyer.delay(paragraph.meta_data["asset_uuid"])

        # TestParagraph.objects.filter(pk__in=paragraph_ids).delete()
        # test.delete()
        
        question.status = TestQuestion.STATUS_ARCHIVED
        question.save()
            

        success(request, pgettext("Success alert message", "You have deleted the Question."))
        return redirect("bbtest:questions")


class ReDraftQuestionView(ExpertPermissionRequiredMixin, View):  # DeveloperPermissionRequiredMixin, 
    def post(self, request, code, *args, **kwargs):
        question = get_object_or_404(TestQuestion.production_question.select_related("developer"), code=code)
        question.status = TestQuestion.STATUS_REDO
        question.save()
        success(request, pgettext("Success alert message", "Question is now draft again."))
        return redirect("bbtest:questions")


class ReApproveQuestionView(ExpertPermissionRequiredMixin, View): # DeveloperPermissionRequiredMixin,
    def post(self, request, code, *args, **kwargs):
        question = get_object_or_404(TestQuestion.production_question.select_related("developer"), code=code)
        question.status = TestQuestion.STATUS_APPROVED
        question.save()
        success(request, pgettext("Success alert message", "Question is now approved again."))
        return redirect("bbtest:questions")

class ActivateQuestionView(AdminPermissionRequiredMixin, View): # DeveloperPermissionRequiredMixin,
    def post(self, request, code, *args, **kwargs):
        question = get_object_or_404(TestQuestion.production_question.select_related("developer"), code=code)
        question.status = TestQuestion.STATUS_ACTIVE
        question.save()
        success(request, pgettext("Success alert message", "Question is active now."))
        return redirect("bbtest:questions")

class DeactivateQuestionView(AdminPermissionRequiredMixin, View): # DeveloperPermissionRequiredMixin,
    def post(self, request, code, *args, **kwargs):
        question = get_object_or_404(TestQuestion.active_questions.select_related("developer"), code=code)
        question.status = TestQuestion.STATUS_APPROVED
        question.save()
        success(request, pgettext("Success alert message", "Question is deactivated."))
        return redirect("bbtest:questions")

# class ToggleFreeTestView(SuperPermissionRequiredMixin, View):
#     def post(self, request, code, free, *args, **kwargs):
#         test = get_object_or_404(Test.production_tests.select_related("developer"), code=code)
#         if free == "true":
#             free = True
#         else:
#             free = False
#         if free:
#             test.is_free = True
#         else:
#             test.is_free = False
#         test.save()
#         if free:
#             success(request, pgettext("Success alert message", "Test is now free."))
#         else:
#             success(request, pgettext("Success alert message", "Test is now paid."))
#         if "r" in self.request.GET:
#             return redirect(self.request.GET["r"])
#         return redirect("bbtest:build_test_preview", code=test.code)


class CheckQuestionView(StaffPermissionRequiredMixin, View):
    def post(self, request, code, *args, **kwargs):
        question = get_question_for_check_or_404(request, code)
        response = {
            "success": True,
        }
        form = QuestionCheckForm(instance=question, data=request.POST)
        if not form.is_valid():
            response["success"] = False
            response["errors"] = loads(form.errors.as_json())
        return TightJsonResponse(response)


class StandaloneQuestionView(StaffPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "test/standalone_question.html"

    def get_context_data(self, **kwargs):
        # print("StandaloneQuestionView.get_context_data", self.kwargs)
        question = get_question_for_edit_or_404(self.request, self.kwargs["code"], include_section=True)
        # print("StandaloneQuestionView.get_context_data", question)

        kwargs["question"] = question
        kwargs["code"] = self.kwargs["code"]
        kwargs["section_name"] = _(question.section.name)
        kwargs["domain_name"] = _(question.section.domain.name)
        kwargs["language"] = question.get_lang()
        # if question.language != Test.LANGUAGE_XX:
        #     kwargs["language"] = next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == question.language)
        kwargs["specification"] = test_specification(question.section, kwargs["language"], get_language())

        kwargs["has_periodic_table"] = tight_dumps([question.has_periodic_table])
        kwargs["has_calculator"] = tight_dumps([question.has_calculator])

        # question_ids = []
        # for data in question.questions.values("id").order_by("order"):
        #     question_ids.append(data["id"])
        kwargs["question_ids"] = tight_dumps([question.id])
        # print("StandaloneQuestionView.get_context_data", kwargs)
        return super().get_context_data(**kwargs)
    

class StandaloneQuestionPreviewView(StaffPermissionRequiredMixin, UserContextMixin, FormView):
    template_name = "test/standalone_question_preview.html"
    form_class = QuestionSendForm
    success_url = reverse_lazy("bbtest:questions")  # TODO

    def get(self, request, *args, **kwargs):
        self._question = get_question_for_preview_or_404(request, self.kwargs["code"])
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self._question = get_question_for_preview_or_404(request, self.kwargs["code"])
        if request.user.has_perm("bbtest.super"):
            raise Http404("Superusers cannot send questions for approval")
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["question"] = self._question
        kwargs["code"] = self.kwargs["code"]
        kwargs["section_name"] = _(self._question.section.name)
        kwargs["domain_name"] = _(self._question.section.domain.name)
        kwargs["language"] = self._question.get_lang() 

        kwargs["comments"] = self._question.comments.order_by("-created_at").all() 
        kwargs["comment_form"] = QuestionCommentForm()

        kwargs["has_periodic_table"] = tight_dumps([self._question.has_periodic_table])
        kwargs["has_calculator"] = tight_dumps([self._question.has_calculator])
        
        for comment in kwargs["comments"]:
            for permission in comment.sender.user_permissions.all():
                if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("admin", "developer", "expert", "student"):
                    comment.sender.role = permission.codename
                    break

        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self._question
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


class StandaloneQuestionSendCommentView(StaffPermissionRequiredMixin, View):

    def post(self, request, code, *args, **kwargs):
        # return self.get(request, code, *args, **kwargs)
    
        form = QuestionCommentForm(data=request.POST)
        if form.is_valid():
            
            question = get_question_for_preview_or_404(request, code)

            comment_content = form.cleaned_data["content"]
            print(request.user, comment_content)

            obj = QuestionComments.objects.create(
                sender = request.user,
                question = question,
                content = comment_content,
            )
            question.last_comment_at = obj.created_at
            question.save()

            print("StandaloneQuestionSendCommentView", obj)

        else:
            error(request, "Could not create comment! %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))

        return redirect("bbtest:build_standalone_question_preview", code)


class StandaloneQuestionPreviewDataView(StaffPermissionRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        question = get_question_for_preview_or_404(request, code)
        response = {
            "success": True,
            "status": "started",
            "seconds": question.section.duration,
            "has_periodic_table": [question.has_periodic_table],
            "has_calculator": [question.has_calculator],
        }
        # inject_questions_and_report_into_started_response(response, question)
        inject_standalone_question_and_report_into_started_response(response, question)
        # inject_texts_into_response(response, question)
        inject_texts_into_question_response(response, question)

        return TightJsonResponse(response)

    def post(self, request, code, *args, **kwargs):
        return self.get(request, code, *args, **kwargs)