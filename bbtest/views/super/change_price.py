from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.messages import warning, success, error
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.utils.translation import pgettext
from django.db.models import Q
from django.utils.timezone import now
from django.http import Http404
from django.http import HttpResponse
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.forms.super import ExportDataForm
from bbtest.http import TightJsonResponse
from bbtest.models import Quiz, TestSection
from xlsxwriter.utility import xl_rowcol_to_cell
from django.db import connection, reset_queries
from functools import lru_cache

# from bbtest.auth.mixins import DeveloperPermissionRequiredMixin
# from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin
from django.db.models import Q

class ChangePriceView(SuperPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "super/change_price.html"

    def get_context_data(self, **kwargs):

        # kwargs["section_price_query"] = ExportDataForm()
        kwargs["domain_price_query"] = {}
        for item in TestSection.objects.all().order_by('id'):
            kwargs["domain_price_query"][item.domain.name] = kwargs["domain_price_query"].get(item.domain.name, []) + [item]

        return super().get_context_data(**kwargs)