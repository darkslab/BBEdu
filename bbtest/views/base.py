from django.shortcuts import resolve_url, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.messages import success
from django.utils.translation import pgettext
from django.core.cache import cache
from urllib.parse import urlencode
from decimal import Decimal
from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.views.generic import FormView, RedirectView, TemplateView, View
from bbtest.views.common import UserContextMixin
from bbtest.forms.user import SettingsForm
from bbtest.forms.base import BuyCreditsForm
from bbtest.forms.message import MessageForm
from bbtest.payment_processors import FirstQazkomPaymentProcessor, PaymentProcessorError
from bbtest.models.shopping.handle import CartHandleAccessMixin, CartHandle
from bbtest.models.shopping.items import CreditItem
from bbtest.models.shopping.operate import charge
from bbtest.models import Cart, TestDomain
from bbtest.texts import FAQ_TEXTS


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        for domain in TestDomain.objects.all():
            if domain.pk == 7911:
                kwargs["nis"] = domain
            elif domain.pk == 7912:
                kwargs["unt"] = domain
            elif domain.pk == 7913:
                kwargs["nufypet"] = domain
        return super().get_context_data(**kwargs)


class NisView(TemplateView):
    template_name = "nis.html"

    def get_context_data(self, **kwargs):
        for domain in TestDomain.objects.all():
            if domain.pk == 7911:
                kwargs["nis"] = domain
        return super().get_context_data(**kwargs)


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

    def form_valid(self, form):
        old_items = []
        for item in self.cart_handle():
            if not isinstance(item, CreditItem):
                old_items.append({
                    "item_class": type(item).__name__,
                    "meta_data": item.meta_data(),
                })
        self.cart_handle().empty()

        CreditItem(self.cart_handle(), Decimal(form.cleaned_data["amount"]), self.request.user)
        self.cart_handle().save()

        cache_cart_timeout = 86400
        cache.set("cart-type-%s" % self.request.user.pk, "credits", cache_cart_timeout)
        if len(old_items):
            cache.set("cart-old-items-%s" % self.request.user.pk, old_items, cache_cart_timeout)

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
            "action": FirstQazkomPaymentProcessor.post_url(test=(settings.DEBUG or settings.STAGING)),
            "signed_order_b64": FirstQazkomPaymentProcessor.encoded_order(self.cart_handle()),
            "appendix": FirstQazkomPaymentProcessor.encoded_appendix(self.cart_handle()),
            "language": "",
        }
        if get_language() == settings.BB_LANGUAGE_CODE_KK:
            kwargs["qazkom_form"]["language"] = "kaz"
        elif get_language() == settings.BB_LANGUAGE_CODE_RU:
            kwargs["qazkom_form"]["language"] = "rus"

        kwargs["cart_rounded_total"] = round(self.cart_handle().total())

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

            payment_processor = FirstQazkomPaymentProcessor(handle.total(), self.request.POST["response"])
            if settings.DEBUG or settings.STAGING:
                payment_processor.set_test()

            charge(
                payment_processor,
                handle,
            )
        except Cart.DoesNotExist as error:
            raise PaymentProcessorError(str(error))

        return HttpResponse("0", content_type="text/plain")


class TermsView(TemplateView):
    template_name = "base/terms.html"


class ContactUsView(FormView):
    template_name = "base/contact_us.html"
    form_class = MessageForm
    success_url = reverse_lazy("bbtest:contact_us")

    def get_context_data(self, **kwargs):
        kwargs["recaptcha_site_key"] = settings.RECAPTCHA_SITE_KEY
        kwargs["recaptcha_secret_key"] = settings.RECAPTCHA_SECRET_KEY
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        success(self.request, pgettext("Success alert message", "Thank you. We have received your message and we will get back to you as soon as possible."))
        return super().form_valid(form)


class FaqView(TemplateView):
    template_name = "base/faq.html"

    def get_context_data(self, **kwargs):
        kwargs["texts"] = FAQ_TEXTS[get_language()]
        return super().get_context_data(**kwargs)
