import random
from typing import List

import numpy as np
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language

from bbtest.auth.mixins import PermissionRequiredMixinFactory
from bbtest.models import Test, TestDomain, TestSection, TestTaxonomy, TestTopic, TestTopicToSubtopicRelation
from bbtest.views.common import PaginationMixin, UserContextMixin
from bbtest.views.generic import TemplateView


class DashboardView(PermissionRequiredMixinFactory(["super", "B2BTeacher"]), UserContextMixin, PaginationMixin, TemplateView):
    template_name = "b2bt/dashboard.html"

    def get_context_data(self, **kwargs):
        kwargs["active_nav_item"] = "dashboard"

        kwargs |= self.produce_rand_data(**kwargs)

        return super().get_context_data(**kwargs)

    def produce_rand_data(self, **kwargs):
        n_students = 20
        student_name_list = [f'Ученик {i + 1}' for i in range(n_students)]

        domain_obj:  TestDomain = TestDomain.objects.prefetch_related("sections").get(name="PISA_ru")
        section_list: List[TestSection] = domain_obj.sections.prefetch_related("topics").all()
        # subject_list = ["Математика", "Естествознание", "Русский язык", "Казахский язык"]

        # produce mapping from section, topic, subtopic to id
        total_id = 0
        map_key_to_id = {"Total": total_id}
        map_key_to_id |= {s: i for i, s in enumerate(section_list, 10)}  # f"Предмет {s.name}"
        topic_id = 1000
        subtopic_id = 2000

        for section_obj in section_list:
            topic_list: List[TestTopic] = section_obj.topics.all()
            for topic_obj in topic_list:
                map_key_to_id[topic_obj] = topic_id
                topic_id += 1

                topic_subtopic_list: List[TestTopicToSubtopicRelation] = TestTopicToSubtopicRelation.objects.filter(topic = topic_obj).order_by("order")
                for topic_subtopic_obj in topic_subtopic_list:
                    map_key_to_id[topic_subtopic_obj.subtopic] = subtopic_id
                    subtopic_id += 1

        map_id_to_key = {v: getattr(k, 'name', k) for k, v in map_key_to_id.items()}
        print(map_key_to_id)
        print(map_id_to_key)
        

        # create tree
        parent_to_children_list = { total_id: [map_key_to_id[s] for s in section_list] }
        for section_obj in section_list:
            section_id = map_key_to_id[section_obj]
            # print(section_obj)
            topic_list: List[TestTopic] = section_obj.topics.all()
            # print(topic_list)
            parent_to_children_list[section_id] = [map_key_to_id[t] for t in topic_list]

            for topic_obj in topic_list:
                topic_id = map_key_to_id[topic_obj]

                parent_to_children_list[section_id] = parent_to_children_list.get(section_id, []) + [topic_id]
                topic_subtopic_list: List[TestTopicToSubtopicRelation] = TestTopicToSubtopicRelation.objects.filter(
                    topic = topic_obj
                ).order_by("order")

                for topic_subtopic_obj in topic_subtopic_list:
                    subtopic_id = map_key_to_id[topic_subtopic_obj.subtopic]
                    parent_to_children_list[topic_id] = parent_to_children_list.get(topic_id, []) + [subtopic_id]


        

        # get students score by subject
        parent_student_scores = { total_id: np.zeros(n_students) }
        for section_obj in section_list:
            section_id = map_key_to_id[section_obj]
            parent_student_scores[section_id] = np.zeros(n_students)

            topic_list: List[TestTopic] = section_obj.topics.all()
            for topic_obj in topic_list:
                topic_id = map_key_to_id[topic_obj]
                parent_student_scores[topic_id] = self.calculate_topic_score_by_student(topic_obj, len(topic_list), n_students)
                parent_student_scores[section_id] += parent_student_scores[topic_id]
                

            parent_student_scores[total_id] += parent_student_scores[section_id]

            
        # get student group mean score by subject
        parent_average_scores = {k: float(np.mean(v)) for k, v in parent_student_scores.items()}

        # conver numpy to list for compatibility
        for key in parent_student_scores.keys():
            parent_student_scores[key] = parent_student_scores[key].tolist()
            # parent_average_scores[key] = parent_average_scores[key].tolist()

        

        # pass data to charts
        kwargs['student_name_list'] = student_name_list
        kwargs['parent_list'] = [total_id] + [map_key_to_id[s] for s in section_list]
        kwargs['parent_to_children_list'] = parent_to_children_list
        kwargs['parent_average_scores'] = parent_average_scores
        kwargs['parent_student_scores'] = parent_student_scores
        # kwargs['map_key_to_id'] = map_key_to_id
        kwargs['map_id_to_key'] = map_id_to_key


        # chart options
        kwargs['subject_chart_height'] = min(n_students * 20, 5000)

        return kwargs

    
    def calculate_topic_score_by_student(self, topic, n_topic, n_students):
        return np.array([random.randint(40 // n_topic, 100 // n_topic) for t in range(n_students)])