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
from bbtest.models import TestSection, TestDomain
from xlsxwriter.utility import xl_rowcol_to_cell
from django.db import connection, reset_queries
from functools import lru_cache

# from bbtest.auth.mixins import DeveloperPermissionRequiredMixin
# from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin
from django.db.models import Q

class ChangePriceView(SuperPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "super/change_price.html"

    def get_context_data(self, **kwargs):
        kwargs["domain_price_query"] = []

        for domain in TestDomain.objects.all().order_by('order'):
            kwargs["domain_price_query"].append({
                "name": domain.name,
                "sections": [item for item in TestSection.objects.filter(domain=domain).order_by('order')]
                })

        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        try:
            price = int(request.POST["price"])
        except ValueError:
            error(request, "Not valid input") 
            return redirect("bbtest:super_change_price")

        sect = request.POST["sect"]
        sect_name = request.POST["sect_name"]
        sect_obj = TestSection.objects.get(id=sect)
        old_price = sect_obj.question_price
        sect_obj.question_price = price
        sect_obj.save()
        success(request, "Price for {} changed from {} to {} per question.".format(repr(sect_name), old_price, price))
        return redirect("bbtest:super_change_price")


