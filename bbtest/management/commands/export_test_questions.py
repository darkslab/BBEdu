from django.core.management.base import BaseCommand
from datetime import datetime
import pytz
from bbtest.models import User
from bbtest.models.test import Test, TestQuestion, TestParagraph
from pprint import pprint

class Command(BaseCommand):
    help = 'export test info' 


    def handle(self, *args, **kwargs):

        test_set = Test.objects.order_by("section").all()
        table = []
        for test_obj in test_set:
            row = [ 
                test_obj.developer.username,
                test_obj.section.domain.name,
                test_obj.section.name,
                test_obj.language,
                test_obj.code,
                str(Test.STATUSES_DICT[test_obj.status]),
                test_obj.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            ]
            table.append(row)

            question_set = test_obj.questions.order_by("order").all()
            for question_obj in question_set:

                row_q = [
                    str(question_obj.order),
                    question_obj.taxonomy.name if question_obj.taxonomy else "",
                    question_obj.topic.name if question_obj.topic else "",
                    question_obj.subtopic.name if question_obj.subtopic else "",
                    question_obj.goal.name if question_obj.goal else "",
                    str(question_obj.answer_class),
                    str(question_obj.meta_data.get("correct_id", None))
                ] 
                
                paragraph_set = question_obj.paragraphs.prefetch_related("through").order_by("through")  # .order_by("order")

                question_text = []
                for paragraph in paragraph_set:
                    # paragraph.meta_data #.get("text", "no text")
                    # row_q.append(paragraph.paragraph_class)
                    # row_q.append(paragraph.meta_data)
                    question_text.append(paragraph.meta_data.get("text", ""))
                row_q.append("\\n".join(question_text))
                table.append(row_q)

            # print(question_set)
            
        
        # pprint(table)
        for row in table:
            # print(row)
            print(",".join(row))


# {
#     'choices': [{'meta_data': {'text': ''}, 'id': 1, 'choice_class': 'MultichoiceTextChoice'}, {'meta_data': {'text': ''}, 'id': 2, 'choice_class': 'MultichoiceTextChoice'}, {'meta_data': {'text': ''}, 'id': 3, 'choice_class': 'MultichoiceTextChoice'}, {'meta_data': {'text': ''}, 'id': 4, 'choice_class': 'MultichoiceTextChoice'}]
# ,   'correct_id': None}