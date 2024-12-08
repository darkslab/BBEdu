from bbtest.models import TestQuestion, TestSection, Test, TestTopic, TestSubTopic, TestSubTopicSection, TestTopicToSubtopicRelation, TestQuestion, TestTopicSection
# 9587, 9584
section_obj = TestSection.objects.get(id=9584)
topic_main_obj = TestTopic.objects.filter(sections=section_obj)[0]
subtopic_list = TestSubTopic.objects.filter(sections=section_obj)
section_obj
topic_main_obj
subtopic_list

for index, subtopic_obj in enumerate(subtopic_list):
    topic_name = subtopic_obj.name
    print(topic_name)
    topic_obj, _ = TestTopic.objects.get_or_create(name=topic_name)
    TestTopicSection.objects.get_or_create(section=section_obj, topic=topic_obj, order=index)
    TestTopicToSubtopicRelation.objects.get_or_create(
            topic = topic_obj,
            subtopic = subtopic_obj,
            order = 0,
        )

question_list = TestQuestion.objects.filter(topic=topic_main_obj)
question_list

for question_obj in question_list:
    try:
        subtopic_name = question_obj.subtopic.name
    except Exception:
        print(question_obj.code, "broken")
        continue
    print(question_obj.code)
    q_topic = TestTopic.objects.get(name=subtopic_name)
    question_obj.topic = q_topic
    question_obj.save()
    # break

topic_main_obj.delete()


from bbtest.models.test import StudentProfile
from bbtest.models import TestQuestion, TestSection, Test
from bbtest.auth.models import User
from django.contrib.auth.models import Permission, ContentType

content_type = ContentType.objects.get_for_model(User)
permission = Permission.objects.get(codename="student", content_type=content_type)

objects = User.objects.filter(
    user_permissions  = permission,
)
for user in objects:
    StudentProfile.objects.create(
        student = user,
        games = "bird",
    )


from bbtest.models import User, TestQuestion, TestSection, Test
from pprint import pprint
import django
# us = User.objects.all()

# us[0].user_permissions.all()

from bbtest.models import User, TestQuestion, TestPackage, TestParagraph, Test, UserTestPackageProfile
for us in User.objects.all():
    try:
        if us.get_user_role() == "student":
            print("deleted:", us.first_name)
            us.delete()
        
        

    except Exception as e:
        print("error:", us.first_name)
        us.delete()
        print(e)


Test.objects.all().delete()
TestQuestion.objects.all().delete()
TestPackage.objects.all().delete()
TestParagraph.objects.all().delete()


UserTestPackageProfile.objects.all()

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


from bbtest.models import User, TestQuestion, TestSection, Test, StudentGroup, UserTestPackageProfile
usr = User.objects.get(username="31102200170")
UserTestPackageProfile.objects.get(student=usr)


TestQuestion.objects.get(code="M9RU230081").test


test.questions.order_by("testtoquestionrelation").all()

{
    "choices": [
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "75, 77, 78, 80", "has_formulas": true},
            "id": 2,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "75, 78, 80, 81", "has_formulas": true},
            "id": 3,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "77, 78, 80, 81", "has_formulas": true},
            "id": 4,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "81, 80, 78, 77", "has_formulas": true},
            "id": 1,
        },
    ],
    "correct_id": 4,
}

# M4RU230000
{
    "choices": [
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "1; 100"},
            "id": 3,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "10; 100"},
            "id": 2,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "100; 1"},
            "id": 4,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "100; 10"},
            "id": 1,
        },
    ],
    "correct_id": 1,
}
# M4RU230001
{
    "correct_id": 3,
    "choices": [
        {
            "meta_data": {"text": "689, 691, 693"},
            "id": 1,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {"text": "688, 690, 692"},
            "id": 2,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {"text": "688, 689, 690"},
            "id": 3,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {"text": "687, 686, 685"},
            "id": 4,
            "choice_class": "MultichoiceTextChoice",
        },
    ],
}

# M4RU230002
{
    "   ": [
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "75, 77, 78, 80", "has_formulas": True},
            "id": 2,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "75, 78, 80, 81", "has_formulas": True},
            "id": 3,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "77, 78, 80, 81", "has_formulas": True},
            "id": 4,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "81, 80, 78, 77", "has_formulas": True},
            "id": 1,
        },
    ],
    "correct_id": 4,
}


{
    "answers": [
        {"answer": {"correct_id": 4}, "observation": {}},
        {"answer": {"correct_id": 4}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 3}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 3}, "observation": {}},
        {"answer": {"correct_id": 1}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 1}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 1}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 1}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 2}, "observation": {}},
        {"answer": {"correct_id": 1}, "observation": {}},
    ],
    "observation": {},
}

# M4KZ230002
{
    "choices": [
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "92, 95, 96, 98"},
            "id": 51918,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "89, 90, 92, 93"},
            "id": 51919,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "92, 93, 95, 96"},
            "id": 51920,
        },
        {
            "choice_class": "MultichoiceTextChoice",
            "meta_data": {"text": "93, 95, 97, 99"},
            "id": 51921,
        },
    ],
    "correct_id": 51920,
}


{
    "choices": [
        {
            "meta_data": {
                "text": "\u0423\u0447\u0438\u0442\u0435\u043b\u044c \u043e\u0431\u044a\u044f\u0441\u043d\u044f\u0435\u0442 \u0442\u0435\u043c\u0443 \u043d\u0435\u043f\u043e\u043d\u044f\u0442\u043d\u043e, \u0441\u043a\u0443\u0447\u043d\u043e \u0438\u043b\u0438 \u043d\u0435\u0438\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u043e"
            },
            "id": 26996,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {
                "text": "\u042f \u043d\u0435 \u043c\u043e\u0433\u0443 \u0441\u043e\u0441\u0440\u0435\u0434\u043e\u0442\u043e\u0447\u0438\u0442\u044c\u0441\u044f \u043d\u0430 \u0442\u0435\u043c\u0435 \u0443\u0440\u043e\u043a\u0430 (\u0438\u0437-\u0437\u0430 \u0448\u0443\u043c\u0430 \u0438\u043b\u0438 \u0434\u0440\u0443\u0433\u0438\u0445 \u043d\u0435\u0443\u0434\u043e\u0431\u0441\u0442\u0432 \u0432 \u043a\u043b\u0430\u0441\u0441\u0435)"
            },
            "id": 26997,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {
                "text": "\u0423\u0447\u0438\u0442\u0435\u043b\u044c \u043d\u0435 \u0441\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0435\u0442, \u0432\u0441\u0435 \u043b\u0438 \u043f\u043e\u043d\u044f\u043b\u0438 \u0442\u0435\u043c\u0443 \u0443\u0440\u043e\u043a\u0430"
            },
            "id": 26998,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {
                "text": "\u0423\u0447\u0438\u0442\u0435\u043b\u044c \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u0442\u043e\u043b\u044c\u043a\u043e \u0441 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u043c\u0438 \u0443\u0447\u0435\u043d\u0438\u043a\u0430\u043c\u0438"
            },
            "id": 26999,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {
                "text": "\u041c\u043d\u0435 \u0442\u0440\u0443\u0434\u043d\u043e \u043f\u043e\u043d\u044f\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0442\u0435\u043c\u0443, \u0442\u0430\u043a \u043a\u0430\u043a \u0447\u0430\u0441\u0442\u043e \u043d\u0435 \u0432\u044b\u0441\u044b\u043f\u0430\u044e\u0441\u044c \u0434\u043e\u043c\u0430"
            },
            "id": 27000,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {
                "text": "\u041c\u043d\u0435 \u0442\u0440\u0443\u0434\u043d\u043e \u0437\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0442\u0435\u043c\u0443, \u0442\u0430\u043a \u043a\u0430\u043a \u0443 \u043c\u0435\u043d\u044f \u0442\u0440\u0443\u0434\u043d\u043e\u0441\u0442\u0438 \u0441 \u043f\u0430\u043c\u044f\u0442\u044c\u044e"
            },
            "id": 27001,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {
                "text": "\u0423 \u043c\u0435\u043d\u044f \u043d\u0435 \u0432\u043e\u0437\u043d\u0438\u043a\u0430\u0435\u0442 \u0442\u0440\u0443\u0434\u043d\u043e\u0441\u0442\u0435\u0439 \u043f\u0440\u0438 \u0438\u0437\u0443\u0447\u0435\u043d\u0438\u0438 \u043d\u043e\u0432\u043e\u0439 \u0442\u0435\u043c\u044b \u043d\u0430 \u0443\u0440\u043e\u043a\u0435"
            },
            "id": 27002,
            "choice_class": "MultichoiceTextChoice",
        },
        {
            "meta_data": {
                "text": "\u0417\u0430\u0442\u0440\u0443\u0434\u043d\u044f\u044e\u0441\u044c \u043e\u0442\u0432\u0435\u0442\u0438\u0442\u044c "
            },
            "id": 27003,
            "choice_class": "MultichoiceTextChoice",
        },
    ],
    "correct_ids": [],
}



