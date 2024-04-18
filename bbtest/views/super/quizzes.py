from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Prefetch, Q
from django.utils.timezone import now
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.models import QuizSet, Quiz, Test


class QuizzesView(SuperPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "super/quizzes.html"

    def get_context_data(self, **kwargs):
        quiz_sets = QuizSet.objects.select_related(
            "student",
            "test_domain",
        ).prefetch_related(
            Prefetch("quizzes", queryset=Quiz.objects.order_by("-order").select_related("test__section").prefetch_related("test__questions").all()),
        ).order_by("-pk").all()
        kwargs["q"] = ""
        try:
            quiz_sets = quiz_sets.filter(
                Q(student__first_name__icontains=self.request.GET["q"])
                |
                Q(student__last_name__icontains=self.request.GET["q"])
                |
                Q(student__email__icontains=self.request.GET["q"])
                |
                Q(quizzes__test__code__iexact=self.request.GET["q"])
            ).distinct()
            kwargs["q"] = self.request.GET["q"]
        except KeyError:
            pass

        paginator = Paginator(quiz_sets, 25)
        try:
            kwargs["quiz_sets"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["quiz_sets"] = paginator.page(1)
        except EmptyPage:
            kwargs["quiz_sets"] = paginator.page(paginator.num_pages)
        paginator.page_indexes = self.page_indexes(kwargs["quiz_sets"], 5)

        for quiz_set in kwargs["quiz_sets"]:
            for quiz in quiz_set.quizzes.all():
                quiz.test.display_language = ""
                if quiz.test.language != Test.LANGUAGE_XX:
                    quiz.test.display_language = next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == quiz.test.language)
                if quiz.is_finished:
                    final_time = quiz.due_at
                    if quiz.ended_at is not None:
                        final_time = quiz.ended_at
                    quiz.display_finish_minutes = round((final_time - quiz.started_at).total_seconds() / 60)

        kwargs["now_at"] = now()

        return super().get_context_data(**kwargs)
