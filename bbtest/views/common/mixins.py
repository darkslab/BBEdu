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


class PaginationMixin:
    def page_indexes(self, page, width):
        if width < 1:
            width = 1
        elif width > page.paginator.num_pages:
            width = page.paginator.num_pages
        padding = (width - 1) // 2
        right_padding = (width - 1) % 2
        indexes = [ page.number ]
        for i in range(padding):
            indexes.insert(0, indexes[0] - 1)
            indexes.append(indexes[-1] + 1)
        for i in range(right_padding):
            indexes.append(indexes[-1] + 1)
        if indexes[0] < 1:
            while True:
                if indexes[0] >= 1:
                    break
                indexes.pop(0)
                indexes.append(indexes[-1] + 1)
        elif indexes[-1] > page.paginator.num_pages:
            while True:
                if indexes[-1] <= page.paginator.num_pages:
                    break
                indexes.pop()
                indexes.insert(0, indexes[0] - 1)
        return indexes
