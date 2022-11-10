from django.core.management.base import BaseCommand
from django.core.cache import cache
from collections import OrderedDict
from django.utils.translation import activate, deactivate
from django.utils.translation import ugettext, pgettext_lazy
from bbtest.models import Subscription, Test, TestSection, Account
from django.utils.timezone import localtime, now
import time


class Command(BaseCommand):
    help = 'help TODO' 


    def handle(self, *args, **kwargs):
        balances = cache.get("balances")
        if not balances:
            balances = {}
            activate("en-us")

            balances["balances_a"] = OrderedDict()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_a"][ugettext("page:/super/trial-balance/:account.cash")]        = Account.objects.get(name="Cash").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_a"][ugettext("page:/super/trial-balance/:account.qazkom")]      = Account.objects.get(name="MerchantFees-Qazkom").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_a"][ugettext("page:/super/trial-balance/:account.beeline")]     = Account.objects.get(name="MerchantFees-Beeline").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_a"][ugettext("page:/super/trial-balance/:account.promo")]       = Account.objects.get(name="Promo-Credits").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_a"][ugettext("page:/super/trial-balance/:account.correction")]  = Account.objects.get(name="Correction-Credits").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_a_sum"] = sum(account_balance for account_name, account_balance in balances["balances_a"].items())
            cache.set("balances_progress", balances, 3600*1)

            balances["balances_l"] = OrderedDict()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_l"][ugettext("page:/super/trial-balance/:account.developers")]  = sum(account.balance() for account in Account.objects.filter(name__istartswith="Developer-").all())
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_l"][ugettext("page:/super/trial-balance/:account.student")]     = sum(account.balance() for account in Account.objects.filter(name__istartswith="BalanceAccount-").all())
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_l"][ugettext("page:/super/trial-balance/:account.nis")]         = Account.objects.get(name="Tests-NIS").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_l"][ugettext("page:/super/trial-balance/:account.unt")]         = Account.objects.get(name="Tests-UNT").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_l"][ugettext("page:/super/trial-balance/:account.nufypet")]     = Account.objects.get(name="Tests-NUFYPET").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_l"][ugettext("page:/super/trial-balance/:account.law")]         = Account.objects.get(name="Tests-LAW").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_l"][ugettext("page:/super/trial-balance/:account.proftest")]    = Account.objects.get(name="Tests-PROFTEST").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_l"][ugettext("page:/super/trial-balance/:account.nqt")]         = Account.objects.get(name="Tests-NQT").balance()
            cache.set("balances_progress", balances, 3600*1)
            balances["balances_l_sum"] = sum(account_balance for account_name, account_balance in balances["balances_l"].items())

            cache.set("balances_progress", balances, 3600*1)
            balances["has_errors"] = Account.objects.has_errors()
            cache.set("balances_progress", balances, 3600*1)
            balances["last_cached"] = now()

            deactivate()
            cache.set("balances", balances, 3600*1)

        # print(balances)
