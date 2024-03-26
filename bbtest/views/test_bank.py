from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, get_object_or_404
from django.contrib.messages import warning, success, error
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.utils.translation import pgettext, gettext_lazy
from django.db.models import Q, F
from django.utils.timezone import now
from django.http import Http404
from django.http import HttpResponse
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.forms.super import  CreateCustomTestSelectionForm, CreateStandaloneQuestionForm
from bbtest.models.test import TestDomain, Test, TestSection, TestQuestion, TestParagraph, TestParagraphQuestion, TestToQuestionRelation
from bbtest.models.quiz import Quiz, QuizSet
from bbtest.http import TightJsonResponse
import uuid
from bbtest.models import User
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, AdminPermissionRequiredMixin, CreateStudentRequiredMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin
from django.core.exceptions import ValidationError
from datetime import datetime
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from random import randint
import json




class BuildSelectTestForAssembleView(AdminPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateResponseMixin, ContextMixin, View):
    template_name = "testbank/test_parameters_create.html"
    
    def get(self, request, *args, **kwargs):

        kwargs['active_nav_item'] = 'testbank'

        domain_set = TestDomain.objects.all()

        CATEGORY_CHOICES = [(None, "-----")]
        for domain_obj in domain_set:
            options = []
            section_list = domain_obj.sections.all()
            for section in section_list:
                options.append((section.pk, gettext_lazy(section.name)))

            if len(options) > 0:
                CATEGORY_CHOICES.append((gettext_lazy(domain_obj.name), tuple(options)))

        
        form = CreateCustomTestSelectionForm(choices = CATEGORY_CHOICES)
        kwargs["select_section_form"] = form

    
        return self.render_to_response(super().get_context_data(**kwargs))
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        question_count, test_duration, section_obj = self.clean(request)

        test = self.create_test_suite(request.user, question_count, test_duration, section_obj)
        print(test)

        # raise Http404("Superusers cannot send tests for approval")
        # return redirect("bbtest:build_assemble_tests")
        return redirect("bbtest:build_assemble_variant", test.code )
    

    def clean(self, request):
        question_count = request.POST["question_count"]
        test_duration = request.POST["test_duration"]
        section_id = request.POST["section"]

        question_count = int(question_count)
        test_duration = int(test_duration) * 60

        section_obj = TestSection.objects.filter(id=section_id)

        assert question_count > 0
        assert test_duration > 0
        assert section_obj.exists()

        section_obj = section_obj[0]

        # print(question_count, test_duration, section_id, section_obj)
        return question_count, test_duration, section_obj


    def create_test_suite(self, developer, question_count, test_duration, section_obj):
        # test = self.save(developer)
        while True:
            code = "%04x" % randint(0x0000, 0xffff)
            if not Test.objects.filter(code=code).exists():
                break

        test = Test.objects.create(
            section = section_obj,
            developer = developer,
            code = code,
            language = section_obj.get_lang(),
            question_count = question_count,
            duration = test_duration,
        )



        print(question_count, test_duration, section_obj, test)

        # shared_paragraph = None
        # for i in range(question_count):
        #     choice_id = 1 
        #     meta_data = {
        #         "choices": [
        #             {"id": choice_id + 0, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
        #             {"id": choice_id + 1, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
        #             {"id": choice_id + 2, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
        #             {"id": choice_id + 3, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
        #         ],
        #         "correct_id": None,
        #     }
        #     # if test.section.id == 9544:
        #     #     meta_data["choices"][0]["meta_data"]["text"] = nis_quantitative_answer(test, "a")
        #     #     meta_data["choices"][1]["meta_data"]["text"] = nis_quantitative_answer(test, "b")
        #     #     meta_data["choices"][2]["meta_data"]["text"] = nis_quantitative_answer(test, "=")
        #     #     meta_data["choices"][3]["meta_data"]["text"] = nis_quantitative_answer(test, "?")

        #     question = TestQuestion.objects.create(
        #         answer_class=TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE,
        #         meta_data=meta_data,
        #         section=test.section,
        #         status=test.status,
        #         code="{}{:%y}{:04}".format(
        #             test.section.code, 
        #             datetime.now(), 
        #             TestQuestion.objects.filter(created_at__year=datetime.now().year, section=test.section).count()),
        #         weight=0,
        #         # order=i,
        #         developer=test.developer,
        #     )
        #     question.weight = TestQuestion.calculate_weight(question)
        #     question.save()

        #     TestToQuestionRelation.objects.create(
        #         test = test,
        #         question = question,
        #         order = i,
        #     )

        #     # if test.section.id == 9540 or test.section.id in (9566, 9567):
        #     paragraph = TestParagraph.objects.create(
        #         paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
        #         meta_data={"text": ""},
        #     )
        #     TestParagraphQuestion.objects.create(
        #         question=question,
        #         paragraph=paragraph,
        #         order=0,
        #     )


        return test


