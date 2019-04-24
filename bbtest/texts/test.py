from django.conf import settings
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


SPECIFICATION_KK_TEST_TEXTS = {
    9540: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для учащихся 6 классов общеобразовательных школ – претендентов в Интеллектуальные школы, по предмету <strong>«Математика»</strong> на русском и казахском языках с выбором одного правильного ответа из 4 предложенных вариантов.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском и казахском языках.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебным программам по предмету «Математика» для 5-6 классов уровня основного среднего образования, разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан (НЕ обновленного содержания <a target="_blank" href="http://nao.kz/loader/load/262">http://nao.kz/loader/load/262</a>).</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все математические формулы должны быть созданы специализированными редакторами (Microsoft Equation и т.п.);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все графики и рисунки должны быть созданы специализированными редакторами (GeoGebra и т.п.) и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов использовать буквы латинского алфавита, записанные курсивом.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по внесению тестовых вопросов на Веб-сайт:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Указывается ФИО Разработчика;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Указывается общий раздел контекста каждого тестового вопроса (отношения и пропорции, рациональные числа, модуль числа, линейные уравнения и неравенства и т.д.);</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.4.</span>Указывается тип когнитивного уровня тестовых вопросов по таксономии Блума (знание/применение).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 40 тестовых вопросов, из них:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="66%" class="text-center">Разделы</th>
                            <th width="34%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>1. Отношения и пропорции</td>
                            <td class="text-center">6</td>
                        </tr>
                        <tr>
                            <td>2. Рациональные числа</td>
                            <td class="text-center">4</td>
                        </tr>
                        <tr>
                            <td>3. Модуль числа</td>
                            <td class="text-center">6</td>
                        </tr>
                        <tr>
                            <td>4. Линейные уравнения и неравенства</td>
                            <td class="text-center">4</td>
                        </tr>
                        <tr>
                            <td>5. Преобразование выражений</td>
                            <td class="text-center">6</td>
                        </tr>
                        <tr>
                            <td>6. Делимость чисел</td>
                            <td class="text-center">6</td>
                        </tr>
                        <tr>
                            <td>7. Проценты</td>
                            <td class="text-center">4</td>
                        </tr>
                        <tr>
                            <td>8. Геометрический материал</td>
                            <td class="text-center">4</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td class="text-right"><strong>Итого:</strong></td>
                            <td class="text-center"><strong>40</strong></td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.3.</span>Один вариант должен содержать 40 тестовых вопросов с разделением на когнитивный уровень:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="50%" class="text-center">Когнитивный уровень</th>
                            <th width="25%" class="text-center">%</th>
                            <th width="25%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Знание</td>
                            <td class="text-center">60</td>
                            <td class="text-center">24</td>
                        </tr>
                        <tr>
                            <td>Применение</td>
                            <td class="text-center">40</td>
                            <td class="text-center">16</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.4.</span>Один вариант должен содержать 40 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="50%" class="text-center">Предполагаемый уровень сложности</th>
                            <th width="25%" class="text-center">%</th>
                            <th width="25%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">25</td>
                            <td class="text-center">10</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">50</td>
                            <td class="text-center">20</td>
                        </tr>
                        <tr>
                            <td>Сложный</td>
                            <td class="text-center">25</td>
                            <td class="text-center">10</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.</span>Образцы тестовых заданий по предмету <a target="_blank" href="http://nis.edu.kz/site/nis/repository/file/Selection%20test_SAMPLES/1%20%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D1%86%D1%8B%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_7%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81_KZ.pdf">«Математика на казахском языке»</a>.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">9.1.</span>Образцы тестовых заданий по предмету <a target="_blank" href="http://nis.edu.kz/site/nis/repository/file/Selection%20test_SAMPLES/1%20%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D1%86%D1%8B%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_7%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81_RU.pdf">«Математика на русском языке»</a>.</p>
        """,
    },
    9541: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для учащихся 6 классов общеобразовательных школ – претендентов в Интеллектуальные школы, по предмету <strong>«Казахский язык для учащихся на казахском языке»</strong> с выбором одного правильного ответа из 4 предложенных вариантов.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые задания должны соответствовать учебным программам по предмету «Казахский язык для учащихся на казахском языке» для 5-6 классов уровня основного среднего образования, разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития учащихся 6-х классов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Задачей тестовых вопросов должна являться оценка навыков понимания прочитанного текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тестовые вопросы должны быть поделены на три типа:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.1.</span>Тестовые вопросы на <strong>значение</strong> – слова, предложения, абзацы, основная идея текста, значение важных элементов текста;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.2.</span>Тестовые вопросы на <strong>структуру</strong> – ссылки, отношения между элементами (синтаксис), умение выделять части текста и определять связь между частями текста (структурой текста);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.3.</span>Тестовые вопросы на <strong>коммуникацию</strong> – умения делать выводы основываясь на мнение, цель, чувства и позицию автора текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.7.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.8.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: <u><strong>жоқ</strong></u>, <u><strong>емес</strong></u>);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по внесению тестовых вопросов на Веб-сайт:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Указывается ФИО Разработчика;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.2.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.3.</span>Указывается общий раздел контекста (человек, животные, природа и т.д.);</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.4.</span>Указывается тип тестовых вопросов по таксономии Блума (значение/коммуникация/структура).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.1.</span>К одному тексту может быть 1/3/5 тестовых вопросов.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.2.</span>Один вариант должен содержать 20 тестовых вопросов и 10 текстов:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="75%" class="text-center" colspan="3">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="25%" class="text-center">Значение</th>
                            <th width="25%" class="text-center">Коммуникация</th>
                            <th width="25%" class="text-center">Структура</th>
                        </tr>
                        <tr>
                            <td>Текст 1</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 3</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 4</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 5</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 6</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 7</td>
                            <td class="text-center">2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 8</td>
                            <td class="text-center">1</td>
                            <td class="text-center">2</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 9</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                        <tr>
                            <td>Текст 10</td>
                            <td class="text-center">3</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td class="text-right"><strong>Итого:</strong></td>
                            <td class="text-center" colspan="3"><strong>20</strong></td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.3.</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="50%" class="text-center">Предполагаемый уровень сложности</th>
                            <th width="25%" class="text-center">%</th>
                            <th width="25%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">50</td>
                            <td class="text-center">10</td>
                        </tr>
                        <tr>
                            <td>Сложный</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">10.</span>Образцы тестовых заданий по предмету <a target="_blank" href="http://nis.edu.kz/site/nis/repository/file/Selection%20test_SAMPLES/1%20%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D1%86%D1%8B%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_7%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81_KZ.pdf">«Казахский язык для учащихся на казахском языке»</a>.</p>
        """,
    },
    9542: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для учащихся 6 классов общеобразовательных школ – претендентов в Интеллектуальные школы, по предмету <strong>«Русский язык для учащихся на казахском языке»</strong> с выбором одного правильного ответа из 4 предложенных вариантов.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском или русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые задания должны соответствовать учебным программам по предмету «Русский язык для учащихся на казахском языке» для 5-6 классов уровня основного среднего образования, разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития учащихся 6-х классов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Задачей тестовых вопросов должна являться оценка навыков понимания прочитанного текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тестовые вопросы должны быть поделены на три типа:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.1.</span>Тестовые вопросы на <strong>значение</strong> – слова, предложения, абзацы, основная идея текста, значение важных элементов текста;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.2.</span>Тестовые вопросы на <strong>структуру</strong> – ссылки, отношения между элементами (синтаксис), умение выделять части текста и определять связь между частями текста (структурой текста);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.3.</span>Тестовые вопросы на <strong>коммуникацию</strong> – умения делать выводы основываясь на мнение, цель, чувства и позицию автора текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.7.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.8.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: <u><strong>не</strong></u>);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по внесению тестовых вопросов на Веб-сайт:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Указывается ФИО Разработчика;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.2.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.3.</span>Указывается общий раздел контекста (человек, животные, природа и т.д.);</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.4.</span>Указывается тип тестовых вопросов по таксономии Блума (значение/коммуникация/структура).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.1.</span>К одному тексту может быть 1/3/5 тестовых вопросов.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.2.</span>Один вариант должен содержать 20 тестовых вопросов и 10 текстов:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="75%" class="text-center" colspan="3">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="25%" class="text-center">Значение</th>
                            <th width="25%" class="text-center">Коммуникация</th>
                            <th width="25%" class="text-center">Структура</th>
                        </tr>
                        <tr>
                            <td>Текст 1</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 3</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 4</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 5</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 6</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 7</td>
                            <td class="text-center">2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 8</td>
                            <td class="text-center">1</td>
                            <td class="text-center">2</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 9</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                        <tr>
                            <td>Текст 10</td>
                            <td class="text-center">3</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td class="text-right"><strong>Итого:</strong></td>
                            <td class="text-center" colspan="3"><strong>20</strong></td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.3.</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="50%" class="text-center">Предполагаемый уровень сложности</th>
                            <th width="25%" class="text-center">%</th>
                            <th width="25%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">50</td>
                            <td class="text-center">10</td>
                        </tr>
                        <tr>
                            <td>Сложный</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">10.</span>Образцы тестовых заданий по предмету <a target="_blank" href="http://nis.edu.kz/site/nis/repository/file/Selection%20test_SAMPLES/1%20%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D1%86%D1%8B%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_7%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81_KZ.pdf">«Русский язык для учащихся на русском языке»</a>.</p>
        """,
    },
    9544: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы на определение способностей количественного мышления для учащихся 6 классов общеобразовательных школ – претендентов в Интеллектуальные школы, на русском и казахском языках в формате сравнения двух значений (переменных, выражений и т.д.) следующим образом:</p>
            <div class="row mt-10 mb-15">
                <div class="col-xs-6 pr-5 pl-5 text-center"><strong><em>Колонка A</em></strong></div>
                <div class="col-xs-6 pr-5 pl-5 text-center"><strong><em>Колонка B</em></strong></div>
                <div class="col-xs-12 pr-5 pl-5 text-center">Условие (дополнительно)</div>
                <div class="col-xs-6 pr-5 pl-5 text-center">Значение</div>
                <div class="col-xs-6 pr-5 pl-5 text-center">Значение</div>
            </div>
            <p class="text-justify text-normal mb-10">Одно из значений может быть больше чем другое, оба значения равны, либо невозможно решить сравнение из-за нехватки информации.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском и казахском языках.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны быть ориентированы на выявление способностей количественного мышления у тестируемого. Тестовые вопросы должны быть основаны на типовые учебные программы по предмету «Математика» для 5-6 классов уровня основного среднего образования и «Алгебра» для 7-9 классов уровня основного среднего образования, разработанных в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В заданиях должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.4.</span>Тестовые вопросы должны быть представлены в форме значения, в виде переменных, чисел, цифр, уравнений, выражений, обозначений, а также слов, использованных в вопросе.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все формулы должны быть созданы специализированными редакторами (Microsoft Equation и т.п.);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все графики и рисунки должны быть созданы специализированными редакторами (GeoGebra и т.п.) и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов использовать буквы латинского алфавита, записанные курсивом.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по внесению тестовых вопросов на Веб-сайт:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Указывается ФИО Разработчика;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового задания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.3.</span>Указывается общий раздел контекста (отношения и пропорции, рациональные числа, модуль числа, линейные уравнения и неравенства и т.д.);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 60 тестовых вопросов, из них:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="66%" class="text-center">Разделы</th>
                            <th width="34%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>1. Алгебраические операции и мышление</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>2. Числа и арифметические операции в десятичной системе счисления</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>3. Числа и арифметические операции с дробями</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>4. Единицы измерения и данные</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>5. Геометрический материал</td>
                            <td class="text-center">4</td>
                        </tr>
                        <tr>
                            <td>6. Отношение и пропорции</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>7. Система счисления</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>8. Выражения и уравнения</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>9. Функции</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>10. Моделирование</td>
                            <td class="text-center">4</td>
                        </tr>
                        <tr>
                            <td>11. Множества</td>
                            <td class="text-center">4</td>
                        </tr>
                        <tr>
                            <td>12. Правило последовательности</td>
                            <td class="text-center">4</td>
                        </tr>
                        <tr>
                            <td>13. Математическая статистика</td>
                            <td class="text-center">2</td>
                        </tr>
                        <tr>
                            <td>14. Комбинаторика</td>
                            <td class="text-center">2</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td class="text-right"><strong>Итого:</strong></td>
                            <td class="text-center"><strong>60</strong></td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.3.</span>Один вариант должен содержать 60 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="50%" class="text-center">Предполагаемый уровень сложности</th>
                            <th width="25%" class="text-center">%</th>
                            <th width="25%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">25</td>
                            <td class="text-center">15</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">50</td>
                            <td class="text-center">30</td>
                        </tr>
                        <tr>
                            <td>Сложный</td>
                            <td class="text-center">25</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.</span>Образцы тестовых заданий по предмету <a target="_blank" href="http://nis.edu.kz/site/nis/repository/file/Selection%20test_SAMPLES/2%20%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D1%86%D1%8B%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_7%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81_KZ.rar">«Количественные характеристики на казахском языке»</a>.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">9.1.</span>Образцы тестовых заданий по предмету <a target="_blank" href="http://nis.edu.kz/site/nis/repository/file/Selection%20test_SAMPLES/2%20%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D1%86%D1%8B%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_7%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81_RU.rar">«Количественные характеристики на русском языке»</a>.</p>
        """,
    },
    9545: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы на определение уровня подготовленности по предмету «История Казахстана» на казахском языке для поступающих в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Содержание тестовых вопросов должно соответствовать учебному материалу по предмету «История Казахстана» в соответствии с учебной программой для общеобразовательной школы.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.7.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.8.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.9.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.10.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Эпоха камня и бронзы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Палеолит, мезолит, неолит, энеолит. Эпоха бронзы.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Казахстан в эпоху железа</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Возникновение кочевого скотоводства. Основы жизнеобеспечения кочевого скотоводства. Культурные достижения ранних кочевников на территории Казахстана.</li>
                                    <li>Саки: сведения о саках, расселение, сакское общество, борьба саков за независимость.</li>
                                    <li>Уйсуны, кангюи: расселение, письменные источники, общественное устройство.</li>
                                    <li>Гунны: письменные источники, государственное устройство, объединение гуннов, перемещение на запад, Аттила и его походы.</li>
                                    <li>Сарматы: расселение, общественный строй.</li>
                                    <li>Саки, уйсуны, кангюи, гунны, сарматы: быт, хозяйство, культура, археологические памятники.</li>
                                    <li>Регионы Казахстана в период раннего железного века.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Государства раннего и развитого средневековья (VI-нач.XIII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Раннесредневековые государства на территории Казахстана: Тюркский, Западно-Тюрксий, Тюргешский, Карлукский каганаты, Огузы, Кимаки: социально-экономическое развитие и общественно-политическая история.</li>
                                    <li>Казахстан в период среднего средневековья: Караханиды, Найманы, Кереи, Жалаиры, Каракитаи, Кипчаки: социально-экономическое развитие и общественно-политическая история.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Культура (VI-XVII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Великий Шелковый путь на территории Казахстана. Культура VI-IX вв.</li>
                                    <li>Городская культура IX-XIII вв. Ремесло, торговля. Религия и культура. Развитие науки и образования.</li>
                                    <li>Развитие культуры Казахстана в XIV-XV вв.</li>
                                    <li>Развитие культуры Казахстана в XVI-XVII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Казахстан в XIII-XVII вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Монгольский период в истории Казахстана. Золотая Орда: образование, общественный строй, усиление, распад. Ак Орда, Моголистан, Ногайская Орда, ханство Абулхаира, Северный Казахстан и Западная Сибирь. Государство Тимура.</li>
                                    <li>Этнические процессы на территории Казахстана. Образование Казахского ханства. Внутренняя и внешняя политика. Укрепление Казахского ханства в XVI-XVII вв.: Касым хан, Хакназар хан, Тауекель хан, Есим хан, Тауке хан</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Социально-экономическое положение Казахстана в XIII-XVII вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Государственно-административное устройство государтсв XIII-XV вв. Система правления в Казахском ханстве.</li>
                                    <li>Экономическое положение Казахстана в XIV-XV вв.</li>
                                    <li>Экономическое положение Казахстана в XVI-XVII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">7</td>
                            <td>Социально-экономическое развитие Казахстана в XVIII-XIX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Торгово-экономические связи Казахстана с Китаем. Экономическое развитие Казахстана во второй половине XIX в. Переселение уйгуров и дунган в Семиречье.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">8</td>
                            <td>Общественно-политическое развитие Казахстана в XVIII-XIX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Борьба казахского народа против джунгарского нашествия. Присоединение Младшего жуза к России. Внутренняя и внешняя политика Абылай хана.</li>
                                    <li>Участие казахов в Крестьянской войне 1773-1775 гг. Восстание казахов Младшего жуза под руководством С.Датулы 1783-1797 гг. Ликвидация ханской власти. Восстание И.Тайманулы и М.Утемисулы 1836-1838 гг., Кенесары Касымулы 1837-1847 гг.</li>
                                    <li>Освободительная борьба казахских шаруа в 50-е годы XIX века. Присоединение Старшего жуза к России. Завершение колониального захвата Казахстана Россией и его последствия. Реформы 1860-1890-х гг. В Казахстане. Освободительная борьба казахского народа в 60-70 годы XIX века.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">9</td>
                            <td>Казахстан в первой половине XX в.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Социально-экономическое развитие Казахстана в начале XX века. Политика «военного коммунизма». Казахстан в годы НЭП. Индустриализация. Коллективизация сельского хозяйства. Наращивание экономической мощи Казахстана в годы ВОВ.</li>
                                    <li>Общественно-политическая жизнь Казахстана в первой половине XX века. Политическое развитие Казахстана в начале XX века. Национально-освободительные движения и их основные направления. Национально-освободительное движение 1916 г. Казахстан в период ФБДР 1917 г. Движение о создании партии Алаш. Октябрьская революция. Национальные автономиив Казахстане. Казахстан в годы Гражданской войны и иностранной военной интервенции. Образование КазАССР. Формирование территории Казахской АССР. Общественно-политическое положение Казахстана в 1920-1940-е гг. Казахстанцы в период ВОВ.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">10</td>
                            <td>Культура Казахстана XVIII-XX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Культура Казахстана в XVIII в.</li>
                                    <li>Культура Казахстана в первой половине XIX в.</li>
                                    <li>Культура Казахстана во второй половине XIX в.</li>
                                    <li>Культура Казахстана в начале XX в.</li>
                                    <li>Культура Казахстана в 1920-1940-е гг.</li>
                                    <li>Культура Казахстана во второй половине XX века (1946-1980 гг.)</li>
                                    <li>Культура Казахстана в конце XX – начале XXI вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">11</td>
                            <td>Казахстан в 50-80-е гг. XX века</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Общественно-политическая жизнь Казахстана в 50-80-е гг. XX века</li>
                                    <li>Социально-экономическое развитие в в 50-80-е гг. XX века</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">12</td>
                            <td>Независимый Казахстан</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Провозглашение и становление независимого Казахстана. Общественно-политическое развитие РК. Внешняя политика РК.</li>
                                    <li>Экономическое развитие РК.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">13</td>
                            <td>История в документах</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Письменные источники об исторических событиях</li>
                                </ul>
                            </td>
                        </tr>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.1.</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">10</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.2.</span>Один тестовый вопрос имеет 1 (один) правильный вариант ответа из 5 (пяти) предложенных.</p>
        """,
    },
    9546: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы на оценку способности к пониманию и осмыслению письменных текстов, к использованию их содержания для достижения собственных целей, развития знаний и возможностей, для активного участия в жизни общества на казахском языке для поступающих в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Содержание тестовых вопросов должно соответствовать содержанию вопросов, используемых в международных сравнительных исследованиях в области образования (PISA, TIMSS и т.п.).</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития поступающих в высшие учебные заведения Республики Казахстан;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.8.</span>Количество слов в текстах и вопросов к одному тексту в одном варианте теста должно составлять:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Текст #</th>
                            <th class="text-center">Количество слов</th>
                            <th class="text-center">Количество вопросов</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td class="text-center">60-100</td>
                            <td class="text-center">2</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td class="text-center">100-200</td>
                            <td class="text-center">4</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td class="text-center">200-350</td>
                            <td class="text-center">6</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td class="text-center">350-500</td>
                            <td class="text-center">8</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.9.</span>Тематика текстов:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th>#</th>
                            <th width="66%" class="text-center">Тема</th>
                            <th width="34%" class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Человек и его окружение</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Семья и ценности жизни.</li>
                                    <li>Друзья. Интересы и увлечения.</li>
                                    <li>Профессия. Работа.</li>
                                    <li>Спорт и здоровый образ жизни. Путешествия. Отдых.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Образование и наука</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Образование</li>
                                    <li>Биография. Деятели науки.</li>
                                    <li>Искусство.</li>
                                    <li>Технический прогресс.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Города и государства</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Географические особенности государств. Экономика.</li>
                                    <li>Столицы и города. Архитектура и строительство.</li>
                                    <li>Политика</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Социальные взаимоотношения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Средства массовой информации.</li>
                                    <li>Праздники, традиции и обычаи.</li>
                                    <li>История. Культурное наследие.</li>
                                    <li>Проблемы человечества.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Природа</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Объекты природы.</li>
                                    <li>Погода и климат.</li>
                                    <li>Животные, насекомые, птицы, растительный мир.</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов: </p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: <span style="text-decoration: underline;"><strong>жоқ, емес</strong></span>);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.9.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.10.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.11.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Тема</th>
                        </tr>
                        <tr>
                            <td>Человек и его окружение</td>
                        </tr>
                        <tr>
                            <td>Образование и наука</td>
                        </tr>
                        <tr>
                            <td>Города и государства</td>
                        </tr>
                        <tr>
                            <td>Социальные взаимоотношения</td>
                        </tr>
                        <tr>
                            <td>Природа</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">10</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.2.</span>Один тестовый вопрос имеет один правильный вариант ответа из пяти предложенных.</p>
        """,
    },
    9547: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы на оценку математического мышления и способности применения навыков знания, применения и интерпритации математики в жизненных ситуациях (в различных контекстах) на казахском языке для поступающих в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Содержание тестовых вопросов должно соответствовать содержанию вопросов, используемых в международных сравнительных исследованиях в области образования (PISA, TIMSS и т.п.).</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов: </p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1</span>Все математические формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2</span>Все графики и рисунки должны быть созданы специализированными редакторами (GeoGebra и т.п.) и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.6</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th>#</th>
                            <th width="66%" class="text-center">Раздел</th>
                            <th width="34%" class="text-center">Проверяемые знание и умение</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Количественные рассуждения</td>
                            <td>Умение:
                                <ul class="list-normal">
                                    <li>решать примеры на вычисление</li>
                                    <li>решать текстовые задачи</li>
                                    <li>вычислять задачи на проценты</li>
                                    <li>решать уравнения</li>
                                    <li>находить значения числовых и буквенных выражений</li>
                                    <li>определять числовые характеристики круговых и столбчатых диаграмм</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Неопределенность</td>
                            <td>Умение вычислять задачи на:
                                <ul class="list-normal">
                                    <li>теорию вероятности</li>
                                    <li>математическую статистику</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Изменение и зависимости</td>
                            <td>Умение решать задачи:
                                <ul class="list-normal">
                                    <li>на функциональную зависимость</li>
                                    <li>по графическим изображениям зависимости</li>
                                    <li>на зависимости, изображенные на диаграммах</li>
                                </ul>
                                Умение:
                                <ul class="list-normal">
                                    <li>вычислять задачи на изменение одной величины в зависимости от другой</li>
                                    <li>вычислять задачи на последовательности</li>
                                    <li>анализировать данные в таблице</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Пространство и форма</td>
                            <td>
                                Умение:
                                <ul class="list-normal">
                                    <li>решать текстовые задачи с геометрическим содержанием</li>
                                    <li>применять формулы площади, периметра геометрических фигур</li>
                                    <li>применять формулы объема и площади поверхности геометрических тел</li>
                                    <li>вычислять задачи на зависимости измерений геометрических фигур и тел</li>
                                    <li>решать нестандартные задачи с геометрическим содержанием</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7</span>Указывается тип когнитивного уровня тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Типы когнитивного уровня тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Применение</td>
                        </tr>
                        <tr>
                            <td>Анализ</td>
                        </tr>
                        <tr>
                            <td>Синтез</td>
                        </tr>
                        <tr>
                            <td>Смешанные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.1</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">10</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2</span>Один тестовый вопрос имеет один правильный вариант ответа из пяти предложенных.</p>
        """,
    },
    9548: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Математика» на казахском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Математика», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1</span>Все математические формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2</span>Все графики и рисунки должны быть созданы специализированными редакторами (GeoGebra и т.п.) и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Арифметические вычисления. Преобразования выражений.</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Уравнения. Системы уравнений. Составление уравнений.</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Неравенства. Системы неравенств.</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Функции. Производные. Интеграл.</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Планиметрия.</td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Стереометрия.</td>
                        </tr>
                        <tr>
                            <td class="text-center">7</td>
                            <td>Последовательности. Прогрессии.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9549: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Физика» на казахском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Физика», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все математические формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все графики и рисунки должны быть созданы специализированными редакторами (GeoGebra и т.п.) и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Механика</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Молекулярная физика. Основы термодинамики</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Электродинамика</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Оптика</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Квантовая и атомная физика</td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Качественные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Анализ</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Синтез</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9550: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Химия» на казахском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Химия», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все математические формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все химические формулы, графики и рисунки должны быть созданы специализированными редакторами и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Общая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Неорганическая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Органическая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Расчетные задачи: Общая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Расчетные задачи: Неорганическая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Расчетные задачи: Органическая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">7</td>
                            <td>Качественные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Анализ</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Синтез</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9551: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Биология» на казахском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Биология», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все графики и рисунки должны быть созданы специализированными редакторами и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Растения</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Животные</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Анатомия и физиология человека</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Цитология, генетика, экология</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Качественные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Анализ</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Синтез</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9552: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «География» на казахском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «География», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все графики и рисунки должны быть созданы специализированными редакторами и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Физическая география мира</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>География Казахстана</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Экономическая и социальная география мира</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Задачи по курсу география</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Качественные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9553: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы на определение уровня подготовленности по предмету «История» на казахском языке для поступающих в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Содержание тестовых вопросов должно соответствовать учебному материалу по предмету «История» в соответствии с учебной программой для общеобразовательной школы.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.7.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.8.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.9.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.10.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Эпоха камня и бронзы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Палеолит, мезолит, неолит, энеолит. Эпоха бронзы.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Казахстан в эпоху железа</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Возникновение кочевого скотоводства. Основы жизнеобеспечения кочевого скотоводства. Культурные достижения ранних кочевников на территории Казахстана.</li>
                                    <li>Саки: сведения о саках, расселение, сакское общество, борьба саков за независимость.</li>
                                    <li>Уйсуны, кангюи: расселение, письменные источники, общественное устройство.</li>
                                    <li>Гунны: письменные источники, государственное устройство, объединение гуннов, перемещение на запад, Аттила и его походы.</li>
                                    <li>Сарматы: расселение, общественный строй.</li>
                                    <li>Саки, уйсуны, кангюи, гунны, сарматы: быт, хозяйство, культура, археологические памятники.</li>
                                    <li>Регионы Казахстана в период раннего железного века.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Государства раннего и развитого средневековья (VI-нач.XIII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Раннесредневековые государства на территории Казахстана: Тюркский, Западно-Тюрксий, Тюргешский, Карлукский каганаты, Огузы, Кимаки: социально-экономическое развитие и общественно-политическая история.</li>
                                    <li>Казахстан в период среднего средневековья: Караханиды, Найманы, Кереи, Жалаиры, Каракитаи, Кипчаки: социально-экономическое развитие и общественно-политическая история.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Культура (VI-XVII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Великий Шелковый путь на территории Казахстана. Культура VI-IX вв.</li>
                                    <li>Городская культура IX-XIII вв. Ремесло, торговля. Религия и культура. Развитие науки и образования.</li>
                                    <li>Развитие культуры Казахстана в XIV-XV вв.</li>
                                    <li>Развитие культуры Казахстана в XVI-XVII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Казахстан в XIII-XVII вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Монгольский период в истории Казахстана. Золотая Орда: образование, общественный строй, усиление, распад. Ак Орда, Моголистан, Ногайская Орда, ханство Абулхаира, Северный Казахстан и Западная Сибирь. Государство Тимура.</li>
                                    <li>Этнические процессы на территории Казахстана. Образование Казахского ханства. Внутренняя и внешняя политика. Укрепление Казахского ханства в XVI-XVII вв.: Касым хан, Хакназар хан, Тауекель хан, Есим хан, Тауке хан</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Социально-экономическое положение Казахстана в XIII-XVII вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Государственно-административное устройство государтсв XIII-XV вв. Система правления в Казахском ханстве. </li>
                                    <li>Экономическое положение Казахстана в XIV-XV вв.</li>
                                    <li>Экономическое положение Казахстана в XVI-XVII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">7</td>
                            <td>Социально-экономическое развитие Казахстана в XVIII-XIX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Торгово-экономические связи Казахстана с Китаем. Экономическое развитие Казахстана во второй половине XIX в. Переселение уйгуров и дунган в Семиречье.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">8</td>
                            <td>Общественно-политическое развитие Казахстана в XVIII-XIX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Борьба казахского народа против джунгарского нашествия. Присоединение Младшего жуза к России. Внутренняя и внешняя политика Абылай хана.</li>
                                    <li>Участие казахов в Крестьянской войне 1773-1775 гг. Восстание казахов Младшего жуза под руководством С.Датулы 1783-1797 гг. Ликвидация ханской власти. Восстание И.Тайманулы и М.Утемисулы 1836-1838 гг., Кенесары Касымулы 1837-1847 гг.</li>
                                    <li>Освободительная борьба казахских шаруа в 50-е годы XIX века. Присоединение Старшего жуза к России. Завершение колониального захвата Казахстана Россией и его последствия. Реформы 1860-1890-х гг. В Казахстане. Освободительная борьба казахского народа в 60-70 годы XIX века.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">9</td>
                            <td>Казахстан в первой половине XX в.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Социально-экономическое развитие Казахстана в начале XX века. Политика «военного коммунизма». Казахстан в годы НЭП. Индустриализация. Коллективизация сельского хозяйства. Наращивание экономической мощи Казахстана в годы ВОВ.</li>
                                    <li>Общественно-политическая жизнь Казахстана в первой половине XX века. Политическое развитие Казахстана в начале XX века. Национально-освободительные движения и их основные направления. Национально-освободительное движение 1916 г. Казахстан в период ФБДР 1917 г. Движение о создании партии Алаш. Октябрьская революция. Национальные автономиив Казахстане. Казахстан в годы Гражданской войны и иностранной военной интервенции. Образование КазАССР. Формирование территории Казахской АССР. Общественно-политическое положение Казахстана в 1920-1940-е гг. Казахстанцы в период ВОВ.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">10</td>
                            <td>Культура Казахстана XVIII-XX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Культура Казахстана в XVIII в.</li>
                                    <li>Культура Казахстана в первой половине XIX в.</li>
                                    <li>Культура Казахстана во второй половине XIX в.</li>
                                    <li>Культура Казахстана в начале XX в.</li>
                                    <li>Культура Казахстана в 1920-1940-е гг.</li>
                                    <li>Культура Казахстана во второй половине XX века (1946-1980 гг.)</li>
                                    <li>Культура Казахстана в конце XX – начале XXI вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">11</td>
                            <td>Казахстан в 50-80-е гг. XX века</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Общественно-политическая жизнь Казахстана в 50-80-е гг. XX века</li>
                                    <li>Социально-экономическое развитие в в 50-80-е гг. XX века</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">12</td>
                            <td>Независимый Казахстан</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Провозглашение и становление независимого Казахстана. Общественно-политическое развитие РК. Внешняя политика РК.</li>
                                    <li>Экономическое развитие РК.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">13</td>
                            <td>История в документах</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Письменные источники об исторических событиях Казахстана</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">14</td>
                            <td>Государства Древнего Востока. Античная цивилизация</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Древние государства Месопотамия, Египет, государства Юго-Западной, Южной и Восточной Азии (социально-экономическое развитие и общественно-политическая история)</li>
                                    <li>Древняя Греция, Македония, Древний Рим в период Республики и период Империи (социально-экономическое развитие и общественно-политическая история)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">15</td>
                            <td>Средневековье (ранее V – X вв., расцвет XI-XV вв., позднее XV-XVII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Западная и Центральная Европа, Византийская империя и Ближний Восток, Центральная Азия, монголо-татары, Средняя Азия, славяне, Киевская Русь, страны Востока, Русь в XI-XIII вв., Россия в XV-XVII вв. (социально-экономическое развитие, общественно-политическая история)</li>
                                    <li>Христианская церковь в XI-XIII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">16</td>
                            <td>Культура древнего мира (до V века), средневековая культура мира (V-XVII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Древняя Греция, Древний Рим, Древний Восток</li>
                                    <li>Западная и Центральная Европа, Византийская империя и Ближний Восток, Центральная Азия, Средняя Азия, славяне, Киевская Русь, страны Востока, Русское государство в XI-XVII вв. Великие географические открытия. Возрождение</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">17</td>
                            <td>Европа и Северная Америка, Страны Азии и Африки (XVII-начало XX вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Англия, Северная Америка, Франция, Россия, Германия, Италия, Австрия, Индия. Османская империя, Китай, Монголия, Япония, Иран (общественно-политическая история и социально-экономическое развитие XVII-XVIII вв.)</li>
                                    <li>США, Англия, Россия, Франция, Германия, Италия, Австро-Венгрия, Китай, Япония, Индия, Османская империя, Иран, Арабские страны (общественно-политическая история и социально-экономическое развитие XIX-нач.XX вв.)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">18</td>
                            <td>Культура Европы, Северной Америки, стран Азии и Африки (XVIII в. – начало XXI в.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Эпоха Просвещения. Развитие науки и техники в XVII-XVIII вв. Культура XIX – первой половины XX вв.</li>
                                    <li>Культура второй половины XX – начала XII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">19</td>
                            <td>Международные отношения (XVII – начало XXI вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Колониальная система и международные отношения в XVII – XVIII вв.</li>
                                    <li>Международные отношения в XIX – начале XXI вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">20</td>
                            <td>Мировые войны и их последствия</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Первая мировая война (1914-1918 гг.), Версальско-Вашингтонская система</li>
                                    <li>Вторая мировая война (1939-1945 гг.). Великобритания, Франция, Германия, Италия, СССР, США, Япония, Китай, Монголия, Индия, Иран, Афганистан, Турция, Арабские страны, Азии и Африки в период второй мировой войны</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">21</td>
                            <td>Страны Европы и Америки, Азии и Африки (1918-2014 гг.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Страны Европы и Америки, Азии и Африки в период между двумя мировыми войнами (1918-1939 гг., Великобритания, Франция, Германия, Италия, Советская Россия, СССР, США, Япония, Китай, Монголия, Индия, Иран, Афганистан, Турция, Арабские страны Азии и Африки)</li>
                                    <li>Страны Западной Европы и Америки, страны Южной, Центральной, Восточной Европы, Страны Азии и Африки (1945-2014 гг., Великобритания, Франция, ФРГ, США, Италия, Страны Центральной и Юго-Восточной Европы, СССР, Российская Федерация, Япония, Китай, МНР, Индия, Пакистан, Иран, Афганистан, Турция, Арабские страны)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">22</td>
                            <td>История в документах</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Письменные источники об исторических событиях:</li>
                                    <li>Государства Древнего Востока. Античная цивилизация</li>
                                    <li>Средневековье (ранее V – X вв., расцвет XI-XV вв., позднее XV-XVII вв.)</li>
                                    <li>Культура древнего мира (до V века), средневековая культура мира (V-XVII вв.)</li>
                                    <li>Европа и Северная Америка, Страны Азии и Африки (XVII-начало XX вв.)</li>
                                    <li>Культура Европы, Северной Америки, стран Азии и Африки (XVIII в. – начало XXI в.)</li>
                                    <li>Международные отношения (XVII – начало XXI вв.)</li>
                                    <li>Мировые войны и их последствия</li>
                                    <li>Страны Европы и Америки, Азии и Африки (1918-2014 гг.)</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9557: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Казахский язык и литература» на казахском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Казахский язык и литература», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития поступающих в высшие учебные заведения Республики Казахстан;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.6.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: емес);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.9.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.10.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.11.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td colspan="4">
                                <ul class="list-normal">
                                    <li>Қазақ тілі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">1</td>
                            <td rowspan="2">Лексика</td>
                            <td>Сөз және сөздің мағыналары</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сөздің тура және ауыспалы мағынасы, көп мағыналы сөздер</li>
                                    <li>Омоним, антоним, синоним</li>
                                    <li>Тұрақты тіркес, мақал-мәтел</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сөздік қор</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Көнерген сөздер, неологизмдер</li>
                                    <li>Кірме сөздер, диалект сөздер</li>
                                    <li>Кәсіби сөздер мен терминдер</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="4" class="text-center">2</td>
                            <td rowspan="4">Фонетика</td>
                            <td>Дауысты дыбыстар</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Дауысты дыбыстардың түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Дауыссыз дыбыстар</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Дауыссыз дыбыстардың түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Буын және тасымал</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Буын түрлері, буынға бөліну ерекшеліктері, тасымал шарты</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Үндестік заңы. Орфография, орфоэпия</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Буын үндестігі, буын үндестігіне бағынбайтын қосымшалар. Дыбыс үндестігі, ықпал түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Сөзжасам</td>
                            <td>Сөздік құрам</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Түбір сөз, туынды сөз</li>
                                    <li>Күрделі сөз, түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="9" class="text-center">4</td>
                            <td rowspan="9">Морфология</td>
                            <td>Зат есім</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Зат есімнің мағыналық, құрамдық түрлері, қызметі</li>
                                    <li>Зат есімнің жалғаулары, көмекші есім</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сын есім</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сын есімнің жасалуы, түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сан есім</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сан есімнің түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Есімдік</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Есімдіктің түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Етістік</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Етістіктің құрамдық, мағыналық түрлері, қызметі</li>
                                    <li>Етістіктің шақтары, райлары</li>
                                    <li>Көсемше мен есімше, етіс</li>
                                    <li>Тұйық етістік, емлесі; Көмекші етістік</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Үстеу</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Үстеудің түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Еліктеу сөздер</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Еліктеу сөздердің түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Одағай</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Одағай түрлері, тыныс белгісі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Шылау</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Шылаудың түрлері, емлесі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="6" class="text-center">5</td>
                            <td rowspan="6">Синтаксис</td>
                            <td>Сөз тіркесі</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сөздердің байланысу тәсілдері мен түрлері</li>
                                    <li>Сөз тіркесі, есімді және етістікті сөз тіркесі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сөйлем мүшелері</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тұрлаулы мүшелер, қызметі</li>
                                    <li>Тұрлаусыз мүшелер, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Жай сөйлем</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Айтылу мақсатына қарай сөйлем түрлері</li>
                                    <li>Құрылысына, құрамына қарай сөйлем түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Құрмалас сөйлем</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Салалас құрмалас сөйлем, жасалуы, түрлері</li>
                                    <li>Сабақтас құрмалас сөйлем, жасалуы, түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Оқшау сөздер. Қаратпа сөз. Қыстырма сөз.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Қаратпа, қыстырма сөздер, тыныс белгілері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Төл сөз</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Төл сөз, автор сөзі, төлеу сөз, тыныс белгілері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">6</td>
                            <td rowspan="2">Пунктуация</td>
                            <td>Тыныс белгілері</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тыныс белгілердің қойылатын орындары, қабаттаса қойылатын тыныс белгілер</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Стилистика. Шешендік сөз</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Стиль түрлері. Шешендік сөз</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="4">
                                <ul class="list-normal">
                                    <li>Қазақ әдебиеті</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">1</td>
                            <td rowspan="2">Ежелгі дүние әдебиеті</td>
                            <td>Көне түркі дәуіріндегі әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Алып Ер Тоңа дастаны, Күлтегін жазуы, Қорқыт ата кітабы, Оғыз қаған жыры</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Ислам дәуіріндегі әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Әбунасыр Әл-Фараби, Ахмет Иүгінеки, Ахмет Яссауи</li>
                                    <li>Жүсіп Баласағұн, Махмұт Қашғари, Рабғузи, Сайф Сараи</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">2</td>
                            <td rowspan="2">Ауыз әдебиеті</td>
                            <td>Ауыз әдебиеті</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тұрмыс-салт жырлары</li>
                                    <li>Ертегілер</li>
                                    <li>Мақал-мәтел, жұмбақтар</li>
                                    <li>Аңыздар</li>
                                    <li>Шешендік сөздер</li>
                                    <li>Батырлар жыры. Алпамыс батыр, Қобыланды батыр, Қамбар батыр</li>
                                    <li>Лира-эпостық жырлар. Қозы Көрпеш – Баян сұлу, Қыз Жібек</li>
                                    <li>Айтыс, түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Жыраулар поэзиясы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Асан қайғы. Өмірі, шығармашылығы</li>
                                    <li>Қазтуған. Өмірі, шығармашылығы</li>
                                    <li>Доспамбет. Өмірі, шығармашылығы</li>
                                    <li>Шалкиіз. Өмірі, шығармашылығы</li>
                                    <li>Жиембет. Өмірі, шығармашылығы</li>
                                    <li>Ақтамберді. Өмірі, шығармашылығы</li>
                                    <li>Үмбетай. Өмірі, шығармашылығы</li>
                                    <li>Бұхар Жырау. Өмірі, шығармашылығы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="4" class="text-center">3</td>
                            <td rowspan="4">ХІХ ғасырдағы әдебиет</td>
                            <td>ХІХ ғ. І жартысындағы әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Махамбет Өтемісұлы</li>
                                    <li>Дулат Бабатайұлы</li>
                                    <li>Мұрат Мөңкеұлы</li>
                                    <li>Шортанбай Қанайұлы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>ХІХ ғ. І жартысындағы ағартушылар</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Шоқан Уәлиханов</li>
                                    <li>Ыбырай Алтынсарин</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Абай Құнанбайұлы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Өмірі, өлеңдері</li>
                                    <li>Поэмалары мен қара сөздері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>ХІХ ғ. ІІ жартысындағы әдебиет. Ақын - сазгер - әншілер</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Біржан сал</li>
                                    <li>Ақан сері</li>
                                    <li>Ә. Найманбаев</li>
                                    <li>Үкілі Ыбырай</li>
                                    <li>Балуан Шолақ</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>ХХ ғ. І жартысындағы әдебиет</td>
                            <td>ХХ ғ. басындағы әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Шәкәрім Құдайбердіұлы</li>
                                    <li>Ахмет Байтұрсынов</li>
                                    <li>Жүсіпбек Аймауытов</li>
                                    <li>Міржақып Дулатов</li>
                                    <li>Мағжан Жұмабаев</li>
                                    <li>Сұлтанмахмұт Торайғыров</li>
                                    <li>Сәкен Сейфуллин</li>
                                    <li>Ілияс Жансүгіров</li>
                                    <li>Бейімбет Майлин</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">5</td>
                            <td rowspan="2">Ұлы Отан соғысы және одан кейінгі жылдардағы  әдебиет</td>
                            <td>Ұлы Отан соғысы және одан кейінгі жылдардағы  әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Қасым Аманжолов</li>
                                    <li>Жамбыл Жабаев</li>
                                    <li>Сәбит Мұқанов</li>
                                    <li>Ғабит Мүсірепов</li>
                                    <li>Ғабиден Мұстафин</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Мұхтар Әуезов</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Өмірі, шығармашылығы</li>
                                    <li>1920-1930 жж. әңгімелері, аудармалары</li>
                                    <li>Драматургиясы</li>
                                    <li>Романдары, Абай жолы роман-эпопеясы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Әдебиет теориясы</td>
                            <td>Көркемдегіш, бейнелеуіш құралдар</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Троп және оның түрлері</li>
                                    <li>Фигура және оның түрлері</li>
                                    <li>Өлең құрылымы, ұйқасы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">7</td>
                            <td rowspan="2">ХХ ғ. ІІ жартысындағы әдебиет</td>
                            <td>ХХ ғ. ІІ жартысындағы поэзия</td>
                            <td>
                                <ul class="list-normal">
                                    <li>М.Мақатаев, Қ.Мырзалиев</li>
                                    <li>Т.Молдағалиев, Ф.Оңғарсынова, Ж.Молдағалиев</li>
                                    <li>О.Сүлейменов, М.Шаханов, Ж.Нәжімеденов</li>
                                    <li>Т.Айбергенов, Қ.Бекхожин</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>ХХ ғ. ІІ жартысындағы проза мен драматургия</td>
                            <td>
                                <ul class="list-normal">
                                    <li>І.Есенберлин, Х.Есенжанов</li>
                                    <li>Ә.Нұрпейісов, Т.Ахтанов, Б.Момышұлы</li>
                                    <li>М.Мағауин, Д.Исабеков</li>
                                    <li>О.Бөкей, Қ.Жұмаділов, Б.Соқпақбаев</li>
                                    <li>Ә.Кекілбаев, Ш.Мұртаза</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.12.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9558: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Русский язык и литература» на русском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Русский язык и литература», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития поступающих в высшие учебные заведения Республики Казахстан;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: не);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.8</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.9</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.10</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.11</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td colspan="4">
                                <ul class="list-normal">
                                    <li>Русский язык</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="3" class="text-center">1</td>
                            <td rowspan="3">Фонетика и орфография</td>
                            <td>Звуки и буквы. Звуки речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Гласные и согласные звуки и буквы</li>
                                    <li>Двойная роль букв Е, Ё, Ю, Я</li>
                                    <li>Твердые и мягкие, звонкие и глухие согласные</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Правописание гласных</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Правописание безударных гласных в корне</li>
                                    <li>Правописание чередующихся гласных в корне</li>
                                    <li>Правописание гласных после шипящих и Ц</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Правописание согласных</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Правописание звонких и глухих согласных</li>
                                    <li>Непроизносимые согласные. Удвоенные согласные</li>
                                    <li>Употребление Ь и Ъ</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">2</td>
                            <td rowspan="2">Лексикология</td>
                            <td>Лексическое значение слова</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Однозначные и многозначные слова</li>
                                    <li>Прямое и переносное значение слова</li>
                                    <li>Лексические группы слов (синонимы, антонимы, омонимы, паронимы)</li>
                                    <li>Группы слов по происхождению и употреблению (диалектные, профессиональные, устаревшие, заимствованные слова)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Фразеология</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Фразеологические обороты</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">3</td>
                            <td rowspan="2">Морфемика и словообразование</td>
                            <td>Морфемика</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Значимые части слова (морфемы)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Словообразование</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Морфологические и неморфологические способы словообразования</li>
                                    <li>Правописание приставок (гласные в приставках)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">4</td>
                            <td rowspan="2">Морфология</td>
                            <td>Самостоятельные части речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Имя существительное</li>
                                    <li>Имя прилагательное</li>
                                    <li>Имя числительное</li>
                                    <li>Местоимение</li>
                                    <li>Глагол (причастие, деепричастие)</li>
                                    <li>Наречие</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Служебные части речи и междометие</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Служебные части речи</li>
                                    <li>Междометие и звукоподражательные слова</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="5" class="text-center">5</td>
                            <td rowspan="5">Синтаксис и пунктуация</td>
                            <td>Словосочетание</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Виды словосочетаний. Виды подчинительной связи</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Простое предложение</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Главные члены предложения. Неполные предложения</li>
                                    <li>Второстепенные члены предложения</li>
                                    <li>Двусоставные и односоставные предложения</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Простое осложненное предложение</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Однородные члены предложения</li>
                                    <li>Предложения с обособленными и уточняющими членами предложения</li>
                                    <li>Предложения со словами, грамматически не связанными с членами предложения</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сложное предложения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сложносочиненные предложения</li>
                                    <li>Сложноподчиненное предложение</li>
                                    <li>Бессоюзное сложное предложение</li>
                                    <li>Знаки препинания в сложных предложениях с различными видами связи</li>
                                </ul>
                            </td>
                        </tr>
                         <tr>
                            <td>Способы передачи чужой речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Предложения с прямой и косвенной речью</li>
                                    <li>Диалог и цитата</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="4">
                                <ul class="list-normal">
                                    <li>Русская литература</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="4" class="text-center">1</td>
                            <td rowspan="4">Теория литературы</td>
                            <td>Изобразительно-выразительные средства языка</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тропы фигуры</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Родо-жанровые особенности</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Роды и жанры фольклора</li>
                                    <li>Роды и жанры литературы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Структура художественного произведения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сюжет и элементы сюжетной композиции</li>
                                    <li>Размер стиха, способы рифмовки</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Литературоведческие термины</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Литературные направления</li>
                                    <li>Компоненты художественного мира</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Биография</td>
                            <td>Биографические факты</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Факты биографий писателей. История создания произведений</li>
                                    <li>Вклад в развитие литературы</li>
                                    <li>Историческая обстановка, характер эпохи</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Литературная критика</td>
                            <td>Критика</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Название критических статей. Авторы  критических статей</li>
                                    <li>Ключевые идеи критических статей. Цитаты</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">4</td>
                            <td rowspan="2">Роль эпизодов</td>
                            <td>Роль эпизодов (сцен) в развитии темы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Место эпизода в произведении. Значение эпизода в развитии темы и идеи</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Идеи, характеры в эпическом и драматическом произведении, мотивы и образы в лирическом произведении</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Основные темы и идеи в эпических произведениях</li>
                                    <li>Основные темы и мотивы в лирических произведениях</li>
                                    <li>Особенности конфликта в драматических произведениях</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Сквозные темы</td>
                            <td>Сквозные темы в группе произведений</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тема «маленького человека»</li>
                                    <li>Тема «лишних людей»</li>
                                    <li>Конфликт «отцов и детей»</li>
                                    <li>Военная тема</li>
                                    <li>Тема родины</li>
                                    <li>Тема города и деревни</li>
                                    <li>Философская тема</li>
                                    <li>Тема человека и природы</li>
                                    <li>Тема любви</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Содержание произведений</td>
                            <td>Содержание произведений</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Название произведения. Автор произведения</li>
                                    <li>Герои произведения. Система образов-персонажей</li>
                                    <li>Основные события произведения</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.12</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9559: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Человек. Общество. Право» на казахском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Человек. Общество. Право», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: емес);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.9.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.10.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.11.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Человек</td>
                            <td>Человек в мире</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Проблема человека. Человек и взаимоотношение людей. Свобода, необходимость и ответственность в человеческой деятельности </li>
                                    <li>Человек и культура. Человек и его мировоззрение. Познавательное отношение человека к миру</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="3" class="text-center">2</td>
                            <td rowspan="3">Общество</td>
                            <td>Социальная сфера</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Понятие общества</li>
                                    <li>Личность и общество</li>
                                    <li>Современное общество</li>
                                    <li>Общество как социальная система</li>
                                    <li>Социальная структура общества</li>
                                    <li>Социальные отношения</li>
                                    <li>Что такое социология</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Экономическая сфера</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Экономическая жизнь общества</li>
                                    <li>Экономическое поведение рыночных субъектов</li>
                                    <li>Что такое экономическая теория</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Духовная сфера</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Духовная жизнь человека</li>
                                    <li>Духовная культура</li>
                                    <li>Что такое философия</li>
                                    <li>Философская антропология</li>
                                    <li>Философия естествознания</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="3" class="text-center">3</td>
                            <td rowspan="3">Политика и право</td>
                            <td>Основы политологии (или Политика)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Политическая жизнь общества</li>
                                    <li>Политическая система</li>
                                    <li>Что такое политология</li>
                                    <li>Культура и политика</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Конституционное право</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Конституция – основной закон РК</li>
                                    <li>Права и обязанности человека и гражданина</li>
                                    <li>РК – правовое государство</li>
                                    <li>Механизм правового регулирования</li>
                                    <li>Законность и правопорядок</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Введение в юриспруденцию</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Понятие права и основных правовых явлений</li>
                                    <li>Основные понятия базовых отраслей Казахстанского права</li>
                                    <li>Основные отрасли частного права</li>
                                    <li>Основные отрасли публичного права</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
}
SPECIFICATION_RU_TEST_TEXTS = {
    9540: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
        """,
    },
    9541: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для учащихся 6 классов общеобразовательных школ – претендентов в Интеллектуальные школы, по предмету <strong>«Казахский язык для учащихся на русском языке»</strong> с выбором одного правильного ответа из 4 предложенных вариантов.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые задания должны соответствовать учебным программам по предмету «Казахский язык для учащихся на русском языке» для 5-6 классов уровня основного среднего образования, разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития учащихся 6-х классов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Задачей тестовых вопросов должна являться оценка навыков понимания прочитанного текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тестовые вопросы должны быть поделены на три типа:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.1.</span>Тестовые вопросы на <strong>значение</strong> – слова, предложения, абзацы, основная идея текста, значение важных элементов текста;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.2.</span>Тестовые вопросы на <strong>структуру</strong> – ссылки, отношения между элементами (синтаксис), умение выделять части текста и определять связь между частями текста (структурой текста);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.3.</span>Тестовые вопросы на <strong>коммуникацию</strong> – умения делать выводы основываясь на мнение, цель, чувства и позицию автора текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.7.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.8.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: <u><strong>жоқ</strong></u>, <u><strong>емес</strong></u>);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по внесению тестовых вопросов на Веб-сайт:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Указывается ФИО Разработчика;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.2.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.3.</span>Указывается общий раздел контекста (человек, животные, природа и т.д.);</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.4.</span>Указывается тип тестовых вопросов по таксономии Блума (значение/коммуникация/структура).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.1.</span>К одному тексту может быть 1/3/5 тестовых вопросов.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.2.</span>Один вариант должен содержать 20 тестовых вопросов и 10 текстов:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="75%" class="text-center" colspan="3">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="25%" class="text-center">Значение</th>
                            <th width="25%" class="text-center">Коммуникация</th>
                            <th width="25%" class="text-center">Структура</th>
                        </tr>
                        <tr>
                            <td>Текст 1</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 3</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 4</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 5</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 6</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 7</td>
                            <td class="text-center">2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 8</td>
                            <td class="text-center">1</td>
                            <td class="text-center">2</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 9</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                        <tr>
                            <td>Текст 10</td>
                            <td class="text-center">3</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td class="text-right"><strong>Итого:</strong></td>
                            <td class="text-center" colspan="3"><strong>20</strong></td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.3.</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="50%" class="text-center">Предполагаемый уровень сложности</th>
                            <th width="25%" class="text-center">%</th>
                            <th width="25%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">50</td>
                            <td class="text-center">10</td>
                        </tr>
                        <tr>
                            <td>Сложный</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">10.</span>Образцы тестовых заданий по предмету <a target="_blank" href="http://nis.edu.kz/site/nis/repository/file/Selection%20test_SAMPLES/1%20%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D1%86%D1%8B%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_7%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81_RU.pdf">«Казахский язык для учащихся на русском языке»</a>.</p>
        """,
    },
    9542: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для учащихся 6 классов общеобразовательных школ – претендентов в Интеллектуальные школы, по предмету <strong>«Русский язык для учащихся на русском языке»</strong> с выбором одного правильного ответа из 4 предложенных вариантов.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые задания должны соответствовать учебным программам по предмету «Русский язык для учащихся на русском языке» для 5-6 классов уровня основного среднего образования, разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития учащихся 6-х классов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Задачей тестовых вопросов должна являться оценка навыков понимания прочитанного текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тестовые вопросы должны быть поделены на три типа:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.1.</span>Тестовые вопросы на <strong>значение</strong> – слова, предложения, абзацы, основная идея текста, значение важных элементов текста;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.2.</span>Тестовые вопросы на <strong>структуру</strong> – ссылки, отношения между элементами (синтаксис), умение выделять части текста и определять связь между частями текста (структурой текста);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.3.</span>Тестовые вопросы на <strong>коммуникацию</strong> – умения делать выводы основываясь на мнение, цель, чувства и позицию автора текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.7.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.8.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: <u><strong>не</strong></u>);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по внесению тестовых вопросов на Веб-сайт:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Указывается ФИО Разработчика;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.2.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.3.</span>Указывается общий раздел контекста (человек, животные, природа и т.д.);</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.4.</span>Указывается тип тестовых вопросов по таксономии Блума (значение/коммуникация/структура).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.1.</span>К одному тексту может быть 1/3/5 тестовых вопросов.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.2.</span>Один вариант должен содержать 20 тестовых вопросов и 10 текстов:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="75%" class="text-center" colspan="3">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="25%" class="text-center">Значение</th>
                            <th width="25%" class="text-center">Коммуникация</th>
                            <th width="25%" class="text-center">Структура</th>
                        </tr>
                        <tr>
                            <td>Текст 1</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 3</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 4</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 5</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 6</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 7</td>
                            <td class="text-center">2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 8</td>
                            <td class="text-center">1</td>
                            <td class="text-center">2</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 9</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                        <tr>
                            <td>Текст 10</td>
                            <td class="text-center">3</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td class="text-right"><strong>Итого:</strong></td>
                            <td class="text-center" colspan="3"><strong>20</strong></td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.3.</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="50%" class="text-center">Предполагаемый уровень сложности</th>
                            <th width="25%" class="text-center">%</th>
                            <th width="25%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">50</td>
                            <td class="text-center">10</td>
                        </tr>
                        <tr>
                            <td>Сложный</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">10.</span>Образцы тестовых заданий по предмету <a target="_blank" href="http://nis.edu.kz/site/nis/repository/file/Selection%20test_SAMPLES/1%20%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D1%86%D1%8B%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_7%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81_RU.pdf">«Русский язык для учащихся на русском языке»</a>.</p>
        """,
    },
    9544: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
        """,
    },
    9545: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы на определение уровня подготовленности по предмету «История Казахстана» на русском языке для поступающих в высшие учебные заведения Республики Казахстан. </p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Содержание тестовых вопросов должно соответствовать учебному материалу по предмету «История Казахстана» в соответствии с учебной программой для общеобразовательной школы.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.7.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.8.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.9.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.10.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Эпоха камня и бронзы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Палеолит, мезолит, неолит, энеолит. Эпоха бронзы.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Казахстан в эпоху железа</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Возникновение кочевого скотоводства. Основы жизнеобеспечения кочевого скотоводства. Культурные достижения ранних кочевников на территории Казахстана.</li>
                                    <li>Саки: сведения о саках, расселение, сакское общество, борьба саков за независимость.</li>
                                    <li>Уйсуны, кангюи: расселение, письменные источники, общественное устройство.</li>
                                    <li>Гунны: письменные источники, государственное устройство, объединение гуннов, перемещение на запад, Аттила и его походы.</li>
                                    <li>Сарматы: расселение, общественный строй.</li>
                                    <li>Саки, уйсуны, кангюи, гунны, сарматы: быт, хозяйство, культура, археологические памятники.</li>
                                    <li>Регионы Казахстана в период раннего железного века.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Государства раннего и развитого средневековья (VI-нач.XIII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Раннесредневековые государства на территории Казахстана: Тюркский, Западно-Тюрксий, Тюргешский, Карлукский каганаты, Огузы, Кимаки: социально-экономическое развитие и общественно-политическая история.</li>
                                    <li>Казахстан в период среднего средневековья: Караханиды, Найманы, Кереи, Жалаиры, Каракитаи, Кипчаки: социально-экономическое развитие и общественно-политическая история.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Культура (VI-XVII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Великий Шелковый путь на территории Казахстана. Культура VI-IX вв.</li>
                                    <li>Городская культура IX-XIII вв. Ремесло, торговля. Религия и культура. Развитие науки и образования.</li>
                                    <li>Развитие культуры Казахстана в XIV-XV вв.</li>
                                    <li>Развитие культуры Казахстана в XVI-XVII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Казахстан в XIII-XVII вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Монгольский период в истории Казахстана. Золотая Орда: образование, общественный строй, усиление, распад. Ак Орда, Моголистан, Ногайская Орда, ханство Абулхаира, Северный Казахстан и Западная Сибирь. Государство Тимура.</li>
                                    <li>Этнические процессы на территории Казахстана. Образование Казахского ханства. Внутренняя и внешняя политика. Укрепление Казахского ханства в XVI-XVII вв.: Касым хан, Хакназар хан, Тауекель хан, Есим хан, Тауке хан</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Социально-экономическое положение Казахстана в XIII-XVII вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Государственно-административное устройство государтсв XIII-XV вв. Система правления в Казахском ханстве.</li>
                                    <li>Экономическое положение Казахстана в XIV-XV вв.</li>
                                    <li>Экономическое положение Казахстана в XVI-XVII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">7</td>
                            <td>Социально-экономическое развитие Казахстана в XVIII-XIX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Торгово-экономические связи Казахстана с Китаем. Экономическое развитие Казахстана во второй половине XIX в. Переселение уйгуров и дунган в Семиречье.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">8</td>
                            <td>Общественно-политическое развитие Казахстана в XVIII-XIX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Борьба казахского народа против джунгарского нашествия. Присоединение Младшего жуза к России. Внутренняя и внешняя политика Абылай хана.</li>
                                    <li>Участие казахов в Крестьянской войне 1773-1775 гг. Восстание казахов Младшего жуза под руководством С.Датулы 1783-1797 гг. Ликвидация ханской власти. Восстание И.Тайманулы и М.Утемисулы 1836-1838 гг., Кенесары Касымулы 1837-1847 гг.</li>
                                    <li>Освободительная борьба казахских шаруа в 50-е годы XIX века. Присоединение Старшего жуза к России. Завершение колониального захвата Казахстана Россией и его последствия. Реформы 1860-1890-х гг. В Казахстане. Освободительная борьба казахского народа в 60-70 годы XIX века.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">9</td>
                            <td>Казахстан в первой половине XX в.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Социально-экономическое развитие Казахстана в начале XX века. Политика «военного коммунизма». Казахстан в годы НЭП. Индустриализация. Коллективизация сельского хозяйства. Наращивание экономической мощи Казахстана в годы ВОВ.</li>
                                    <li>Общественно-политическая жизнь Казахстана в первой половине XX века. Политическое развитие Казахстана в начале XX века. Национально-освободительные движения и их основные направления. Национально-освободительное движение 1916 г. Казахстан в период ФБДР 1917 г. Движение о создании партии Алаш. Октябрьская революция. Национальные автономиив Казахстане. Казахстан в годы Гражданской войны и иностранной военной интервенции. Образование КазАССР. Формирование территории Казахской АССР. Общественно-политическое положение Казахстана в 1920-1940-е гг. Казахстанцы в период ВОВ.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">10</td>
                            <td>Культура Казахстана XVIII-XX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Культура Казахстана в XVIII в.</li>
                                    <li>Культура Казахстана в первой половине XIX в.</li>
                                    <li>Культура Казахстана во второй половине XIX в.</li>
                                    <li>Культура Казахстана в начале XX в.</li>
                                    <li>Культура Казахстана в 1920-1940-е гг.</li>
                                    <li>Культура Казахстана во второй половине XX века (1946-1980 гг.)</li>
                                    <li>Культура Казахстана в конце XX – начале XXI вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">11</td>
                            <td>Казахстан в 50-80-е гг. XX века</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Общественно-политическая жизнь Казахстана в 50-80-е гг. XX века</li>
                                    <li>Социально-экономическое развитие в в 50-80-е гг. XX века</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">12</td>
                            <td>Независимый Казахстан</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Провозглашение и становление независимого Казахстана. Общественно-политическое развитие РК. Внешняя политика РК.</li>
                                    <li>Экономическое развитие РК.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">13</td>
                            <td>История в документах</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Письменные источники об исторических событиях</li>
                                </ul>
                            </td>
                        </tr>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.1.</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">10</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.2.</span>Один тестовый вопрос имеет 1 (один) правильный вариант ответа из 5 (пяти) предложенных.</p>
        """,
    },
    9546: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы на оценку способности к пониманию и осмыслению письменных текстов, к использованию их содержания для достижения собственных целей, развития знаний и возможностей, для активного участия в жизни общества на русском языке для поступающих в высшие учебные заведения Республики Казахстан. </p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Содержание тестовых вопросов должно соответствовать содержанию вопросов, используемых в международных сравнительных исследованиях в области образования (PISA, TIMSS и т.п.).</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития поступающих в высшие учебные заведения Республики Казахстан;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.8.</span>Количество слов в текстах и вопросов к одному тексту в одном варианте теста должно составлять:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Текст #</th>
                            <th class="text-center">Количество слов</th>
                            <th class="text-center">Количество вопросов</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td class="text-center">60-100</td>
                            <td class="text-center">2</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td class="text-center">100-200</td>
                            <td class="text-center">4</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td class="text-center">200-350</td>
                            <td class="text-center">6</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td class="text-center">350-500</td>
                            <td class="text-center">8</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.9.</span>Тематика текстов:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th>#</th>
                            <th width="66%" class="text-center">Тема</th>
                            <th width="34%" class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Человек и его окружение</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Семья и ценности жизни.</li>
                                    <li>Друзья. Интересы и увлечения.</li>
                                    <li>Профессия. Работа.</li>
                                    <li>Спорт и здоровый образ жизни. Путешествия. Отдых.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Образование и наука</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Образование</li>
                                    <li>Биография. Деятели науки.</li>
                                    <li>Искусство.</li>
                                    <li>Технический прогресс.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Города и государства</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Географические особенности государств. Экономика.</li>
                                    <li>Столицы и города. Архитектура и строительство.</li>
                                    <li>Политика</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Социальные взаимоотношения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Средства массовой информации.</li>
                                    <li>Праздники, традиции и обычаи.</li>
                                    <li>История. Культурное наследие.</li>
                                    <li>Проблемы человечества.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Природа</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Объекты природы.</li>
                                    <li>Погода и климат.</li>
                                    <li>Животные, насекомые, птицы, растительный мир.</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов: </p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: <span style="text-decoration: underline;"><strong>жоқ, емес</strong></span>);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.9.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.10.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.11.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Тема</th>
                        </tr>
                        <tr>
                            <td>Человек и его окружение</td>
                        </tr>
                        <tr>
                            <td>Образование и наука</td>
                        </tr>
                        <tr>
                            <td>Города и государства</td>
                        </tr>
                        <tr>
                            <td>Социальные взаимоотношения</td>
                        </tr>
                        <tr>
                            <td>Природа</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">10</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.2.</span>Один тестовый вопрос имеет один правильный вариант ответа из пяти предложенных.</p>
        """,
    },
    9547: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы на оценку математического мышления и способности применения навыков знания, применения и интерпритации математики в жизненных ситуациях (в различных контекстах) на русском языке для поступающих в высшие учебные заведения Республики Казахстан. </p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Содержание тестовых вопросов должно соответствовать содержанию вопросов, используемых в международных сравнительных исследованиях в области образования (PISA, TIMSS и т.п.).</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов: </p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1</span>Все математические формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2</span>Все графики и рисунки должны быть созданы специализированными редакторами (GeoGebra и т.п.) и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.6</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th>#</th>
                            <th width="66%" class="text-center">Раздел</th>
                            <th width="34%" class="text-center">Проверяемые знание и умение</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Количественные рассуждения</td>
                            <td>Умение:
                                <ul class="list-normal">
                                    <li>решать примеры на вычисление</li>
                                    <li>решать текстовые задачи</li>
                                    <li>вычислять задачи на проценты</li>
                                    <li>решать уравнения</li>
                                    <li>находить значения числовых и буквенных выражений</li>
                                    <li>определять числовые характеристики круговых и столбчатых диаграмм</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Неопределенность</td>
                            <td>Умение вычислять задачи на:
                                <ul class="list-normal">
                                    <li>теорию вероятности</li>
                                    <li>математическую статистику</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Изменение и зависимости</td>
                            <td>Умение решать задачи:
                                <ul class="list-normal">
                                    <li>на функциональную зависимость</li>
                                    <li>по графическим изображениям зависимости</li>
                                    <li>на зависимости, изображенные на диаграммах</li>
                                </ul>
                                Умение:
                                <ul class="list-normal">
                                    <li>вычислять задачи на изменение одной величины в зависимости от другой</li>
                                    <li>вычислять задачи на последовательности</li>
                                    <li>анализировать данные в таблице</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Пространство и форма</td>
                            <td>
                                Умение:
                                <ul class="list-normal">
                                    <li>решать текстовые задачи с геометрическим содержанием</li>
                                    <li>применять формулы площади, периметра геометрических фигур</li>
                                    <li>применять формулы объема и площади поверхности геометрических тел</li>
                                    <li>вычислять задачи на зависимости измерений геометрических фигур и тел</li>
                                    <li>решать нестандартные задачи с геометрическим содержанием</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7</span>Указывается тип когнитивного уровня тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Типы когнитивного уровня тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Применение</td>
                        </tr>
                        <tr>
                            <td>Анализ</td>
                        </tr>
                        <tr>
                            <td>Синтез</td>
                        </tr>
                        <tr>
                            <td>Смешанные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.1</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">10</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2</span>Один тестовый вопрос имеет один правильный вариант ответа из пяти предложенных.</p>
        """,
    },
    9548: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Математика» на русском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Математика», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1</span>Все математические формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2</span>Все графики и рисунки должны быть созданы специализированными редакторами (GeoGebra и т.п.) и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Арифметические вычисления. Преобразования выражений.</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Уравнения. Системы уравнений. Составление уравнений.</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Неравенства. Системы неравенств.</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Функции. Производные. Интеграл.</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Планиметрия.</td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Стереометрия.</td>
                        </tr>
                        <tr>
                            <td class="text-center">7</td>
                            <td>Последовательности. Прогрессии.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9549: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Физика» на русском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Физика», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все математические формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все графики и рисунки должны быть созданы специализированными редакторами (GeoGebra и т.п.) и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Механика</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Молекулярная физика. Основы термодинамики</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Электродинамика</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Оптика</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Квантовая и атомная физика</td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Качественные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Анализ</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Синтез</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9550: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Химия» на русском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Химия», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все математические формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все химические формулы, графики и рисунки должны быть созданы специализированными редакторами и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Общая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Неорганическая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Органическая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Расчетные задачи: Общая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Расчетные задачи: Неорганическая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Расчетные задачи: Органическая химия</td>
                        </tr>
                        <tr>
                            <td class="text-center">7</td>
                            <td>Качественные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Анализ</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Синтез</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9551: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Биология» на русском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Биология», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все графики и рисунки должны быть созданы специализированными редакторами и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Растения</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Животные</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Анатомия и физиология человека</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Цитология, генетика, экология</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Качественные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Анализ</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Синтез</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9552: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «География» на русском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «География», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению и внесению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Все формулы должны быть внесены на языке программирования Latex;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Все графики и рисунки должны быть созданы специализированными редакторами и иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Для обозначения фигур и их элементов необходимо использовать буквы латинского алфавита, записанные курсивом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Указывается общий раздел контекста каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Физическая география мира</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>География Казахстана</td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Экономическая и социальная география мира</td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Задачи по курсу география</td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Качественные задачи</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9553: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы на определение уровня подготовленности по предмету «История» на русском языке для поступающих в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Содержание тестовых вопросов должно соответствовать учебному материалу по предмету «История» в соответствии с учебной программой для общеобразовательной школы.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.7.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.8.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.9.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.10.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Эпоха камня и бронзы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Палеолит, мезолит, неолит, энеолит. Эпоха бронзы.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Казахстан в эпоху железа</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Возникновение кочевого скотоводства. Основы жизнеобеспечения кочевого скотоводства. Культурные достижения ранних кочевников на территории Казахстана.</li>
                                    <li>Саки: сведения о саках, расселение, сакское общество, борьба саков за независимость.</li>
                                    <li>Уйсуны, кангюи: расселение, письменные источники, общественное устройство.</li>
                                    <li>Гунны: письменные источники, государственное устройство, объединение гуннов, перемещение на запад, Аттила и его походы.</li>
                                    <li>Сарматы: расселение, общественный строй.</li>
                                    <li>Саки, уйсуны, кангюи, гунны, сарматы: быт, хозяйство, культура, археологические памятники.</li>
                                    <li>Регионы Казахстана в период раннего железного века.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Государства раннего и развитого средневековья (VI-нач.XIII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Раннесредневековые государства на территории Казахстана: Тюркский, Западно-Тюрксий, Тюргешский, Карлукский каганаты, Огузы, Кимаки: социально-экономическое развитие и общественно-политическая история.</li>
                                    <li>Казахстан в период среднего средневековья: Караханиды, Найманы, Кереи, Жалаиры, Каракитаи, Кипчаки: социально-экономическое развитие и общественно-политическая история.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Культура (VI-XVII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Великий Шелковый путь на территории Казахстана. Культура VI-IX вв.</li>
                                    <li>Городская культура IX-XIII вв. Ремесло, торговля. Религия и культура. Развитие науки и образования.</li>
                                    <li>Развитие культуры Казахстана в XIV-XV вв.</li>
                                    <li>Развитие культуры Казахстана в XVI-XVII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Казахстан в XIII-XVII вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Монгольский период в истории Казахстана. Золотая Орда: образование, общественный строй, усиление, распад. Ак Орда, Моголистан, Ногайская Орда, ханство Абулхаира, Северный Казахстан и Западная Сибирь. Государство Тимура.</li>
                                    <li>Этнические процессы на территории Казахстана. Образование Казахского ханства. Внутренняя и внешняя политика. Укрепление Казахского ханства в XVI-XVII вв.: Касым хан, Хакназар хан, Тауекель хан, Есим хан, Тауке хан</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Социально-экономическое положение Казахстана в XIII-XVII вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Государственно-административное устройство государтсв XIII-XV вв. Система правления в Казахском ханстве. </li>
                                    <li>Экономическое положение Казахстана в XIV-XV вв.</li>
                                    <li>Экономическое положение Казахстана в XVI-XVII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">7</td>
                            <td>Социально-экономическое развитие Казахстана в XVIII-XIX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Торгово-экономические связи Казахстана с Китаем. Экономическое развитие Казахстана во второй половине XIX в. Переселение уйгуров и дунган в Семиречье.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">8</td>
                            <td>Общественно-политическое развитие Казахстана в XVIII-XIX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Борьба казахского народа против джунгарского нашествия. Присоединение Младшего жуза к России. Внутренняя и внешняя политика Абылай хана.</li>
                                    <li>Участие казахов в Крестьянской войне 1773-1775 гг. Восстание казахов Младшего жуза под руководством С.Датулы 1783-1797 гг. Ликвидация ханской власти. Восстание И.Тайманулы и М.Утемисулы 1836-1838 гг., Кенесары Касымулы 1837-1847 гг.</li>
                                    <li>Освободительная борьба казахских шаруа в 50-е годы XIX века. Присоединение Старшего жуза к России. Завершение колониального захвата Казахстана Россией и его последствия. Реформы 1860-1890-х гг. В Казахстане. Освободительная борьба казахского народа в 60-70 годы XIX века.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">9</td>
                            <td>Казахстан в первой половине XX в.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Социально-экономическое развитие Казахстана в начале XX века. Политика «военного коммунизма». Казахстан в годы НЭП. Индустриализация. Коллективизация сельского хозяйства. Наращивание экономической мощи Казахстана в годы ВОВ.</li>
                                    <li>Общественно-политическая жизнь Казахстана в первой половине XX века. Политическое развитие Казахстана в начале XX века. Национально-освободительные движения и их основные направления. Национально-освободительное движение 1916 г. Казахстан в период ФБДР 1917 г. Движение о создании партии Алаш. Октябрьская революция. Национальные автономиив Казахстане. Казахстан в годы Гражданской войны и иностранной военной интервенции. Образование КазАССР. Формирование территории Казахской АССР. Общественно-политическое положение Казахстана в 1920-1940-е гг. Казахстанцы в период ВОВ.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">10</td>
                            <td>Культура Казахстана XVIII-XX вв.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Культура Казахстана в XVIII в.</li>
                                    <li>Культура Казахстана в первой половине XIX в.</li>
                                    <li>Культура Казахстана во второй половине XIX в.</li>
                                    <li>Культура Казахстана в начале XX в.</li>
                                    <li>Культура Казахстана в 1920-1940-е гг.</li>
                                    <li>Культура Казахстана во второй половине XX века (1946-1980 гг.)</li>
                                    <li>Культура Казахстана в конце XX – начале XXI вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">11</td>
                            <td>Казахстан в 50-80-е гг. XX века</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Общественно-политическая жизнь Казахстана в 50-80-е гг. XX века</li>
                                    <li>Социально-экономическое развитие в в 50-80-е гг. XX века</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">12</td>
                            <td>Независимый Казахстан</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Провозглашение и становление независимого Казахстана. Общественно-политическое развитие РК. Внешняя политика РК.</li>
                                    <li>Экономическое развитие РК.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">13</td>
                            <td>История в документах</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Письменные источники об исторических событиях Казахстана</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">14</td>
                            <td>Государства Древнего Востока. Античная цивилизация</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Древние государства Месопотамия, Египет, государства Юго-Западной, Южной и Восточной Азии (социально-экономическое развитие и общественно-политическая история)</li>
                                    <li>Древняя Греция, Македония, Древний Рим в период Республики и период Империи (социально-экономическое развитие и общественно-политическая история)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">15</td>
                            <td>Средневековье (ранее V – X вв., расцвет XI-XV вв., позднее XV-XVII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Западная и Центральная Европа, Византийская империя и Ближний Восток, Центральная Азия, монголо-татары, Средняя Азия, славяне, Киевская Русь, страны Востока, Русь в XI-XIII вв., Россия в XV-XVII вв. (социально-экономическое развитие, общественно-политическая история)</li>
                                    <li>Христианская церковь в XI-XIII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">16</td>
                            <td>Культура древнего мира (до V века), средневековая культура мира (V-XVII вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Древняя Греция, Древний Рим, Древний Восток</li>
                                    <li>Западная и Центральная Европа, Византийская империя и Ближний Восток, Центральная Азия, Средняя Азия, славяне, Киевская Русь, страны Востока, Русское государство в XI-XVII вв. Великие географические открытия. Возрождение</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">17</td>
                            <td>Европа и Северная Америка, Страны Азии и Африки (XVII-начало XX вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Англия, Северная Америка, Франция, Россия, Германия, Италия, Австрия, Индия. Османская империя, Китай, Монголия, Япония, Иран (общественно-политическая история и социально-экономическое развитие XVII-XVIII вв.)</li>
                                    <li>США, Англия, Россия, Франция, Германия, Италия, Австро-Венгрия, Китай, Япония, Индия, Османская империя, Иран, Арабские страны (общественно-политическая история и социально-экономическое развитие XIX-нач.XX вв.)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">18</td>
                            <td>Культура Европы, Северной Америки, стран Азии и Африки (XVIII в. – начало XXI в.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Эпоха Просвещения. Развитие науки и техники в XVII-XVIII вв. Культура XIX – первой половины XX вв.</li>
                                    <li>Культура второй половины XX – начала XII вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">19</td>
                            <td>Международные отношения (XVII – начало XXI вв.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Колониальная система и международные отношения в XVII – XVIII вв.</li>
                                    <li>Международные отношения в XIX – начале XXI вв.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">20</td>
                            <td>Мировые войны и их последствия</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Первая мировая война (1914-1918 гг.), Версальско-Вашингтонская система</li>
                                    <li>Вторая мировая война (1939-1945 гг.). Великобритания, Франция, Германия, Италия, СССР, США, Япония, Китай, Монголия, Индия, Иран, Афганистан, Турция, Арабские страны, Азии и Африки в период второй мировой войны</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">21</td>
                            <td>Страны Европы и Америки, Азии и Африки (1918-2014 гг.)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Страны Европы и Америки, Азии и Африки в период между двумя мировыми войнами (1918-1939 гг., Великобритания, Франция, Германия, Италия, Советская Россия, СССР, США, Япония, Китай, Монголия, Индия, Иран, Афганистан, Турция, Арабские страны Азии и Африки)</li>
                                    <li>Страны Западной Европы и Америки, страны Южной, Центральной, Восточной Европы, Страны Азии и Африки (1945-2014 гг., Великобритания, Франция, ФРГ, США, Италия, Страны Центральной и Юго-Восточной Европы, СССР, Российская Федерация, Япония, Китай, МНР, Индия, Пакистан, Иран, Афганистан, Турция, Арабские страны)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">22</td>
                            <td>История в документах</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Письменные источники об исторических событиях:</li>
                                    <li>Государства Древнего Востока. Античная цивилизация</li>
                                    <li>Средневековье (ранее V – X вв., расцвет XI-XV вв., позднее XV-XVII вв.)</li>
                                    <li>Культура древнего мира (до V века), средневековая культура мира (V-XVII вв.)</li>
                                    <li>Европа и Северная Америка, Страны Азии и Африки (XVII-начало XX вв.)</li>
                                    <li>Культура Европы, Северной Америки, стран Азии и Африки (XVIII в. – начало XXI в.)</li>
                                    <li>Международные отношения (XVII – начало XXI вв.)</li>
                                    <li>Мировые войны и их последствия</li>
                                    <li>Страны Европы и Америки, Азии и Африки (1918-2014 гг.)</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9557: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Казахский язык и литература» на казахском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Казахский язык и литература», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития поступающих в высшие учебные заведения Республики Казахстан;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.6.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: емес);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.9.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.10.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.11.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td colspan="4">
                                <ul class="list-normal">
                                    <li>Қазақ тілі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">1</td>
                            <td rowspan="2">Лексика</td>
                            <td>Сөз және сөздің мағыналары</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сөздің тура және ауыспалы мағынасы, көп мағыналы сөздер</li>
                                    <li>Омоним, антоним, синоним</li>
                                    <li>Тұрақты тіркес, мақал-мәтел</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сөздік қор</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Көнерген сөздер, неологизмдер</li>
                                    <li>Кірме сөздер, диалект сөздер</li>
                                    <li>Кәсіби сөздер мен терминдер</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="4" class="text-center">2</td>
                            <td rowspan="4">Фонетика</td>
                            <td>Дауысты дыбыстар</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Дауысты дыбыстардың түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Дауыссыз дыбыстар</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Дауыссыз дыбыстардың түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Буын және тасымал</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Буын түрлері, буынға бөліну ерекшеліктері, тасымал шарты</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Үндестік заңы. Орфография, орфоэпия</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Буын үндестігі, буын үндестігіне бағынбайтын қосымшалар. Дыбыс үндестігі, ықпал түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Сөзжасам</td>
                            <td>Сөздік құрам</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Түбір сөз, туынды сөз</li>
                                    <li>Күрделі сөз, түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="9" class="text-center">4</td>
                            <td rowspan="9">Морфология</td>
                            <td>Зат есім</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Зат есімнің мағыналық, құрамдық түрлері, қызметі</li>
                                    <li>Зат есімнің жалғаулары, көмекші есім</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сын есім</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сын есімнің жасалуы, түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сан есім</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сан есімнің түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Есімдік</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Есімдіктің түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Етістік</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Етістіктің құрамдық, мағыналық түрлері, қызметі</li>
                                    <li>Етістіктің шақтары, райлары</li>
                                    <li>Көсемше мен есімше, етіс</li>
                                    <li>Тұйық етістік, емлесі; Көмекші етістік</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Үстеу</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Үстеудің түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Еліктеу сөздер</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Еліктеу сөздердің түрлері, емлесі, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Одағай</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Одағай түрлері, тыныс белгісі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Шылау</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Шылаудың түрлері, емлесі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="6" class="text-center">5</td>
                            <td rowspan="6">Синтаксис</td>
                            <td>Сөз тіркесі</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сөздердің байланысу тәсілдері мен түрлері</li>
                                    <li>Сөз тіркесі, есімді және етістікті сөз тіркесі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сөйлем мүшелері</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тұрлаулы мүшелер, қызметі</li>
                                    <li>Тұрлаусыз мүшелер, қызметі</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Жай сөйлем</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Айтылу мақсатына қарай сөйлем түрлері</li>
                                    <li>Құрылысына, құрамына қарай сөйлем түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Құрмалас сөйлем</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Салалас құрмалас сөйлем, жасалуы, түрлері</li>
                                    <li>Сабақтас құрмалас сөйлем, жасалуы, түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Оқшау сөздер. Қаратпа сөз. Қыстырма сөз.</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Қаратпа, қыстырма сөздер, тыныс белгілері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Төл сөз</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Төл сөз, автор сөзі, төлеу сөз, тыныс белгілері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">6</td>
                            <td rowspan="2">Пунктуация</td>
                            <td>Тыныс белгілері</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тыныс белгілердің қойылатын орындары, қабаттаса қойылатын тыныс белгілер</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Стилистика. Шешендік сөз</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Стиль түрлері. Шешендік сөз</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="4">
                                <ul class="list-normal">
                                    <li>Қазақ әдебиеті</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">1</td>
                            <td rowspan="2">Ежелгі дүние әдебиеті</td>
                            <td>Көне түркі дәуіріндегі әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Алып Ер Тоңа дастаны, Күлтегін жазуы, Қорқыт ата кітабы, Оғыз қаған жыры</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Ислам дәуіріндегі әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Әбунасыр Әл-Фараби, Ахмет Иүгінеки, Ахмет Яссауи</li>
                                    <li>Жүсіп Баласағұн, Махмұт Қашғари, Рабғузи, Сайф Сараи</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">2</td>
                            <td rowspan="2">Ауыз әдебиеті</td>
                            <td>Ауыз әдебиеті</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тұрмыс-салт жырлары</li>
                                    <li>Ертегілер</li>
                                    <li>Мақал-мәтел, жұмбақтар</li>
                                    <li>Аңыздар</li>
                                    <li>Шешендік сөздер</li>
                                    <li>Батырлар жыры. Алпамыс батыр, Қобыланды батыр, Қамбар батыр</li>
                                    <li>Лира-эпостық жырлар. Қозы Көрпеш – Баян сұлу, Қыз Жібек</li>
                                    <li>Айтыс, түрлері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Жыраулар поэзиясы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Асан қайғы. Өмірі, шығармашылығы</li>
                                    <li>Қазтуған. Өмірі, шығармашылығы</li>
                                    <li>Доспамбет. Өмірі, шығармашылығы</li>
                                    <li>Шалкиіз. Өмірі, шығармашылығы</li>
                                    <li>Жиембет. Өмірі, шығармашылығы</li>
                                    <li>Ақтамберді. Өмірі, шығармашылығы</li>
                                    <li>Үмбетай. Өмірі, шығармашылығы</li>
                                    <li>Бұхар Жырау. Өмірі, шығармашылығы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="4">3</td>
                            <td rowspan="4">ХІХ ғасырдағы әдебиет</td>
                            <td>ХІХ ғ. І жартысындағы әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Махамбет Өтемісұлы</li>
                                    <li>Дулат Бабатайұлы</li>
                                    <li>Мұрат Мөңкеұлы</li>
                                    <li>Шортанбай Қанайұлы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>ХІХ ғ. І жартысындағы ағартушылар</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Шоқан Уәлиханов</li>
                                    <li>Ыбырай Алтынсарин</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Абай Құнанбайұлы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Өмірі, өлеңдері</li>
                                    <li>Поэмалары мен қара сөздері</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>ХІХ ғ. ІІ жартысындағы әдебиет. Ақын - сазгер - әншілер</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Біржан сал</li>
                                    <li>Ақан сері</li>
                                    <li>Ә. Найманбаев</li>
                                    <li>Үкілі Ыбырай</li>
                                    <li>Балуан Шолақ</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>4</td>
                            <td>ХХ ғ. І жартысындағы әдебиет</td>
                            <td>ХХ ғ. басындағы әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Шәкәрім Құдайбердіұлы</li>
                                    <li>Ахмет Байтұрсынов</li>
                                    <li>Жүсіпбек Аймауытов</li>
                                    <li>Міржақып Дулатов</li>
                                    <li>Мағжан Жұмабаев</li>
                                    <li>Сұлтанмахмұт Торайғыров</li>
                                    <li>Сәкен Сейфуллин</li>
                                    <li>Ілияс Жансүгіров</li>
                                    <li>Бейімбет Майлин</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2">5</td>
                            <td rowspan="2">Ұлы Отан соғысы және одан кейінгі жылдардағы  әдебиет</td>
                            <td>Ұлы Отан соғысы және одан кейінгі жылдардағы  әдебиет</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Қасым Аманжолов</li>
                                    <li>Жамбыл Жабаев</li>
                                    <li>Сәбит Мұқанов</li>
                                    <li>Ғабит Мүсірепов</li>
                                    <li>Ғабиден Мұстафин</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Мұхтар Әуезов</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Өмірі, шығармашылығы</li>
                                    <li>1920-1930 жж. әңгімелері, аудармалары</li>
                                    <li>Драматургиясы</li>
                                    <li>Романдары, Абай жолы роман-эпопеясы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Әдебиет теориясы</td>
                            <td>Көркемдегіш, бейнелеуіш құралдар</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Троп және оның түрлері</li>
                                    <li>Фигура және оның түрлері</li>
                                    <li>Өлең құрылымы, ұйқасы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">7</td>
                            <td rowspan="2">ХХ ғ. ІІ жартысындағы әдебиет</td>
                            <td>ХХ ғ. ІІ жартысындағы поэзия</td>
                            <td>
                                <ul class="list-normal">
                                    <li>М.Мақатаев, Қ.Мырзалиев</li>
                                    <li>Т.Молдағалиев, Ф.Оңғарсынова, Ж.Молдағалиев</li>
                                    <li>О.Сүлейменов, М.Шаханов, Ж.Нәжімеденов</li>
                                    <li>Т.Айбергенов, Қ.Бекхожин</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>ХХ ғ. ІІ жартысындағы проза мен драматургия</td>
                            <td>
                                <ul class="list-normal">
                                    <li>І.Есенберлин, Х.Есенжанов</li>
                                    <li>Ә.Нұрпейісов, Т.Ахтанов, Б.Момышұлы</li>
                                    <li>М.Мағауин, Д.Исабеков</li>
                                    <li>О.Бөкей, Қ.Жұмаділов, Б.Соқпақбаев</li>
                                    <li>Ә.Кекілбаев, Ш.Мұртаза</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.12.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9558: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Русский язык и литература» на русском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Русский язык и литература», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития поступающих в высшие учебные заведения Республики Казахстан;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: не);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.8</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.9</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.10</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.11</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td colspan="4">
                                <ul class="list-normal">
                                    <li>Русский язык</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="3" class="text-center">1</td>
                            <td rowspan="3">Фонетика и орфография</td>
                            <td>Звуки и буквы. Звуки речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Гласные и согласные звуки и буквы</li>
                                    <li>Двойная роль букв Е, Ё, Ю, Я</li>
                                    <li>Твердые и мягкие, звонкие и глухие согласные</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Правописание гласных</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Правописание безударных гласных в корне</li>
                                    <li>Правописание чередующихся гласных в корне</li>
                                    <li>Правописание гласных после шипящих и Ц</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Правописание согласных</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Правописание звонких и глухих согласных</li>
                                    <li>Непроизносимые согласные. Удвоенные согласные</li>
                                    <li>Употребление Ь и Ъ</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">2</td>
                            <td rowspan="2">Лексикология</td>
                            <td>Лексическое значение слова</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Однозначные и многозначные слова</li>
                                    <li>Прямое и переносное значение слова</li>
                                    <li>Лексические группы слов (синонимы, антонимы, омонимы, паронимы)</li>
                                    <li>Группы слов по происхождению и употреблению (диалектные, профессиональные, устаревшие, заимствованные слова)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Фразеология</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Фразеологические обороты</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">3</td>
                            <td rowspan="2">Морфемика и словообразование</td>
                            <td>Морфемика</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Значимые части слова (морфемы)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Словообразование</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Морфологические и неморфологические способы словообразования</li>
                                    <li>Правописание приставок (гласные в приставках)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">4</td>
                            <td rowspan="2">Морфология</td>
                            <td>Самостоятельные части речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Имя существительное</li>
                                    <li>Имя прилагательное</li>
                                    <li>Имя числительное</li>
                                    <li>Местоимение</li>
                                    <li>Глагол (причастие, деепричастие)</li>
                                    <li>Наречие</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Служебные части речи и междометие</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Служебные части речи</li>
                                    <li>Междометие и звукоподражательные слова</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="5" class="text-center">5</td>
                            <td rowspan="5">Синтаксис и пунктуация</td>
                            <td>Словосочетание</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Виды словосочетаний. Виды подчинительной связи</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Простое предложение</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Главные члены предложения. Неполные предложения</li>
                                    <li>Второстепенные члены предложения</li>
                                    <li>Двусоставные и односоставные предложения</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Простое осложненное предложение</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Однородные члены предложения</li>
                                    <li>Предложения с обособленными и уточняющими членами предложения</li>
                                    <li>Предложения со словами, грамматически не связанными с членами предложения</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сложное предложения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сложносочиненные предложения</li>
                                    <li>Сложноподчиненное предложение</li>
                                    <li>Бессоюзное сложное предложение</li>
                                    <li>Знаки препинания в сложных предложениях с различными видами связи</li>
                                </ul>
                            </td>
                        </tr>
                         <tr>
                            <td>Способы передачи чужой речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Предложения с прямой и косвенной речью</li>
                                    <li>Диалог и цитата</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="4">
                                <ul class="list-normal">
                                    <li>Русская литература</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="4" class="text-center">1</td>
                            <td rowspan="4">Теория литературы</td>
                            <td>Изобразительно-выразительные средства языка</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тропы фигуры</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Родо-жанровые особенности</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Роды и жанры фольклора</li>
                                    <li>Роды и жанры литературы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Структура художественного произведения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Сюжет и элементы сюжетной композиции</li>
                                    <li>Размер стиха, способы рифмовки</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Литературоведческие термины</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Литературные направления</li>
                                    <li>Компоненты художественного мира</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Биография</td>
                            <td>Биографические факты</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Факты биографий писателей. История создания произведений</li>
                                    <li>Вклад в развитие литературы</li>
                                    <li>Историческая обстановка, характер эпохи</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Литературная критика</td>
                            <td>Критика</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Название критических статей. Авторы  критических статей</li>
                                    <li>Ключевые идеи критических статей. Цитаты</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="2" class="text-center">4</td>
                            <td rowspan="2">Роль эпизодов</td>
                            <td>Роль эпизодов (сцен) в развитии темы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Место эпизода в произведении. Значение эпизода в развитии темы и идеи</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Идеи, характеры в эпическом и драматическом произведении, мотивы и образы в лирическом произведении</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Основные темы и идеи в эпических произведениях</li>
                                    <li>Основные темы и мотивы в лирических произведениях</li>
                                    <li>Особенности конфликта в драматических произведениях</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Сквозные темы</td>
                            <td>Сквозные темы в группе произведений</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Тема «маленького человека»</li>
                                    <li>Тема «лишних людей»</li>
                                    <li>Конфликт «отцов и детей»</li>
                                    <li>Военная тема</li>
                                    <li>Тема родины</li>
                                    <li>Тема города и деревни</li>
                                    <li>Философская тема</li>
                                    <li>Тема человека и природы</li>
                                    <li>Тема любви</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">6</td>
                            <td>Содержание произведений</td>
                            <td>Содержание произведений</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Название произведения. Автор произведения</li>
                                    <li>Герои произведения. Система образов-персонажей</li>
                                    <li>Основные события произведения</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.12</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9559: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Человек. Общество. Право» на русском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Человек. Общество. Право», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: емес);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.9.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.10.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.11.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Человек</td>
                            <td>Человек в мире</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Проблема человека. Человек и взаимоотношение людей. Свобода, необходимость и ответственность в человеческой деятельности </li>
                                    <li>Человек и культура. Человек и его мировоззрение. Познавательное отношение человека к миру</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="3" class="text-center">2</td>
                            <td rowspan="3">Общество</td>
                            <td>Социальная сфера</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Понятие общества</li>
                                    <li>Личность и общество</li>
                                    <li>Современное общество</li>
                                    <li>Общество как социальная система</li>
                                    <li>Социальная структура общества</li>
                                    <li>Социальные отношения</li>
                                    <li>Что такое социология</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Экономическая сфера</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Экономическая жизнь общества</li>
                                    <li>Экономическое поведение рыночных субъектов</li>
                                    <li>Что такое экономическая теория</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Духовная сфера</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Духовная жизнь человека</li>
                                    <li>Духовная культура</li>
                                    <li>Что такое философия</li>
                                    <li>Философская антропология</li>
                                    <li>Философия естествознания</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="3" class="text-center">3</td>
                            <td rowspan="3">Политика и право</td>
                            <td>Основы политологии (или Политика)</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Политическая жизнь общества</li>
                                    <li>Политическая система</li>
                                    <li>Что такое политология</li>
                                    <li>Культура и политика</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Конституционное право</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Конституция – основной закон РК</li>
                                    <li>Права и обязанности человека и гражданина</li>
                                    <li>РК – правовое государство</li>
                                    <li>Механизм правового регулирования</li>
                                    <li>Законность и правопорядок</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Введение в юриспруденцию</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Понятие права и основных правовых явлений</li>
                                    <li>Основные понятия базовых отраслей Казахстанского права</li>
                                    <li>Основные отрасли частного права</li>
                                    <li>Основные отрасли публичного права</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
}
SPECIFICATION_XX_TEST_TEXTS = {
    9543: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для учащихся 6 классов общеобразовательных школ – претендентов в Интеллектуальные школы, по предмету <strong>«Английский язык»</strong> с выбором одного правильного ответа из 4 предложенных вариантов.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском или казахском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые задания должны соответствовать учебным программам по предмету «Английский язык» для 5-6 классов уровня основного среднего образования, разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития учащихся 6-х классов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Задачей тестовых вопросов должна являться оценка навыков понимания прочитанного текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тестовые вопросы должны быть поделены на три типа:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.1.</span>Тестовые вопросы на <strong>значение (meaning)</strong> – слова, предложения, абзацы, основная идея текста, значение важных элементов текста;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.2.</span>Тестовые вопросы на <strong>структуру (structure)</strong> – ссылки, отношения между элементами (синтаксис), умение выделять части текста и определять связь между частями текста (структурой текста);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.3.</span>Тестовые вопросы на <strong>коммуникацию (communication)</strong> – умения делать выводы основываясь на мнение, цель, чувства и позицию автора текста.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.7.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.8.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: <u><strong>not</strong></u>);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по внесению тестовых вопросов на Веб-сайт:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Указывается ФИО Разработчика;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.2.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.3.</span>Указывается общий раздел контекста (человек, животные, природа и т.д.);</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.4.</span>Указывается тип тестовых вопросов по таксономии Блума (значение/коммуникация/структура).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.1.</span>К одному тексту может быть 1/3/5 тестовых вопросов.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.2.</span>Один вариант должен содержать 20 тестовых вопросов и 10 текстов:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="75%" class="text-center" colspan="3">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <th width="25%" class="text-center"></th>
                            <th width="25%" class="text-center">Значение</th>
                            <th width="25%" class="text-center">Коммуникация</th>
                            <th width="25%" class="text-center">Структура</th>
                        </tr>
                        <tr>
                            <td>Текст 1</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 3</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 4</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 5</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 6</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 7</td>
                            <td class="text-center">2</td>
                            <td class="text-center">1</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 8</td>
                            <td class="text-center">1</td>
                            <td class="text-center">2</td>
                            <td class="text-center"></td>
                        </tr>
                        <tr>
                            <td>Текст 9</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                        <tr>
                            <td>Текст 10</td>
                            <td class="text-center">3</td>
                            <td class="text-center">1</td>
                            <td class="text-center">1</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td class="text-right"><strong>Итого:</strong></td>
                            <td class="text-center" colspan="3"><strong>20</strong></td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">9.3.</span>Один вариант должен содержать 20 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th width="50%" class="text-center">Предполагаемый уровень сложности</th>
                            <th width="25%" class="text-center">%</th>
                            <th width="25%" class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">50</td>
                            <td class="text-center">10</td>
                        </tr>
                        <tr>
                            <td>Сложный</td>
                            <td class="text-center">25</td>
                            <td class="text-center">5</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">10.</span>Образцы тестовых заданий по предмету <a target="_blank" href="http://nis.edu.kz/site/nis/repository/file/Selection%20test_SAMPLES/1%20%D0%B4%D0%B5%D0%BD%D1%8C_%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D1%86%D1%8B%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_7%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81_RU.pdf">«Английский язык»</a>.</p>
        """,
    },
    9554: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Английский язык» на английском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Английский язык», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития поступающих в высшие учебные заведения Республики Казахстан;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: not);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.9.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.10.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.11.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td rowspan="3" class="text-center">1</td>
                            <td rowspan="3">Лексика и орфография</td>
                            <td>Синонимы, антонимы</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Синонимы, антонимы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Сочетаемость лексических единиц</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Лексика разговорных тем, орфография, фонетика</li>
                                    <li>Перефразирование, перевод</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Устойчивые выражения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Фразовые глаголы</li>
                                    <li>Идиомы. Пословицы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td rowspan="3" class="text-center">2</td>
                            <td rowspan="3">Морфология</td>
                            <td>Артикли, предлоги</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Артикли, предлоги</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Словообразование</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Приставки, суффиксы, окончания, сложные слова</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Части речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Имя существительное. Категория числа существительного. Притяжательная форма существительного</li>
                                    <li>Местоимение: личные, притяжательные, возвратные, указательные, неопределенные и отрицательные, вопросительные и относительные</li>
                                    <li>Имя прилагательное и наречие. Степени сравнения</li>
                                    <li>Имя числительное. Порядковые и количественные</li>
                                    <li>Глагол. Основные формы глагола: 'to be', Indefinite Tense (present, past, future), Continuous Tense (present, past, future), Perfect Tense (present, past, future), Future in the past, Passive Voice. Модальные глаголы</li>
                                    <li>Неличные формы глагола: Gerund, Participle I, II, Infinitive</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Синтаксис</td>
                            <td>Предложения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Предложения: простые, вопросительные и отрицательные. Порядок слов в предложении</li>
                                    <li>Прямая и косвенная речь. Согласование времен</li>
                                    <li>Наклонения: повелительное, сослагательное и условное</li>
                                    <li>Complex Object. Complex Subject</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Работа с текстом</td>
                            <td>Работа с текстом</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Работа с текстом</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Страноведение</td>
                            <td>Страноведение</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Казахстан</li>
                                    <li>Великобритания, англоязычные страны</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.12.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9555: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Французский язык» на французском языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Французский язык», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития поступающих в высшие учебные заведения Республики Казахстан;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.6.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: ne pas);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.9.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.10.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.11.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td rowspan="7" class="text-center">1</td>
                            <td rowspan="7">Морфология</td>
                            <td>Глагол</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Глагол. Present, Imparfait, Passe simple, futur simple, Passe compose. Plus-que-parfait. Future immediat. Passe immediat. Отрицательная форма глагола. Пассивная форма глагола. Инфинитив. Местоименные глаголы</li>
                                    <li>Причастие (Participe present, Participe passe). Деепричастие (Gerondif)</li>
                                    <li>Порядок слов в повелительном предложении. Условное наклонение Conditionnel. Сослагательное наклонение Subjonctif. Согласование времен в сложноподчиненных предложениях</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Прилагательные</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Род имен, число имен прилагательных</li>
                                    <li>Указательные, притяжательные, вопросительные прилагательные</li>
                                    <li>Степени сравнения прилагательных</li>
                                    <li>Место прилагательного-определения</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Существительное</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Род имен, число имен существительных</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Служебные части речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Артикли: определенный, неопределенный, слитный. Частичный артикль. Предлоги. Употребление предлогов. Управление глаголов. Союзы.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Числительные</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Количественные, порядковые числительные</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Местоимения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Местоимение-дополнения. Относительные, притяжательные, указательные местоимения. Неопределенно-личное местоимение «on». Самостоятельные личные, адвербиальные, вопросительные местоимения</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Наречие</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Образование наречии, степени сравнения наречия</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Лексика, перевод, фонетика</td>
                            <td>Лексика, перевод, фонетика</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Лексика, перевод, фонетика</li>
                                    <li>Словообразовательные элементы: суффиксы существительных, прилагательных, наречий</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Синтаксис</td>
                            <td>Предложения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Порядок слов в повествовательном и вопросительном предложениях. Постановка общего, специального, альтернативного вопроса. Косвенная речь</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Страноведение</td>
                            <td>Страноведение</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Франция, франкоговорящие страны</li>
                                    <li>Казахстан</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Работа с текстом</td>
                            <td>Работа с текстом</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Работа с текстом</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.12.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9556: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.</span>Разработать тестовые вопросы для определения уровня подготовленности абитуриентов по предмету «Немецкий язык» на немецком языке с целью приема в высшие учебные заведения Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.</span>Предоставить комментарий/рекомендаций пошагового определения правильного ответа к каждому тестовому вопросу для работы над ошибками на русском языке.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.</span>Все тестовые вопросы должны соответствовать учебной программе для общеобразовательной школы по предмету «Немецкий язык», разработанного в соответствии с государственным общеобязательным стандартом образования Республики Казахстан.</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.</span>Тестовые вопросы НЕ должны принадлежать интеллектуальной собственности государственных казенных предприятий и других структур Министерства образования и науки Республики Казахстан, автономных организаций образования, других юридических и физически лиц. Тестовые вопросы должны быть защищены от несанкционированного просмотра, скачивания, копирования и дальнейшего использования третьими лицами.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.</span>Требования к составлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1.</span>В вопросах должны отсутствовать орфографические ошибки и ошибки на пунктуацию;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2.</span>В формулировке тестовых вопросов, ответах и неправильных вариантах ответов (дистракторы) должны отсутствовать прямые или косвенные подсказки, сленг, жаргонные фразы;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.3.</span>Дистракторы должны быть составлены с учетом предполагаемых ошибочных рассуждений тестируемого, которые могут привести к данным вариантам ответов;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.4.</span>Недопустимы варианты ответов: «все вышеперечисленное верно», «все указанные ответы неверны», и т.п.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.5.</span>Тестовые вопросы не должны содержать лишней информации, взаимоисключающих вариантов ответов, двойного отрицания;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.6.</span>Тестовые вопросы должны быть представлены в форме краткого, грамотно сформулированного логического высказывания, исключающего неоднозначность заключения тестируемого.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.</span>Требования к составлению текстов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1.</span>Тексты должны быть аутентичными или основываться на аутентичном материале;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.2.</span>Тематика текстов должна соответствовать опыту, интересам и уровню развития поступающих в высшие учебные заведения Республики Казахстан;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.3.</span>Тексты могут содержать иллюстраций, примеры и прочие формы дублирования (с указанием источника);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.4.</span>При адаптации дублированных текстов также указывается источник со ссылкой "отредактировано/изменено";</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.5.</span>Тексты должны в основном содержать широко употребляемые слова;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.6.</span>У текстов должна быть четкая структура, информация скрытой, предложения сложными;</p>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.7.</span>Содержание текста должно быть актуальным (как минимум на несколько лет), информативным и занимательным на разные темы (избегайте деликатных тем).</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.</span>Требования по оформлению тестовых вопросов:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1.</span>Текст вопроса выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2.</span>Слова отрицания в вопросе выделяются жирным шрифтом и подчеркиваются (пример: nicht);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.3.</span>Слова из текста в вопросе выделены кавычками;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.4.</span>Текст варианта ответов в виде предложения начинаются с заглавной буквы. В конце ставится точка;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.5.</span>Текст варианта ответов в виде слов или словосочетаний начинается с маленькой буквы без точки в конце;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.6.</span>Повторяющееся слово в начале каждого варианта ответов выносится до вариантов ответов (после вопроса);</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.7.</span>Многоточие, обозначающие пропущенные слова или словосочетание, в тексте выделяется жирным шрифтом;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.8.</span>Свободные места, обозначающие пропущенные слова или словосочетание, в тексте подчеркиваются.</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.9.</span>Загружаемые рисунки должны иметь формат не менее 600 х 400 точек на дюйм;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.10.</span>Указывается предполагаемая сложность (легкий/средний/сложный) каждого тестового вопроса;</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.11.</span>Указывается общая тема для каждого тестового вопроса:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Раздел</th>
                            <th class="text-center">Тема</th>
                            <th class="text-center">Подтема</th>
                        </tr>
                        <tr>
                            <td rowspan="8" class="text-center">1</td>
                            <td rowspan="8">Морфология</td>
                            <td>Глагол</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Глагол. Основные формы глагола: сильные, слабые, особая группа. Временные формы действительного залога: Praesens, Praeteritum, Perfekt, Plusquamperfekt, Futurum. Временные формы страдательного залога: Praesens, Praeteritum, Perfekt, Plusquamperfekt, Futurum. Вспомогательные глаголы.</li>
                                    <li>Повелительное наклонение. Партицип I, II: в качестве определения, обстоятельства, в качестве согласованного определения.</li>
                                    <li>Инфинитивные группы: глагольные сочетания haben/sein + Infinitiv, um…zu + Infinitiv, ohne…zu + Infinitiv, anstatt…zu + Infinitiv. Сослогательное наклонение.</li>
                                    <li>Управление глаголов: с зависимым винительным падежом, с зависимым дательным падежом, с двумя дополнениями в разных падежах</li>
                                    <li>Модальные глаголы</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Служебные части речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Артикль. Употребление определенного/неопределенного артикля, отсутствие артикля. Вопросительные слова. Предлоги. Дательного, винительного падежа, предлоги, управляющие дательным и винительным падежами.</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Существительное</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Существительные  мужского, женского, среднего родов. Множественное число имен существительных. Склонение имен существительных: сильное, слабое, женское склонение существительных во множественном числе</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Прилагательное и наречие</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Склонение имен прилагательных: сильное, слабое склонение, склонение прилагательных после неопределенного артикля, притяжательных местоимений, отрицательного местоимения kein/e, степени сравнения прилагательных и наречий</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Местоимения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Личные, притяжательные, указательные, отрицательные, относительные местоимения, возвратное местоимение sich, безличное местоимение es и неопределенно-личное местоимение man</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Числительные</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Количественные, порядковые, составные числительные</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Словообразование</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Приставки, суффиксы, окончания, сложные слова</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td>Части речи</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Имя существительное. Категория числа существительного. Притяжательная форма существительного</li>
                                    <li>Местоимение: личные, притяжательные, возвратные, указательные, неопределенные и отрицательные, вопросительные и относительные</li>
                                    <li>Имя прилагательное и наречие. Степени сравнения</li>
                                    <li>Имя числительное. Порядковые и количественные</li>
                                    <li>Глагол. Основные формы глагола: 'to be', Indefinite Tense (present, past, future), Continuous Tense (present, past, future), Perfect Tense (present, past, future), Future in the past, Passive Voice. Модальные глаголы</li>
                                    <li>Неличные формы глагола: Gerund, Participle I, II, Infinitive</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Синтаксис</td>
                            <td>Предложения</td>
                            <td>
                                <ul class="list-normal">
                                    <li>Порядок слов в предложении</li>
                                    <li>Сложноподчиненные предложения, сложноподчиненные предложения</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">3</td>
                            <td>Лексика и перевод</td>
                            <td></td>
                            <td>
                                <ul class="list-normal">
                                    <li>Лексика и перевод</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">4</td>
                            <td>Работа с текстом</td>
                            <td></td>
                            <td>
                                <ul class="list-normal">
                                    <li>Работа с текстом</li>
                                    <li>Микродиалог</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="text-center">5</td>
                            <td>Страноведение</td>
                            <td></td>
                            <td>
                                <ul class="list-normal">
                                    <li>Казахстан</li>
                                    <li>Германия, немецкоговорящие страны</li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.12.</span>Указывается цель оценивания тестовых вопросов по таксономии Блума:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">#</th>
                            <th class="text-center">Цели оценивания</th>
                        </tr>
                        <tr>
                            <td class="text-center">1</td>
                            <td>Знание</td>
                        </tr>
                        <tr>
                            <td class="text-center">2</td>
                            <td>Применение</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.</span>Требования по формированию вариантов теста:</p>
            <p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1.</span>Один вариант должен содержать 30 тестовых вопросов с разделением на предполагаемый уровень сложности:</p>
            <div class="table-responsive">
                <table class="table table-bordered table-condensed mt-5 mb-10">
                    <tbody>
                        <tr>
                            <th class="text-center">Предполагаемый уровень сложности</th>
                            <th class="text-center">Количество тестовых вопросов</th>
                        </tr>
                        <tr>
                            <td>Высокий</td>
                            <td class="text-center">7</td>
                        </tr>
                        <tr>
                            <td>Средний</td>
                            <td class="text-center">8</td>
                        </tr>
                        <tr>
                            <td>Легкий</td>
                            <td class="text-center">15</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.2.</span>Один вариант должен содержать 20 тестовых вопросов с выбором одного правильного ответа из 5 предложенных и 10 тестовых вопросов с выбором одного или нескольких правильных ответов из 5 – 8 предложенных.</p>
        """,
    },
    9560: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-center text-normal mb-10">Тестовую спецификацию вы сможете найти в <a href="https://admissions.nu.edu.kz/wps/wcm/connect/7832d3ca-5c62-4d5e-81f1-adfba0e7b325/List+of+topics-Mathematics.pdf?MOD=AJPERES" target="_blank">nu.edu.kz</a>.</p>
        """,
    },
    9561: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-center text-normal mb-10">Тестовую спецификацию вы сможете найти в <a href="https://admissions.nu.edu.kz/wps/wcm/connect/2df8c78c-b78e-4943-8f18-f5ac56643003/List+of+topics-Physics.pdf?MOD=AJPERES" target="_blank">nu.edu.kz</a>.</p>
        """,
    },
    9562: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-center text-normal mb-10">Тестовую спецификацию вы сможете найти в <a href="https://admissions.nu.edu.kz/wps/wcm/connect/8540ed2c-3f8b-4d76-b08c-4a4388e51b5f/List+of+topics-Biology.pdf?MOD=AJPERES" target="_blank">nu.edu.kz (Biology)</a> и <a href="https://admissions.nu.edu.kz/wps/wcm/connect/4182627e-f01e-47f2-b6bf-06abed6477cd/List+of+topics-Chemistry.pdf?MOD=AJPERES" target="_blank">nu.edu.kz (Chemistry)</a>.</p>
        """,
    },
    9563: {
        settings.BB_LANGUAGE_CODE_KK: """
        """,
        settings.BB_LANGUAGE_CODE_RU: """
            <h6 class="text-center">ТРЕБОВАНИЯ К СОДЕРЖАНИЮ РАБОТ</h6>
            <p class="text-center text-normal mb-10">Тестовую спецификацию вы сможете найти в <a href="https://admissions.nu.edu.kz/wps/wcm/connect/b2e91b2c-cdd1-4f7b-a881-50072b0e53ab/List+of+topics-Thinking+Skills.pdf?MOD=AJPERES" target="_blank">nu.edu.kz</a>.</p>
        """,
    },
}

SPECIFICATION_KK_TEST_TEXTS[9540][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9540][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9540][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9540][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9540][settings.BB_LANGUAGE_CODE_RU] = SPECIFICATION_KK_TEST_TEXTS[9540][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9541][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9541][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9541][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9541][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9542][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9542][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9542][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9542][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_XX_TEST_TEXTS[9543][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_XX_TEST_TEXTS[9543][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9544][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9544][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9544][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9544][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9544][settings.BB_LANGUAGE_CODE_RU] = SPECIFICATION_KK_TEST_TEXTS[9544][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9545][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9545][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9545][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9545][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9546][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9546][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9546][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9546][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9547][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9547][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9547][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9547][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9548][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9548][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9548][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9548][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9549][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9549][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9549][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9549][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9550][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9550][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9550][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9550][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9551][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9551][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9551][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9551][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9552][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9552][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9552][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9552][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9553][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9553][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9553][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9553][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_XX_TEST_TEXTS[9554][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_XX_TEST_TEXTS[9554][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_XX_TEST_TEXTS[9555][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_XX_TEST_TEXTS[9555][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_XX_TEST_TEXTS[9556][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_XX_TEST_TEXTS[9556][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9557][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9557][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9557][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9557][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9558][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9558][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9558][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9558][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_KK_TEST_TEXTS[9559][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_KK_TEST_TEXTS[9559][settings.BB_LANGUAGE_CODE_RU]
SPECIFICATION_RU_TEST_TEXTS[9559][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_RU_TEST_TEXTS[9559][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_XX_TEST_TEXTS[9560][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_XX_TEST_TEXTS[9560][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_XX_TEST_TEXTS[9561][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_XX_TEST_TEXTS[9561][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_XX_TEST_TEXTS[9562][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_XX_TEST_TEXTS[9562][settings.BB_LANGUAGE_CODE_RU]

SPECIFICATION_XX_TEST_TEXTS[9563][settings.BB_LANGUAGE_CODE_KK] = SPECIFICATION_XX_TEST_TEXTS[9563][settings.BB_LANGUAGE_CODE_RU]

def test_specification(test_section, test_language, language):
    try:
        container = None
        if test_section.pk in SPECIFICATION_XX_TEST_TEXTS.keys():
            container = SPECIFICATION_XX_TEST_TEXTS
        else:
            if test_language == Test.LANGUAGE_KK:
                container = SPECIFICATION_KK_TEST_TEXTS
            else:
                container = SPECIFICATION_RU_TEST_TEXTS
        return container[test_section.pk][language]
    except KeyError:
        pass
    return ""
