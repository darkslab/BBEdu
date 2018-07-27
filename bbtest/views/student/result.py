from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.lorem_ipsum import paragraphs, words
from random import randint
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.utils.json import tight_dumps
from bbtest.utils.colors import GOOGLE_COLORS, GOOGLE_COLORS_BLEACHED


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

        for index, quiz_set in enumerate(kwargs["quiz_sets"]):
            quiz_set.index = paginator.count - (kwargs["quiz_sets"].start_index() + index - 1)

            for quiz in quiz_set.quizzes.all():
                quiz.stats = {
                    "row": {
                        "max": quiz.test.max_score(),
                        "colors": tight_dumps([ quiz.test.section.fg_color(), quiz.test.section.bg_color() ]),
                        "score": quiz.score(),
                    },
                }
                # DARK_TODO  implement this!
                quiz.stats["row"]["avg"] = quiz.stats["row"]["max"] // 2

                if quiz.test.section.can_measure_topics():
                    # BranchedResultDetailModule
                    quiz.stats["detail"] = {
                        "type": "branched",
                        "branches": [],
                        "colors": quiz.stats["row"]["colors"],
                        "avg": quiz.stats["row"]["avg"],
                        "progress": tight_dumps([ 350, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]),
                    }
                    topic_branches = quiz.test.topic_branches()
                    for i, topic_branch in enumerate(topic_branches):
                        quiz.stats["detail"]["branches"].append({
                            "max": quiz.test.max_score(topic_branch["question_ids"]),
                            "score": quiz.score(topic_branch["question_ids"]),
                            "colors": tight_dumps([
                                GOOGLE_COLORS[i % len(GOOGLE_COLORS)],
                                GOOGLE_COLORS_BLEACHED[i % len(GOOGLE_COLORS_BLEACHED)],
                            ]),
                            "title": words(randint(2, 4), False),
                            "texts": paragraphs(randint(1, 3), False),
                        })

                else:
                    # SimpleResultDetailModule
                    quiz.stats["detail"] = {
                        "type": "simple",
                        "max": quiz.stats["row"]["max"],
                        "colors": quiz.stats["row"]["colors"],
                        "score": quiz.stats["row"]["score"],
                        "avg": quiz.stats["row"]["avg"],
                        "progress": tight_dumps([ 350, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]),
                        "texts": paragraphs(randint(1, 2), False),
                    }

        return super().get_context_data(**kwargs)
