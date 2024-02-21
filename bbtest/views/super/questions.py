from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.urls import reverse
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.auth.mixins import SuperPermissionRequiredMixin, ExpertPermissionRequiredMixin, StaffPermissionRequiredMixin
from bbtest.models import Test, TestQuestion


from bbtest.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()


class QuestionView(StaffPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "testbank/questions.html"

    def get_context_data(self, **kwargs):
        
        if self.request.user.has_perm("bbtest.super"):
            questions = TestQuestion.objects.select_related("section__domain", "developer") # .order_by("-created_at") # .order_by("taxonomy") #
        elif self.request.user.has_perm("bbtest.expert"):
            if self.request.user.expert_profile.permission_all:
                questions = TestQuestion.objects.select_related("section__domain", "developer") #.order_by("-created_at")
            else:
                section_list = self.request.user.expert_profile.section.all()
                questions = TestQuestion.objects.filter(section__in=section_list).select_related("section__domain", "developer") #.order_by("-created_at")
        elif self.request.user.has_perm("bbtest.admin"):
            questions = TestQuestion.objects.select_related("section__domain", "developer")  #.order_by("-created_at")
        elif self.request.user.has_perm("bbtest.developer"):
            questions = TestQuestion.objects.select_related("section__domain", "developer").filter(developer = self.request.user)  # .order_by("-created_at")
        else:
            raise PermissionDenied()

        kwargs["statuses"] = [[str(a), b] for a,b in TestQuestion.STATUSES]

        print("self.request.GET", self.request.GET)

        kwargs["question_id"] = self.request.GET.get("question_id", "")
        kwargs["filter_status"] = self.request.GET.get("filter_status", "")
        kwargs["order_by"] = self.request.GET.get("order_by", "")
        kwargs["filter_developer"] = self.request.GET.get("filter_developer", "")
        kwargs["filter_with_comments"] = self.request.GET.get("filter_with_comments", "")
        

        if kwargs["question_id"]:
            questions = questions.filter(code__icontains=kwargs["question_id"] )

        if kwargs["filter_status"]:
            kwargs["filter_status"] = str(kwargs["filter_status"])
            questions = questions.filter(status=kwargs["filter_status"] )

        if kwargs["filter_with_comments"]:
            questions = questions.filter(comments__isnull=False).distinct()

        developers_ids = questions.values_list('developer', flat=True).distinct()
        kwargs["developers_options"] =  list(User.objects.filter(id__in=developers_ids))
        # print(kwargs["developers_options"])

        if kwargs["order_by"] == "time":
            questions = questions.order_by("-created_at")
        elif kwargs["order_by"] == "comment":
            questions = questions.order_by("-last_comment_at")
        elif kwargs["order_by"] == "status":
            questions = questions.order_by("status")
        elif kwargs["order_by"] == "id":
            questions = questions.order_by("code")
        elif kwargs["order_by"] == "developer":
            questions = questions.order_by("developer")
        else:
            questions = questions.order_by("-created_at")


        if kwargs["filter_developer"]:
            # kwargs["filter_developer"] = str(kwargs["filter_developer"])
            questions = questions.filter(developer__id=kwargs["filter_developer"] )
        

        paginator = Paginator(questions, 25)
        try:
            kwargs["questions"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["questions"] = paginator.page(1)
        except EmptyPage:
            kwargs["questions"] = paginator.page(paginator.num_pages)

        paginator.page_indexes = self.page_indexes(kwargs["questions"], 9)


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
