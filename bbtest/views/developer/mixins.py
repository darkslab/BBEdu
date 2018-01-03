from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from bbtest.models import DeveloperAcknowledgement


class DeveloperAcknowledgementRequiredMixin:
    unaccepted_acknowledgement_redirect_urlpattern = None

    def dispatch(self, request, *args, **kwargs):
        if DeveloperAcknowledgement.objects.filter(developer=self.request.user).exists():
            return super().dispatch(request, *args, **kwargs)
        if self.unaccepted_acknowledgement_redirect_urlpattern is None:
            raise ImproperlyConfigured("No URL to redirect to. Provide a unaccepted_acknowledgement_redirect_urlpattern.")
        return redirect(self.unaccepted_acknowledgement_redirect_urlpattern)


class DeveloperUnacceptedAcknowledgementRequiredMixin:
    accepted_acknowledgement_redirect_urlpattern = None

    def dispatch(self, request, *args, **kwargs):
        if not DeveloperAcknowledgement.objects.filter(developer=self.request.user).exists():
            return super().dispatch(request, *args, **kwargs)
        if self.accepted_acknowledgement_redirect_urlpattern is None:
            raise ImproperlyConfigured("No URL to redirect to. Provide a accepted_acknowledgement_redirect_urlpattern.")
        return redirect(self.accepted_acknowledgement_redirect_urlpattern)
