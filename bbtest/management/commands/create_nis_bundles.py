from django.core.management.base import BaseCommand
from decimal import Decimal
from bbtest.models import Test, BundleNISItem



class Command(BaseCommand):
    help = 'generate NIS bundles from existing tests' 


    def handle(self, *args, **kwargs):

        count = {"ru": {}, "kk": {}, "xx": {}}

        for ob in Test.objects.all():
            if ob.status == 2 and ob.section.domain.order == 0:  # test is developed and NIS
                sec = str(ob.section)
                lang = str(ob.language)
                count_lang = count[lang]
                count_lang[sec] = count_lang.get(sec, []) + [ob]

        
        for k, v in count["ru"].items():
            print(k, v)

        for i in range(2):
            lang = "ru"
            BundleNISItem.objects.create(
                math =       count[lang]["Mathematics"][i],
                quantative = count[lang]["Quantitative"][i],
                rus =        count[lang]["Russian Language"][i],
                kaz =        count[lang]["Kazakh Language"][i],
                eng =        count["xx"]["English Language"][i],
                natural =    count[lang]["Natural Science"][i],
                language =   lang    
            )
        for i in range(2):
            lang = "kk"
            BundleNISItem.objects.create(
                math =       count[lang]["Mathematics"][i],
                quantative = count[lang]["Quantitative"][i],
                rus =        count[lang]["Russian Language"][i],
                kaz =        count[lang]["Kazakh Language"][i],
                eng =        count["xx"]["English Language"][i+2],
                natural =    count[lang]["Natural Science"][i],
                language =   lang    
            )