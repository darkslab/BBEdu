from bbtest.models import TestQuestion, TestParagraph
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Runs Kaspi QR payment email service'

    def handle(self, *args, **kwargs):
        TestQuestion.objects.update(has_periodic_table=False, has_calculator=False)
        TestQuestion.objects.filter(paragraphs__paragraph_class=TestParagraph.PARAGRAPH_CLASS_PERIODIC_TABLE).update(has_periodic_table=True)
        TestQuestion.objects.filter(paragraphs__paragraph_class=TestParagraph.PARAGRAPH_CLASS_CALCULATOR).update(has_calculator=True)