class BuildTestAssembleView(AdminPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateResponseMixin, ContextMixin, View):
    template_name = "testbank/test_assemble.html"
    
    def get(self, request, code, *args, **kwargs):
        kwargs['active_nav_item'] = 'testbank'
        kwargs['preview_button'] = True

        test = get_object_or_404(Test.objects, code=code)
        question_count = test.question_count
        test_question_list = [None] * question_count

        relation_query = TestToQuestionRelation.objects.filter(test=test)

        question_list = TestQuestion.finished_questions.filter(section=test.section)

        for relation in relation_query:
            order = relation.order
            test_question_list[order] = {
                "index": order + 1,
                "question": relation.question,
                "code": relation.question.code,
                "section": test.section,
            }

        for i in range(question_count):
            if test_question_list[i] is None:
                test_question_list[i] = {
                    "index": i + 1,
                    "question": None,
                    "code": "TODO",
                    "section": test.section,
                }
                kwargs['preview_button'] = False


        kwargs["test_question_list"] = test_question_list
        kwargs["question_list"] = question_list
        kwargs['test'] = test

        if kwargs['preview_button'] and test.status == Test.STATUS_DRAFT:
            test.status = Test.STATUS_APPROVED
            test.save()

        if not kwargs['preview_button'] and test.status != Test.STATUS_DRAFT:
            test.status = Test.STATUS_DRAFT
            test.save()

        return self.render_to_response(super().get_context_data(**kwargs))
    
    def post(self, request, code, *args, **kwargs):
        # print("BuildTestAssembleView", request.POST, request.body)

        data = json.loads(request.body.decode("utf-8"))
        test = get_object_or_404(Test.objects, code=code)
        question_code = data['question_code']
        order = int(data["question_index"]) - 1
        question = TestQuestion.objects.get(code = question_code)

        # if TestToQuestionRelation.objects.filter(test=test, order=order).exists():
        TestToQuestionRelation.objects.filter(test=test, order=order).delete()
        TestToQuestionRelation.objects.filter(test=test, question=question).delete()

        relation = TestToQuestionRelation.objects.create(
            test=test, 
            question=question,
            order=order
        )
        
        # print(test.pk, question.pk, relation)

        return redirect("bbtest:build_assemble_variant", test.code )
    


class BuildStandaloneQuestionCreateView(AdminPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateResponseMixin, ContextMixin, View):
    template_name = "testbank/question_create.html"
    
    def get(self, request, *args, **kwargs):
        kwargs['active_nav_item'] = 'question_create'
        user = request.user


        if user.is_superuser:
            domain_dict = {
                domain: domain.sections.all() for domain in TestDomain.objects.prefetch_related("sections").all()
            }

        elif user.user_permissions.get().codename == "developer" and user.developer_profile is not None:
            if user.developer_profile.permission_all:
                domain_dict = {
                    domain: domain.sections.all() for domain in TestDomain.objects.prefetch_related("sections").all()
                }
            else:
                section_list = user.developer_profile.section.prefetch_related("domain").all()
                domain_dict = {}
                for section_obj in section_list:
                    domain = section_obj.domain
                    domain_dict[domain] = domain_dict.get(domain, []) + [section_obj] 
        else:
            domain_dict = {}



        CATEGORY_CHOICES = [(None, "-----")]
        for domain_obj, section_list in domain_dict.items():
            options = []
            # section_list = domain_obj.sections.all()
            for section in section_list:
                options.append((section.pk, gettext_lazy(section.name)))

            if len(options) > 0:
                CATEGORY_CHOICES.append((gettext_lazy(domain_obj.name), tuple(options)))

        
        form = CreateStandaloneQuestionForm(choices = CATEGORY_CHOICES)
        kwargs["select_section_form"] = form

    
        return self.render_to_response(super().get_context_data(**kwargs))
    

    def post(self, request, *args, **kwargs):
        print(request.POST)
        section_id = request.POST["section"]
        section_obj = TestSection.objects.get(id=section_id)

        question = self.create_question_suite(request.user, section_obj)
        print(question)

        # raise Http404("Superusers cannot send tests for approval")
        # return redirect("bbtest:build_assemble_tests")
        return redirect("bbtest:build_standalone_question", question.code )



    def create_question_suite(self, developer, section_obj):

        choice_id = 1 
        meta_data = {
            "choices": [
                {"id": choice_id + 0, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
                {"id": choice_id + 1, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
                {"id": choice_id + 2, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
                {"id": choice_id + 3, "choice_class": "MultichoiceTextChoice", "meta_data": {"text": ""}},
            ],
            "correct_id": None,
        }

        question = TestQuestion.objects.create(
            answer_class=TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE,
            meta_data=meta_data,
            section=section_obj,
            status=TestQuestion.STATUS_DRAFT,
            code="{}{:%y}{:04}".format(
                section_obj.code, 
                datetime.now(), 
                TestQuestion.objects.filter(created_at__year=datetime.now().year, section=section_obj).count()),
            weight=0,
            # order=i,
            developer=developer,
        )
        question.weight = TestQuestion.calculate_weight(question)
        question.save()

        # if test.section.id == 9540 or test.section.id in (9566, 9567):
        paragraph = TestParagraph.objects.create(
            paragraph_class=TestParagraph.PARAGRAPH_CLASS_TEXT,
            meta_data={"text": ""},
        )
        TestParagraphQuestion.objects.create(
            question=question,
            paragraph=paragraph,
            order=0,
        )

        return question