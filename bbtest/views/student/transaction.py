from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Prefetch
from django.utils.translation import ugettext as _, pgettext
from decimal import Decimal
from django.shortcuts import get_object_or_404
from bbtest.views.generic import TemplateView
from bbtest.views.common import UserContextMixin, PaginationMixin
from bbtest.auth.mixins import StudentPermissionRequiredMixin
from bbtest.models import LineItem, Test
from bbtest.models.shopping.items import CreditItem
from bbtest.models.shopping.items.test import TestItem


def prepare_carts(carts):
    test_ids = set()
    for cart in carts:
        for line_item in cart.line_items.all():
            if not issubclass(line_item.item_class_class(), TestItem):
                continue
            test_ids.add(line_item.meta_data["test_id"])
    test_display_descriptions = {}
    for test in Test.objects.filter(pk__in=test_ids).select_related("section__domain"):
        if test.language != Test.LANGUAGE_XX:
            test_display_descriptions[test.pk] = pgettext("/student/transactions/xxxx/", "%(section)s (%(domain)s) - %(language)s") % {
                "section": _(test.section.name),
                "domain": _(test.section.domain.name),
                "language": next(test_language[1] for test_language in Test.LANGUAGES if test_language[0] == test.language),
            }
        else:
            test_display_descriptions[test.pk] = pgettext("/student/transactions/xxxx/", "%(section)s (%(domain)s)") % {
                "section": _(test.section.name),
                "domain": _(test.section.domain.name),
            }

    cart.total = Decimal("0.00")
    cart.actual_money = False
    for cart in carts:
        for line_item in cart.line_items.all():
            cart.total = cart.total + line_item.price - line_item.discount
            if issubclass(line_item.item_class_class(), CreditItem):
                cart.actual_money = True
                line_item.display_description = pgettext("/student/transactions/xxxx/", "%(credits).0f Credits") % {
                    "credits": line_item.price,
                }
            elif issubclass(line_item.item_class_class(), TestItem):
                line_item.display_description = test_display_descriptions[line_item.meta_data["test_id"]]
        cart.total -= cart.discount


class TransactionsView(StudentPermissionRequiredMixin, UserContextMixin, PaginationMixin, TemplateView):
    template_name = "student/transactions/base.html"

    def get_context_data(self, **kwargs):
        paginator = Paginator(
            self.request.user.carts.filter(is_current=None).order_by("-completed_at").prefetch_related(
                Prefetch("line_items", queryset=LineItem.objects.order_by("pk").all())
            ).all(),
            10,
        )
        try:
            kwargs["carts"] = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            kwargs["carts"] = paginator.page(1)
        except EmptyPage:
            kwargs["carts"] = paginator.page(paginator.num_pages)
        paginator.page_indexes = self.page_indexes(kwargs["carts"], 5)

        prepare_carts(kwargs["carts"])

        return super().get_context_data(**kwargs)


class TransactionView(StudentPermissionRequiredMixin, UserContextMixin, TemplateView):
    template_name = "student/transaction.html"

    def get_context_data(self, **kwargs):
        carts = [ get_object_or_404(self.request.user.carts.filter(is_current=None).prefetch_related(
            Prefetch("line_items", queryset=LineItem.objects.order_by("pk").all())
        ).all(), pk=self.kwargs["transaction_id"]) ]

        prepare_carts(carts)
        kwargs["cart"] = carts[0]

        return super().get_context_data(**kwargs)