{
    "success": true,
    "status": "started",
    "section": [
        "\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 9 \u0421\u044b\u043d\u044b\u043f",
        "5DB6"
    ],
    "seconds": 2492,
    "reload": false,
    "questions": [
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0421\u0443 \u043c\u043e\u043b\u0435\u043a\u0443\u043b\u0430\u0441\u044b\u043d\u044b\u04a3 \u043c\u0430\u0441\u0441\u0430\u0441\u044b \u0448\u0430\u043c\u0430\u043c\u0435\u043d $3*10^{-26}$ \u043a\u0433, \u0430\u043b \u0441\u0443\u0442\u0435\u0433\u0456 \u043c\u043e\u043b\u0435\u043a\u0443\u043b\u0430\u0441\u044b\u043d\u044b\u04a3 \u043c\u0430\u0441\u0441\u0430\u0441\u044b \u0448\u0430\u043c\u0430\u043c\u0435\u043d $3,3*10^{-27}$ \u043a\u0433 \u0442\u0435\u04a3.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0421\u0443 \u043c\u043e\u043b\u0435\u043a\u0443\u043b\u0430\u0441\u044b\u043d\u044b\u04a3 \u043c\u0430\u0441\u0441\u0430\u0441\u044b \u0441\u0443\u0442\u0435\u0433\u0456 \u043c\u043e\u043b\u0435\u043a\u0443\u043b\u0430\u0441\u044b\u043d\u044b\u04a3 \u043c\u0430\u0441\u0441\u0430\u0441\u044b\u043d\u0430\u043d \u043d\u0435\u0448\u0435 \u0435\u0441\u0435 \u0430\u0440\u0442\u044b\u049b \u0435\u043a\u0435\u043d\u0456\u043d \u0448\u0430\u043c\u0430\u043c\u0435\u043d \u0435\u0441\u0435\u043f\u0442\u0435\u04a3\u0456\u0437."
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "id": 198,
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "0,9"
                        }
                    },
                    {
                        "id": 199,
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "9,1"
                        }
                    },
                    {
                        "id": 200,
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "90"
                        }
                    },
                    {
                        "id": 201,
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "900"
                        }
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230080"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041c\u04d9\u0440\u0438\u044f\u043c \u0434\u0435\u043d\u0435\u043b\u0435\u0440\u0434\u0456\u04a3 \u043a\u04e9\u043b\u0435\u043c\u0434\u0435\u0440\u0456\u043d \u04e9\u043b\u0448\u0435\u0443 \u0431\u043e\u0439\u044b\u043d\u0448\u0430 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0430\u043b\u044b\u049b \u0436\u04b1\u043c\u044b\u0441\u0442\u044b \u043e\u0440\u044b\u043d\u0434\u0430\u0434\u044b. \u041e\u043b \u0431\u0430\u0440\u043b\u044b\u049b \u0434\u0435\u0440\u0435\u043a\u0442\u0435\u0440\u0434\u0456 \u043a\u0435\u0441\u0442\u0435\u0433\u0435 \u0435\u043d\u0433\u0456\u0437\u0434\u0456."
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "77475977343547c09ad480248999fbc8",
                        "asset_object_name": "assets/77475977343547c09ad480248999fbc8/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/77475977343547c09ad480248999fbc8/file?Expires=1713285471&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=jQmxU%2FfR6kmaFEqldaALASdrYrNexbs3%2BxGNxKX%2FMwP6o2Blc%2FJkDZ3lOBM9WdsHQ%2FvYLo%2Bj0I%2FcnRg7xa%2FUqLyHkyuo5QB971q6P2JnWvv3QlJ6JhY17JYS1q7nMS5WSdu6rozZ9WYQl%2B0NqpXgsexJTQYBig1OBwNtw40f8myXKVatZuilm94DrrXEueK8DXR9bCtDVv9FtbxhrYH6LIhJSFoPijvJV7e%2F8bpz6o5XIw6K8UHIQi6zSzqaxsOz9Y4VTQKb0gBhZZtrtvXacKYhd2XqK%2BNksiP75zJ1Mx%2Fk7%2FD9ceOKRLBRTEFVkTkpvJzeLBbT7SvlXM2BQAisZg%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u049a\u0430\u0439 \u0434\u0435\u043d\u0435\u043d\u0456\u04a3 \u043a\u04e9\u043b\u0435\u043c\u0456 \u0435\u04a3 \u043a\u0456\u0448\u0456?"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "id": 14100,
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u21161"
                        }
                    },
                    {
                        "id": 14101,
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u21162"
                        }
                    },
                    {
                        "id": 14102,
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u21163"
                        }
                    },
                    {
                        "id": 14103,
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u21164"
                        }
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230081"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041a\u0430\u0440\u0442\u0430\u0434\u0430 \u04e8\u0440\u0456\u043a \u043a\u04e9\u0448\u0435\u0441\u0456 \u043c\u0435\u043d \u0416\u04af\u0437\u0456\u043c \u043a\u04e9\u0448\u0435\u0441\u0456 48$^o$ \u0431\u04b1\u0440\u044b\u0448\u043f\u0435\u043d, \u0430\u043b \u0410\u043b\u043c\u0430 \u043a\u04e9\u0448\u0435\u0441\u0456 \u043c\u0435\u043d \u0416\u04af\u0437\u0456\u043c \u043a\u04e9\u0448\u0435\u0441\u0456 52$^o$ \u0431\u04b1\u0440\u044b\u0448\u043f\u0435\u043d \u049b\u0438\u044b\u043b\u044b\u0441\u0430\u0434\u044b.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "9c0e9f7e20364b22993439a02acde6e6",
                        "asset_object_name": "assets/9c0e9f7e20364b22993439a02acde6e6/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/9c0e9f7e20364b22993439a02acde6e6/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=C0A6SAtglcs%2BN0Nc0wT6ufJaagHgUcEkqVtVVydIOrpZlHBJhdF7z11dUa69OzV2BEjzx%2BXZwa2dqLWuEV9g0UkzCQR%2Fm1m6XABT1v9KApK1DsG%2Fr3SoIa17MfceW%2Frrp4FbJ4tBAGJvqCyPGHEfeD9ULQyq%2BAk%2F0SndALP0GmuHWuhIQB4bejqERP%2FHxBtE1bJ%2FmCDxJaknq7bAZNA9BRjLuGv%2FI652hixSwuA3SV%2Frvm01GCQ8XUxqMXNrZXeePx5OlDV2FBFS1lBNuR5QJ8Ihl7UBiz6uZtRxTqUq41%2FQKjfFK78mgRkDFrkxrwBWJzYXdYUMq8743Ru%2Fp%2B4CYA%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041a\u04e9\u0448\u0435 \u0430\u0442\u0430\u0443\u043b\u0430\u0440\u044b\u043d \u049b\u0438\u044b\u043b\u044b\u0441\u0443\u0493\u0430 \u0434\u0435\u0439\u0456\u043d\u0433\u0456 \u04b1\u0437\u044b\u043d\u0434\u044b\u0493\u044b\u043d\u0430 \u049b\u0430\u0440\u0430\u0439 \u043a\u0435\u043c\u0443 \u0440\u0435\u0442\u0456\u043c\u0435\u043d \u043e\u0440\u043d\u0430\u043b\u0430\u0441\u0442\u044b\u0440\u044b\u04a3\u044b\u0437."
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u04e8\u0440\u0456\u043a \u043a\u04e9\u0448\u0435\u0441\u0456, \u0410\u043b\u043c\u0430 \u043a\u04e9\u0448\u0435\u0441\u0456, \u0416\u04af\u0437\u0456\u043c \u043a\u04e9\u0448\u0435\u0441\u0456"
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u04e8\u0440\u0456\u043a \u043a\u04e9\u0448\u0435\u0441\u0456, \u0416\u04af\u0437\u0456\u043c \u043a\u04e9\u0448\u0435\u0441\u0456, \u0410\u043b\u043c\u0430 \u043a\u04e9\u0448\u0435\u0441\u0456"
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u0410\u043b\u043c\u0430 \u043a\u04e9\u0448\u0435\u0441\u0456, \u0416\u04af\u0437\u0456\u043c \u043a\u04e9\u0448\u0435\u0441\u0456, \u04e8\u0440\u0456\u043a \u043a\u04e9\u0448\u0435\u0441\u0456"
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u0416\u04af\u0437\u0456\u043c \u043a\u04e9\u0448\u0435\u0441\u0456, \u04e8\u0440\u0456\u043a \u043a\u04e9\u0448\u0435\u0441\u0456, \u0410\u043b\u043c\u0430 \u043a\u04e9\u0448\u0435\u0441\u0456"
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230082"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0424\u0435\u0440\u043c\u0435\u0440 \u0441\u0443\u0440\u0435\u0442\u0442\u0435 \u043a\u04e9\u0440\u0441\u0435\u0442\u0456\u043b\u0433\u0435\u043d \u0436\u0435\u0440 \u0442\u0435\u043b\u0456\u043c\u0456\u043d\u0435 \u049b\u0430\u0437\u0434\u0430\u0440\u0493\u0430 \u0430\u0440\u043d\u0430\u043f \u049b\u043e\u0440\u0430 \u0441\u0430\u043b\u0493\u044b\u0441\u044b \u043a\u0435\u043b\u0435\u0434\u0456. \u04d8\u0440 \u049b\u0430\u0437\u0434\u044b\u04a3 \u0435\u0440\u043a\u0456\u043d \u0436\u0430\u0439\u044b\u043b\u044b\u043c\u044b \u04af\u0448\u0456\u043d 6 \u043c$^2$ \u049b\u0430\u0436\u0435\u0442. ",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "7f1d4cb752524fd6a504f68e6138e378",
                        "asset_object_name": "assets/7f1d4cb752524fd6a504f68e6138e378/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/7f1d4cb752524fd6a504f68e6138e378/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=TL1j35Rhjr%2BKrTJDPhqFjcml1xESzx3sGi5ZbR5YAk1%2BdCn%2BaPF%2FrhM8DW0pV%2BF1jWl9DkW26ZAa7iG1ye0ENLy7XyETKnutMhVF3xrrKlY4SUzOmkVTF9ZQ%2B9RLGqzGzynoKMjWWIuyBYsV0vIssyB3hGh3xoZFILmnkTto2wgNjJczz%2BQ%2FjJN0XwKjFNf6U47nQ8phWXFKERkUOdo4U7KXbqB4qNjifoDa%2FKB4zhJWyUM3PSh4G1OmcOrKrlsUi25z9dcNC2GVl7pgCTExkW0WUi3U47XE377cP9AhPO4n8376qkGkVwAOXc%2BqzaF%2B7yqRdCuiI1JtbZv0Ui%2FmTw%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0411\u04b1\u043b \u049b\u043e\u0440\u0430\u0493\u0430 \u049b\u0430\u043d\u0448\u0430 \u049b\u0430\u0437 \u0441\u044b\u044f\u0434\u044b?"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "11",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "12",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "13",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "14",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230083"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0411\u0456\u0440 \u043a\u0435\u0441\u0435 \u0431\u0430\u043b\u043c\u04b1\u0437\u0434\u0430\u049b 750 \u0442\u0435\u04a3\u0433\u0435 \u0442\u04b1\u0440\u0430\u0434\u044b. \u0411\u0430\u043b\u043c\u04b1\u0437\u0434\u0430\u049b\u0442\u044b \u043d\u0435\u0448\u0435 \u0442\u04af\u0440\u043b\u0456 \u0441\u0430\u043b\u044b\u043d\u0434\u044b\u043b\u0430\u0440\u043c\u0435\u043d \u0431\u0435\u0437\u0435\u043d\u0434\u0456\u0440\u0443\u0433\u0435 \u0431\u043e\u043b\u0430\u0434\u044b: \u0448\u043e\u043a\u043e\u043b\u0430\u0434, \u0436\u0430\u04a3\u0493\u0430\u049b, \u0434\u0430\u0440\u0448\u044b\u043d \u0436\u04d9\u043d\u0435 \u0442.\u0431. \u04d8\u0440 \u049b\u043e\u0441\u043f\u0430\u043d\u044b\u04a3 \u0431\u0430\u0493\u0430\u0441\u044b 100 \u0442\u0435\u04a3\u0433\u0435 \u0442\u04b1\u0440\u0430\u0434\u044b. ",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "67af7a7ffeab4c36bcf71f1b181822c6",
                        "asset_object_name": "assets/67af7a7ffeab4c36bcf71f1b181822c6/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/67af7a7ffeab4c36bcf71f1b181822c6/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=fxOIn3a9FT5Nm%2BTFvUdEkELmFnc2oh0V2ITSnAVjm%2FzzaGaDLilszLX8Gp5DbGcNhPk5VU1D7d2uyTbONM8YdcJoJGTSSVWUTQgl6JFXIgejec9%2FAOg4Nu03TJ9QF6ULUIySqr4zNAXP1FI7%2FV1MZMhCg882YLDfSWPbkOfYXoeRyyT%2FREohsX0nKHr5ge077ERxQw4U%2Bnw6RfgG6UvMUs%2F66sEY9tRDZXPCo0gMyzIVY%2BWTlmalN7ft7Pbipz0ybr2d0RqTbiJc5jHW0j816Is0SpuxsnbvBt8RE1cH2xKTG2gjY9syFfigEX1kU2RY2jThd5xwypJ4UIdplyAMdA%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0422\u04e9\u043c\u0435\u043d\u0434\u0435\u0433\u0456 \u0442\u0435\u04a3\u0434\u0435\u0443\u043b\u0435\u0440\u0434\u0456\u04a3 \u049b\u0430\u0439\u0441\u044b\u0441\u044b $k$ \u0441\u0430\u043b\u044b\u043d\u0434\u044b\u043b\u0430\u0440 \u0441\u0430\u043d\u044b \u043c\u0435\u043d $Y$ \u0431\u0430\u043b\u043c\u04b1\u0437\u0434\u0430\u049b\u0442\u044b\u04a3 \u049b\u04b1\u043d\u044b \u0430\u0440\u0430\u0441\u044b\u043d\u0434\u0430\u0493\u044b \u0431\u0430\u0439\u043b\u0430\u043d\u044b\u0441\u0442\u044b \u043a\u04e9\u0440\u0441\u0435\u0442\u0435\u0434\u0456?",
                        "has_formulas": true
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": " $Y=750+ 100k$",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$Y=100(750+ k)$",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$Y=750(k+100)$",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$Y=750+k:100$",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230084"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0415\u04a3\u0431\u0435\u043a \u0441\u0430\u0431\u0430\u0493\u044b\u043d\u0434\u0430 \u043e\u049b\u0443\u0448\u044b \u0430\u0493\u0430\u0448 \u0442\u0430\u049b\u0442\u0430\u0439\u0448\u0430\u0434\u0430\u043d \u0444\u043e\u0442\u043e\u0440\u0430\u043c\u043a\u0430 \u0436\u0430\u0441\u0430\u0434\u044b. \u0424\u043e\u0442\u043e\u0440\u0430\u043c\u043a\u0430\u043d\u044b\u04a3 \u04b1\u0437\u044b\u043d\u0434\u044b\u0493\u044b \u043c\u0435\u043d \u0435\u043d\u0456 \u0441\u04d9\u0439\u043a\u0435\u0441\u0456\u043d\u0448\u0435 $(18a+3,5b)$ \u043c \u0436\u04d9\u043d\u0435 $(21a-4b)$ \u043c \u04e9\u0440\u043d\u0435\u043a\u0442\u0435\u0440\u0456\u043c\u0435\u043d \u0431\u0435\u0440\u0456\u043b\u0433\u0435\u043d. ",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "a1a979591e3f44d2a14efd1c881fa7eb",
                        "asset_object_name": "assets/a1a979591e3f44d2a14efd1c881fa7eb/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/a1a979591e3f44d2a14efd1c881fa7eb/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=CwlTHv1hZnnEGwF6l1%2B3kfKsBSrrgQ8EIRR7YfbQIzJ6KJr2mQUPg2BJvuNNnJ4grpKijvihCBwQjgT60Rqu8hgaVPk7H2ffHgvWIsurM661UtVX%2Fy%2FbOnTj3jBYUPg3%2BZA9yqDEXIYBu20q1TCSnrGl5Kk8X7dgPxf3ieOfb1aa%2BiwZj9kgl0pjFOhRwS7595aov8YGRrPhhBrXUuB6MAwi%2BeUTMsXFlh0lhRO%2BIgWORmHEDdg5yhG1l9cgXbareIacboVOuxSHFT9jwOawlr7cKkE%2BnSGnxplK2YHzE8YiZv1sEIvGED%2Fzq7JMyXIZJDy4XVx0dLHhzaSQmjzfUQ%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041e\u0441\u044b\u043d\u0434\u0430\u0439 5 \u0444\u043e\u0442\u043e\u0440\u0430\u043c\u043a\u0430\u043d\u044b \u0436\u0430\u0441\u0430\u0443 \u04af\u0448\u0456\u043d \u043d\u0435\u0448\u0435 \u043c\u0435\u0442\u0440 \u0430\u0493\u0430\u0448 \u0442\u0430\u049b\u0442\u0430\u0439\u0448\u0430 \u049b\u0430\u0436\u0435\u0442?",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$(390a-5b)$ \u043c",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$(78a-b)$ \u043c",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$(390a-75b)$ \u043c",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$(390a+5b)$ \u043c",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230085"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041c\u0435\u043a\u0442\u0435\u043f\u0442\u0435 \u043e\u049b\u0443\u0448\u044b\u043b\u0430\u0440 \u0431\u0430\u043b\u044b\u049b \u0448\u0430\u0431\u0430\u049b\u0442\u0430\u0440\u044b\u043d\u0430 \u0430\u0437\u044b\u049b \u0440\u0435\u0442\u0456\u043d\u0434\u0435 \u0431\u0456\u0440 \u0436\u0430\u0441\u0443\u0448\u0430\u043b\u044b \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u043c\u0434\u0435\u0440\u0434\u0456 \u04e9\u0441\u0456\u0440\u0435\u0434\u0456. \u0411\u04b1\u043b \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u043c\u0434\u0435\u0440\u0434\u0456\u04a3 \u043a\u04e9\u0431\u0435\u044e\u0456 \u04d9\u0440\u0431\u0456\u0440 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u043c\u0434\u0435\u0440\u0434\u0456\u04a3 \u0435\u043a\u0456 \u0431\u04e9\u043b\u0456\u043a\u043a\u0435 \u0431\u04e9\u043b\u0456\u043d\u0443\u0456 \u0430\u0440\u049b\u044b\u043b\u044b \u0436\u04af\u0440\u0435\u0434\u0456. \u0411\u0430\u0441\u0442\u0430\u043f\u049b\u044b\u0434\u0430 \u044b\u0434\u044b\u0441\u0442\u0430 6 \u0431\u0456\u0440 \u0436\u0430\u0441\u0443\u0448\u0430\u043b\u044b \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u043c \u0431\u043e\u043b\u0434\u044b. "
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "b995b2f08c0e42e98aa7442b4bd948ef",
                        "asset_object_name": "assets/b995b2f08c0e42e98aa7442b4bd948ef/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/b995b2f08c0e42e98aa7442b4bd948ef/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=M3dDcm%2Bb3XStWGbwd8toJtop2jnxC4OWgQtGcP4vzNfGEIu45hw42fEjZLTkvx0IQfZs3CnzgggKFKsYzRX%2Bowl8aCpCdo0SKJHwkvFcgsa2rPGOG2aENyKqKgnKZaKs%2B8sQIeYE7QUZnye70J%2Fz8PAVokW24sdsI1X1ezzjuyxyo70SHj384muLUT8jhVp7QxlAv%2BTO7IVTOYhh6t162%2FdPPZEdzUGB%2Bh8R995F%2FgF4zdlRsEQrhguiFqlCuL1%2FvA0Ie%2Fe2oDxcbRbfDg%2FtbixuD6Wgjc%2B%2B6LEhtocOY9ssXlRbf%2FYTyi2t3EcWU8edDQ0SVZ50FK0RG3%2BXTxb2nQ%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0410\u043b\u0442\u044b \u0440\u0435\u0442 \u0431\u04e9\u043b\u0456\u043d\u0443 \u043f\u0440\u043e\u0446\u0435\u0441\u0456\u043d\u0435\u043d \u043a\u0435\u0439\u0456\u043d \u044b\u0434\u044b\u0441\u0442\u0430 \u043d\u0435\u0448\u0435 \u0431\u0456\u0440 \u0436\u0430\u0441\u0443\u0448\u0430\u043b\u044b \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u043c \u0431\u043e\u043b\u0430\u0442\u044b\u043d\u044b\u043d \u0430\u043d\u044b\u049b\u0442\u0430\u04a3\u044b\u0437."
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "96",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "192",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "384",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "768",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230086"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0421\u0443\u0440\u0435\u0442\u0448\u0456 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0442\u0430\u0440\u0434\u044b\u04a3 \u0448\u0435\u043a\u0441\u0456\u0437 \u0441\u0430\u043d\u044b\u043d \u0441\u0430\u043b\u0430 \u0431\u0430\u0441\u0442\u0430\u0434\u044b, \u043c\u04b1\u043d\u0434\u0430\u0493\u044b \u0435\u04a3 \u04af\u043b\u043a\u0435\u043d \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0442\u044b\u04a3 \u049b\u0430\u0431\u044b\u0440\u0493\u0430\u0441\u044b 4 \u0441\u043c, \u043a\u0435\u043b\u0435\u0441\u0456 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0442\u044b\u04a3 \u049b\u0430\u0431\u044b\u0440\u0493\u0430\u0441\u044b \u0430\u043b\u0434\u044b\u04a3\u0493\u044b\u0441\u044b\u043d\u0430\u043d 2 \u0435\u0441\u0435 \u043a\u0456\u0448\u0456. ",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "c66bacddc286481593c0bde53a006c0e",
                        "asset_object_name": "assets/c66bacddc286481593c0bde53a006c0e/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/c66bacddc286481593c0bde53a006c0e/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=fKCT0Ii2zEAxze5bYeZOEtkzkxCCA5dTlmHsrSV3fONOnPD1kpLicjtcAVFZ6YkVTzYtbbqQ8VzjT0R4YGphXc2t%2BA93A5ssUNydWbCjhfWiYAIBV%2BtpA2BQHxSXoGxDuQaljlPwnriyeBoYe%2B%2FgM1JBjJ6CzeqE%2FCkmUR4Sp56%2B0tovE60xRv4OjWBTxFO3IN%2FF8kM1Ydto5apYUcegN71maVYIpc02ZZNbVXL%2FwPed%2BDzn%2Fg8Ygmo5dRw4XK8UM7MOtPHLQOFI%2FRjf6XiVZBgW4VenBCHbK67k2QWNj4M7TYWEwEYddmaWDZLOYZBgIJaGIJ%2FzJL2jU6m2a6wFNQ%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041e\u0441\u044b \u0448\u0435\u043a\u0441\u0456\u0437 \u0441\u0430\u043b\u044b\u043d\u0493\u0430\u043d \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0442\u0430\u0440\u0434\u044b\u04a3 \u0430\u0443\u0434\u0430\u043d\u0434\u0430\u0440\u044b\u043d\u044b\u04a3 \u049b\u043e\u0441\u044b\u043d\u0434\u044b\u0441\u044b \u043d\u0435\u0433\u0435 \u0442\u0435\u04a3?"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$21$ \u0441\u043c$^2$",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$21\\frac{1}{3}$ \u0441\u043c$^2$",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$28$ \u0441\u043c$^2$",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$32$ \u0441\u043c$^2$",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230087"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0410\u0440\u0441\u0435\u043d \u0435\u0441\u0435\u043f \u049b\u04b1\u0440\u0430\u0441\u0442\u044b\u0440\u0443 \u0431\u0430\u0440\u044b\u0441\u044b\u043d\u0434\u0430 $CAE$ \u0431\u04b1\u0440\u044b\u0448\u044b\u043d \u043f\u0430\u0439\u0434\u0430\u043b\u0430\u043d\u0434\u044b. \u0415\u0441\u0435\u043f\u0442\u0456\u04a3 \u0441\u044b\u0437\u0431\u0430\u0441\u044b \u0442\u04e9\u043c\u0435\u043d\u0434\u0435 \u043a\u04e9\u0440\u0441\u0435\u0442\u0456\u043b\u0433\u0435\u043d, \u043c\u04b1\u043d\u0434\u0430\u0493\u044b $BD$ $||$ $CE$, $AB=4a$, $BC=\\frac{7}{3} a+4$, $AD=\\frac{1}{3} b+2$, $DE=\\frac{2}{3} b-4$.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "38845d829d50447993119fd397481d4b",
                        "asset_object_name": "assets/38845d829d50447993119fd397481d4b/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/38845d829d50447993119fd397481d4b/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=pKkf7wM%2FEbeZxyPeuCj4wdQlBixaEFxaPT9Em%2FdFMYinE5lLgxEiFThm0zJ2bAMMJvpmaxU9Ro4MvKxqbGTORKJR8ntZLpbQmWhn9PpuhWB890ilokFO5ATY3%2BB1%2FZucQEDQk1GPJW9xmukJ6iU5rC5QW7q2WTUe%2B%2B%2FO9bQvJLTirfgoeLUPaUMpgHddIKn67cT0u5dqJ%2Ft1eZQZoxva3yJFsgJTjpeW84pPZiTWg8nKLHXb1jtnbBIQhh9yHHLInmoDsPk9%2Bav8cAeaPSez3CtAbYTWl6FWbpqVo1CNCwmT8x9v6fj9LZxep8uJY3PdBu2gVlr0p%2Bd2zWibTuTccQ%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0421\u044b\u0437\u0431\u0430\u043d\u044b \u043f\u0430\u0439\u0434\u0430\u043b\u0430\u043d\u044b\u043f, $a$ \u0436\u04d9\u043d\u0435 $b$ \u043c\u04d9\u043d\u0434\u0435\u0440\u0456\u043d \u0435\u0441\u0435\u043f\u0442\u0435\u04a3\u0456\u0437.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$a=2,4; b=2$",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$a=2,4; b=18$",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$a=2,5; b= 18$",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$a=2,6; b= 6$",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230088"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430 \u0440\u0430\u0434\u0438\u043e\u0434\u0430\u0493\u044b 4 \u0441\u0430\u0493\u0430\u0442\u0442\u044b\u049b \u044d\u0444\u0438\u0440 \u043a\u0435\u0437\u0456\u043d\u0434\u0435 \u0436\u0456\u0431\u0435\u0440\u0456\u043b\u0433\u0435\u043d SMS \u0445\u0430\u0431\u0430\u0440\u043b\u0430\u043c\u0430\u043b\u0430\u0440\u0434\u044b\u04a3 \u0441\u0430\u043d\u044b\u043d \u043a\u04e9\u0440\u0441\u0435\u0442\u0435\u0434\u0456. ",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "083bfaba86034780af206a1cc312ed9f",
                        "asset_object_name": "assets/083bfaba86034780af206a1cc312ed9f/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/083bfaba86034780af206a1cc312ed9f/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=vvl%2BfnEiNrcuDsee5y75yTIQgbEgURqILOuW%2BAQBj8JCpIjl65uaL9OHJjCRkfobKyCP2Yrl%2BoCf%2Fs%2BmPrPzPVuXoQTkWzIr%2FZD9CqnGO5w%2FxsSKFkHl6xqIWQ%2FFwSRx5gxDJ0ux6ZP4%2Fb7xb4WFg15T%2F6tFCn3DXdvPN%2BfY4ylxBnsLuzjEs3xzPZyB%2FOFAKsaAHyAsWW9Do34MaFpAqHeG%2FJApAUzHSOFhfPmvwXTkiTvW1oD85YuMzh9hOA1wrUbdBBMWRw0CxCCWP4h%2FiAW89BYa9z44FEraJ1JBMmEFFQP5ul8NvWQzZ50hGfSFs83o7OqVrSeQt0leEC1zZA%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "4 \u0441\u0430\u0493\u0430\u0442\u0442\u044b\u049b \u044d\u0444\u0438\u0440\u0434\u0435 \u0436\u0456\u0431\u0435\u0440\u0456\u043b\u0433\u0435\u043d \u0445\u0430\u0431\u0430\u0440\u043b\u0430\u043c\u0430\u043b\u0430\u0440\u0434\u044b\u04a3 \u043e\u0440\u0442\u0430\u0448\u0430 \u0441\u0430\u043d\u044b\u043d \u0430\u043d\u044b\u049b\u0442\u0430\u04a3\u044b\u0437.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "15",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "20",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "25",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "30",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230089"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041d\u04d9\u0434\u0456\u0440 \u0446\u0438\u0440\u043a\u0442\u0435 \u0430\u043a\u0440\u043e\u0431\u0430\u0442\u0442\u0430\u0440\u0434\u044b\u04a3 \u049b\u0443\u043b\u044b\u0493\u044b\u043d \u043a\u04e9\u0440\u0434\u0456: \u04af\u0448 \u0430\u043a\u0440\u043e\u0431\u0430\u0442 \u04af\u0448\u0431\u04b1\u0440\u044b\u0448\u0442\u044b \u0431\u0456\u0440\u0442\u0435\u043a\u0442\u0456 \u043f\u043b\u0430\u0441\u0442\u0438\u043d\u0430\u043d\u044b\u04a3 \u0431\u04b1\u0440\u044b\u0448\u0442\u0430\u0440\u044b\u043d\u0434\u0430 \u0442\u04b1\u0440\u0434\u044b, \u0430\u043b \u0442\u04e9\u0440\u0442\u0456\u043d\u0448\u0456\u0441\u0456 \u043e\u043b\u0430\u0440\u0434\u044b \u0431\u0456\u0440 \u0430\u044f\u0493\u044b\u043c\u0435\u043d \u04b1\u0441\u0442\u0430\u0434\u044b. \u0411\u04b1\u043b \u049b\u0443\u043b\u044b\u049b\u0442\u044b \u0442\u04af\u0441\u0456\u043d\u0443 \u04af\u0448\u0456\u043d \u043e\u043b \u04af\u0439\u0434\u0435 \u0442\u04e9\u0431\u0435\u043b\u0435\u0440\u0456\u043d\u0456\u04a3 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u043b\u0430\u0440\u044b $F(-8;4)$, $G(-4;4)$, $H(-6;-2)$ \u0431\u043e\u043b\u0430\u0442\u044b\u043d $FGH$ \u04af\u0448\u0431\u04b1\u0440\u044b\u0448\u044b\u043d \u0441\u0430\u043b\u0434\u044b. \u0411\u04af\u043a\u0456\u043b \u049b\u0443\u043b\u044b\u049b \u04af\u0448\u0431\u04b1\u0440\u044b\u0448\u0442\u044b\u04a3 \u0430\u0443\u044b\u0440\u043b\u044b\u049b \u0446\u0435\u043d\u0442\u0440\u0456\u043d\u0434\u0435 \u0436\u0430\u0442\u049b\u0430\u043d\u044b\u043d \u0431\u0430\u0439\u049b\u0430\u0434\u044b (\u04af\u0448\u0431\u04b1\u0440\u044b\u0448\u0442\u044b\u04a3 \u043c\u0435\u0434\u0438\u0430\u043d\u0430\u043b\u0430\u0440\u044b\u043d\u044b\u04a3 \u049b\u0438\u044b\u043b\u044b\u0441\u0443 \u043d\u04af\u043a\u0442\u0435\u0441\u0456).",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "1806c8b30441411c941426b22639dc27",
                        "asset_object_name": "assets/1806c8b30441411c941426b22639dc27/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/1806c8b30441411c941426b22639dc27/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=Pjokk3cC%2Fhk2Shwrf3ovnT6b%2FsomlZFPmVkRwI6WwHsyHaY93QLtLVc0k79tNoT%2FOf6xnStPU6oQAppFkTgd%2F9koAcEK%2Bw6AL8ixoO%2BaV0o1NbTvomrItyMVBbAQOVv0OxzpDcQnAufTLwG8Lciev42IrJKeAZWvg5yaw8ShQ4LIjOehu5zjUO%2FDO0QrLD7oSq%2Fvx39Tj58aH0KAzeWTlgci6Zx17rxJ11c2IQKPHg7AX0QT8HY6V%2FmpLEMKVL5WyHOfbdQqBa%2BCNDs%2FIu4TCl4e12lpjT6LEDHBVmQ6PaZ4k4wcA95aW5OQ4jHjAv1lyGXDQ3JMpPZx0pm%2B5cmc%2FA%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "$FGH$ \u04af\u0448\u0431\u04b1\u0440\u044b\u0448\u044b\u043d\u044b\u04a3 $O$ \u0430\u0443\u044b\u0440\u043b\u044b\u049b \u0446\u0435\u043d\u0442\u0440\u0456\u043d\u0456\u04a3 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u043b\u0430\u0440\u044b\u043d \u0442\u0430\u0431\u044b\u04a3\u044b\u0437.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "correct_id": null,
                "choices": [
                    {
                        "meta_data": {
                            "text": "$O(-6; 2)$",
                            "has_formulas": true
                        },
                        "id": 1,
                        "choice_class": "MultichoiceTextChoice"
                    },
                    {
                        "meta_data": {
                            "text": "$O(0; -4)$",
                            "has_formulas": true
                        },
                        "id": 2,
                        "choice_class": "MultichoiceTextChoice"
                    },
                    {
                        "meta_data": {
                            "text": "$O(-6; 4)$",
                            "has_formulas": true
                        },
                        "id": 3,
                        "choice_class": "MultichoiceTextChoice"
                    },
                    {
                        "meta_data": {
                            "text": "$O(-5; 1)$",
                            "has_formulas": true
                        },
                        "id": 4,
                        "choice_class": "MultichoiceTextChoice"
                    }
                ],
                "question_code": "M9KZ230090"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0420\u0438\u043d\u0430\u0442 \u0436\u0430\u0442\u0442\u044b\u0493\u0443 \u0437\u0430\u043b\u044b\u043d\u0434\u0430 \u0441\u043e\u043b\u0442\u04af\u0441\u0442\u0456\u043a\u043a\u0435 2 \u043c, \u0448\u044b\u0493\u044b\u0441\u049b\u0430 1,5 \u043c, \u043e\u04a3\u0442\u04af\u0441\u0442\u0456\u043a\u043a\u0435 1 \u043c, \u0431\u0430\u0442\u044b\u0441\u049b\u0430 3,5 \u043c \u0436\u04d9\u043d\u0435 \u0441\u043e\u043b\u0442\u04af\u0441\u0442\u0456\u043a\u043a\u0435 \u049b\u0430\u0440\u0430\u0439 3 \u043c \u0436\u04af\u0440\u0435\u0434\u0456.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0411\u0430\u0441\u0442\u0430\u043f\u049b\u044b \u043d\u04af\u043a\u0442\u0435\u0434\u0435\u043d \u0441\u043e\u04a3\u0493\u044b \u043d\u04af\u043a\u0442\u0435\u0433\u0435 \u0434\u0435\u0439\u0456\u043d\u0433\u0456 \u049b\u0430\u0448\u044b\u049b\u0442\u044b\u049b\u0442\u044b \u0430\u043d\u044b\u049b\u0442\u0430\u04a3\u044b\u0437."
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$\\sqrt6$ \u043c",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$2\\sqrt5$ \u043c",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$\\sqrt{41}$ \u043c",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$\\sqrt{61}$ \u043c",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230091"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u049a\u0430\u0440\u0430\u0442\u0430\u0435\u0432\u0442\u0430\u0440 \u043e\u0442\u0431\u0430\u0441\u044b \u0430\u0443\u0434\u0430\u043d\u044b 96 \u043c$^2$ \u0431\u043e\u043b\u0430\u0442\u044b\u043d \u0442\u0456\u043a\u0442\u04e9\u0440\u0442\u0431\u04b1\u0440\u044b\u0448\u0442\u044b \u0436\u0435\u0440 \u0442\u0435\u043b\u0456\u043c\u0456\u043d \u0441\u0430\u0442\u044b\u043f \u0430\u043b\u044b\u043f, \u043e\u043b \u0430\u0443\u043c\u0430\u049b\u0442\u044b \u049b\u043e\u0440\u0448\u0430\u0443\u0493\u0430 \u0448\u0435\u0448\u0456\u043c \u049b\u0430\u0431\u044b\u043b\u0434\u0430\u0434\u044b. \u041e\u0442\u0431\u0430\u0441\u044b \u043c\u04af\u0448\u0435\u043b\u0435\u0440\u0456\u043d\u0456\u04a3 \u0430\u0439\u0442\u0443\u044b\u043d\u0448\u0430, 40 \u043c \u0434\u0443\u0430\u043b \u0441\u0430\u0442\u044b\u043f \u0430\u043b\u0443\u044b \u043a\u0435\u0440\u0435\u043a. ",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u049a\u043e\u0440\u0448\u0430\u0443\u0434\u044b\u04a3 \u04b1\u0437\u044b\u043d\u0434\u044b\u0493\u044b \u043c\u0435\u043d \u0435\u043d\u0456\u043d \u0430\u043d\u044b\u049b\u0442\u0430\u04a3\u044b\u0437."
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "11 \u043c; 9 \u043c",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "12 \u043c; 8 \u043c",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "13 \u043c; 7 \u043c",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "14 \u043c; 6 \u043c",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230092"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0416\u044b\u043b\u044b\u0436\u0430\u0439\u0434\u0430 \u043d\u0430\u0440\u0446\u0438\u0441\u0441 \u04e9\u0441\u0456\u0440\u0443 \u04af\u0448\u0456\u043d \u0442\u0456\u043a\u0431\u04b1\u0440\u044b\u0448\u0442\u044b \u04af\u0448\u0431\u04b1\u0440\u044b\u0448 \u0444\u043e\u0440\u043c\u0430\u0441\u044b\u043d\u0434\u0430\u0493\u044b \u0436\u0435\u0440 \u0443\u0447\u0430\u0441\u043a\u0435\u0441\u0456 \u0431\u0430\u0440. \u0416\u0435\u0440 \u0443\u0447\u0430\u0441\u043a\u0435\u0441\u0456\u043d\u0456\u04a3 \u04e9\u043b\u0448\u0435\u043c\u0434\u0435\u0440\u0456 \u0441\u0443\u0440\u0435\u0442\u0442\u0435 \u043a\u04e9\u0440\u0441\u0435\u0442\u0456\u043b\u0433\u0435\u043d. "
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "20af46c7af16472bb6c8b8573ecd20e0",
                        "asset_object_name": "assets/20af46c7af16472bb6c8b8573ecd20e0/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/20af46c7af16472bb6c8b8573ecd20e0/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=YKcV1xlZJb1zbuqnzCdG4oqmZzswiRPr%2B74%2F0cLsNZtqwVResAAX%2BmsD%2BPaMlO0utRgCzszz6ICtW7R4UUQS%2BsJX0ivlftlh9dwurIh0IjBy6laZMWRkMYGhbB9P%2FXSwRk0vhYtn9xik%2BobvB2R2bf57joP%2FcoT7DalpDf4lVVypWpi1Uk9M%2BTruZq0RF16NqOe9Je0C80Sbl1fvzL6669Rnr8qsc6gr%2FSrh6No%2B3LvgMYcuYJj6xOKUCclXndYpJzT3nIgYFSw8F9drrQYyvMCRh%2B6IADvO%2BIMv3IAoapVSTFMXzcRYWDquzd1fj%2FKKvlIojfTfPyefWKfO7pHrMQ%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0422\u0438\u0456\u0441\u0442\u0456 \u0435\u0441\u0435\u043f\u0442\u0435\u0443\u043b\u0435\u0440\u0434\u0456 \u0436\u04af\u0440\u0433\u0456\u0437\u0456\u043f, $x$ \u043c\u04d9\u043d\u0456\u043d \u0430\u043d\u044b\u049b\u0442\u0430\u04a3\u044b\u0437.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "3",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "4",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "6",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "8",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230093"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041a\u043e\u043d\u0434\u0438\u0442\u0435\u0440 \u0444\u0430\u0431\u0440\u0438\u043a\u0430\u0441\u044b\u043d\u044b\u04a3 \u0442\u043e\u0440\u0442\u0442\u0430\u0440\u0434\u044b \u0441\u0430\u0442\u0443\u0434\u0430\u043d \u0442\u04af\u0441\u043a\u0435\u043d \u0442\u0430\u0431\u044b\u0441\u044b $P(x) = -0,5x^2+30x-19$ \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u0441\u044b\u043c\u0435\u043d \u0441\u0438\u043f\u0430\u0442\u0442\u0430\u043b\u0430\u0434\u044b, \u043c\u04b1\u043d\u0434\u0430\u0493\u044b $x$ - \u0442\u043e\u0440\u0442\u0442\u0430\u0440 \u0441\u0430\u043d\u044b. ",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041d\u0435\u0448\u0435 \u0442\u043e\u0440\u0442 \u0441\u0430\u0442\u049b\u0430\u043d\u0434\u0430 \u0444\u0430\u0431\u0440\u0438\u043a\u0430\u043d\u044b\u04a3 \u043a\u0456\u0440\u0456\u0441\u0456 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u0434\u044b \u043c\u04d9\u043d\u0433\u0435 \u0438\u0435 \u0431\u043e\u043b\u0430\u0434\u044b?"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "15",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "19",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "30",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "60",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230094"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0421\u0443 \u0434\u043e\u0431\u044b \u043a\u043e\u043c\u0430\u043d\u0434\u0430\u0441\u044b\u043d\u044b\u04a3 \u049b\u04b1\u0440\u0430\u043c\u044b\u043d\u0434\u0430 16 \u043e\u0439\u044b\u043d\u0448\u044b \u0431\u0430\u0440 \u0436\u04d9\u043d\u0435 \u0436\u0430\u0442\u0442\u044b\u049b\u0442\u044b\u0440\u0443\u0448\u044b \u0431\u0456\u0440\u0456\u043d\u0448\u0456 \u043c\u0430\u0442\u0447\u049b\u0430 3 \u043e\u0439\u044b\u043d\u0448\u044b \u0442\u0430\u04a3\u0434\u0430\u043f \u04af\u043b\u0433\u0435\u0440\u0433\u0435\u043d. \u041e\u043b \u0435\u043d\u0434\u0456 7 \u043e\u0439\u044b\u043d\u0448\u044b\u0434\u0430\u043d \u0442\u04b1\u0440\u0430\u0442\u044b\u043d \u0442\u043e\u043b\u044b\u049b \u049b\u04b1\u0440\u0430\u043c\u0434\u044b \u0436\u0430\u0441\u0430\u049b\u0442\u0430\u0443 \u04af\u0448\u0456\u043d \u0442\u0430\u0493\u044b 4 \u043e\u0439\u044b\u043d\u0448\u044b\u043d\u044b \u0442\u0430\u04a3\u0434\u0430\u0443\u044b \u043a\u0435\u0440\u0435\u043a. ",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "8a4d1a1cdc944ac9b83f667f08068ba7",
                        "asset_object_name": "assets/8a4d1a1cdc944ac9b83f667f08068ba7/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/8a4d1a1cdc944ac9b83f667f08068ba7/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=U1kCq%2BI583rHaQknbDwhmyzeTCNng6IJVbT1TVwGc6%2BPh%2B7n60zGdMTkAUCrjveq41u9CUjSW9x4PcYDdh87kapHlOctOoafTsvJxIfHo%2B9DO4CjaGyLmQI7RuvqBdG5a13fJer89sDpQWX%2Ft9o%2BbN6OCreKnS46PLzovlucYWYUYr5MMTZKVGG1zUL%2Bxe7S6atvmBiHRrPaCzqXwiRjyIAdvXOkz%2BuhB4vGnxYlj2NdyeySkfCf4m%2B6nwpnDSOaHT9z0OFv9gBh9cWVZXmoFqna2d%2FclgtfdbEe3zMfVbqsxzDg5m48ZhrAjVqw3GgbvhduFXbeaEpYUM%2BfHGgdaw%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041e\u0441\u044b 4 \u043e\u0439\u044b\u043d\u0448\u044b\u043d\u044b \u0442\u0430\u04a3\u0434\u0430\u0443\u0434\u044b\u04a3 \u043d\u0435\u0448\u0435 \u0442\u04af\u0440\u043b\u0456 \u0436\u043e\u043b\u044b \u0431\u0430\u0440?",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "413",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "510",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "715",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "729",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230095"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0416\u043e\u043b \u0443\u0447\u0430\u0441\u043a\u0435\u0441\u0456\u043d\u0434\u0435 7 \u043a\u04e9\u043b\u0456\u043a\u0442\u0456\u04a3 \u0436\u044b\u043b\u0434\u0430\u043c\u0434\u044b\u0493\u044b \u0431\u0435\u043b\u0433\u0456\u043b\u0456. \u0410\u043b\u0430\u0439\u0434\u0430, \u0435\u043a\u0456 \u043a\u04e9\u043b\u0456\u043a\u0442\u0456\u04a3 \u0436\u044b\u043b\u0434\u0430\u043c\u0434\u044b\u0493\u044b \u0442\u0443\u0440\u0430\u043b\u044b \u0434\u0435\u0440\u0435\u043a\u0442\u0435\u0440 \u0436\u043e\u0493\u0430\u043b\u044b\u043f \u043a\u0435\u0442\u043a\u0435\u043d. \u0411\u0430\u0440\u043b\u044b\u049b \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c\u0434\u0435\u0440\u0434\u0456\u04a3 \u043e\u0440\u0442\u0430\u0448\u0430 \u0436\u044b\u043b\u0434\u0430\u043c\u0434\u044b\u0493\u044b 80 \u043a\u043c/\u0441\u0430\u0493, \u0430\u043b \u0431\u0430\u0440\u043b\u044b\u049b \u043a\u04e9\u043b\u0456\u043a\u0442\u0435\u0440 \u0436\u044b\u043b\u0434\u0430\u043c\u0434\u044b\u0493\u044b\u043d\u044b\u04a3 \u043c\u0435\u0434\u0438\u0430\u043d\u0430\u0441\u044b 78 \u043a\u043c/\u0441\u0430\u0493.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "3bc9d90c383d40958a52dcae76637ce3",
                        "asset_object_name": "assets/3bc9d90c383d40958a52dcae76637ce3/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/3bc9d90c383d40958a52dcae76637ce3/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=Ol4pRhnCIjGY%2FN5o3fX65kysfeu9PYsXNJVm5RHoUdyD8047keiRvmosqzxurw8cXEILmhyrEhHNq1H8esqB7%2BjDfhzJIgi1gcCyhkW25Gxp6Om0Qg1U7X%2F6cOcfMkWxqHN7HFz69d5RKXj9oLluT8%2FgMIAzx6PJgzi2VW8Z4dT1SAMScZuWs5hcbuqh3efExYteAZ58Ys%2FusrwFWbE5Mu416CjX%2B0ndCXelHFuacqX%2BtQg7O6TEpORe8bHJlqdUqCOJbuNqZYlBkcHAxft9D6x9mVKok%2BWpTFY4rD3XAZ%2BqIiNP0ba608XR5fjjtPjO3aEC1h4pFHI7KeRtZrQtPQ%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0415\u0433\u0435\u0440 \u21162-\u043d\u0456\u04a3 \u0436\u044b\u043b\u0434\u0430\u043c\u0434\u044b\u0493\u044b \u21167-\u043d\u0456\u04a3 \u0436\u044b\u043b\u0434\u0430\u043c\u0434\u044b\u0493\u044b\u043d\u0430\u043d \u0430\u0440\u0442\u044b\u049b \u0431\u043e\u043b\u0441\u0430, \u043e\u0441\u044b \u0435\u043a\u0456 \u043a\u04e9\u043b\u0456\u043a\u0442\u0456\u04a3 \u0436\u044b\u043b\u0434\u0430\u043c\u0434\u044b\u0493\u044b\u043d \u0430\u043d\u044b\u049b\u0442\u0430\u04a3\u044b\u0437."
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u21162 \u2013 79, \u21167 \u2013 70",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u21162 \u2013 82, \u21167 \u2013 76",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u21162 \u2013 93, \u21167 \u2013 75",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "\u21162 \u2013 100, \u21167 \u2013 78",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230096"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041e\u049b\u0443\u0448\u044b\u043b\u0430\u0440 \u043a\u0443\u0431\u0442\u044b\u04a3 \u0442\u043e\u043b\u044b\u049b \u0431\u0435\u0442\u0456\u043d\u0456\u04a3 \u0430\u0443\u0434\u0430\u043d\u044b\u043d\u0430 \u0437\u0435\u0440\u0442\u0442\u0435\u0443 \u0436\u04af\u0440\u0433\u0456\u0437\u0443\u0434\u0435. \u0411\u0430\u0441\u0442\u0430\u043f\u049b\u044b\u0434\u0430 \u043e\u043b\u0430\u0440\u0434\u0430 \u049b\u044b\u0440\u044b\u043d\u044b\u04a3 \u04b1\u0437\u044b\u043d\u0434\u044b\u0493\u044b 8 \u0441\u043c \u0431\u043e\u043b\u0430\u0442\u044b\u043d \u043a\u0443\u0431 \u0431\u0430\u0440. \u04d8\u0440\u0456 \u049b\u0430\u0440\u0430\u0439 \u043e\u049b\u0443\u0448\u044b\u043b\u0430\u0440 \u043a\u0443\u0431\u0442\u044b\u04a3 \u043f\u0456\u0448\u0456\u043d\u0456\u043d \u0441\u0430\u049b\u0442\u0430\u0439 \u043e\u0442\u044b\u0440\u044b\u043f, \u043e\u043d\u044b\u04a3 \u04d9\u0440\u0431\u0456\u0440 \u049b\u044b\u0440\u044b\u043d\u044b\u04a3 \u04b1\u0437\u044b\u043d\u0434\u044b\u0493\u044b\u043d 50%-\u0493\u0430 \u04b1\u043b\u0493\u0430\u0439\u0442\u0430\u0434\u044b. \u041e\u043b\u0430\u0440 \u04b1\u043b\u0493\u0430\u0439\u0442\u0443 \u043f\u0440\u043e\u0446\u0435\u0441\u0456\u043d \u0431\u0456\u0440\u043d\u0435\u0448\u0435 \u0440\u0435\u0442 \u049b\u0430\u0439\u0442\u0430\u043b\u0430\u0439\u0434\u044b.",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041a\u0443\u0431\u0442\u044b\u04a3 \u0442\u043e\u043b\u044b\u049b \u0431\u0435\u0442\u0456\u043d\u0456\u04a3 \u0430\u0443\u0434\u0430\u043d\u044b 4000 \u0441\u043c$^2$-\u0442\u0430\u043d \u043a\u04e9\u043f \u0431\u043e\u043b\u0443 \u04af\u0448\u0456\u043d \u0435\u04a3 \u043a\u0435\u043c \u0434\u0435\u0433\u0435\u043d\u0434\u0435 \u049b\u044b\u0440\u044b\u043d \u043d\u0435\u0448\u0435 \u0440\u0435\u0442 \u04b1\u043b\u0493\u0430\u0439\u0442\u0443\u044b \u043a\u0435\u0440\u0435\u043a?",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "3",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "4",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "5",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "6",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230097"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041e\u049b\u0443\u0448\u044b\u043b\u0430\u0440 5 \u043a\u04af\u043d \u0431\u043e\u0439\u044b \u049b\u0430\u043b\u0430\u0434\u0430\u0493\u044b \u0448\u0443 \u0434\u0435\u04a3\u0433\u0435\u0439\u0456\u043d \u04e9\u043b\u0448\u0435\u0439\u0434\u0456. \u042d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442 \u043d\u04d9\u0442\u0438\u0436\u0435\u043b\u0435\u0440\u0456 \u043a\u0435\u0441\u0442\u0435\u0434\u0435 \u043a\u0435\u043b\u0442\u0456\u0440\u0456\u043b\u0433\u0435\u043d:",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "3903a0ba4eae4db3bc05d21fa122d0de",
                        "asset_object_name": "assets/3903a0ba4eae4db3bc05d21fa122d0de/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/3903a0ba4eae4db3bc05d21fa122d0de/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=BzjVWA3FR2d%2FymQoPrJ%2FkAWMOMO2LkWPlPXMr%2B1e8e5z69fUe2ujtWQQJPl0chToI3dJ%2FJdm4JWNXutQnk2%2FybpC5auaBnPwCJHkml1jJVcMyVpr03eHuDyuo8m1WvrwIgNEP1l5DHKTfXJ85AuBlA1fJXEthIeCvLWMALiffKUaBaPoVIMvOmTXyvoPn4xTA23YmndCKCdcQ%2FM1za3KxRlkK%2BXEpkJhVXjSaxJpZk%2Bg5JP2%2FH%2BZgvGbrYtneU41TWm6NxIwg1SK4sTQNbrsheRde1VQKqkH2rs3jt7qBOVzSfar3dMtQb9J1iZvLY9%2B3b3%2FsutOP6ExXx6hxR1GBg%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u041e\u049b\u0443\u0448\u044b\u043b\u0430\u0440 5 \u043a\u04af\u043d \u0456\u0448\u0456\u043d\u0434\u0435\u0433\u0456 \u0448\u0443 \u0434\u0435\u04a3\u0433\u0435\u0439\u0456\u043d\u0456\u04a3 99,7%-\u044b \u0448\u0443 \u0434\u0435\u04a3\u0433\u0435\u0439\u0456\u043d\u0456\u04a3 \u043e\u0440\u0442\u0430\u0448\u0430 \u043c\u04d9\u043d\u0456\u043d\u0435\u043d 3 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u0442\u044b \u0430\u0443\u044b\u0442\u049b\u0443 \u0430\u0440\u0430\u043b\u044b\u0493\u044b\u043d\u0434\u0430 \u0436\u0430\u0442\u0430\u0442\u044b\u043d\u044b\u043d \u0431\u0456\u043b\u0435\u0434\u0456. \u042f\u0493\u043d\u0438,",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "ImageParagraph",
                    "meta_data": {
                        "asset_uuid": "0af8de2d33b149dc9c4b0f8c4c703412",
                        "asset_object_name": "assets/0af8de2d33b149dc9c4b0f8c4c703412/file",
                        "asset_url": "https://monitoring.edu.kz/storage/iac-001/assets/0af8de2d33b149dc9c4b0f8c4c703412/file?Expires=1713285472&GoogleAccessId=storage-service-account%40bbtest-287409.iam.gserviceaccount.com&Signature=0qG62M3tI7NXi4MUA9mh31hVWotlP8YHc50dBzyvkc4msVYhGjRCCf3RmdLcB0zQxNe9s1lbaaohKWw%2BAuj%2FVZ%2Fqq%2BPJcftYQoPP7hleRTdlS2abu%2F0NWh8agYqm7s%2FF%2BWffSREoYS5JQx%2Fwhhz9DTcvNiRTrexkA7ahAL%2FiFU7SD4pdnPJlhpBtPHCNCFHL3%2BsXMSOITRtXBxXezzymucViiWxIq0%2Fxc0cp4ejKZmbsgveNVxNn%2FLr%2FQGBEvDJUDJ%2BvLiDEpJVgwQG5xbHBDAGn2hCmc7gA1odq8ifHEbJylT%2Fj3BdAvH7vTaoSc0xqJD2YGLu2d8%2Fr8RtaGdaK%2Bw%3D%3D"
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0428\u0443 \u0434\u0435\u04a3\u0433\u0435\u0439\u0456\u043d\u0456\u04a3 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u0442\u044b \u0430\u0443\u044b\u0442\u049b\u0443\u044b 3 \u0434\u0435\u0446\u0438\u0431\u0435\u043b."
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0428\u0443 \u0434\u0435\u04a3\u0433\u0435\u0439\u0456\u043d\u0456\u04a3 99,7%-\u044b \u0436\u0430\u0442\u0430\u0442\u044b\u043d \u0430\u0440\u0430\u043b\u044b\u049b\u0442\u044b \u0430\u043d\u044b\u049b\u0442\u0430\u04a3\u044b\u0437."
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "CalculatorParagraph",
                    "meta_data": {
                        "text": "",
                        "calculator": "TODO"
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "(70; 88)",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "(72; 84)",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "(75; 85)",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "(76; 84)",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230098"
            }
        },
        {
            "paragraphs": [
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0410\u0443\u044b\u043b \u0442\u04b1\u0440\u0493\u044b\u043d\u0434\u0430\u0440\u044b\u043d\u044b\u04a3 \u0441\u0430\u043d\u044b \u0436\u044b\u043b \u0441\u0430\u0439\u044b\u043d 5%-\u0493\u0430 \u0430\u0440\u0442\u0430\u0434\u044b. \u0422\u04b1\u0440\u0493\u044b\u043d\u0434\u0430\u0440\u0434\u044b\u04a3 \u0431\u0430\u0441\u0442\u0430\u043f\u049b\u044b \u0441\u0430\u043d\u044b \u2013 200 \u0430\u0434\u0430\u043c \u0434\u0435\u043b\u0456\u043a. ",
                        "has_formulas": true
                    },
                    "is_shared": false
                },
                {
                    "paragraph_class": "TextParagraph",
                    "meta_data": {
                        "text": "\u0411\u0435\u0440\u0456\u043b\u0433\u0435\u043d $F(t)$ \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u043b\u0430\u0440\u044b\u043d\u044b\u04a3 \u049b\u0430\u0439\u0441\u044b\u0441\u044b \u0430\u0443\u044b\u043b\u0434\u0430\u0493\u044b $t$ \u0436\u044b\u043b \u04e9\u0442\u043a\u0435\u043d\u0434\u0435\u0433\u0456 \u0442\u04b1\u0440\u0493\u044b\u043d\u0434\u0430\u0440\u0434\u044b\u04a3 \u0441\u0430\u043d\u044b\u043d \u0430\u043d\u044b\u049b\u0442\u0430\u0443\u0493\u0430 \u043a\u04e9\u043c\u0435\u043a\u0442\u0435\u0441\u0435\u0434\u0456?",
                        "has_formulas": true
                    },
                    "is_shared": false
                }
            ],
            "answer_class": "MultichoiceOneAnswer",
            "meta_data": {
                "choices": [
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$F(t)=200*(0,95)^t$",
                            "has_formulas": true
                        },
                        "id": 1
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$F(t)=200*(1,05)^t$",
                            "has_formulas": true
                        },
                        "id": 2
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$F(t)=200+0,05t$",
                            "has_formulas": true
                        },
                        "id": 3
                    },
                    {
                        "choice_class": "MultichoiceTextChoice",
                        "meta_data": {
                            "text": "$F(t)=205*(1,05)^t$",
                            "has_formulas": true
                        },
                        "id": 4
                    }
                ],
                "correct_id": null,
                "question_code": "M9KZ230099"
            }
        }
    ],
    "report": {
        "answers": [
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            },
            {
                "answer": null,
                "observation": {}
            }
        ],
        "observation": {}
    },
    "texts": {
        "shared_paragraph_header": "\u041c\u04d9\u0442\u0456\u043d",
        "column_a": "A \u049b\u0430\u0442\u0430\u0440\u044b",
        "column_b": "B \u049b\u0430\u0442\u0430\u0440\u044b"
    }
}

from bbtest.models import User

user_list = [
    "91108400001",
    "91108400002",
    "91108400003",
]
qset = User.objects.filter(username__in=user_list)

qset.update(is_active=False)