from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import get_language
from bbtest.auth.mixins import DeveloperLoginRequiredMixin
from bbtest.forms.acknowledgement import DeveloperAcknowledgementForm
from bbtest.models import DeveloperAcknowledgement
from .mixins import DeveloperUnacceptedAcknowledgementRequiredMixin


AGREEMENT_TEXTS = {
    "plan_a": {
        "kk": "",
        "ru": """
<h6 class="text-center">1. ОБЩИЕ ПОЛОЖЕНИЯ</h6>
<p class="text-justify text-normal mb-10">1.1 Настоящая публичная оферта является официальным предложением ТОО «BBMINDS», БИН 171040002110 (далее – Заказчик) заключить договор по разработке тестовых вопросов для пробного тестирования (далее – Оферта) на сайте www.bbtest.kz (далее – Веб-сайт) с любыми совершеннолетними лицами, которые подтвердили свое полное и безоговорочное согласие с условиями настоящей Оферты, зарегистрировались на Веб-сайте и получили доступ к личному кабинету, путем заполнения анкеты Заказчика (далее – Разработчик).</p>
<p class="text-justify text-normal mb-10">В соответствии со статьями 395 – 399 Гражданского кодекса Республики Казахстан, принятие и подтверждение Разработчиком своего полного и безоговорочного согласия с условиями настоящей Оферты равносильно заключению договора публичной оферты (далее – Договор) на условиях, изложенных в настоящем документе.</p>
<p class="text-justify text-normal mb-10">В СВЯЗИ С ВЫШЕИЗЛОЖЕННЫМ, ВНИМАТЕЛЬНО ОЗНАКОМЬТЕСЬ С ТЕКСТОМ НАСТОЯЩЕГО ДОКУМЕНТА. ЕСЛИ ВЫ НЕ СОГЛАСНЫ С КАКИМ-ЛИБО ПУНКТОМ ОФЕРТЫ, ЗАКАЗЧИК ПРЕДЛАГАЕТ ВАМ ОТКАЗАТЬСЯ ОТ РЕГИСТРАЦИИ НА ВЕБ-САЙТЕ.</p>
<p class="text-justify text-normal mb-10">1.2 Оферта считается принятой Разработчиком полностью и безоговорочно и договор заключенным между Заказчиком и Разработчиком, совместно именуемыми Сторонами с момента выполнения Разработчиком совокупности следующих действий:<br>1) Регистрация на Веб-сайте путем заполнения личных данных;<br>2) Отправка тестовых вопросов на рассмотрение Заказчику через Веб-сайт.</p>

<h6 class="text-center">2. ПРЕДМЕТ ДОГОВОРА</h6>
<p class="text-justify text-normal mb-0">2.1 По настоящему Договору Разработчик обязуется оказать услуги по разработке тестовых вопросов для пробного тестирования на Веб-сайте (далее – Услуги), а Заказчик оплатить Услуги в соответствии с условиями настоящего Договора.</p>
<p class="text-justify text-normal mb-0">2.2 Услуги считаются оказанными после проведения Заказчиком проверки содержания тестовых вопросов на соответствие тестовой спецификации по предмету/разделу пробного тестирования, находящейся на Веб-сайте, (далее – Экспертиза).</p>
<p class="text-justify text-normal mb-10">2.3 Сроки проведения Проверки устанавливает Заказчик. Сроки завершения Проверки не должны превышать 3 месяцев со дня отправки Разработчиком последнего тестового вопроса.</p>

<h6 class="text-center">3. СТОИМОСТЬ ДОГОВОРА И ПОРЯДОК ОПЛАТЫ</h6>
<p class="text-justify text-normal mb-0">3.1 Согласно условиям настоящего Договора Заказчик обязуется оплатить 300 (триста) тенге за 1 (один) тестовый вопрос, прошедшего экспертизу Заказчика.</p>
<p class="text-justify text-normal mb-0">3.2 Стоимость Договора не включает в себя налог на добавленную стоимость.</p>
<p class="text-justify text-normal mb-0">3.3 Оплата за осуществление Услуг производится путем перечисления денежных средств на банковский счет Разработчика, указанного при регистрации на Веб-сайте.</p>
<p class="text-justify text-normal mb-0">3.4 Оплата за осуществление Услуг производится только в безналичной форме. Любые банковские комиссии при получении оплаты от Заказчика оплачиваются Разработчиком за свой счет.</p>
<p class="text-justify text-normal mb-10">3.5 Сроки оплаты за осуществление Услуг устанавливает Заказчик.</p>

<h6 class="text-center">4. ОБЯЗАННОСТИ СТОРОН</h6>
<p class="text-justify text-normal mb-0">4.1 Заказчик обязуется:</p>
<p class="text-justify text-normal mb-0">4.1.1 Оплатить Услуги в соответствии с условиями настоящего Договора;</p>
<p class="text-justify text-normal mb-0">4.1.2 Не разглашать и не передавать третьим лицам сведения о Разработчике;</p>
<p class="text-justify text-normal mb-0">4.1.3 Оповестить Разработчика о любых изменениях в условиях настоящего Договора путем опубликования на Веб-сайте.</p>
<p class="text-justify text-normal mb-0">4.2 Разработчик обязуется:</p>
<p class="text-justify text-normal mb-0">4.2.1 Предоставить достоверную информацию о себе в личном кабинете Веб-сайта;</p>
<p class="text-justify text-normal mb-0">4.2.2 Предоставить Заказчику копии документов, подтверждающих специальные знания и профессиональные навыки Разработчика, для предоставления Услуг;</p>
<p class="text-justify text-normal mb-0">4.2.3 Соблюдать Законы РК при предоставлении Услуг;</p>
<p class="text-justify text-normal mb-0">4.2.4 Не нарушать авторское право третьих лиц при предоставлении Услуг в том числе не копировать тестовые вопросы и/или тексты с официальных источников организаций образования;</p>
<p class="text-justify text-normal mb-0">4.2.5 Качественно предоставить Услуги Заказчику согласно техническому заданию (Приложение);</p>
<p class="text-justify text-normal mb-10">4.2.6 Передать авторские права на предоставляемые Услуги Заказчику.</p>

<h6 class="text-center">5. ОТВЕТСТВЕННОСТЬ СТОРОН И ПОРЯДОК РАЗРЕШЕНИЯ СПОРОВ</h6>
<p class="text-justify text-normal mb-0">5.1 Заказчик несет полную ответственность за достоверность данных указанных в заявке на участие в пробном тестировании.</p>
<p class="text-justify text-normal mb-0">5.2 За исключением обстоятельств непреодолимой силы (форс-мажор) за неисполнение или ненадлежащее исполнение обязательств по настоящему Договору Стороны несут ответственность в соответствии с действующим законодательством Республики Казахстан.</p>
<p class="text-justify text-normal mb-10">5.3 Споры и разногласия, которые могут возникать при исполнении настоящего Договора, будут по возможности разрешаться путем переговоров между Сторонами.</p>

<h6 class="text-center">6. ФОРС-МАЖОР</h6>
<p class="text-justify text-normal mb-0">6.1 Стороны не несут ответственность за неисполнение условий Договора, если оно явилось результатом форс-мажорных обстоятельств.</p>
<p class="text-justify text-normal mb-10">6.2 «Форс-мажор» означает событие, неподвластное контролю Сторон, и имеющее непредвиденный характер. Такие события могут включать: военные действия, природные или стихийные бедствия и другие.</p>

<h6 class="text-center">7. ПРОЧИЕ УСЛОВИЯ</h6>
<p class="text-justify text-normal mb-0">7.1 Договор вступает в силу с момента принятия настоящей Оферты Разработчиком путем регистрации на Веб-сайте и действует до полного его исполнения Сторонами своих обязательств.</p>
<p class="text-justify text-normal mb-0">7.2 Разработчик не вправе привлекать для выполнения своих обязательств по Договору третьих лиц без согласования с Заказчиком.</p>
<p class="text-justify text-normal mb-10">7.3 В случае возникновения вопросов Разработчик вправе обратиться к Заказчику через Веб-сайт.</p>

<h6 class="text-center">8. ЗАКЛЮЧИТЕЛЬНЫЕ ПОЛОЖЕНИЯ</h6>
<p class="text-justify text-normal mb-0">8.1 Настоящая Оферта вступает в силу с момента регистрации Разработчика на Веб-сайте и действует до оказания Услуг Разработчиком.</p>
<p class="text-justify text-normal mb-0">8.2 Заказчик оставляет за собой право внести изменения в условия настоящей Оферты или отозвать Оферту в любой момент по своему усмотрению. Датой вступления в силу изменений настоящей Оферты является дата опубликования на Веб-сайте Оферты или информации об отзыве Оферты.</p>
<p class="text-justify text-normal mb-0">8.3 Принимая условия настоящей Оферты путем ее акцепта, Заказчик подтверждает, что заключает Договор добровольно и соглашается со всеми условиями, изложенными в Оферте.</p>
<p class="text-justify text-normal mb-10">8.4 Настоящая Оферта составлена в единственном экземпляре и опубликована на Веб-сайте.</p>
        """,
    },
    "plan_b": {
        "kk": "",
        "ru": "",
    },
    "plan_c": {
        "kk": "",
        "ru": "",
    },
}

