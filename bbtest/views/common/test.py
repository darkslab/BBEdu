from django.db.models import Prefetch
from django.core.cache import cache
from random import randint
from bbtest.models import TestQuestion, TestParagraph, Quiz
from bbtest.models.upload import expiring_url


def inject_questions_and_report_into_started_response(response, test, hide_answers=True):
    response["questions"] = []
    response["report"] = {
        "answers": [],
        "observation": {},
    }

    paragraphs_map = {}
    paragraphs_questions = {}
    for question in test.questions.prefetch_related(
        Prefetch("paragraphs", queryset=TestParagraph.objects.order_by("through").all()),
    ).all():
        _answer = {
            "answer": None,
            "observation": {},
        }

        answer_meta_data = question.meta_data
        if question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_ONE:
            if answer_meta_data["correct_id"] is not None:
                _answer["answer"] = {
                    "correct_id": answer_meta_data["correct_id"],
                }
                if hide_answers:
                    answer_meta_data["correct_id"] = None
        elif question.answer_class == TestQuestion.ANSWER_CLASS_MULTICHOICE_MULTI:
            if len(answer_meta_data["correct_ids"]):
                _answer["answer"] = {
                    "correct_ids": answer_meta_data["correct_ids"],
                }
                if hide_answers:
                    answer_meta_data["correct_ids"] = []

        _question = {
            "paragraphs": [],
            "answer_class": question.answer_class,
            "meta_data": answer_meta_data,
        }

        for paragraph in question.paragraphs.all():
            if paragraph.paragraph_class == TestParagraph.PARAGRAPH_CLASS_IMAGE:
                paragraph.meta_data["asset_url"] = expiring_url(paragraph.meta_data["asset_object_name"], expire_in=test.section.duration)

            _paragraph = {
                "paragraph_class": paragraph.paragraph_class,
                "meta_data": paragraph.meta_data,
                "is_shared": False,
            }
            _question["paragraphs"].append(_paragraph)

            if paragraph.pk not in paragraphs_map:
                paragraphs_map[paragraph.pk] = []
            paragraphs_map[paragraph.pk].append(_paragraph)

            if paragraph.pk not in paragraphs_questions:
                paragraphs_questions[paragraph.pk] = set()
            paragraphs_questions[paragraph.pk].add(question.pk)

        response["questions"].append(_question)
        response["report"]["answers"].append(_answer)

    for paragraph_pk, questions_pk_set in paragraphs_questions.items():
        if len(questions_pk_set) > 1:
            for _paragraph in paragraphs_map[paragraph_pk]:
                _paragraph["is_shared"] = True


def results_progress(test_section, user):
    key = "test-progress-%s-%s" % (user.pk, test_section.pk)
    progress = cache.get(key)
    if progress is not None:
        return progress
    limit = 10
    progress = []
    for quiz in Quiz.objects.filter(
        quiz_set__student=user,
        test__section=test_section,
        is_finished=True,
    ).select_related("test__section").prefetch_related("test__questions").order_by("-pk")[:limit].all():
        progress.append(quiz.score())
    progress.reverse()
    for i in range(limit - len(progress)):
        progress.append(0)
    cache.set(key, progress, None)
    return progress


def average_score(test_section):
    key = "test-average-score-%s" % test_section.pk
    score = cache.get(key)
    if score is not None:
        return score
    score = 0
    scores_count = 0
    for quiz in Quiz.objects.filter(
        test__section=test_section,
        is_finished=True,
    ).exclude(
        report=None,
    ).select_related("test__section").prefetch_related("test__questions").all():
        if quiz.test.is_free:
            continue
        score += quiz.score()
        scores_count += 1
    # DARK_TODO  As of right now, we are mixing an actual average score with an artificial one. But one
    #            day we should get rid of it. Remove the condition below when ready.
    if True and scores_count > 0:
        first_test = test_section.tests.first()
        if first_test:
            score += round(first_test.max_score() * ((70 + randint(0, 10)) / 100))
            scores_count += 1
    if scores_count > 0:
        score = round(score / scores_count)
    cache.set(key, score, None)
    return score
