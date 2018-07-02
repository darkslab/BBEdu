from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from bbtest.models import DeveloperAcknowledgement


class DeveloperAcknowledgementRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("bbtest.super") or DeveloperAcknowledgement.objects.filter(developer=self.request.user).exists():
            return super().dispatch(request, *args, **kwargs)
        if request.is_ajax():
            raise PermissionDenied("Permission denied for AJAX call")
        return redirect("bbtest:developer_acknowledgement")


class DeveloperUnacceptedAcknowledgementRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("bbtest.super") and not DeveloperAcknowledgement.objects.filter(developer=self.request.user).exists():
            return super().dispatch(request, *args, **kwargs)
        if request.is_ajax():
            raise PermissionDenied("Permission denied for AJAX call")
        return redirect("bbtest:developer_tests")
