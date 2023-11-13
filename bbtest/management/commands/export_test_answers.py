from django.core.management.base import BaseCommand
from datetime import datetime
import pytz
from bbtest.models import User
from bbtest.models.test import Test, TestQuestion, TestParagraph, StudentGroup, TestPackage
from bbtest.models.quiz import Quiz, QuizSet

from pprint import pprint

class Command(BaseCommand):
    help = 'export test info' 


    def handle(self, *args, **kwargs):
        group_set_obj = StudentGroup.objects.all()

        result = []

        for i, group_obj in enumerate(group_set_obj):


            for j, student_test_profile in enumerate(group_obj.students.all()):
                print(i, j, " "*20, end="\r")
                student = student_test_profile.student
                quiz_set_list = student.quiz_sets.all()

                if len(quiz_set_list) != 1:
                    continue
                # print(quiz_set_list)
                for quiz in quiz_set_list[0].quizzes.all():
                    test = quiz.test

                    answers = []
                    for ans in quiz.get_answers_ids():
                        if ans is None:
                            answers.append("")
                        else:
                            answers.append(str(ans))

                    started_at = str(quiz.started_at.strftime("%Y.%m.%d %H:%M:%S")) if quiz.started_at else ""
                    row = [student.username, group_obj.name, test.section.name, started_at] + answers
                    result.append(";".join(row))

        res = "\n".join(result)
        with open("answers.csv", "w") as f:
            f.write(res) 

        # print(res)
        