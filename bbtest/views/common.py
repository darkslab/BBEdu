from django.views.generic import TemplateView
from bbtest.auth.mixins import LoginRequiredMixin, StudentLoginRequiredMixin


class HomeView(TemplateView):
    template_name = "home.html"

class TestView(StudentLoginRequiredMixin, TemplateView):
    template_name = "test.html"
