from django.shortcuts import redirect


class RunningTestsRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        return super().dispatch(request, *args, **kwargs)


class NonRunningTestsRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        # DARK_TODO  implement this!
        return super().dispatch(request, *args, **kwargs)
