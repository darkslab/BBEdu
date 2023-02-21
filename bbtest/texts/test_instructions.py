from django.utils.translation import gettext as _
from bbtest.models import Test


NIS_LANGUAGES_TEST_INSTRUCTION_TEXTS = {
    Test.LANGUAGE_KK: [
        [
            "Бұл пән бойынша 10 мәтінге 20 сұрақ берілген.",
            "Сұрақтарға жауап беру уақыты 40 минут.",
            "Жауаптарды мұқиат тексеріңіз.",
        ],
    ],
    Test.LANGUAGE_RU: [
        [
            "Данный предмет содержит 10 текстов и 20 вопросов к ним.",
            "Для ответа на все вопросы выделено 40 минут.",
            "Не забудьте перепроверить свои ответы.",
        ],
    ],
    Test.LANGUAGE_XX: [
        [
            "This subject contains 10 texts and 20 questions.",
            "To answer all questions you will have 40 minutes.",
            "Do not forget to double-check your answers.",
        ],
    ],
}
NIS_TEST_INSTRUCTION_TEXTS = {
    9540: {
        Test.LANGUAGE_KK: [
            [
                "Бұл пән бойынша 40 сұрақ берілген.",
                "Сұрақтарға жауап беру уақыты 60 минут.",
                "Жауаптарды мұқиат тексеріңіз.",
            ],
        ],
        Test.LANGUAGE_RU: [
            [
                "Данный предмет содержит 40 вопросов.",
                "Для ответа на все вопросы выделено 60 минут.",
                "Не забудьте перепроверить свои ответы.",
            ],
        ],
    },
    9541: {
        Test.LANGUAGE_KK: NIS_LANGUAGES_TEST_INSTRUCTION_TEXTS[Test.LANGUAGE_KK],
        Test.LANGUAGE_RU: NIS_LANGUAGES_TEST_INSTRUCTION_TEXTS[Test.LANGUAGE_KK],
    },
    9542: {
        Test.LANGUAGE_KK: NIS_LANGUAGES_TEST_INSTRUCTION_TEXTS[Test.LANGUAGE_RU],
        Test.LANGUAGE_RU: NIS_LANGUAGES_TEST_INSTRUCTION_TEXTS[Test.LANGUAGE_RU],
    },
    9543: {
        Test.LANGUAGE_XX: NIS_LANGUAGES_TEST_INSTRUCTION_TEXTS[Test.LANGUAGE_XX],
    },
    9544: {
        Test.LANGUAGE_KK: [
            [
                "Бұл пән бойынша әрбір сұрақ екі бөліктен тұрады. А қатарында тапсырманың бірінші бөлігі орналасқан, ал В қатарында тапсырманың екінші бөлігі орналасқан.",
            ],
            [
                "Сіз бірінші қатардағы тапсырманың мәні екінші қатардағы мәнге қарағанда үлкен немесе тең екенін, не болмаса берілген тапсырмаға жауап беру үшін ақпарат жеткіліксіз екенін көрсетуіңіз қажет:",
            ],
            [
                "Егер А қатарындағы мән үлкен болса, онда А жауабын;",
                "Егер В қатарындағы мән үлкен болса, онда В жауабын;",
                "Егер екі мән өзара тең болса, онда С жауабын;",
                "Егер тапсырмаға жауап беру үшін ақпарат жеткіліксіз болса, онда D жауабын таңдаңыз.",
            ],
            [
                "Бұл пән бойынша 60 сұрақ берілген.",
                "Сұрақтарға жауап беру уақыты 30 минут.",
                "Жауаптарды мұқиат тексеріңіз.",
            ],
        ],
        Test.LANGUAGE_RU: [
            [
                "В данном разделе каждый вопрос состоит из двух частей. Первая часть расположена в колонке А. Вторая часть расположена в колонке В.",
            ],
            [
                "Вам необходимо определить, в какой колонке значение больше, равны ли значения в обеих колонках или недостаточно информации. Выберите ответ:",
            ],
            [
                "А, если значение в колонке А больше;",
                "В, если значение в колонке В больше;",
                "С, если оба значения равны между собой;",
                "D, если недостаточно информации.",
            ],
            [
                "Данный предмет содержит 60 вопросов.",
                "Для ответа на все вопросы выделено 30 минут.",
                "Не забудьте перепроверить свои ответы.",
            ],
        ],
    },
    9539: {
        Test.LANGUAGE_KK: [
            [
                "Бұл пән бойынша 20 сұрақ берілген.",
                "Сұрақтарға жауап беру уақыты 30 минут.",
                "Жауаптарды мұқиат тексеріңіз.",
            ],
        ],
        Test.LANGUAGE_RU: [
            [
                "Данный предмет содержит 20 вопросов.",
                "Для ответа на все вопросы выделено 30 минут.",
                "Не забудьте перепроверить свои ответы.",
            ],
        ],
    },
}

