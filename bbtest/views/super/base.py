from django.contrib.auth import get_user_model
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.utils.timezone import localtime, now
from django.utils.translation import gettext
from django.core.cache import cache
import csv
from collections import OrderedDict
from bbtest.auth.mixins import SuperPermissionRequiredMixin
from bbtest.views.generic import TemplateView, View
from bbtest.views.common import UserContextMixin
from bbtest.models import Subscription, Test, TestSection, Account


User = get_user_model()

class DashboardView(SuperPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "super/dashboard.html"

    def get_context_data(self, **kwargs):
        kwargs["student_count"] = User.active_users.filter(user_permissions__codename="student").count()
        kwargs["developer_count"] = User.active_users.filter(user_permissions__codename="developer").count()
        kwargs["admin_count"] = User.active_users.filter(user_permissions__codename="admin").count()
        kwargs["expert_count"] = User.active_users.filter(user_permissions__codename="expert").count()
        kwargs["demouser_count"] = User.active_users.filter(user_permissions__codename="demouser").count()
        kwargs["B2BTeacher_count"] = User.active_users.filter(user_permissions__codename="B2BTeacher").count()
        kwargs["super_count"] = User.active_users.filter(is_superuser=True).count()

        kwargs["developer_tests_stats"] = User.active_users.filter(user_permissions__codename="developer").order_by("last_name").all()
        for developer in kwargs["developer_tests_stats"]:
            developer.total_tests_count = developer.tests.count()
            developer.approved_tests_count = developer.tests(manager="approved_tests").count()
            developer.pending_tests_count = developer.tests(manager="pending_tests").count()
            developer.draft_tests_count = developer.tests(manager="draft_tests").count()
        kwargs["superuser_tests_stats"] = {
            "total_tests_count": Test.objects.filter(developer__is_superuser=True).count(),
            "approved_tests_count": Test.approved_tests.filter(developer__is_superuser=True).count(),
            "pending_tests_count": Test.pending_tests.filter(developer__is_superuser=True).count(),
            "draft_tests_count": Test.draft_tests.filter(developer__is_superuser=True).count(),
        }

        # kwargs["subscriptions_total"] = Subscription.objects.count()
        # kwargs["subscriptions_last"] = Subscription.objects.order_by("-created_at").first()

        kwargs["tests_demand"] = {
            "nis_sections": TestSection.objects.filter(domain=7911).only("name").all(),
            # "unt_sections": TestSection.objects.filter(domain=7912).only("name").all(),
        }
        for section in kwargs["tests_demand"]["nis_sections"]:
            # if section.pk in (9540, 9541, 9542, 9544, 9566, 9567):
            section.tests_info = []
            counts = section.tests(manager="approved_tests").filter(language=Test.LANGUAGE_KK).values("section").annotate(sales_count_sum=Sum("sales_count"), completed_count_sum=Sum("completed_count")).order_by().all()
            section.tests_info.append({
                "language": Test.LANGUAGE_KK,
                "requires_development": not len(counts),
                "sales_count": counts[0]["sales_count_sum"] if len(counts) else 0,
                "completed_count": counts[0]["completed_count_sum"] if len(counts) else 0,
            })
            counts = section.tests(manager="approved_tests").filter(language=Test.LANGUAGE_RU).values("section").annotate(sales_count_sum=Sum("sales_count"), completed_count_sum=Sum("completed_count")).order_by().all()
            section.tests_info.append({
                "language": Test.LANGUAGE_RU,
                "requires_development": not len(counts),
                "sales_count": counts[0]["sales_count_sum"] if len(counts) else 0,
                "completed_count": counts[0]["completed_count_sum"] if len(counts) else 0,
            })

        sections_with_pending_tests = Test.approved_tests.filter(quizzes__isnull=True).values("section", "language").annotate(count=Count("*")).order_by().all()
        for index, domain_sections in kwargs["tests_demand"].items():
            for section in domain_sections:
                for test_info in section.tests_info:
                    test_info["display_language"] = ""
                    if test_info["language"] != Test.LANGUAGE_XX:
                        test_info["display_language"] = next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == test_info["language"])
                    test_info["queued_for_purchase"] = 0
                    try:
                        test_info["queued_for_purchase"] = next(data for data in sections_with_pending_tests if data["section"] == section.pk and data["language"] == test_info["language"])["count"]
                    except StopIteration:
                        pass

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


class TrialBalanceView(SuperPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "super/trial_balance.html"

    def get_context_data(self, **kwargs):
        balances = cache.get("balances")

        if not balances:
            balances = {}

            balances["balances_a"] = OrderedDict()
            balances["balances_a"][gettext("page:/super/trial-balance/:account.cash")]        = Account.objects.get(name="Cash").balance()
            balances["balances_a"][gettext("page:/super/trial-balance/:account.qazkom")]      = Account.objects.get(name="MerchantFees-Qazkom").balance()
            balances["balances_a"][gettext("page:/super/trial-balance/:account.beeline")]     = Account.objects.get(name="MerchantFees-Beeline").balance()
            balances["balances_a"][gettext("page:/super/trial-balance/:account.promo")]       = Account.objects.get(name="Promo-Credits").balance()
            balances["balances_a"][gettext("page:/super/trial-balance/:account.correction")]  = Account.objects.get(name="Correction-Credits").balance()
            balances["balances_a_sum"] = sum(account_balance for account_name, account_balance in balances["balances_a"].items())

            balances["balances_l"] = OrderedDict()
            balances["balances_l"][gettext("page:/super/trial-balance/:account.developers")]  = sum(account.balance() for account in Account.objects.filter(name__istartswith="Developer-").all())
            balances["balances_l"][gettext("page:/super/trial-balance/:account.student")]     = sum(account.balance() for account in Account.objects.filter(name__istartswith="BalanceAccount-").all())
            balances["balances_l"][gettext("page:/super/trial-balance/:account.nis")]         = Account.objects.get(name="Tests-NIS").balance()
            balances["balances_l"][gettext("page:/super/trial-balance/:account.unt")]         = Account.objects.get(name="Tests-UNT").balance()
            balances["balances_l"][gettext("page:/super/trial-balance/:account.nufypet")]     = Account.objects.get(name="Tests-NUFYPET").balance()
            balances["balances_l"][gettext("page:/super/trial-balance/:account.law")]         = Account.objects.get(name="Tests-LAW").balance()
            balances["balances_l_sum"] = sum(account_balance for account_name, account_balance in balances["balances_l"].items())

            balances["has_errors"] = Account.objects.has_errors()
            balances["last_cached"] = now()

            cache.set("balances", balances, 300)

        kwargs.update(balances)
        return super().get_context_data(**kwargs)
