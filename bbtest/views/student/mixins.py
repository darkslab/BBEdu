from django.shortcuts import redirect


class CurrentQuizSetRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.quiz_set() is None:
            return redirect("bbtest:student_buy_test_domains")
        return super().dispatch(request, *args, **kwargs)

    def quiz_set(self):
        try:
            self.__quiz_set
        except AttributeError:
            self.__quiz_set = self.request.user.quiz_sets.filter(is_current=True).select_related("test_domain").first()
        return self.__quiz_set


class NonCurrentQuizSetRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.quiz_sets.filter(is_current=True).exists():
            return redirect("bbtest:student_exam")
        return super().dispatch(request, *args, **kwargs)
