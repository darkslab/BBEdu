from django.contrib.auth import get_user_model
from django.utils.lorem_ipsum import paragraph, words
from random import randint
from bbtest.models import TestQuestion
from bbtest.forms.test import TestForm


_developer = get_user_model().objects.get(pk=3085)
_test_lang = "kk"


# NIS Mathematics
_test = TestForm(data={
    "section": 9540,
    "language": _test_lang,
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


# NIS Quantitative
_test = TestForm(data={
    "section": 9544,
    "language": _test_lang,
}).create_test_suite(_developer)
for i, _question in enumerate(_test.questions.all()):
    # difficulty
    if i in range(0, 15):
        _question.difficulty = TestQuestion.DIFFICULTY_LOW
    elif i in range(15, 45):
        _question.difficulty = TestQuestion.DIFFICULTY_NORMAL
    elif i in range(45, 60):
        _question.difficulty = TestQuestion.DIFFICULTY_HIGH
    # topic
    if i in range(0, 5):
        _question.topic_id = 5164
    elif i in range(5, 10):
        _question.topic_id = 5165
    elif i in range(10, 15):
        _question.topic_id = 5166
    elif i in range(15, 20):
        _question.topic_id = 5167
    elif i in range(20, 24):
        _question.topic_id = 5163
    elif i in range(24, 29):
        _question.topic_id = 5156
    elif i in range(29, 34):
        _question.topic_id = 5168
    elif i in range(34, 39):
        _question.topic_id = 5169
    elif i in range(39, 44):
        _question.topic_id = 5170
    elif i in range(44, 48):
        _question.topic_id = 5171
    elif i in range(48, 52):
        _question.topic_id = 5172
    elif i in range(52, 56):
        _question.topic_id = 5173
    elif i in range(56, 58):
        _question.topic_id = 5174
    elif i in range(58, 60):
        _question.topic_id = 5175
    # answer
    _question.meta_data["correct_id"] = _question.meta_data["choices"][0]["id"]
    _question.save()
    # paragraphs
    _paragraph = _question.paragraphs.first()
    _paragraph.meta_data["right"]["text"] = words(randint(3, 6), False)
    _paragraph.meta_data["left"]["text"] = words(randint(3, 6), False)
    _paragraph.save()


# NIS Kazakh language
_test = TestForm(data={
    "section": 9541,
    "language": _test_lang,
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


# NIS Russian language
_test = TestForm(data={
    "section": 9542,
    "language": _test_lang,
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


# NIS English language
_test = TestForm(data={
    "section": 9543,
    "language": "xx",
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

# NIS Natural Science TODO
# No need for taxonomy. 24.01.2022
# No need to explicitely limit topics. 24.01.2022
_test = TestForm(data={
    "section": 9539,
    "language": _test_lang,
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
    # if i in range(0, 13):
    #     _question.taxonomy_id = 3531
    # elif i in range(13, 18):
    #     _question.taxonomy_id = 3532
    # elif i in range(18, 20):
    #     _question.taxonomy_id = 3533
    # # topic
    # if i in range(0, 5):
    #     _question.topic_id = 5339
    # elif i in range(5, 10):
    #     _question.topic_id = 5340
    # elif i in range(10, 15):
    #     _question.topic_id = 5341
    # elif i in range(15, 20):
    #     _question.topic_id = 5342
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
