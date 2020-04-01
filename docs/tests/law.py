from django.contrib.auth import get_user_model
from django.utils.lorem_ipsum import paragraph, words
from random import randint
from bbtest.models import TestQuestion
from bbtest.forms.test import TestForm


_developer = get_user_model().objects.get(pk=3083)
_test_lang = "ru"


# LAW
_test = TestForm(data={
    "section": 9565,
    "language": _test_lang,
}).create_test_suite(_developer)
for i, _question in enumerate(_test.questions.all()):
    # difficulty
    _question.difficulty = TestQuestion.DIFFICULTY_NORMAL
    # taxonomy
    pass
    # topic
    _question.topic_id = randint(5326, 5335)
    # answer
    _question.meta_data["correct_id"] = _question.meta_data["choices"][0]["id"]
    for _choice in _question.meta_data["choices"]:
        _choice["meta_data"]["text"] = words(randint(3, 6), False)
    _question.save()
    # paragraphs
    _paragraph = _question.paragraphs.first()
    _paragraph.meta_data["text"] = paragraph()
    _paragraph.save()
