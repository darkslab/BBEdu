from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, results_progress, average_score
from bbtest.utils.json import tight_dumps
from bbtest.utils.colors import GOOGLE_COLORS, GOOGLE_COLORS_BLEACHED
from django.utils.translation import pgettext


class DashboardView(StudentPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/dashboard.html"

    def get_context_data(self, **kwargs):
        kwargs["is_current"] = self.request.user.quiz_sets.filter(is_current=True).count() > 0
        return super().get_context_data(**kwargs)
    
    
    def get_context_data2(self, **kwargs):
        kwargs["quiz_set"] = self.request.user.quiz_sets.select_related("test_domain").prefetch_related("quizzes__test__questions", "quizzes__test__section").order_by("-created_at").first()
        kwargs["has_results"] = False

        if kwargs["quiz_set"]:
            kwargs["has_results"] = True
            for quiz in kwargs["quiz_set"].quizzes.all():
                quiz.stats = {
                    "row": {
                        "max": quiz.test.max_score(),
                        "score": 0,
                        "progress": tight_dumps(results_progress(quiz.test.section, self.request.user)),
                        "colors": tight_dumps([ quiz.test.section.fg_color(), quiz.test.section.bg_color() ]),
                    },
                }
                if quiz.is_finished:
                    quiz.stats["row"]["score"] = quiz.score()

                quiz.stats["row"]["avg"] = average_score(quiz.test.section)

        else:
            kwargs["quiz_set"] = {
                "is_current": False,
                "quizzes": {
                    "all": [],
                },
                "test_domain": {
                    "name": pgettext("/student/", "Test Domain 1"),
                },
            }
            kwargs["quiz_set"]["quizzes"]["all"].append({
                "test": {
                    "section": {
                        "name": pgettext("/student/", "Section 1"),
                    },
                    "code": "45AD",
                },
                "is_finished": True,
                "stats": {
                    "row": {
                        "max": 400,
                        "score": 340,
                        "colors": [ GOOGLE_COLORS[0], GOOGLE_COLORS_BLEACHED[0] ],
                        "avg": 350,
                        "progress": [ 275, 250, 375, 325, 350, 300, 325, 400, 350, 375 ],
                    },
                },
            })
            kwargs["quiz_set"]["quizzes"]["all"].append({
                "test": {
                    "section": {
                        "name": pgettext("/student/", "Section 2"),
                    },
                    "code": "F4B1",
                },
                "is_finished": True,
                "stats": {
                    "row": {
                        "max": 200,
                        "score": 190,
                        "colors": [ GOOGLE_COLORS[1], GOOGLE_COLORS_BLEACHED[1] ],
                        "avg": 175,
                        "progress": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                    },
                },
            })
            kwargs["quiz_set"]["quizzes"]["all"].append({
                "test": {
                    "section": {
                        "name": pgettext("/student/", "Section 3"),
                    },
                    "code": "8C73",
                },
                "is_finished": True,
                "stats": {
                    "row": {
                        "max": 200,
                        "score": 160,
                        "colors": [ GOOGLE_COLORS[2], GOOGLE_COLORS_BLEACHED[2] ],
                        "avg": 180,
                        "progress": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                    },
                },
            })
            kwargs["quiz_set"]["quizzes"]["all"].append({
                "test": {
                    "section": {
                        "name": pgettext("/student/", "Section 4"),
                    },
                    "code": "14EF",
                },
                "is_finished": True,
                "stats": {
                    "row": {
                        "max": 600,
                        "score": 520,
                        "colors": [ GOOGLE_COLORS[3], GOOGLE_COLORS_BLEACHED[3] ],
                        "avg": 490,
                        "progress": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                    },
                },
            })

        return super().get_context_data(**kwargs)
