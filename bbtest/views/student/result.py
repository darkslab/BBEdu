from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.utils.json import tight_dumps


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

            # DARK_TODO  implement this!
            for quiz in quiz_set.quizzes.all():
                quiz.stats = {
                    "row": {
                        "max": 400,
                        "color": "#3366cc",
                        "score": 350,
                        "avg": 300,
                        "progress": tight_dumps([ 350, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]),
                    },
                    "detail": {},
                }

        return super().get_context_data(**kwargs)
