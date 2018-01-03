from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from bbtest.auth.mixins import DeveloperLoginRequiredMixin
from bbtest.forms.acknowledgement import DeveloperAcknowledgementForm
from bbtest.models import DeveloperAcknowledgement
from .mixins import DeveloperUnacceptedAcknowledgementRequiredMixin


class AcknowledgementView(DeveloperLoginRequiredMixin, DeveloperUnacceptedAcknowledgementRequiredMixin, FormView):
    template_name = "developer/acknowledgement.html"
    form_class = DeveloperAcknowledgementForm
    success_url = reverse_lazy("bbtest:developer_tests")
    accepted_acknowledgement_redirect_urlpattern = "bbtest:developer_tests"

    def get_context_data(self, **kwargs):
        kwargs["plan_a"] = {
            "name": DeveloperAcknowledgement.PLANS[0][1],
            "value": DeveloperAcknowledgement.PLANS[0][0],
        }
        kwargs["plan_b"] = {
            "name": DeveloperAcknowledgement.PLANS[1][1],
            "value": DeveloperAcknowledgement.PLANS[1][0],
        }
        kwargs["plan_c"] = {
            "name": DeveloperAcknowledgement.PLANS[2][1],
            "value": DeveloperAcknowledgement.PLANS[2][0],
        }
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.make_acknowledgement(self.request)
        return super().form_valid(form)
