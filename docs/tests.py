from django.contrib.auth import get_user_model
from django.utils.lorem_ipsum import paragraph, words
from random import randint
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
    _question.meta_data["correct_id"] = _question.meta_data["choices"][0]["id"]
    for _choice in _question.meta_data["choices"]:
        _choice["meta_data"]["text"] = words(randint(3, 6), False)
    _question.save()
    # paragraphs
    _paragraph = _question.paragraphs.first()
    _paragraph.meta_data["text"] = paragraph()
    _paragraph.save()


# NIS Kazakh language
_test = TestForm(data={
    "section": 9541,
    "language": "kk",
}).create_test_suite(_developer)
for i, _question in enumerate(_test.questions.all()):
    # difficulty
    if i in range(0, 5):
        _question.difficulty = TestQuestion.DIFFICULTY_LOW
    elif i in range(5, 15):
        _question.difficulty = TestQuestion.DIFFICULTY_NORMAL
    elif i in range(15, 20):
        _question.difficulty = TestQuestion.DIFFICULTY_HIGH
    # taxonomy
    if i in range(0, 13):
        _question.taxonomy_id = 3531
    elif i in range(13, 18):
        _question.taxonomy_id = 3532
    elif i in range(18, 20):
        _question.taxonomy_id = 3533
    # topic
    if i in range(0, 5):
        _question.topic_id = 5176
    elif i in range(5, 10):
        _question.topic_id = 5182
    elif i in range(10, 15):
        _question.topic_id = 5185
    elif i in range(15, 20):
        _question.topic_id = 5190
    # answer
    _question.meta_data["correct_id"] = _question.meta_data["choices"][0]["id"]
    for _choice in _question.meta_data["choices"]:
        _choice["meta_data"]["text"] = words(randint(3, 6), False)
    _question.save()
    # paragraphs
    _shared_paragraph_pks = set()
    if _question.paragraphs.count():
        _paragraph = _question.paragraphs.first()
        if _paragraph.pk not in _shared_paragraph_pks:
            _paragraph.meta_data["text"] = paragraph()
            _paragraph.save()
            _shared_paragraph_pks.add(_paragraph.pk)
        _paragraph = _question.paragraphs.last()
        _paragraph.meta_data["text"] = paragraph()
        _paragraph.save()
    else:
        _paragraph = _question.paragraphs.first()
        _paragraph.meta_data["text"] = paragraph()
        _paragraph.save()
