from django.core.management.base import BaseCommand
from decimal import Decimal
from bbtest.models import Test#, BundleNISItem


map_to_code = {'Natural Science': 9539,
               'Mathematics': 9540, 
               'Kazakh Language': 9541, 
               'Russian Language': 9542, 
               'English Language': 9543,
               'Quantitative': 9544}


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

        for i, v in enumerate(count["xx"]["English Language"]):
            if i % 2:
                count["ru"]["English Language"] = count["ru"].get("English Language", []) + [v]
            else:
                count["kk"]["English Language"] = count["kk"].get("English Language", []) + [v]
            # print(i, v)


        # for k, v in count["ru"].items():
        #     print(k, v)

        final_bundle = {"ru": [], "kk": []}
        for lang in ["ru", "kk"]:
            for bund in range(5):
                tests = {9539: "", 9540: "", 9541: "", 9542: "", 9543: "", 9544: ""}
                for k, v in count[lang].items():
                    try:
                        tests[map_to_code[k]] = str(v[bund])
                    except IndexError:
                        tests[map_to_code[k]] = ""
                final_bundle[lang].append(tests)

            for b in final_bundle[lang]:
                print(b)

        print(final_bundle)
        # for i in range(2):
        #     lang = "ru"
        #     BundleNISItem.objects.create(
        #         math =       count[lang]["Mathematics"][i],
        #         quantative = count[lang]["Quantitative"][i],
        #         rus =        count[lang]["Russian Language"][i],
        #         kaz =        count[lang]["Kazakh Language"][i],
        #         eng =        count["xx"]["English Language"][i],
        #         natural =    count[lang]["Natural Science"][i],
        #         language =   lang    
        #     )
        # for i in range(2):
        #     lang = "kk"
        #     BundleNISItem.objects.create(
        #         math =       count[lang]["Mathematics"][i],
        #         quantative = count[lang]["Quantitative"][i],
        #         rus =        count[lang]["Russian Language"][i],
        #         kaz =        count[lang]["Kazakh Language"][i],
        #         eng =        count["xx"]["English Language"][i+2],
        #         natural =    count[lang]["Natural Science"][i],
        #         language =   lang    
        #     )