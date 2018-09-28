from django.urls import reverse_lazy
from django.utils.translation import get_language
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin
from bbtest.views.generic import FormView
from bbtest.views.common import UserContextMixin
from bbtest.forms.acknowledgement import DeveloperAcknowledgementForm
from bbtest.models import DeveloperAcknowledgement
from bbtest.texts import DEVELOPER_AGREEMENT_TEXTS
from .mixins import DeveloperUnacceptedAcknowledgementRequiredMixin


AGREEMENT_TEXTS = {
    "plan_a": {
        "kk": "",
        "ru": DEVELOPER_AGREEMENT_TEXTS[DeveloperAcknowledgement.AGREEMENT_CODES_FOR_PLANS[DeveloperAcknowledgement.PLAN_A]]["ru"],
    },
    "plan_c": {
        "kk": "",
        "ru": DEVELOPER_AGREEMENT_TEXTS[DeveloperAcknowledgement.AGREEMENT_CODES_FOR_PLANS[DeveloperAcknowledgement.PLAN_C]]["ru"],
    },
}

class AcknowledgementView(DeveloperPermissionRequiredMixin, DeveloperUnacceptedAcknowledgementRequiredMixin, UserContextMixin, FormView):
    template_name = "developer/acknowledgement.html"
    form_class = DeveloperAcknowledgementForm
    success_url = reverse_lazy("bbtest:developer_tests")

    def get_context_data(self, **kwargs):
        kwargs["plan_a"] = {
            "name": DeveloperAcknowledgement.PLANS[0][1],
            "value": DeveloperAcknowledgement.PLANS[0][0],
            "agreement_text": AGREEMENT_TEXTS["plan_a"][get_language()],
            "agreement_code": DeveloperAcknowledgement.AGREEMENT_CODES_FOR_PLANS[DeveloperAcknowledgement.PLAN_A],
        }
        kwargs["plan_c"] = {
            "name": DeveloperAcknowledgement.PLANS[1][1],
            "value": DeveloperAcknowledgement.PLANS[1][0],
            "agreement_text": AGREEMENT_TEXTS["plan_c"][get_language()],
            "agreement_code": DeveloperAcknowledgement.AGREEMENT_CODES_FOR_PLANS[DeveloperAcknowledgement.PLAN_C],
        }
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.make_acknowledgement(self.request)
        return super().form_valid(form)
