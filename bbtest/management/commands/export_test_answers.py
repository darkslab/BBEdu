from django.core.management.base import BaseCommand
from django.db.models import Q
from datetime import datetime
import pytz
from bbtest.models import User
from bbtest.models.test import Test, TestQuestion, TestParagraph, StudentGroup, TestPackage
from bbtest.models.quiz import Quiz, QuizSet
from datetime import timedelta
from pprint import pprint


class Command(BaseCommand):
    help = 'export test info' 

    def handle(self, *args, **kwargs):
        domain_name = "Klass_4"
        # domain_name = "Klass_9"
        # domain_name = "Teacher"

        for day in [15, 16, 17]:
            from_date = datetime(2024, 4, day, 0, 0, 0, tzinfo=pytz.timezone('Asia/Almaty'))
            self.export(from_date, domain_name)


    def export(self, from_date: datetime, domain_name: str):
        to_date = from_date + timedelta(hours=24)
        dt = timedelta(hours=5)  # correct time zone offset

        domain_name_filter = [f"{domain_name}_ru", f"{domain_name}_kz"]
        print(domain_name_filter)

        date_filter_condition = Q(
            students__student__quiz_sets__quizzes__started_at__gte=from_date
        ) & Q(students__student__quiz_sets__quizzes__started_at__lte=to_date)

        group_set_obj = (
            StudentGroup.objects.prefetch_related("package", "package__domain")
            .filter(package__domain__name__in=domain_name_filter)
            .filter(date_filter_condition)
            .distinct()
            .order_by("package__domain")
        )

        print(f"answers_{domain_name}_{from_date:%Y.%m.%d}_{to_date:%Y.%m.%d}", group_set_obj.count())

        result = []
        with open(f"answers_{domain_name}_{from_date:%Y.%m.%d}_{to_date:%Y.%m.%d}.csv", "w") as f:

            for i, group_obj in enumerate(group_set_obj.all()):
                domain_obj = group_obj.package.domain

                if domain_obj.name not in domain_name_filter:
                    continue

                for j, student_test_profile in enumerate(group_obj.students.prefetch_related("student__quiz_sets").order_by("student__username").all()):
                    print(i, j, " "*20, end="\r")
                    student = student_test_profile.student
                    quiz_set_list = student.quiz_sets.all()

                    if len(quiz_set_list) != 1:
                        continue

                    email = student.email if student.email else ""
                    # print(quiz_set_list)
                    row = [student.username, email, group_obj.name] 

                    for quiz in quiz_set_list[0].quizzes.order_by("test__section__order", "order").all():
                        if not quiz.started_at or quiz.started_at <= from_date or quiz.started_at >= to_date: continue

                        test = quiz.test
                        answers = [""] * test.question_count

                        for i, ans in enumerate(quiz.get_answers_letters()):
                            if ans is not None:
                                answers[i] = str(ans)

                        started_at = str((quiz.started_at + dt).strftime("%Y.%m.%d %H:%M:%S")) if quiz.started_at else ""
                        due_at = str((quiz.due_at + dt).strftime("%Y.%m.%d %H:%M:%S")) if quiz.due_at else ""
                        ended_at = str((quiz.ended_at + dt).strftime("%Y.%m.%d %H:%M:%S")) if quiz.ended_at else due_at
                        row = row + [test.section.name, test.code, str(quiz.calc_score()),  started_at, ended_at] + answers

                    # result.append(";".join(row))
                    if len(row) > 4:
                        f.write(";".join(row) + "\n") 

        # res = "\n".join(result)
        # print(res)
