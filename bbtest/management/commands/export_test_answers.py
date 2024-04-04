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
        domain_name_filter = ["Teacher_ru", "Teacher_kz"]
        # domain_name_filter = ["Klass_4_ru", "Klass_4_kz"]
        # domain_name_filter = ["Klass_9_ru", "Klass_9_kz"]
        # domain_name_filter = ["Teacher_ru", "Teacher_kz"]

        group_set_obj = StudentGroup.objects
        group_set_obj = group_set_obj.filter(package__domain__name__in=domain_name_filter)
        group_set_obj.order_by("package__domain").all()

        result = []

        for i, group_obj in enumerate(group_set_obj):
            domain_obj = group_obj.package.domain

            if domain_obj.name not in domain_name_filter:
                continue

            for j, student_test_profile in enumerate(group_obj.students.order_by("student__username").all()):
                print(i, j, " "*20, end="\r")
                student = student_test_profile.student
                quiz_set_list = student.quiz_sets.all()

                if len(quiz_set_list) != 1:
                    continue

                email = student.email if student.email else ""
                # print(quiz_set_list)
                row = [student.username, email, group_obj.name] 

                for quiz in quiz_set_list[0].quizzes.order_by("test__section__order", "order").all():
                    test = quiz.test

                    answers = [""] * test.question_count

                    for i, ans in enumerate(quiz.get_answers_ids()):
                        if ans is not None:
                            answers[i] = str(ans)

                    started_at = str(quiz.started_at.strftime("%Y.%m.%d %H:%M:%S")) if quiz.started_at else ""
                    due_at = str(quiz.due_at.strftime("%Y.%m.%d %H:%M:%S")) if quiz.due_at else ""
                    ended_at = str(quiz.ended_at.strftime("%Y.%m.%d %H:%M:%S")) if quiz.ended_at else due_at
                    row += [test.section.name, started_at, ended_at] + answers

                result.append(";".join(row))

        res = "\n".join(result)
        with open("answers.csv", "w") as f:
            f.write(res) 

        # print(res)
        