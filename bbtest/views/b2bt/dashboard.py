import random
from typing import List

import numpy as np
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language

from bbtest.auth.mixins import PermissionRequiredMixinFactory
from bbtest.models import Test, TestDomain, TestSection, TestTaxonomy, TestTopic
from bbtest.views.common import PaginationMixin, UserContextMixin
from bbtest.views.generic import TemplateView


class DashboardView(PermissionRequiredMixinFactory(["super", "B2BTeacher"]), UserContextMixin, PaginationMixin, TemplateView):
    template_name = "b2bt/dashboard.html"

    def get_context_data(self, **kwargs):
        kwargs["active_nav_item"] = "dashboard"
        n_students = 20
        students = [f'Ученик {i + 1}' for i in range(n_students)]

        domain_obj:  TestDomain = TestDomain.objects.prefetch_related("sections").get(name="PISA_ru")
        section_list: List[TestSection] = domain_obj.sections.prefetch_related("topics").all()


        for section_obj in section_list:
            print(section_obj)
            topic_list: List[TestTopic] = section_obj.topics.all()
            print(topic_list)

        # subject_list = ["Математика", "Естествознание", "Русский язык", "Казахский язык"]
        subject_list = [s.name for s in section_list]

        # get students score by subject
        scores = { "Total": np.zeros(n_students) }
        for subj in subject_list:
            scores[subj] = np.array([random.randint(40, 100) for _ in range(n_students)])
            scores["Total"] += scores[subj]

        # get student group mean score by subject
        mean_subj = { "Total": 0 }
        for subj in subject_list:
            mean_subj[subj] = np.mean(scores[subj])
            mean_subj["Total"] += mean_subj[subj]


        # conver numpy to list for compatibility
        for key in scores.keys():
            scores[key] = scores[key].tolist()
            mean_subj[key] = mean_subj[key].tolist()

        

        # pass data to charts
        kwargs['subject_list'] = subject_list
        kwargs['mean_subj'] = mean_subj
        kwargs['students'] = students
        kwargs['scoresData'] = scores

        # chart options
        kwargs['subject_chart_height'] = min(n_students * 20, 5000)

        return super().get_context_data(**kwargs)


