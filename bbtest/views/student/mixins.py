from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from bbtest.models import Quiz, QuizSet

class CurrentQuizSetRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.quiz_set() is None:
            if request.is_ajax():
                raise PermissionDenied("Permission denied for AJAX call")
            return redirect("bbtest:student_dashboard")
        return super().dispatch(request, *args, **kwargs)

    def quiz_set(self) -> QuizSet:
        try:
            self.__quiz_set
        except AttributeError:
            self.__quiz_set = self.request.user.quiz_sets.filter(is_current=True).select_related("test_domain").first()
        return self.__quiz_set

    def current_quiz(self) -> Quiz:
        try:
            self.__current_quiz
        except AttributeError:
            self.reset_current_quiz()
        return self.__current_quiz

    def reset_current_quiz(self):
        self.__current_quiz = None
        for quiz in self.quiz_set().quizzes.all():
            if quiz.is_finished:
                continue
            self.__current_quiz = quiz
            break


class NonCurrentQuizSetRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.quiz_sets.filter(is_current=True).exists():
            if request.is_ajax():
                raise PermissionDenied("Permission denied for AJAX call")
            return redirect("bbtest:student_exam")
        return super().dispatch(request, *args, **kwargs)
