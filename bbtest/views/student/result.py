from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import ugettext as _, pgettext
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from random import randint
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin, PaginationMixin, results_progress, inject_questions_and_report_into_started_response, average_score
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.utils.json import tight_dumps
from bbtest.utils.colors import GOOGLE_COLORS, GOOGLE_COLORS_BLEACHED
from bbtest.models import TestTopic, Quiz
from bbtest.http import TightJsonResponse
from bbtest.texts import result_main_description_text, result_topic_description_text, inject_texts_into_response


class ResultsView(StudentPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "student/results/base.html"

    def get_context_data(self, **kwargs):
        paginator = Paginator(
            self.request.user.quiz_sets.select_related("test_domain").prefetch_related("quizzes__test__questions", "quizzes__test__section").order_by("-created_at"),
            5,
        )
        try:
            kwargs["quiz_sets"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["quiz_sets"] = paginator.page(1)
        except EmptyPage:
            kwargs["quiz_sets"] = paginator.page(paginator.num_pages)
        paginator.page_indexes = self.page_indexes(kwargs["quiz_sets"], 5)

        topic_ids = set()
        for index, quiz_set in enumerate(kwargs["quiz_sets"]):
            quiz_set.index = paginator.count - (kwargs["quiz_sets"].start_index() + index - 1)
            quiz_set.has_extra_column = False

            for quiz in quiz_set.quizzes.all():
                quiz.nis_passed = None
                quiz.stats = {
                    "row": {
                        "max": quiz.test.max_score(),
                        "score": 0,
                        "colors": tight_dumps([ quiz.test.section.fg_color(), quiz.test.section.bg_color() ]),
                    },
                }
                if quiz.is_finished:
                    quiz.stats["row"]["score"] = quiz.score()
                if quiz.test.section.pk in (9540, 9544):
                    quiz_set.has_extra_column = True
                    quiz.nis_passed = False
                    if quiz.test.section.pk == 9540 and quiz.stats["row"]["score"] >= 140:
                        quiz.nis_passed = True
                    elif quiz.test.section.pk == 9544 and quiz.stats["row"]["score"] >= 120:
                        quiz.nis_passed = True

                quiz.stats["row"]["avg"] = average_score(quiz.test.section)

                if not quiz.is_finished:
                    continue

                if quiz.test.section.can_measure_topics():
                    # BranchedResultDetailModule
                    quiz.stats["detail"] = {
                        "type": "branched",
                        "branches": [],
                        "colors": quiz.stats["row"]["colors"],
                        "avg": quiz.stats["row"]["avg"],
                        "progress": tight_dumps(results_progress(quiz.test.section, self.request.user)),
                        "texts": result_main_description_text(quiz.test.section.pk),
                    }
                    topic_branches = quiz.test.topic_branches()
                    topic_ids |= set([ topic_branch["topic_id"] for topic_branch in topic_branches ])
                    for i, topic_branch in enumerate(topic_branches):
                        correct_question_ids = []
                        score = quiz.score(topic_branch["question_ids"], correct_question_ids)
                        quiz.stats["detail"]["branches"].append({
                            "max": quiz.test.max_score(topic_branch["question_ids"]),
                            "score": score,
                            "questions_count": len(topic_branch["question_ids"]),
                            "correct_questions_count": len(correct_question_ids),
                            "colors": tight_dumps([
                                GOOGLE_COLORS[i % len(GOOGLE_COLORS)],
                                GOOGLE_COLORS_BLEACHED[i % len(GOOGLE_COLORS_BLEACHED)],
                            ]),
                            "title": None,
                            "__topic_id": topic_branch["topic_id"],
                            "texts": result_topic_description_text(topic_branch["topic_id"]),
                        })

                else:
                    # SimpleResultDetailModule
                    quiz.stats["detail"] = {
                        "type": "simple",
                        "max": quiz.stats["row"]["max"],
                        "colors": quiz.stats["row"]["colors"],
                        "score": quiz.stats["row"]["score"],
                        "avg": quiz.stats["row"]["avg"],
                        "progress": tight_dumps(results_progress(quiz.test.section, self.request.user)),
                        "texts": result_main_description_text(quiz.test.section.pk),
                    }

                # DARK_TODO  enable this when NIS 2018 average scores are available
                if False and quiz.test.section.is_nis():
                    quiz.stats["detail"]["avg_texts"] = pgettext("/student/results/", "The red line is the average score of the current test subject in comparison to your own results. The score represents an actual average result of NIS 2018 students (data is taken from nis.edu.kz).")

        if len(topic_ids):
            topic_branch_names = {}
            for topic_branch in TestTopic.objects.filter(pk__in=topic_ids).all():
                topic_branch_names[topic_branch.pk] = _(topic_branch.name)
            for quiz_set in kwargs["quiz_sets"]:
                for quiz in quiz_set.quizzes.all():
                    if not quiz.is_finished or quiz.stats["detail"]["type"] != "branched":
                        continue
                    for branch in quiz.stats["detail"]["branches"]:
                        branch["title"] = topic_branch_names[branch["__topic_id"]]

        return super().get_context_data(**kwargs)


def get_quiz_for_result_or_404(request, test_code):
    return get_object_or_404(Quiz.objects.filter(
        is_finished=True,
        quiz_set__student=request.user,
        test__code=test_code,
    ).select_related("test"))


class ResultView(StudentPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/result.html"

    def get_context_data(self, **kwargs):
        quiz = get_quiz_for_result_or_404(self.request, self.kwargs["code"])
        kwargs["test"] = quiz.test
        kwargs["code"] = self.kwargs["code"]
        kwargs["section_name"] = _(quiz.test.section.name)
        kwargs["result_page"] = self.request.GET.get("page")
        return super().get_context_data(**kwargs)


class ResultDataView(StudentPermissionRequiredMixin, View):
    def get(self, request, code, *args, **kwargs):
        quiz = get_quiz_for_result_or_404(request, code)
        response = {
            "success": True,
            "status": "started",
            "seconds": quiz.test.duration,
        }
        inject_questions_and_report_into_started_response(response, quiz.test, hide_answers=False)
        inject_texts_into_response(response, quiz.test)
        if quiz.report is None:
            for data in response["report"]["answers"]:
                data["answer"] = None
        else:
            response["report"] = quiz.report
        return TightJsonResponse(response)

    def post(self, request, code, *args, **kwargs):
        return self.get(request, code, *args, **kwargs)
