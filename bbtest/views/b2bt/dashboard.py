import random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import get_language
from django.shortcuts import get_object_or_404
from bbtest.auth.mixins import PermissionRequiredMixinFactory
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.models import Test
import numpy as np


class DashboardView(PermissionRequiredMixinFactory(["super", "B2BTeacher"]), UserContextMixin, PaginationMixin, TemplateView):
    template_name = "b2bt/dashboard.html"

    def get_context_data(self, **kwargs):
        kwargs["active_nav_item"] = "dashboard"

        students = [f'Ученик {i + 1}' for i in range(20)]
        subject_list = ["Математика", "Естествознание", "Русский язык", "Казахский язык"]

        scores = { "Total": np.zeros(20) }
        mean_subj = { "Total": 0 }
        for subj in subject_list:
            scores[subj] = np.array([random.randint(40, 100) for _ in range(20)])
            mean_subj[subj] = np.mean(scores[subj])

            scores["Total"] += scores[subj]
            mean_subj["Total"] += mean_subj[subj]

        for key in scores.keys():
            scores[key] = scores[key].tolist()
            mean_subj[key] = mean_subj[key].tolist()

        kwargs['subject_list'] = subject_list
        kwargs['mean_subj'] = mean_subj
        kwargs['students'] = students
        kwargs['scoresData'] = scores

        return super().get_context_data(**kwargs)


