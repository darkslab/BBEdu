import random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import get_language
from django.shortcuts import get_object_or_404
from bbtest.auth.mixins import PermissionRequiredMixinFactory
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.models import Test


class DashboardView(PermissionRequiredMixinFactory(["super", "B2BTeacher"]), UserContextMixin, PaginationMixin, TemplateView):
    template_name = "b2bt/dashboard.html"

    def get_context_data(self, **kwargs):
        kwargs["active_nav_item"] = "dashboard"

        kwargs["data"] = [10, 20, 30, 40]  # Example data
        kwargs["labels"] = ['January', 'February', 'March', 'April']

        students = [f'Student {i + 1}' for i in range(20)]
        scores = {}
        scores["subject1"] = [random.randint(50, 100) for _ in range(20)]
        scores["subject2"] = [random.randint(50, 100) for _ in range(20)]
        scores["subject3"] = [random.randint(50, 100) for _ in range(20)]

        kwargs = {
            'students': students,
            'scoresData': scores,
        }

        return super().get_context_data(**kwargs)


