from django.views.generic import TemplateView, RedirectView, FormView
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.urls import reverse
from urllib.parse import urlencode
from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.forms.user import SettingsForm
from bbtest.forms.subscription import SubscriptionForm


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
        self.url = resolve_url(self.request.user)
        return super().get_redirect_url(*args, **kwargs)


class SettingsView(LoginRequiredMixin, FormView):
    template_name = "settings.html"
    form_class = SettingsForm
    success_url = reverse_lazy("bbtest:dashboard")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            "instance": self.request.user,
        })
        return kwargs

    def form_valid(self, form):
        login(self.request, form.save())
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        if "template_name" not in kwargs:
            if self.request.user.has_perm("bbtest.super"):
                kwargs["template_name"] = "./super/super_base_2.html"
            elif self.request.user.has_perm("bbtest.admin"):
                kwargs["template_name"] = "./admin/admin_base_2.html"
            elif self.request.user.has_perm("bbtest.developer"):
                kwargs["template_name"] = "./developer/developer_base_2.html"
            elif self.request.user.has_perm("bbtest.student"):
                kwargs["template_name"] = "./student/student_base_2.html"
        return super().get_context_data(**kwargs)
