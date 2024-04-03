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
            "This subject contains 20 questions.",
            "To answer all questions you will have 30 minutes.",
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
    9566: {
        Test.LANGUAGE_KK: [
            [
                "Бұл пән бойынша 5 сұрақ берілген.",
                "Сұрақтарға жауап беру уақыты 20 минут.",
                "Жауаптарды мұқиат тексеріңіз.",
            ],
        ],
        Test.LANGUAGE_RU: [
            [
                "Данный предмет содержит 5 вопросов.",
                "Для ответа на все вопросы выделено 20 минут.",
                "Не забудьте перепроверить свои ответы.",
            ],
        ],
    },
    9567: {
        Test.LANGUAGE_KK: [
            [
                "Бұл пән бойынша 20 сұрақ берілген.",
                "Сұрақтарға жауап беру уақыты 10 минут.",
                "Жауаптарды мұқиат тексеріңіз.",
            ],
        ],
        Test.LANGUAGE_RU: [
            [
                "Данный предмет содержит 20 вопросов.",
                "Для ответа на все вопросы выделено 10 минут.",
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
Test
def test_instructions(test):
    if test.language == Test.LANGUAGE_RU:
        return  [
            [
                "Данный предмет содержит {} вопросов.".format(test.question_count),
                "Для ответа на все вопросы выделено {} минут.".format(test.duration // 60),
                "Не забудьте перепроверить свои ответы.",
            ]
        ]
    else:
        return  [
            [
                "Бұл пән {} сұрақтан тұрады.".format(test.question_count),
                "Барлық сұрақтарға жауап беруге {} минут беріледі.".format(test.duration // 60),
                "Жауаптарыңызды екі рет тексеруді ұмытпаңыз.",
            ]
        ]
 

    return NIS_TEST_INSTRUCTION_TEXTS[9540][test.language]

    if test.section.is_nis():
        return NIS_TEST_INSTRUCTION_TEXTS[test.section.pk][test.language]
    # elif test.section.is_unt_compulsory() or test.section.is_unt_profile():
    #     return UNT_TEST_INSTRUCTION_TEXTS[test.section.pk]
    # elif test.section.is_nufypet():
    #     return [
    #         [
    #             "This is an unofficial NUFYPET Simulation.",
    #             "Total time given for the test: 60 min.",
    #         ],
    #         [
    #             "Choose the choice you find correct one in multichoice questions.",
    #             "Dictionaries and Calculators MUST NOT be used.",
    #             "Figures are NOT accurately drawn and NOT to scale, except if it is mentioned otherwise in a question.",
    #             "There is only one correct choice in each question, answers with two or more selected choices are counted as an incorrect answer.",
    #             "The total score of the test is 30 points (Each question has a score of 1 point).",
    #             "There is NO penalty for wrong answers.",
    #         ],
    #         [
    #             "Read each question carefully.",
    #             "Keep track of the timer (2 minutes for each question in average)",
    #             "Don't stay in one task for long.",
    #             "Try to answer for all questions.",
    #             "Recheck your answers if possible.",
    #         ],
    #         [
    #             "If you think something is wrong with the test, please contact us.",
    #         ],
    #     ]
    # elif test.section.is_law():
    #     return [
    #         [
    #             "Данный предмет содержит 60 вопросов.",
    #             "Для ответа на все вопросы выделено 60 минут.",
    #             "Не забудьте перепроверить свои ответы.",
    #         ],
    #     ]
    return []


# 9541	Math_4	60	0	2	7911
# 9542	Kazakh_4	60	10	3	7911
# 9543	Russian_4	60	10	4	7911
# 9544	Natural_Science_4	60	20	5	7911
# 9545	Math_9	60	20	6	7911
# 9546	Biology_9	60	7	7	7911
# 9547	Geography_9	60	7	8	7911
# 9548	Kazakh_9	60	15	9	7911
# 9549	Russian_9	60	15	10	7911
# 9550	Physics_9	60	8	11	7911
# 9551	Chemistry_9	60	8	12	7911


PSEUDO_NIS_TEST_INSTRUCTION_TITLE_TEXTS = {
    9540: {
        Test.LANGUAGE_KK: "Generic",
        Test.LANGUAGE_RU: "Generic",
    },
    9541: {
        Test.LANGUAGE_KK: "Математика 4 Класс",
        Test.LANGUAGE_RU: "Математика 4 Класс",
    },
    9542: {
        Test.LANGUAGE_KK: "Казахский язык 4 Класс",
        Test.LANGUAGE_RU: "Казахский язык 4 Класс",
    },
    9543: {
        Test.LANGUAGE_KK: "Русский язык 4 Класс",
        Test.LANGUAGE_RU: "Русский язык 4 Класс",
    },
    9544: {
        Test.LANGUAGE_KK: "Естествознание 4 Класс",
        Test.LANGUAGE_RU: "Естествознание 4 Класс",
    },
    9545: {
        Test.LANGUAGE_KK: "Математика 9 Класс",
        Test.LANGUAGE_RU: "Математика 9 Класс",
    },
    9546: {
        Test.LANGUAGE_KK: "Биология 9 Класс",
        Test.LANGUAGE_RU: "Биология 9 Класс",
    },
    9547: {
        Test.LANGUAGE_KK: "География 9 Класс",
        Test.LANGUAGE_RU: "География 9 Класс",
    },
    9548: {
        Test.LANGUAGE_KK: "Казахский язык 9 Класс",
        Test.LANGUAGE_RU: "Казахский язык 9 Класс",
    },
    9549: {
        Test.LANGUAGE_KK: "Русский язык 9 Класс",
        Test.LANGUAGE_RU: "Русский язык 9 Класс",
    },
    9550: {
        Test.LANGUAGE_KK: "Физика 9 Класс",
        Test.LANGUAGE_RU: "Физика 9 Класс",
    },
    9551: {
        Test.LANGUAGE_KK: "Химия 9 Класс",
        Test.LANGUAGE_RU: "Химия 9 Класс",
    },
}

def test_instructions_title(test):
    return [
            _(test.section.name), #PSEUDO_NIS_TEST_INSTRUCTION_TITLE_TEXTS[9540][test.language],
            test.code.upper(),
        ]
    # if test.section.is_nis():
    #     return [
    #         PSEUDO_NIS_TEST_INSTRUCTION_TITLE_TEXTS[test.section.pk][test.language],
    #         test.code.upper(),
    #     ]
    # return []


NIS_TEST_VIDEO_LINKS = {
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
