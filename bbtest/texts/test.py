from bbtest.models import Test


def nis_quantitative_answer(test, answer_type):
    if test.language == Test.LANGUAGE_KK:
        if answer_type == "a":
            return "А қатардағы мән үлкен."
        elif answer_type == "b":
            return "В қатардағы мән үлкен."
        elif answer_type == "=":
            return "Екі мән өзара тең."
        elif answer_type == "?":
            return "Ақпарат жеткіліксіз."
    elif test.language == Test.LANGUAGE_RU:
        if answer_type == "a":
            return "Значение А больше."
        elif answer_type == "b":
            return "Значение В больше."
        elif answer_type == "=":
            return "Оба значения равны."
        elif answer_type == "?":
            return "Не достаточно информации."
    raise AttributeError("Cannot find correct answer")
