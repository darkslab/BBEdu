class UserContextMixin:
    def get_context_data(self, **kwargs):
        if self.request.user.has_perm("bbtest.student"):
            kwargs["balance_account_total"] = self.request.user.balance_account().balance()
        return super().get_context_data(**kwargs)
