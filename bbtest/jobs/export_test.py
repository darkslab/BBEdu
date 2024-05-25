import csv
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from pprint import pprint
from random import randint

import pytz
from django.conf import settings
from django.contrib.auth.models import Permission
from django.db.models import Q, QuerySet
from django_rq import job

from bbtest.models import (
    JobProgress,
    StudentGroup,
    Test,
    TestPackage,
    User,
    UserTestPackageProfile,
)
from bbtest.models.quiz import Quiz, QuizSet
from bbtest.models.test import (
    StudentGroup,
    Test,
    TestPackage,
    TestParagraph,
    TestQuestion,
)

BASE_DIR = Path(settings.BASE_DIR_PATH).resolve().parent

# tzinfo=pytz.timezone('Asia/Almaty')

@job("default", timeout=600000000)
def job_export_results(from_date: datetime, to_date: datetime, domain_name: str, job_progress: JobProgress):
    _job_export_results(from_date, to_date, domain_name, job_progress)


def _job_export_results(from_date: datetime, to_date: datetime, domain_name: str, job_progress: JobProgress = None):
    if job_progress is not None:
        job_progress.percentage = 0
        job_progress.save()

    # to_date = from_date + timedelta(hours=24)
    dt = timedelta(hours=5)  # correct time zone offset

    domain_name_filter = [f"{domain_name}_ru", f"{domain_name}_kz"]
    # print(domain_name_filter)

    date_filter_condition = Q(
        students__student__quiz_sets__quizzes__started_at__gte=from_date
    ) & Q(students__student__quiz_sets__quizzes__started_at__lte=to_date)
    student_date_filter_condition = Q(student__quiz_sets__quizzes__started_at__gte=from_date) & Q(student__quiz_sets__quizzes__started_at__lte=to_date)


    group_set_obj: StudentGroup = (
        StudentGroup.objects.prefetch_related("package", "package__domain")
        .filter(package__domain__name__in=domain_name_filter)
        .filter(date_filter_condition)
        .distinct()
        .order_by("package__domain")
    )

    student_group_count = group_set_obj.count()

    # print(f"answers_{domain_name}_{from_date:%Y.%m.%d}_{to_date:%Y.%m.%d}", group_set_obj.count())
    # result = []

    with open(f"{BASE_DIR}/logins/exam_exports/answers_{domain_name}_{from_date:%Y.%m.%d}_{to_date:%Y.%m.%d}.csv", "w") as f:

        for i, group_obj in enumerate(group_set_obj.all()):
            domain_obj = group_obj.package.domain

            if domain_obj.name not in domain_name_filter:
                continue

            

            student_test_profile_set_obj = (
                group_obj.students.prefetch_related("student__quiz_sets")
                .filter(student_date_filter_condition)
                .distinct()
                .order_by("student__username")
            )
            student_test_profile_count = student_test_profile_set_obj.count()
            # print(f"{i} student_test_profile_set_obj", student_test_profile_set_obj.count())

            for j, student_test_profile in enumerate(student_test_profile_set_obj.all()):
                # print(i, j, " "*20, end="\r")
                student: User = student_test_profile.student
                quiz_set_list: QuerySet[QuizSet] = student.quiz_sets.all()

                if len(quiz_set_list) < 1:
                    continue

                email = student.email if student.email else ""
                # print(quiz_set_list)

                for quiz_set in quiz_set_list:
                    row = [student.username, email, group_obj.name] 
                    quiz_list: QuerySet[Quiz] = quiz_set.quizzes.order_by("test__section__order", "order").all()

                    for quiz in quiz_list:
                        if not quiz.started_at or quiz.started_at <= from_date or quiz.started_at >= to_date:
                            continue

                        test: Test = quiz.test
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

                if job_progress is not None and j % 100 == 0:
                    job_progress.percentage = (i + j / student_test_profile_count) / student_group_count 
                    job_progress.save()

    if job_progress is not None:
        job_progress.percentage = 100
        job_progress.is_finished = True
        job_progress.finished_at = datetime.now()
        job_progress.save()
