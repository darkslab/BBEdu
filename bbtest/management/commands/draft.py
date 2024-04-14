from bbtest.models import User, TestQuestion, TestSection, Test
from pprint import pprint
import django
# us = User.objects.all()

# us[0].user_permissions.all()

# res = []
# for u in us:
#     res.append([u.username, u.user_permissions.all()])

# pprint(res)

# User.objects.filter(user_permissions__codename="expert").all()

# User.active_users.filter(user_permissions__codename="student").count()
# User.objects.filter(user_permissions__codename="developer").count()
# User.active_users.filter(user_permissions__codename="admin").count()
# User.active_users.filter(user_permissions__codename="expert").count()
# User.active_users.filter(is_superuser=True).count()


# res = []
# for u in us:
#     if u.is_superuser:
#         res.append("super: {}".format(str(u.username)) )
#         continue
#     codename = str(u.user_permissions.get().codename)
#     if codename == "student":
#         continue
#     res.append("{}: {}".format(codename, str(u.username)) )

# pprint(res)

#     # res.append([u.username, u.user_permissions.all()])


# User.objects.get(username="Dev-007")

# from bbtest.models import User
# user = User.objects.get(username="Expert-007")
# user.expert_profile

question = TestQuestion.objects.create(
    answer_class=TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE,
    meta_data=meta_data,
    section=test.section,
    status=test.status,
    code="{}{:%y}{:04}".format(
        test.section.code, 
        datetime.now(), 
        TestQuestion.objects.filter(created_at__year=datetime.now().year, section=test.section).count()),
    weight=0,
    # order=i,
    developer=test.developer,
)


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


    # except django.db.utils.IntegrityError:



print(res)

from bbtest.models import User, TestQuestion, TestParagraph
TestQuestion.objects.update(has_periodic_table=False, has_calculator=False)
TestQuestion.objects.filter(paragraphs__paragraph_class=TestParagraph.PARAGRAPH_CLASS_PERIODIC_TABLE).update(has_periodic_table=True)
TestQuestion.objects.filter(paragraphs__paragraph_class=TestParagraph.PARAGRAPH_CLASS_CALCULATOR).update(has_calculator=True)

# ----------------- 

from bbtest.models import User, TestQuestion, TestParagraph
obj = TestQuestion.objects.first()
obj.paragraphs.filter(paragraph_class = TestParagraph.PARAGRAPH_CLASS_PERIODIC_TABLE).exist()
asd = TestQuestion.objects.filter(paragraphs__paragraph_class=TestParagraph.PARAGRAPH_CLASS_PERIODIC_TABLE).count()
asd2 = TestQuestion.objects.filter(paragraphs__paragraph_class=TestParagraph.PARAGRAPH_CLASS_CALCULATOR).count()



TestQuestion.objects.filter(has_calculator=True).count()

from bbtest.models import User, TestQuestion, TestSection, Test, StudentGroup
test = Test.objects.first()
test.actual_question_count



group_obj = StudentGroup.objects.get(name="test_user")
# group_obj.students.update(student__is_active=True)
User.student_test_profile.filter(student_test_profile=group_obj).count()



User.objects.filter(student_test_profile__isnull=False, student_test_profile__student_group=group_obj).count()


User.objects.filter(student_test_profile__isnull=False, student_test_profile__student_group=group_obj).update(is_active=False)