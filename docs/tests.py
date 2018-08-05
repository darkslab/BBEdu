from django.contrib.auth import get_user_model
from django.utils.lorem_ipsum import paragraph, words
from random import randint, choice
from bbtest.models import TestQuestion
from bbtest.forms.test import TestForm


_developer = get_user_model().objects.get(pk=3085)


# NIS Mathematics
_test = TestForm(data={
    "section": 9540,
    "language": "kk",
}).create_test_suite(_developer)
for i, _question in enumerate(_test.questions.all()):
    # difficulty
    if i in range(0, 10):
        _question.difficulty = TestQuestion.DIFFICULTY_LOW
    elif i in range(10, 30):
        _question.difficulty = TestQuestion.DIFFICULTY_NORMAL
    elif i in range(30, 40):
        _question.difficulty = TestQuestion.DIFFICULTY_HIGH
    # taxonomy
    if i in range(0, 24):
        _question.taxonomy_id = 3529
    elif i in range(24, 40):
        _question.taxonomy_id = 3530
    # topic
    if i in range(0, 6):
        _question.topic_id = 5156
    elif i in range(6, 10):
        _question.topic_id = 5157
    elif i in range(10, 16):
        _question.topic_id = 5158
    elif i in range(16, 20):
        _question.topic_id = 5159
    elif i in range(20, 26):
        _question.topic_id = 5160
    elif i in range(26, 32):
        _question.topic_id = 5161
    elif i in range(32, 36):
        _question.topic_id = 5162
    elif i in range(36, 40):
        _question.topic_id = 5163
    # answer
    _question.meta_data["correct_id"] = choice([ _choice["id"] for _choice in _question.meta_data["choices"] ])
    for _choice in _question.meta_data["choices"]:
        _choice["meta_data"]["text"] = words(randint(3, 6), False)
    _question.save()
    # paragraphs
    _paragraph = _question.paragraphs.first()
    _paragraph.meta_data["text"] = paragraph()
    _paragraph.save()
