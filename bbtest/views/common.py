from django.views.generic import TemplateView
from bbtest.auth.views import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = "home.html"

class TestView(LoginRequiredMixin, TemplateView):
    template_name = "test.html"
