from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import get_user_model
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin


User = get_user_model()

class UsersView(SuperPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "super/users.html"

    def get_context_data(self, **kwargs):
        paginator = Paginator(
            User.objects.filter(is_superuser=False).order_by("-joined_at").prefetch_related("user_permissions__content_type"),
            25,
        )
        try:
            kwargs["users"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["users"] = paginator.page(1)
        except EmptyPage:
            kwargs["users"] = paginator.page(paginator.num_pages)
        paginator.page_indexes = self.page_indexes(kwargs["users"], 5)

        for user in kwargs["users"]:
            for permission in user.user_permissions.all():
                if permission.content_type.natural_key() == ("bbtest", "user") and permission.codename in ("admin", "developer", "student"):
                    user.role = permission.codename
                    break

        return super().get_context_data(**kwargs)
