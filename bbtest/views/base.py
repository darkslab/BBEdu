from django.views.generic import TemplateView, RedirectView
from django.shortcuts import resolve_url
from bbtest.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = "home.html"


class DashboardView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.url = resolve_url(self.request.user)
        return super().get_redirect_url(*args, **kwargs)
