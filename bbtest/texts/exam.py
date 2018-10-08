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

def inject_texts_into_response(response, test):
    response["texts"] = {
        "shared_paragraph_header": None,
        "column_a": None,
        "column_b": None,
    }
    if test.language == Test.LANGUAGE_KK:
        response["texts"]["shared_paragraph_header"] = "Мәтін"
        response["texts"]["column_a"] = "Қатар A"
        response["texts"]["column_b"] = "Қатар B"
    elif test.language == Test.LANGUAGE_RU:
        response["texts"]["shared_paragraph_header"] = "Текст"
        response["texts"]["column_a"] = "Колонка A"
        response["texts"]["column_b"] = "Колонка B"
    elif test.language == Test.LANGUAGE_XX:
        response["texts"]["shared_paragraph_header"] = "Text"
        response["texts"]["column_a"] = "Column A"
        response["texts"]["column_b"] = "Column B"
    else:
        raise AttributeError("Cannot inject texts into response")
    return response
