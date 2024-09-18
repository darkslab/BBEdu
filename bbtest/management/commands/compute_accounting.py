from django.core.management.base import BaseCommand
from django.core.cache import cache
from collections import OrderedDict
from django.utils.translation import activate, deactivate
from django.utils.translation import ugettext, pgettext_lazy
from bbtest.models import Account
from django.utils.timezone import localtime, now

# run script every day at 4 Am
# crontab -e
# 0 4 * * * /usr/local/bin/python3 ~/BBEdu/manage.py compute_accounting
class Command(BaseCommand):
    help = 'updates trial balance cache' 


    def handle(self, *args, **kwargs):
        balances = {}
        activate("en-us")

        balances["balances_a"] = OrderedDict()
        balances["balances_a"][ugettext("page:/super/trial-balance/:account.cash")]        = Account.objects.get(name="Cash").balance()
        balances["balances_a"][ugettext("page:/super/trial-balance/:account.qazkom")]      = Account.objects.get(name="MerchantFees-Qazkom").balance()
        balances["balances_a"][ugettext("page:/super/trial-balance/:account.beeline")]     = Account.objects.get(name="MerchantFees-Beeline").balance()
        balances["balances_a"][ugettext("page:/super/trial-balance/:account.promo")]       = Account.objects.get(name="Promo-Credits").balance()
        balances["balances_a"][ugettext("page:/super/trial-balance/:account.correction")]  = Account.objects.get(name="Correction-Credits").balance()
        balances["balances_a_sum"] = sum(account_balance for account_name, account_balance in balances["balances_a"].items())

        balances["balances_l"] = OrderedDict()
        balances["balances_l"][ugettext("page:/super/trial-balance/:account.developers")]  = sum(account.balance() for account in Account.objects.filter(name__istartswith="Developer-").all())
        balances["balances_l"][ugettext("page:/super/trial-balance/:account.student")]     = sum(account.balance() for account in Account.objects.filter(name__istartswith="BalanceAccount-").all())
        balances["balances_l"][ugettext("page:/super/trial-balance/:account.nis")]         = Account.objects.get(name="Tests-NIS").balance()
        balances["balances_l"][ugettext("page:/super/trial-balance/:account.unt")]         = Account.objects.get(name="Tests-UNT").balance()
        balances["balances_l"][ugettext("page:/super/trial-balance/:account.nufypet")]     = Account.objects.get(name="Tests-NUFYPET").balance()
        balances["balances_l"][ugettext("page:/super/trial-balance/:account.law")]         = Account.objects.get(name="Tests-LAW").balance()
        balances["balances_l"][ugettext("page:/super/trial-balance/:account.proftest")]    = Account.objects.get(name="Tests-PROFTEST").balance()
        balances["balances_l"][ugettext("page:/super/trial-balance/:account.nqt")]         = Account.objects.get(name="Tests-NQT").balance()
        balances["balances_l"][ugettext("page:/super/trial-balance/:account.fizmat")]      = Account.objects.get(name="Tests-FIZMAT").balance()
        balances["balances_l_sum"] = sum(account_balance for account_name, account_balance in balances["balances_l"].items())

        balances["has_errors"] = Account.objects.has_errors()
        balances["last_cached"] = now()

        deactivate()
        cache.set("balances", balances, 3600*25)

        # print(balances)
