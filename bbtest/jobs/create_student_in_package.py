import csv
import uuid
from pathlib import Path
from random import randint
from typing import List

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.transaction import atomic
from django.forms import ValidationError
from django_rq import job

from bbtest.auth.models import User
from bbtest.models import (
    QuizSet,
    StudentGroup,
    Test,
    TestPackage,
    UserTestPackageProfile,
)

BASE_DIR = Path(settings.BASE_DIR_PATH).resolve().parent


def create_students(username, email, password, is_active):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = username
    user.is_active = is_active
    # user.last_name = "Electric"
    user.save()
    content_type = ContentType.objects.get_for_model(type(user))
    permissions = []
    permissions.append(Permission.objects.get(codename="student", content_type=content_type))
    user.user_permissions.set(permissions)
    return user


@job("default", timeout=600000000)
def populate_package_student_group(package_code, student_group_name, prefix, amount = 1):
    group_obj = StudentGroup.objects.get(name=student_group_name)
    package_obj = TestPackage.objects.get(code = package_code)


    # initialize csv table response
    with open(f"{BASE_DIR}/logins/export_logins_{package_code}_{student_group_name}.csv", "w+") as f:
        writer = csv.writer(f)

        student_count = group_obj.students.count()
        student_list = []

        package_name = package_obj.name
        print("populate_package_student_group", BASE_DIR,  package_name, group_obj.name, student_count)
        
        
        count = 0

        for i in range(student_count + 1, student_count + amount + 1):
            print(f"Creating users {i}/{amount}            ", end="\r")
            # username = "{}{}{:03}".format(package_name, group_obj.name, i)
            username = "{}{:05}".format(group_obj.name, i)
            login_email =  None
            if len(prefix) > 0:
                login_email = "{}_{}@not.real.email.kz".format(prefix, uuid.uuid4().hex[:12])
            # else:
            #     login_email = "{}@not.real.email.kz".format(uuid.uuid4().hex[:12])
            gen_pass = "{:05}".format(randint(10000, 99999))
            
            try:
                student_obj = create_students(username, login_email, gen_pass, group_obj.is_active)
                UserTestPackageProfile.objects.create(
                    student = student_obj,
                    student_group = group_obj,
                )
                student_list.append(student_obj)
                # package_obj.students.add(student_obj)

                writer.writerow([username, login_email, gen_pass])
            except ValidationError:
                writer.writerow([username, login_email, "already_exist"])

            count += 1
            if count % 100 == 0:
                group_obj.student_count += 100
                group_obj.save()

    if package_obj.finalized:
        test_set = package_obj.tests.order_by('section__order').all()
        domain = package_obj.domain

        for i, student_obj in enumerate(student_list):
            quiz_set = student_obj.quiz_sets.create(test_domain=domain, cart=None)
            for quiz_order, test in enumerate(test_set):
                quiz_set.quizzes.create(test=test, order=quiz_order, line_item=None)
                # test.update(sales_count=(F("sales_count") + 1))
            
            print(f"Creating quizzes {i}/{len(student_list)}     ", end="\r")

    # group_obj.student_count = student_count + amount
    group_obj.student_count = group_obj.students.count()
    group_obj.save()
    
    print("Success", "Created %s students." % amount)



@job("default", timeout=600000000)
def activate_package(group_obj: StudentGroup, active_state: bool):
    User.objects.filter(student_test_profile__isnull=False, student_test_profile__student_group=group_obj).update(is_active=active_state)
    group_obj.is_active = active_state
    group_obj.save()

    # for student_test_profile_obj in group_obj.students.all():
    #     student_test_profile_obj.student.is_active = is_active
    #     student_test_profile_obj.student.save()


@job("default", timeout=600000000)
def populate_demouser_test(user: User):
    if settings.DEBUG: 
        package_obj = TestPackage.objects.get(code = "2404085ebe")
    else: 
        package_obj = TestPackage.objects.get(code = "241103f825")
    
    # print(package_obj)
    test_set = package_obj.tests.order_by('section__order').all()
    domain = package_obj.domain

    quiz_set: QuizSet = user.quiz_sets.create(test_domain=domain, cart=None)
    # quiz_set: QuizSet = QuizSet.objects.create(
    #     test_domain = domain,
    #     student = user,
    #     cart = None,
    # )
    # print(quiz_set)

    for quiz_order, test in enumerate(test_set):
        quiz_set.quizzes.create(test=test, order=quiz_order, line_item=None)






@job("high", timeout=3600*2)
def hash_users_passwords(user_list: List[User]):
    # create_package_pair_quiz_users_helper(package_quiz_obj)

    # Find users with unhashed passwords
    for user in user_list:
        # if not is_password_usable(user.password) or len(user.password) < 10 or not user.password.startswith("pbkdf2_sha256"):
        # print(user.password)
        user.password = make_password(user.password)
        user.save()
    