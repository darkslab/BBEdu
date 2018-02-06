from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bbtest.views.generic import TemplateView
from bbtest.auth.mixins import SuperLoginRequiredMixin
from bbtest.models import Test


class TestsView(SuperLoginRequiredMixin, TemplateView):
    template_name = "super/tests.html"

    def get_context_data(self, **kwargs):
        tests = Test.objects.select_related("section__domain", "developer").order_by("-created_at")
        paginator = Paginator(tests, 25)

        try:
            kwargs["tests"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["tests"] = paginator.page(1)
        except EmptyPage:
            kwargs["tests"] = paginator.page(paginator.num_pages)

        return super().get_context_data(**kwargs)
