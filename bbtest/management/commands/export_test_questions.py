from datetime import datetime
from pprint import pprint

import pytz
from django.core.management.base import BaseCommand
from django.db.models import QuerySet

from bbtest.models import User
from bbtest.models.test import Test, TestParagraph, TestQuestion, TestToQuestionRelation


class Command(BaseCommand):
    help = 'export test info' 


    def handle(self, *args, **kwargs):
        # self.handleQuestion(*args, **kwargs)
        self.handleTest(*args, **kwargs)

    def handleQuestion(self, *args, **kwargs):

        test_question_set = TestQuestion.objects.order_by("code").all()
        table = []
        for question_obj in test_question_set:
            row = [ 
                question_obj.developer.username,
                question_obj.developer.email if question_obj.developer.email else "",
                question_obj.section.domain.name,
                question_obj.section.name,
                question_obj.language,
                question_obj.code,
                str(TestQuestion.STATUSES_DICT[question_obj.status]),
                question_obj.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            ]
            # table.append(row)

            row_q = [
                # str(question_obj.order),
                repr(question_obj.taxonomy.name) if question_obj.taxonomy else "",
                repr(question_obj.topic.name) if question_obj.topic else "",
                repr(question_obj.subtopic.name) if question_obj.subtopic else "",
                repr(question_obj.goal.name) if question_obj.goal else "",
                str(question_obj.answer_class),
                str(question_obj.meta_data.get("correct_id", None)),
                str(question_obj.meta_data.get("choices", None)),
            ] 

            answers = [""] * 5
            choices = question_obj.meta_data.get("choices", None)
            if choices:
                for i in range(min(5, len(choices))):
                    qid = choices[i].get('id', None)
                    if not qid or qid <= 0:
                        continue
                    meta = choices[i].get('meta_data', {})
                    text = meta.get("text")
                    answers[i] = repr(text)
            
            row_q += answers

            # print(question_obj.meta_data)
            paragraph_set = question_obj.paragraphs.prefetch_related("through").order_by("through")  # .order_by("order")


            question_text = []
            for paragraph in paragraph_set:
                # paragraph.meta_data #.get("text", "no text")
                # row_q.append(paragraph.paragraph_class)
                # row_q.append(paragraph.meta_data)
                question_text.append(paragraph.meta_data.get("text", ""))
            row_q.append(repr("\\n".join(question_text)))

            table.append(row + row_q)

            # print(question_set)
            
        
        # pprint(table)
        out = "|".join([
            "developer",
            "email",
            "domain",
            "section",
            "language",
            "code",
            "status",
            "created_at",
            # "#",
            "taxonomy",
            "topic",
            "subtopic",
            "goal",
            "answer_class",
            "correct_id",
            "choices_metadata",
            "A",
            "B",
            "C",
            "D",
            "E",
            "question_text",
        ]) + "\n"
        for row in table:
            # print(row)
            row = "|".join(row)
            # print(row)
            out += row + "\n"

        with open("test_questions.csv", "w") as f:
            f.write(out)

    def question_to_letter(self, question_obj: TestQuestion):
        alphabet = "ABCDEFGH"
        correct_id = question_obj.meta_data.get("correct_id", None)
        if correct_id is None:
            return "9"

        choices = question_obj.meta_data.get('choices', [])
        if question_obj.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
            for i, ch in enumerate(choices):
                if correct_id == ch["id"]:
                    return alphabet[i]
            else:
                return "9"
        elif question_obj.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI:
            temp = []
            for i, ch in enumerate(choices):
                if correct_id and ch["id"] in correct_id:
                    temp.append(alphabet[i])
            return temp
        else:
            return "8"

    def handleTest(self, *args, **kwargs):

        test_set = Test.objects.order_by("section").all()
        table = []
        for test_obj in test_set:
            row = [ 
                test_obj.developer.username,
                test_obj.developer.email if test_obj.developer.email else "",
                test_obj.section.domain.name,
                test_obj.section.name,
                test_obj.language,
                test_obj.code,
                str(Test.STATUSES_DICT[test_obj.status]),
                test_obj.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            ]
            # table.append(row)

            # question_set = test_obj.questions.order_by("testtoquestionrelation").all()

            test_to_question_set: QuerySet[TestToQuestionRelation] = TestToQuestionRelation.objects.filter(test=test_obj).order_by("order").all()

            for test_to_question_obj in test_to_question_set:
                question_obj: TestQuestion = test_to_question_obj.question

                row_q = [
                    str(test_to_question_obj.order),
                    str(question_obj.code),
                    repr(question_obj.taxonomy.name) if question_obj.taxonomy else "",
                    repr(question_obj.topic.name) if question_obj.topic else "",
                    repr(question_obj.subtopic.name) if question_obj.subtopic else "",
                    repr(question_obj.goal.name) if question_obj.goal else "",
                    str(question_obj.answer_class),
                    str(self.question_to_letter(question_obj)),  # str(question_obj.meta_data.get("correct_id", None)),
                    str(question_obj.meta_data.get("choices", None)),
                ] 

                answers = [""] * 5
                choices = question_obj.meta_data.get("choices", None)
                if choices:
                    for i in range(min(5, len(choices))):
                        qid = choices[i].get('id', None)
                        if not qid or qid <= 0:
                            continue
                        meta = choices[i].get('meta_data', {})
                        text = meta.get("text")
                        answers[i] = repr(text)
                
                row_q += answers

                # print(question_obj.meta_data)
                paragraph_set = question_obj.paragraphs.prefetch_related("through").order_by("through")  # .order_by("order")


                question_text = []
                for paragraph in paragraph_set:
                    # paragraph.meta_data #.get("text", "no text")
                    # row_q.append(paragraph.paragraph_class)
                    # row_q.append(paragraph.meta_data)
                    question_text.append(paragraph.meta_data.get("text", ""))
                row_q.append(repr("\\n".join(question_text)))

                table.append(row + row_q)

            # print(question_set)
            
        
        # pprint(table)
        out = "|".join([
            "developer",
            "email",
            "domain",
            "section",
            "language",
            "code",
            "status",
            "created_at",
            "#",
            "question code",
            "taxonomy",
            "topic",
            "subtopic",
            "goal",
            "answer_class",
            "correct_id",
            "choices_metadata",
            "A",
            "B",
            "C",
            "D",
            "E",
            "question_text",
        ]) + "\n"
        for row in table:
            # print(row)
            row = "|".join(row)
            # print(row)
            out += row + "\n"

        with open("test_questions.csv", "w") as f:
            f.write(out)


# {
#     'choices': [{'meta_data': {'text': ''}, 'id': 1, 'choice_class': 'MultichoiceTextChoice'}, {'meta_data': {'text': ''}, 'id': 2, 'choice_class': 'MultichoiceTextChoice'}, {'meta_data': {'text': ''}, 'id': 3, 'choice_class': 'MultichoiceTextChoice'}, {'meta_data': {'text': ''}, 'id': 4, 'choice_class': 'MultichoiceTextChoice'}]
# ,   'correct_id': None}