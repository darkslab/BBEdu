from django.shortcuts import resolve_url
from django.urls import reverse
from django.contrib.auth import login
from urllib.parse import urlencode
from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.views.generic import FormView, RedirectView
from bbtest.forms.user import SettingsForm
from bbtest.forms.subscription import SubscriptionForm


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
