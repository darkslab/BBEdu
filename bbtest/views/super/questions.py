from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.urls import reverse
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.auth.mixins import SuperPermissionRequiredMixin, ExpertPermissionRequiredMixin, StaffPermissionRequiredMixin
from bbtest.models import Test


class QuestionView(StaffPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "super/tests.html"

    def get_context_data(self, **kwargs):
        
        if self.request.user.has_perm("bbtest.super") or self.request.user.has_perm("bbtest.admin"):
            tests = Test.objects.select_related("section__domain", "developer").order_by("-created_at")
        elif self.request.user.has_perm("bbtest.expert"):
            section_list = self.request.user.expert_profile.section.all()
            tests = Test.objects.filter(section__in=section_list).select_related("section__domain", "developer").order_by("-created_at")

        kwargs["q"] = ""
        try:    
            tests = tests.filter(
                Q(developer__first_name__icontains=self.request.GET["q"])
                |
                Q(developer__last_name__icontains=self.request.GET["q"])
                |
                Q(developer__email__icontains=self.request.GET["q"])
                |
                Q(code__iexact=self.request.GET["q"])
            )
            kwargs["q"] = self.request.GET["q"]
        except KeyError:
            pass

        paginator = Paginator(tests, 25)
        try:
            kwargs["tests"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["tests"] = paginator.page(1)
        except EmptyPage:
            kwargs["tests"] = paginator.page(paginator.num_pages)
        paginator.page_indexes = self.page_indexes(kwargs["tests"], 5)

        kwargs["test_page_redirect"] = reverse("bbtest:super_tests")
        if self.request.GET.get("page"):
            if self.request.user.has_perm("bbtest.super"):
                kwargs["test_page_redirect"] = "%s?page=%s" % (reverse("bbtest:super_tests"), self.request.GET.get("page"))
            elif self.request.user.has_perm("bbtest.expert"):
                kwargs["test_page_redirect"] = "%s?page=%s" % (reverse("bbtest:expert_dashboard"), self.request.GET.get("page"))
            elif self.request.user.has_perm("bbtest.admin"):
                kwargs["test_page_redirect"] = "%s?page=%s" % (reverse("bbtest:admin_dashboard"), self.request.GET.get("page"))

        for test in kwargs["tests"]:
            test.display_language = ""
            if test.language != Test.LANGUAGE_XX:
                test.display_language = next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == test.language)

        return super().get_context_data(**kwargs)
