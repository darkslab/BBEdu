from django.shortcuts import resolve_url
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.conf import settings
from django.http import HttpResponse
from urllib.parse import urlencode
from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.views.generic import FormView, RedirectView, TemplateView, View
from bbtest.forms.user import SettingsForm
from bbtest.forms.subscription import SubscriptionForm
from bbtest.forms.base import BuyCreditsForm
from bbtest.payment_processors import FirstQazkomPaymentProcessor
from bbtest.models.shopping.handle import CartHandle


class HomeView(FormView):
    template_name = "base/home.html"
    form_class = SubscriptionForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return "%s?%s" % (reverse("bbtest:home"), urlencode({
            "subscribed": "true",
        }))


class DashboardView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return resolve_url(self.request.user)


class SettingsView(LoginRequiredMixin, FormView):
    template_name = "base/settings.html"
    form_class = SettingsForm

    def get_success_url(self):
        return resolve_url(self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.request.user
        return kwargs

    def form_valid(self, form):
        login(self.request, form.save())
        return super().form_valid(form)


class BuyCreditsView(LoginRequiredMixin, FormView):
    template_name = "base/buy_credits.html"
    form_class = BuyCreditsForm
    success_url = reverse_lazy("bbtest:buy_credits_qazkom")

    def get_initial(self):
        # DARK_TODO  check cart and put the total or fall back to 1000
        return {
            "amount": 1000,
        }

    def form_valid(self, form):
        # DARK_TODO  massage the cart
        return super().form_valid(form)


class BuyCreditsQazkomView(LoginRequiredMixin, TemplateView):
    template_name = "base/buy_credits_qazkom.html"

    def get_context_data(self, **kwargs):
        handle = CartHandle(self.request.user.cart())
        # DARK_TODO  redirect to BuyCreditsView if cart is empty or doesn't contain CreditItem

        kwargs["qazkom_form"] = {
            "action": FirstQazkomPaymentProcessor.post_url(test=settings.DEBUG),
            "signed_order_b64": FirstQazkomPaymentProcessor.encoded_order(handle),
            "appendix": FirstQazkomPaymentProcessor.encoded_appendix(handle),
            "language": "rus",
        }
        return super().get_context_data(**kwargs)


class ProcessCreditsQazkomView(View):
    def post(self, request, *args, **kwargs):
        # DARK_TODO  process an actual buying part
        return HttpResponse("0", content_type="text/plain")