class AcknowledgementView(DeveloperLoginRequiredMixin, DeveloperUnacceptedAcknowledgementRequiredMixin, FormView):
    template_name = "developer/acknowledgement.html"
    form_class = DeveloperAcknowledgementForm
    success_url = reverse_lazy("bbtest:developer_tests")
    accepted_acknowledgement_redirect_urlpattern = "bbtest:developer_tests"

    def get_context_data(self, **kwargs):
        kwargs["plan_a"] = {
            "name": DeveloperAcknowledgement.PLANS[0][1],
            "value": DeveloperAcknowledgement.PLANS[0][0],
            "agreement_text": AGREEMENT_TEXTS["plan_a"][get_language()],
            "agreement_code": DeveloperAcknowledgement.AGREEMENT_CODES_FOR_PLANS[DeveloperAcknowledgement.PLAN_A],
        }
        kwargs["plan_b"] = {
            "name": DeveloperAcknowledgement.PLANS[1][1],
            "value": DeveloperAcknowledgement.PLANS[1][0],
            "agreement_text": AGREEMENT_TEXTS["plan_b"][get_language()],
            "agreement_code": DeveloperAcknowledgement.AGREEMENT_CODES_FOR_PLANS[DeveloperAcknowledgement.PLAN_B],
        }
        kwargs["plan_c"] = {
            "name": DeveloperAcknowledgement.PLANS[2][1],
            "value": DeveloperAcknowledgement.PLANS[2][0],
            "agreement_text": AGREEMENT_TEXTS["plan_c"][get_language()],
            "agreement_code": DeveloperAcknowledgement.AGREEMENT_CODES_FOR_PLANS[DeveloperAcknowledgement.PLAN_C],
        }
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.make_acknowledgement(self.request)
        return super().form_valid(form)
