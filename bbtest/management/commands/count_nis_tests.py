from django.core.management.base import BaseCommand
from decimal import Decimal
from bbtest.models import Test, BundleNISItem



class Command(BaseCommand):
    help = 'generate NIS bundles from existing tests' 


    def handle(self, *args, **kwargs):

        count = {}

        for ob in Test.objects.all():
            if ob.status == 2 and ob.section.domain.order == 0:  # test is developed and NIS
                key = "{}_{}".format(ob.language, ob.section)
                count[key] = count.get(key, 0) + 1

        for section, n in sorted(count.items()):
            print("{}: {:2}".format(section, n))