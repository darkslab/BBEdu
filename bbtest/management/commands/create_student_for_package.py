from django.core.management.base import BaseCommand
from django.forms import ValidationError
from bbtest.models import User, Test, StudentGroup, TestPackage, UserTestPackageProfile
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from bbtest.models import Account
from random import randint
import csv
import uuid


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


def populate_package_student_group(package_code, student_group_name, prefix, amount = 1):
    group_obj = StudentGroup.objects.get(name=student_group_name)
    package_obj = TestPackage.objects.get(code = package_code)

    # initialize csv table response
    with open("export_logins.csv", "w+") as f:
        writer = csv.writer(f)


        student_count = group_obj.student_count 
        student_list = []

        package_name = package_obj.name
        print("ManagePackageStudentsFormView", package_name, group_obj.name, student_count)
        
        
        for i in range(student_count + 1, student_count + amount + 1):
            print(f"{i}/{amount}            ", end="\r")
            # username = "{}{}{:03}".format(package_name, group_obj.name, i)
            username = "{}{:03}".format(group_obj.name, i)
            login_email =  None
            if len(prefix) > 0:
                login_email = "{}_{}@not.real.email.kz".format(prefix, uuid.uuid4().hex[:12])
            # else:
            #     login_email = "{}@not.real.email.kz".format(uuid.uuid4().hex[:12])
            gen_pass = "{:05}".format(randint(1, 99999))
            
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

        if package_obj.finalized:
            test_set = package_obj.tests.order_by('section__order').all()
            domain = package_obj.domain

            for student_obj in student_list:
                quiz_set = student_obj.quiz_sets.create(test_domain=domain, cart=None)
                for quiz_order, test in enumerate(test_set):
                    quiz_set.quizzes.create(test=test, order=quiz_order, line_item=None)
                    # test.update(sales_count=(F("sales_count") + 1))

        group_obj.student_count += amount
        group_obj.save()
        
        print("Success", "Created %s students." % amount)
            


class Command(BaseCommand):
    help = 'export student info (phone, email, etc.)' 


    def handle(self, *args, **kwargs):
        package_code = "2404085ebe"
        student_group_name = "9084"
        prefix = "9084"

        # package_code = "240327a01c"
        # student_group_name = "test_user"
        # prefix = "nz"

        populate_package_student_group(package_code, student_group_name, prefix, amount = 1)