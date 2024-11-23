from __future__ import annotations

import hashlib
import inspect
import random
from collections import defaultdict
from typing import TYPE_CHECKING, List

import numpy as np
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import get_language

from bbtest.auth.mixins import LoginRequiredMixin, PermissionRequiredMixinFactory
from bbtest.auth.models import User
from bbtest.http import TightJsonResponse
from bbtest.models import (
    Test,
    TestQuestion,
    TestDomain,
    TestPackage,
    TestPackageRusKazPair,
    TestPackageRusKazQuiz,
    TestSection,
    TestTaxonomy,
    TestTopic,
    TestSubTopic,
    TestTopicToSubtopicRelation,
)
from bbtest.models.quiz import Quiz, QuizSet
from bbtest.views.common import PaginationMixin, UserContextMixin
from bbtest.views.generic import TemplateView

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.db.models import QuerySet

    from bbtest.auth.models import User


def get_function_hash(func):
    # Retrieve the source code of the function
    source_code = inspect.getsource(func)
    # Compute a hash of the source code
    return hashlib.sha256(source_code.encode('utf-8')).hexdigest()



class DashboardRedirectView(LoginRequiredMixin, UserContextMixin, TemplateView):
    template_name = ""

    def get(self, request: WSGIRequest, *args, **kwargs):
        q: QuerySet = TestPackageRusKazQuiz.objects.filter(
            user = request.user,
            payed = True,
            started = True,
        )
        if not q:
            return redirect("bbtest:b2bt_build_package_stats", "demo")

        quiz_pair: TestPackageRusKazQuiz = q.latest('created_at')
        return redirect("bbtest:b2bt_build_package_stats", quiz_pair.pk)


