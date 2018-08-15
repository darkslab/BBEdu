from django.shortcuts import resolve_url, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from urllib.parse import urlencode
from decimal import Decimal
from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.views.generic import FormView, RedirectView, TemplateView, View
from bbtest.views.common import UserContextMixin
from bbtest.forms.user import SettingsForm
from bbtest.forms.subscription import SubscriptionForm
from bbtest.forms.base import BuyCreditsForm
from bbtest.payment_processors import FirstQazkomPaymentProcessor, PaymentProcessorError
from bbtest.models.shopping.handle import CartHandleAccessMixin, CartHandle
from bbtest.models.shopping.items import CreditItem
from bbtest.models.shopping.operate import charge
from bbtest.models import Cart


class HomeView(FormView):
    template_name = "home.html"
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


class SettingsView(LoginRequiredMixin, UserContextMixin, FormView):
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


class BuyCreditsView(LoginRequiredMixin, CartHandleAccessMixin, UserContextMixin, FormView):
    template_name = "base/buy_credits.html"
    form_class = BuyCreditsForm
    success_url = reverse_lazy("bbtest:buy_credits_qazkom")

    def get_initial(self):
        amount = Decimal("0.00")
        for item in self.cart_handle():
            if isinstance(item, CreditItem):
                amount += item.total()
        if amount.is_zero():
            amount = Decimal("1000.00")
        return {
            "amount": int(amount),
        }

    def form_valid(self, form):
        credit_item = None
        old_items = []
        for item in self.cart_handle():
            if isinstance(item, CreditItem):
                credit_item = item
            else:
                old_items.append({
                    "item_class": type(item).__name__,
                    "meta_data": item.meta_data(),
                })
        self.cart_handle().empty()

        amount = Decimal(form.cleaned_data["amount"])
        if credit_item is None:
            credit_item = CreditItem(self.cart_handle(), amount, self.request.user)
        credit_item.set_amount(amount)
        self.cart_handle().save()

        self.request.session["cart_type"] = "credits"
        if len(old_items):
            self.request.session["cart_old_items"] = old_items

        return super().form_valid(form)


class BuyCreditsQazkomView(LoginRequiredMixin, CartHandleAccessMixin, UserContextMixin, TemplateView):
    template_name = "base/buy_credits_qazkom.html"

    def get(self, request, *args, **kwargs):
        should_redirect = True
        for item in self.cart_handle():
            if not isinstance(item, CreditItem):
                should_redirect = True
                break
            should_redirect = False
        if should_redirect:
            return redirect("bbtest:buy_credits")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["qazkom_form"] = {
            "action": FirstQazkomPaymentProcessor.post_url(test=settings.DEBUG),
            "signed_order_b64": FirstQazkomPaymentProcessor.encoded_order(self.cart_handle()),
            "appendix": FirstQazkomPaymentProcessor.encoded_appendix(self.cart_handle()),
            "language": "",
        }
        if get_language() == settings.BB_LANGUAGE_CODE_KK:
            kwargs["qazkom_form"]["language"] = "kaz"
        elif get_language() == settings.BB_LANGUAGE_CODE_RU:
            kwargs["qazkom_form"]["language"] = "rus"

        return super().get_context_data(**kwargs)


@method_decorator(csrf_exempt, name="dispatch")
class ProcessCreditsQazkomView(View):
    def post(self, request, *args, **kwargs):
        try:
            handle = CartHandle(Cart.objects.get(pk=FirstQazkomPaymentProcessor.order_id(self.request.POST["response"])))

            incorrect_cart = True
            for item in handle:
                if not isinstance(item, CreditItem):
                    incorrect_cart = True
                    break
                incorrect_cart = False
            if incorrect_cart:
                raise PaymentProcessorError("Working on incorrect cart")

            charge(
                FirstQazkomPaymentProcessor(handle.total(), self.request.POST["response"]),
                handle,
            )
        except Cart.DoesNotExist as error:
            raise PaymentProcessorError(str(error))

        return HttpResponse("0", content_type="text/plain")


class TermsView(TemplateView):
    template_name = "base/terms.html"


class ContactUsView(FormView):
    template_name = "base/contact_us.html"
