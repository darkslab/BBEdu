class UserContextMixin:
    def get_context_data(self, **kwargs):
        if self.__is_student():
            kwargs["balance_account_total"] = self.request.user.balance_account().balance()

        if self.__is_student():
            kwargs["has_exam"] = True
            if not hasattr(self, "quiz_set") and not self.request.user.quiz_sets.filter(is_current=True).exists():
                kwargs["has_exam"] = False

        return super().get_context_data(**kwargs)

    def __is_student(self):
        if self.request.user.is_superuser:
            return False
        return self.request.user.has_perm("bbtest.student")
