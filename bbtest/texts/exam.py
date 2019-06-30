from bbtest.models import Test


def inject_texts_into_response(response, test):
    response["texts"] = {
        "shared_paragraph_header": None,
        "column_a": None,
        "column_b": None,
    }
    if test.language == Test.LANGUAGE_KK:
        response["texts"]["shared_paragraph_header"] = "Мәтін"
        response["texts"]["column_a"] = "A қатары"
        response["texts"]["column_b"] = "B қатары"
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
