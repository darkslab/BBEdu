from django.core.management.base import BaseCommand

from bbtest.models import TestQuestion


class Command(BaseCommand):
    help = 'assign code to questions based on template' 


    def handle(self, *args, **kwargs):
        # clear previous assignments
        for obj in TestQuestion.objects.all():
            obj.code = obj.pk
            obj.save()

        res = ""
        for obj in TestQuestion.objects.order_by("created_at").all():
            try: 
                int(obj.code)
            except ValueError:
                continue
            index = TestQuestion.objects.filter(created_at__year=obj.created_at.year, section=obj.section, code__icontains=obj.section.code).count()
            code="{}{:%y}{:04}".format(obj.section.code, obj.created_at, index)
            res += str(obj.code) + " vs " + code + "\n"
            obj.code = code
            obj.save()


        print(res)


