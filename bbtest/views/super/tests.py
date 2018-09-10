from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.models import Test


class TestsView(SuperPermissionRequiredMixin, UserContextMixin, TemplateView):
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
        for test in kwargs["tests"]:
            test.display_language = ""
            if test.language != Test.LANGUAGE_XX:
                test.display_language = next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == test.language)

        return super().get_context_data(**kwargs)