class DashboardView(PermissionRequiredMixinFactory(["super", "B2BTeacher"]), UserContextMixin, PaginationMixin, TemplateView):
    template_name = "b2bt/dashboard.html"

    def get(self, request: WSGIRequest, package_pair_quiz_id: str|int, *args, **kwargs):
        kwargs["active_nav_item"] = "dashboard"

        self.pixels_per_student = 20

        if package_pair_quiz_id == "demo":
            kwargs |= self.compute_statistic_fake()
            return self.render_to_response(super().get_context_data(**kwargs))


        user: User = request.user

        quiz_pair: TestPackageRusKazQuiz = get_object_or_404(
            TestPackageRusKazQuiz.objects,
            id=package_pair_quiz_id,
            # user=user,
            # payed=True,
            # started=True,
        )

        if not (quiz_pair.user == user or user.has_perm("bbtest.super")):
            return TightJsonResponse({"error": "можно смотреть только свои тесты"})
        if not quiz_pair.payed:
            return TightJsonResponse({"error": "тестирование не орлачено"})
        if not quiz_pair.started:
            return TightJsonResponse({"error": "тестирование ещё не было начато"})

        # q: QuerySet = TestPackageRusKazQuiz.objects.filter(
        #     user = user,
        #     payed = True,
        #     started = True,
        # )
            
        # quiz_pair: TestPackageRusKazQuiz = q.latest('created_at')
        fhash = get_function_hash(self.get)

        stats = None # cache.get(f"dashboard_result_{package_pair_quiz_id}_{fhash}")
        if stats is None or True:
            stats = self.compute_statistic(quiz_pair)
            cache.set(f"dashboard_result_{package_pair_quiz_id}_{fhash}", stats, 100)

        kwargs |= stats

        return self.render_to_response(super().get_context_data(**kwargs))


    def compute_statistic(self, quiz_pair: TestPackageRusKazQuiz):
        kwargs = {}

        # Get student list
        student_username_list: List[str] = [row[0] for row in quiz_pair.student_table]
        student_obj_list: QuerySet[User] = get_user_model().objects.filter(username__in=student_username_list).all()
        student_obj_list = sorted(student_obj_list, key=lambda obj: student_username_list.index(obj.username))
        n_students = len(student_username_list)
        
        domain_obj_kz: TestDomain = quiz_pair.TestPackagePair.test_package_kz.domain
        domain_obj_ru: TestDomain = quiz_pair.TestPackagePair.test_package_ru.domain

        section_list_kz: List[TestSection] = list(domain_obj_kz.sections.prefetch_related("topics").all())
        section_list_ru: List[TestSection] = list(domain_obj_ru.sections.prefetch_related("topics").all())
        section_list = section_list_kz + section_list_ru

        # produce mapping from section, topic, subtopic to id
        total_id = 0
        map_key_to_id_ru = self.produce_key_to_id_mapping(section_list_ru, total_id, lang="rus")
        map_key_to_id_kz = self.produce_key_to_id_mapping(section_list_kz, total_id, lang="kaz")
        map_key_to_id = map_key_to_id_ru | map_key_to_id_kz

        map_id_to_key = {v: getattr(k, 'name', k) for k, v in map_key_to_id.items()}
        # print(map_key_to_id)
        # print(map_id_to_key)


        # create tree
        parent_to_children_list_ru = self.produce_parent_to_children_list(section_list_ru, map_key_to_id, total_id, lang="rus")
        parent_to_children_list_kz = self.produce_parent_to_children_list(section_list_kz, map_key_to_id, total_id, lang="kaz")
        parent_to_children_list = parent_to_children_list_ru | parent_to_children_list_kz


        # parent_student_scores = defaultdict(lambda: [])  # { total_id: np.zeros(n_students) }
        parent_student_scores = {k: np.zeros(n_students) for k in map_id_to_key.keys()}
        parent_student_scores_by_difficulty = {k: np.zeros((len(TestQuestion.DIFFICULTIES), n_students)) for k in map_id_to_key.keys()}


        for student_i, (student, row) in enumerate(zip(student_obj_list, quiz_pair.student_table)):
            # username = row[0]
            # first_name = row[1]
            # last_name = row[2]
            student_lang = row[3]
            # pwd = row[4]

            quiz_set_list: QuerySet[QuizSet] = student.quiz_sets.all()
            if len(quiz_set_list) < 1:
                continue
            assert len(quiz_set_list) == 1

            quiz_set = quiz_set_list[0]
            # for quiz_set in quiz_set_list:

            quiz_list: QuerySet[Quiz] = quiz_set.quizzes.order_by("test__section__order", "order").all()
            total_score = 0

            for quiz_obj in quiz_list:
                section_obj: TestSection = quiz_obj.test.section
                section_id = map_key_to_id[section_obj]

                if not quiz_obj.is_finished:
                    continue
                
                # compute scores
                score, score_topic, score_subtopic, score_difficulty = quiz_obj.calc_score_by_topic_subtopic()
                # print(score, score_topic, score_subtopic, score_difficulty)

                parent_student_scores[section_id][student_i] = score
                total_score += score

                for topic_obj, topic_score in score_topic.items():
                    topic_id = map_key_to_id[topic_obj]
                    parent_student_scores[topic_id][student_i] = topic_score
                # for subtopic, subtopic_score in score_topic.items():
                #     subtopic_id = map_key_to_id[subtopic]
                #     parent_student_scores[subtopic_id].append(subtopic_score)
                for question_difficulty, difficulty_score in score_difficulty.items():
                    irow_difficulty = TestQuestion.DIFFICULTIES_MAP[question_difficulty]
                    parent_student_scores_by_difficulty[section_id][irow_difficulty, student_i] = difficulty_score

            parent_student_scores[f"{total_id}{student_lang}"][student_i] = total_score


        student_name_list_by_lang = {"rus": [], "kaz": []}
        slice_by_lang = {"rus": [], "kaz": []}
        for i, row in enumerate(quiz_pair.student_table):
            # username = row[0]
            first_name = row[1]
            last_name = row[2]
            student_lang = row[3]
            # pwd = row[4]
            student_name_list_by_lang[student_lang].append(f"{i+1}) {first_name} {last_name}")
            slice_by_lang[student_lang].append(i)

        parent_student_scores_by_lang = {
            "rus": {k: scores[slice_by_lang["rus"]].tolist() for k, scores in parent_student_scores.items() if k.lower().endswith("rus")},
            "kaz": {k: scores[slice_by_lang["kaz"]].tolist() for k, scores in parent_student_scores.items() if k.lower().endswith("kaz")},
        }
        parent_student_scores_by_difficulty_by_lang = {
            # slice starts from in order to remove Questions with not specified difficulty
            "rus": {k: scores[1:, slice_by_lang["rus"]].tolist() for k, scores in parent_student_scores_by_difficulty.items() if k.lower().endswith("rus")},
            "kaz": {k: scores[1:, slice_by_lang["kaz"]].tolist() for k, scores in parent_student_scores_by_difficulty.items() if k.lower().endswith("kaz")},
        }

        # get student group mean score by subject
        parent_average_scores = {k: float(np.mean(v)) for k, v in parent_student_scores.items()}

        # pass data to charts
        kwargs['student_name_list'] = student_name_list_by_lang # [s.get_full_name() for s in student_obj_list]
        kwargs['parent_list'] = {
            "rus": [f"{total_id}rus"] + [map_key_to_id[s] for s in section_list_ru],
            "kaz": [f"{total_id}kaz"] + [map_key_to_id[s] for s in section_list_kz],
        }
        
        kwargs['parent_to_children_list'] = parent_to_children_list
        kwargs['parent_average_scores'] = parent_average_scores
        kwargs['parent_student_scores'] = parent_student_scores_by_lang
        kwargs['parent_student_scores_by_difficulty'] = parent_student_scores_by_difficulty_by_lang 
        # kwargs['map_key_to_id'] = map_key_to_id
        kwargs['map_id_to_key'] = map_id_to_key


        # chart options
        kwargs['subject_chart_height'] = min(n_students * self.pixels_per_student, 10000)

        return kwargs

    def compute_statistic_fake(self):
        kwargs = {}

        # Get student list
        n_students = 30
        student_name_list = [f'Ученик {i + 1}' for i in range(n_students)]

        domain_obj_ru: TestDomain = TestDomain.objects.prefetch_related("sections").get(name="PISA_ru")
        domain_obj_kz: TestDomain = TestDomain.objects.prefetch_related("sections").get(name="PISA_kz")

        section_list_ru: List[TestSection] = list(domain_obj_ru.sections.prefetch_related("topics").all())
        section_list_kz: List[TestSection] = list(domain_obj_kz.sections.prefetch_related("topics").all())
        section_list = {
            "rus": section_list_ru,
            "kaz": section_list_kz,
        }

        # produce mapping from section, topic, subtopic to id
        total_id = 0
        map_key_to_id_ru = self.produce_key_to_id_mapping(section_list_ru, total_id, lang="rus")
        map_key_to_id_kz = self.produce_key_to_id_mapping(section_list_kz, total_id, lang="kaz")
        map_key_to_id = map_key_to_id_ru | map_key_to_id_kz

        map_id_to_key = {v: getattr(k, 'name', k) for k, v in map_key_to_id.items()}


        # create tree
        parent_to_children_list_ru = self.produce_parent_to_children_list(section_list_ru, map_key_to_id, total_id, lang="rus")
        parent_to_children_list_kz = self.produce_parent_to_children_list(section_list_kz, map_key_to_id, total_id, lang="kaz")
        parent_to_children_list = parent_to_children_list_ru | parent_to_children_list_kz


        parent_student_scores = {k: np.zeros(n_students) for k in map_id_to_key.keys()}

        student_name_list_by_lang = {"rus": [], "kaz": []}
        slice_by_lang = {"rus": [], "kaz": []}
        for student_i, student in enumerate(student_name_list):
            student_lang = random.choice(["rus", "kaz"])
            student_name_list_by_lang[student_lang].append(f"{student_i+1}) {student}")
            slice_by_lang[student_lang].append(student_i)

            total_score = 0

            for section_obj in section_list[student_lang]:
                section_id = map_key_to_id[section_obj]

                # compute scores
                score, score_topic, score_subtopic = self.fake_calc_score_by_topic_subtopic(section_obj)
                # print(score, score_topic, score_subtopic)

                parent_student_scores[section_id][student_i] = score
                total_score += score

                for topic_obj, topic_score in score_topic.items():
                    topic_id = map_key_to_id[topic_obj]
                    parent_student_scores[topic_id][student_i] = topic_score
                # for subtopic, subtopic_score in score_topic.items():
                #     subtopic_id = map_key_to_id[subtopic]
                #     parent_student_scores[subtopic_id].append(subtopic_score)

            parent_student_scores[f"{total_id}{student_lang}"][student_i] = total_score

            

        parent_student_scores_by_lang = {
            "rus": {k: scores[slice_by_lang["rus"]].tolist() for k, scores in parent_student_scores.items() if k.lower().endswith("rus")},
            "kaz": {k: scores[slice_by_lang["kaz"]].tolist() for k, scores in parent_student_scores.items() if k.lower().endswith("kaz")},
        }
         

        # get student group mean score by subject
        parent_average_scores = {k: float(np.mean(v)) for k, v in parent_student_scores.items()}
        # conver numpy to list for compatibility
        for key in parent_student_scores.keys():
            parent_student_scores[key] = parent_student_scores[key].tolist()

        # pass data to charts
        kwargs['student_name_list'] = student_name_list_by_lang # [s.get_full_name() for s in student_obj_list]
        kwargs['parent_list'] = {
            "rus": [f"{total_id}rus"] + [map_key_to_id[s] for s in section_list_ru],
            "kaz": [f"{total_id}kaz"] + [map_key_to_id[s] for s in section_list_kz],
        }
        
        kwargs['parent_to_children_list'] = parent_to_children_list
        kwargs['parent_average_scores'] = parent_average_scores
        kwargs['parent_student_scores'] = parent_student_scores_by_lang  # parent_student_scores
        # kwargs['map_key_to_id'] = map_key_to_id
        kwargs['map_id_to_key'] = map_id_to_key


        # chart options
        kwargs['subject_chart_height'] = min(n_students * self.pixels_per_student, 10000)

        return kwargs

    def produce_key_to_id_mapping(self, section_list: List[TestSection],  total_id = 0, lang = "rus"):
        map_key_to_id = {f"Общее {lang}": f"{total_id}{lang}"}
        map_key_to_id |= {s: f"{i}{lang}" for i, s in enumerate(section_list, 10)}  # f"Предмет {s.name}"
        topic_id = 1000
        subtopic_id = 2000

        for section_obj in section_list:
            topic_list: List[TestTopic] = section_obj.topics.all()
            for topic_obj in topic_list:
                map_key_to_id[topic_obj] = f"{topic_id}{lang}"
                topic_id += 1

                topic_subtopic_list: List[TestTopicToSubtopicRelation] = TestTopicToSubtopicRelation.objects.filter(topic = topic_obj).order_by("order")
                for topic_subtopic_obj in topic_subtopic_list:
                    map_key_to_id[topic_subtopic_obj.subtopic] = f"{subtopic_id}{lang}"
                    subtopic_id += 1

        # map_id_to_key = {v: getattr(k, 'name', k) for k, v in map_key_to_id.items()}
        return map_key_to_id
    

    def produce_parent_to_children_list(self, section_list: List[TestSection], map_key_to_id, total_id = 0, lang = "rus"):

        parent_to_children_list = { f"{total_id}{lang}": [map_key_to_id[s] for s in section_list] }
        for section_obj in section_list:
            section_id = map_key_to_id[section_obj]
            # print(section_obj)
            topic_list: List[TestTopic] = section_obj.topics.all()
            # print(topic_list)
            parent_to_children_list[section_id] = [map_key_to_id[t] for t in topic_list]

            for topic_obj in topic_list:
                topic_id = map_key_to_id[topic_obj]

                # parent_to_children_list[section_id] = parent_to_children_list.get(section_id, []) + [topic_id]
                topic_subtopic_list: List[TestTopicToSubtopicRelation] = TestTopicToSubtopicRelation.objects.filter(
                    topic = topic_obj
                ).order_by("order")

                for topic_subtopic_obj in topic_subtopic_list:
                    subtopic_id = map_key_to_id[topic_subtopic_obj.subtopic]
                    parent_to_children_list[topic_id] = parent_to_children_list.get(topic_id, []) + [subtopic_id]
        return parent_to_children_list

    def calculate_topic_score_by_student(self, topic, n_topic, n_students):
        return np.array([random.randint(40 // n_topic, 100 // n_topic) for t in range(n_students)])
    

    def fake_calc_score_by_topic_subtopic(self, section_obj: TestSection) -> tuple[int, dict, dict]:
        # topic_list, subtopic_list = self.get_question_topic_subtopic()
        n = 100
        all_topic_list: List[TestTopic] = section_obj.topics.all()
        all_subtopic_list: List[TestSubTopic] = section_obj.subtopics.all()

        score = 0
        score_topic = defaultdict(int)
        score_subtopic = defaultdict(int)

        for topic, subtopic in zip(
            random.choices(all_topic_list, k=n), random.choices(all_subtopic_list, k=n)
        ):
            is_correct = 0 if random.random() > 0.8 else 1

            score_topic[topic] += is_correct
            score_subtopic[subtopic] += is_correct
            score += is_correct

        return score, score_topic, score_subtopic
    


class HelpPageView(PermissionRequiredMixinFactory(["super", "B2BTeacher"]), UserContextMixin, PaginationMixin, TemplateView):
    template_name = "b2bt/help_page.html"

    def get(self, request: WSGIRequest, *args, **kwargs):
        kwargs["active_nav_item"] = "help_instructions"
        kwargs["youtube_video_id"] = "U_ApFztnWa8"
        
        return self.render_to_response(super().get_context_data(**kwargs))