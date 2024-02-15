from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.urls import reverse
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.auth.mixins import SuperPermissionRequiredMixin, ExpertPermissionRequiredMixin, StaffPermissionRequiredMixin
from bbtest.models import Test, TestQuestion


class QuestionView(StaffPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "testbank/questions.html"

    def get_context_data(self, **kwargs):
        
        if self.request.user.has_perm("bbtest.super"):
            questions = TestQuestion.objects.select_related("section__domain", "developer").order_by("-created_at") # .order_by("taxonomy") #
        elif self.request.user.has_perm("bbtest.expert"):
            section_list = self.request.user.expert_profile.section.all()
            questions = TestQuestion.objects.filter(section__in=section_list).select_related("section__domain", "developer").order_by("-created_at")
        elif self.request.user.has_perm("bbtest.admin"):
            questions = TestQuestion.objects.select_related("section__domain", "developer").order_by("-created_at")
        elif self.request.user.has_perm("bbtest.developer"):
            questions = TestQuestion.objects.select_related("section__domain", "developer").order_by("-created_at").filter(developer = self.request.user)
        else:
            raise PermissionDenied()

        
        kwargs["q"] = ""
        # try:    
        #     tests = tests.filter(
        #         Q(developer__first_name__icontains=self.request.GET["q"])
        #         |
        #         Q(developer__last_name__icontains=self.request.GET["q"])
        #         |
        #         Q(developer__email__icontains=self.request.GET["q"])
        #         |
        #         Q(code__iexact=self.request.GET["q"])
        #     )
        #     kwargs["q"] = self.request.GET["q"]
        # except KeyError:
        #     pass


        paginator = Paginator(questions, 25)
        try:
            kwargs["questions"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["questions"] = paginator.page(1)
        except EmptyPage:
            kwargs["questions"] = paginator.page(paginator.num_pages)

        paginator.page_indexes = self.page_indexes(kwargs["questions"], 5)


        if self.request.user.has_perm("bbtest.super"):
            kwargs["question_page_redirect"] = reverse("bbtest:super_tests")
        elif self.request.user.has_perm("bbtest.expert"):
            kwargs["question_page_redirect"] = reverse("bbtest:expert_dashboard")
        elif self.request.user.has_perm("bbtest.admin"):
            kwargs["question_page_redirect"] = reverse("bbtest:admin_dashboard")
        elif self.request.user.has_perm("bbtest.developer"):
            kwargs["question_page_redirect"] = reverse("bbtest:developer_dashboard")

        if self.request.GET.get("page"):
            kwargs["question_page_redirect"] = "%s?page=%s" % (kwargs["question_page_redirect"], self.request.GET.get("page"))


        # for test in kwargs["tests"]:
        #     test.display_language = ""
        #     if test.language != Test.LANGUAGE_XX:
        #         test.display_language = next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == test.language)

        return super().get_context_data(**kwargs)
