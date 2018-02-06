from django.contrib.auth import get_user_model
from django.db.models import Count
from bbtest.auth.mixins import SuperLoginRequiredMixin
from bbtest.views.generic import TemplateView
from bbtest.models import Subscription


User = get_user_model()

class DashboardView(SuperLoginRequiredMixin, TemplateView):
    template_name = "super/dashboard.html"

    def get_context_data(self, **kwargs):
        kwargs["student_count"] = User.active_users.filter(user_permissions__codename="student").count()
        kwargs["developer_count"] = User.active_users.filter(user_permissions__codename="developer").count()
        kwargs["admin_count"] = User.active_users.filter(user_permissions__codename="admin").count()
        kwargs["super_count"] = User.active_users.filter(is_superuser=True).count()

        kwargs["developer_stats"] = User.active_users.filter(
            user_permissions__codename="developer",
        ).annotate(
            tests_count=Count("tests"),
        ).order_by("last_name")

        kwargs["subscriptions_total"] = Subscription.objects.count()
        kwargs["subscriptions_last"] = Subscription.objects.order_by("-created_at").first()

        return super().get_context_data(**kwargs)
