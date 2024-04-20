from datetime import datetime

import pytz

# from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages import error, success, warning
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now
from django.utils.translation import pgettext

from bbtest.auth.mixins import (
    AdminPermissionRequiredMixin,
    DeveloperPermissionRequiredMixin,
    SuperPermissionRequiredMixin,
)
from bbtest.forms.super import ExportDataForm
from bbtest.http import TightJsonResponse
from bbtest.jobs.export_test import _job_export_results, job_export_results
from bbtest.models import Quiz, TestSection
from bbtest.models.job_progress import JobProgress
from bbtest.views.common import PaginationMixin, UserContextMixin
from bbtest.views.developer.mixins import DeveloperAcknowledgementRequiredMixin
from bbtest.views.generic import TemplateView, View


class ExportDataView(AdminPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "super/export_data.html"


    def get(self, request, *args, **kwargs):
        kwargs["job_progress_list"] = request.user.job_progresses.order_by("-started_at").all()
        # print(kwargs["job_progress_list"])
        kwargs["active_nav_item"] = "export_data"
        kwargs["export_data_form"] = ExportDataForm()

        return self.render_to_response(super().get_context_data(**kwargs))


class ExportDataFormView(AdminPermissionRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        print("TODO: TestSection.objects.get(name=section_name).question_count is probably depreciated")
        form = ExportDataForm(data=request.POST)
        valid = form.is_valid()    # is_valid should be called before form.cleaned_data could be accessed

        if not valid:
            error(request, "Errors %s" % " ".join([ " ".join(errors) for key, errors in form.errors.items() ]))
            return redirect("bbtest:super_export_data")
        
        start_date = form.cleaned_data["start_date"]
        klass_domain = form.cleaned_data["klass_domain"] 

        start_date =  datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0, tzinfo=pytz.timezone('Asia/Almaty'))

        print(start_date, klass_domain)
        job_progress_bar = JobProgress.objects.create(
            user = request.user,
            job_name = f"{klass_domain} {start_date} export answers"
        )
        # _job_export_results(start_date, klass_domain, job_progress_bar)
        job_export_results.delay(start_date, klass_domain, job_progress_bar)
            
        return redirect("bbtest:super_export_data")

