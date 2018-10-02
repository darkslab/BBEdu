from django.contrib.auth import get_user_model
from django.db.models import Count
from django.http import HttpResponse
from django.utils.timezone import localtime
import csv
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin
from bbtest.models import Subscription, Test


User = get_user_model()

class DashboardView(SuperPermissionRequiredMixin, UserContextMixin, TemplateView):
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

        kwargs["superuser_tests_count"] = Test.objects.filter(developer__is_superuser=True).count()

        kwargs["subscriptions_total"] = Subscription.objects.count()
        kwargs["subscriptions_last"] = Subscription.objects.order_by("-created_at").first()

        return super().get_context_data(**kwargs)


class DownloadSubscriptionListView(SuperPermissionRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=\"subscription-list.csv\""

        subscription_list = csv.writer(response)
        subscription_list.writerow(["Email", "Time"])
        for entry in Subscription.objects.order_by("created_at").all():
            subscription_list.writerow([
                entry.email,
                localtime(entry.created_at).strftime("%Y-%m-%d %H:%M:%S"),
            ])

        return response
