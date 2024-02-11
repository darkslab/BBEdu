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
from bbtest.forms.super import  CreatePackageForm, ManagePackageStudentsForm, ManagePackageTestForm, CreateStudentGroupForm, CreateCustomTestSelectionForm
from bbtest.models.test import TestDomain, Test, TestPackage, TestSection, TestPackageRelation, StudentGroup, UserTestPackageProfile
from bbtest.models.quiz import Quiz, QuizSet
from bbtest.http import TightJsonResponse
import uuid
from bbtest.models import User
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin, AdminPermissionRequiredMixin, CreateStudentRequiredMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin
from django.core.exceptions import ValidationError
from datetime import datetime
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View





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
                options.append((section, gettext_lazy(section.name)))

            if len(options) > 0:
                CATEGORY_CHOICES.append((gettext_lazy(domain_obj.name), tuple(options)))

        kwargs["select_section_form"] = CreateCustomTestSelectionForm(choices = CATEGORY_CHOICES)

        return self.render_to_response(super().get_context_data(**kwargs))