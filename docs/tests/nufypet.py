from django.contrib.auth import get_user_model
from django.utils.lorem_ipsum import paragraph, words
from random import randint, choice
from bbtest.models import TestQuestion
from bbtest.forms.test import TestForm


_developer = get_user_model().objects.get(pk=3085)
_test_lang = "xx"


# NUFYPET Mathematics
_test = TestForm(data={
    "section": 9560,
    "language": _test_lang,
}).create_test_suite(_developer)
for i, _question in enumerate(_test.questions.all()):
    # difficulty
    _question.difficulty = choice((
        TestQuestion.DIFFICULTY_LOW,
        TestQuestion.DIFFICULTY_NORMAL,
        TestQuestion.DIFFICULTY_HIGH,
    ))
    # topic
    _question.topic_id = randint(5286, 5289)
    # answer
    _question.meta_data["correct_id"] = _question.meta_data["choices"][0]["id"]
    for _choice in _question.meta_data["choices"]:
        _choice["meta_data"]["text"] = words(randint(3, 6), False)
    _question.save()
    # paragraphs
    _paragraph = _question.paragraphs.first()
    _paragraph.meta_data["text"] = paragraph()
    _paragraph.save()


# NUFYPET Physics
_test = TestForm(data={
    "section": 9561,
    "language": _test_lang,
}).create_test_suite(_developer)
for i, _question in enumerate(_test.questions.all()):
    # difficulty
    _question.difficulty = choice((
        TestQuestion.DIFFICULTY_LOW,
        TestQuestion.DIFFICULTY_NORMAL,
        TestQuestion.DIFFICULTY_HIGH,
    ))
    # topic
    _question.topic_id = randint(5290, 5295)
    # answer
    _question.meta_data["correct_id"] = _question.meta_data["choices"][0]["id"]
    for _choice in _question.meta_data["choices"]:
        _choice["meta_data"]["text"] = words(randint(3, 6), False)
    _question.save()
    # paragraphs
    _paragraph = _question.paragraphs.first()
    _paragraph.meta_data["text"] = paragraph()
    _paragraph.save()


# NUFYPET Biology/Chemistry
_test = TestForm(data={
    "section": 9562,
    "language": _test_lang,
}).create_test_suite(_developer)
for i, _question in enumerate(_test.questions.all()):
    # difficulty
    _question.difficulty = choice((
        TestQuestion.DIFFICULTY_LOW,
        TestQuestion.DIFFICULTY_NORMAL,
        TestQuestion.DIFFICULTY_HIGH,
    ))
    # topic
    _question.topic_id = randint(5296, 5318)
    # answer
    _question.meta_data["correct_id"] = _question.meta_data["choices"][0]["id"]
    for _choice in _question.meta_data["choices"]:
        _choice["meta_data"]["text"] = words(randint(3, 6), False)
    _question.save()
    # paragraphs
    _paragraph = _question.paragraphs.first()
    _paragraph.meta_data["text"] = paragraph()
    _paragraph.save()


# NUFYPET Thinking skills
_test = TestForm(data={
    "section": 9563,
    "language": _test_lang,
}).create_test_suite(_developer)
for i, _question in enumerate(_test.questions.all()):
    # difficulty
    _question.difficulty = choice((
        TestQuestion.DIFFICULTY_LOW,
        TestQuestion.DIFFICULTY_NORMAL,
        TestQuestion.DIFFICULTY_HIGH,
    ))
    # topic
    _question.topic_id = randint(5319, 5320)
    # answer
    _question.meta_data["correct_id"] = _question.meta_data["choices"][0]["id"]
    for _choice in _question.meta_data["choices"]:
        _choice["meta_data"]["text"] = words(randint(3, 6), False)
    _question.save()
    # paragraphs
    _paragraph = _question.paragraphs.first()
    _paragraph.meta_data["text"] = paragraph()
    _paragraph.save()