UNT_COMPULSORY_TEST_INSTRUCTION_TEXTS = [
    [
        "Данный предмет содержит 20 вопросов.",
        "Для ответа на все вопросы выделено 40 минут.",
        "Не забудьте перепроверить свои ответы.",
    ],
]
UNT_PROFILE_TEST_INSTRUCTION_TEXTS = [
    [
        "Данный предмет содержит 20 вопросов с выбором одного правильного ответа и 10 вопросов с выбором одного или нескольких правильных ответов.",
        "Для ответа на все вопросы выделено 60 минут.",
        "Не забудьте перепроверить свои ответы.",
    ],
]
UNT_TEST_INSTRUCTION_TEXTS = {
    9547: UNT_COMPULSORY_TEST_INSTRUCTION_TEXTS,
    9546: UNT_COMPULSORY_TEST_INSTRUCTION_TEXTS,
    9545: UNT_COMPULSORY_TEST_INSTRUCTION_TEXTS,

    9548: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9549: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9550: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9551: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9552: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9553: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9554: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9555: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9556: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9557: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9558: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
    9559: UNT_PROFILE_TEST_INSTRUCTION_TEXTS,
}

def test_instructions(test):
    if test.section.is_nis():
        return NIS_TEST_INSTRUCTION_TEXTS[test.section.pk][test.language]
    elif test.section.is_unt_compulsory() or test.section.is_unt_profile():
        return UNT_TEST_INSTRUCTION_TEXTS[test.section.pk]
    elif test.section.is_nufypet():
        return [
            [
                "This is an unofficial NUFYPET Simulation.",
                "Total time given for the test: 60 min.",
            ],
            [
                "Choose the choice you find correct one in multichoice questions.",
                "Dictionaries and Calculators MUST NOT be used.",
                "Figures are NOT accurately drawn and NOT to scale, except if it is mentioned otherwise in a question.",
                "There is only one correct choice in each question, answers with two or more selected choices are counted as an incorrect answer.",
                "The total score of the test is 30 points (Each question has a score of 1 point).",
                "There is NO penalty for wrong answers.",
            ],
            [
                "Read each question carefully.",
                "Keep track of the timer (2 minutes for each question in average)",
                "Don't stay in one task for long.",
                "Try to answer for all questions.",
                "Recheck your answers if possible.",
            ],
            [
                "If you think something is wrong with the test, please contact us.",
            ],
        ]
    elif test.section.is_law():
        return [
            [
                "Данный предмет содержит 60 вопросов.",
                "Для ответа на все вопросы выделено 60 минут.",
                "Не забудьте перепроверить свои ответы.",
            ],
        ]
    elif test.section.is_proftest():
        return [
            [
                "TODO Данный предмет содержит 60 вопросов.",
                "Для ответа на все вопросы выделено 60 минут.",
                "Не забудьте перепроверить свои ответы.",
            ],
        ]
    return []


NIS_TEST_INSTRUCTION_TITLE_TEXTS = {
    9540: {
        Test.LANGUAGE_KK: "Математика",
        Test.LANGUAGE_RU: "Математика",
    },
    9541: {
        Test.LANGUAGE_KK: "Қазақ тілі",
        Test.LANGUAGE_RU: "Қазақ тілі",
    },
    9542: {
        Test.LANGUAGE_KK: "Русский язык",
        Test.LANGUAGE_RU: "Русский язык",
    },
    9543: {
        Test.LANGUAGE_XX: "English language",
    },
    9544: {
        Test.LANGUAGE_KK: "Сандық сипаттамалар",
        Test.LANGUAGE_RU: "Количественные характеристики",
    },
    9539: {
        Test.LANGUAGE_KK: "Жаратылыстану",
        Test.LANGUAGE_RU: "Естествознание",
    },
}

def test_instructions_title(test):
    if test.section.is_nis():
        return [
            NIS_TEST_INSTRUCTION_TITLE_TEXTS[test.section.pk][test.language],
            test.code.upper(),
        ]
    elif test.section.is_unt_compulsory() or test.section.is_unt_profile():
        return [
            _(test.section.name),
            test.code.upper(),
        ]
    elif test.section.is_nufypet():
        return [
            _(test.section.name),
            test.code.upper(),
        ]
    elif test.section.is_law():
        return [
            "",
            test.code.upper(),
        ]
    elif test.section.is_proftest():
        return [
            _(test.section.name),
            test.code.upper(),
        ]
    return []


NIS_TEST_VIDEO_LINKS = {
    9539: {
        Test.LANGUAGE_KK: "",  ## TODO: Provide relevant link
        Test.LANGUAGE_RU: "",
    },
    9540: {
        Test.LANGUAGE_KK: "https://www.youtube.com/embed/QakiQUwFyqo",
        Test.LANGUAGE_RU: "https://www.youtube.com/embed/a6wdikhANVI",
    },
    9541: {
        Test.LANGUAGE_KK: "https://www.youtube.com/embed/vgw8KAiCapY",
        Test.LANGUAGE_RU: "https://www.youtube.com/embed/JSpK3Mtmio0",
    },
    9542: {
        Test.LANGUAGE_KK: "https://www.youtube.com/embed/7ZPcaY5tlSc",
        Test.LANGUAGE_RU: "https://www.youtube.com/embed/gVw0dgXxFic",
    },
    9543: {
        Test.LANGUAGE_XX: "https://www.youtube.com/embed/8Dsjsbwp5Tc",
    },
    9544: {
        Test.LANGUAGE_KK: "https://www.youtube.com/embed/iUtaOOySSqM",
        Test.LANGUAGE_RU: "https://www.youtube.com/embed/Bj31L0mADvw",
    },
}

def test_video(test):
    if not test.section.is_nis():
        return None
    return NIS_TEST_VIDEO_LINKS[test.section.pk][test.language]
