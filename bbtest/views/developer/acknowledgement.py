from django.urls import reverse_lazy
from django.utils.translation import get_language
from bbtest.auth.mixins import DeveloperPermissionRequiredMixin
from bbtest.views.generic import FormView, UserContextMixin
from bbtest.forms.acknowledgement import DeveloperAcknowledgementForm
from bbtest.models import DeveloperAcknowledgement
from .mixins import DeveloperUnacceptedAcknowledgementRequiredMixin


AGREEMENT_TEXTS = {
    "plan_a": {
        "kk": "",
        "ru": """
<h6 class="text-center">1. ОБЩИЕ ПОЛОЖЕНИЯ</h6>
<p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.1</span>Настоящая публичная оферта является официальным предложением ТОО «BBMINDS», БИН 171040002110 (далее – Заказчик) заключить договор по разработке тестовых вопросов для пробного тестирования (далее – Оферта) на сайте www.bbtest.kz (далее – Веб-сайт) с любыми совершеннолетними лицами, которые подтвердили свое полное и безоговорочное согласие с условиями настоящей Оферты, зарегистрировались на Веб-сайте и получили доступ к личному кабинету, путем заполнения анкеты Заказчика (далее – Разработчик).</p>
<p class="text-justify text-normal mb-10">В соответствии со статьями 395 – 399 Гражданского кодекса Республики Казахстан, принятие и подтверждение Разработчиком своего полного и безоговорочного согласия с условиями настоящей Оферты равносильно заключению договора публичной оферты (далее – Договор) на условиях, изложенных в настоящем документе.</p>
<p class="text-justify text-normal mb-10">В СВЯЗИ С ВЫШЕИЗЛОЖЕННЫМ, ВНИМАТЕЛЬНО ОЗНАКОМЬТЕСЬ С ТЕКСТОМ НАСТОЯЩЕГО ДОКУМЕНТА. ЕСЛИ ВЫ НЕ СОГЛАСНЫ С КАКИМ-ЛИБО ПУНКТОМ ОФЕРТЫ, ЗАКАЗЧИК ПРЕДЛАГАЕТ ВАМ ОТКАЗАТЬСЯ ОТ РЕГИСТРАЦИИ НА ВЕБ-САЙТЕ.</p>
<p class="text-justify text-normal mb-10"><span class="text-left mr-5">1.2</span>Оферта считается принятой Разработчиком полностью и безоговорочно и договор заключенным между Заказчиком и Разработчиком, совместно именуемыми Сторонами с момента выполнения Разработчиком совокупности следующих действий:<br>1) Регистрация на Веб-сайте путем заполнения личных данных;<br>2) Отправка тестовых вопросов на рассмотрение Заказчику через Веб-сайт.</p>

<h6 class="text-center">2. ПРЕДМЕТ ДОГОВОРА</h6>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">2.1</span>По настоящему Договору Разработчик обязуется оказать услуги по разработке тестовых вопросов для пробного тестирования на Веб-сайте (далее – Услуги), а Заказчик оплатить Услуги в соответствии с условиями настоящего Договора.</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">2.2</span>Услуги считаются оказанными после проведения Заказчиком проверки содержания тестовых вопросов на соответствие тестовой спецификации по предмету/разделу пробного тестирования, находящейся на Веб-сайте, (далее – Экспертиза).</p>
<p class="text-justify text-normal mb-10"><span class="text-left mr-5">2.3</span>Сроки проведения Проверки устанавливает Заказчик. Сроки завершения Проверки не должны превышать 3 месяцев со дня отправки Разработчиком последнего тестового вопроса.</p>

<h6 class="text-center">3. СТОИМОСТЬ ДОГОВОРА И ПОРЯДОК ОПЛАТЫ</h6>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">3.1</span>Согласно условиям настоящего Договора Заказчик обязуется оплатить 300 (триста) тенге за 1 (один) тестовый вопрос, прошедшего экспертизу Заказчика.</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">3.2</span>Стоимость Договора не включает в себя налог на добавленную стоимость.</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">3.3</span>Оплата за осуществление Услуг производится путем перечисления денежных средств на банковский счет Разработчика, указанного при регистрации на Веб-сайте.</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">3.4</span>Оплата за осуществление Услуг производится только в безналичной форме. Любые банковские комиссии при получении оплаты от Заказчика оплачиваются Разработчиком за свой счет.</p>
<p class="text-justify text-normal mb-10"><span class="text-left mr-5">3.5</span>Сроки оплаты за осуществление Услуг устанавливает Заказчик.</p>

<h6 class="text-center">4. ОБЯЗАННОСТИ СТОРОН</h6>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.1</span>Заказчик обязуется:</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.1.1</span>Оплатить Услуги в соответствии с условиями настоящего Договора;</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.1.2</span>Не разглашать и не передавать третьим лицам сведения о Разработчике;</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.1.3</span>Оповестить Разработчика о любых изменениях в условиях настоящего Договора путем опубликования на Веб-сайте.</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.2</span>Разработчик обязуется:</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.2.1</span>Предоставить достоверную информацию о себе в личном кабинете Веб-сайта;</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.2.2</span>Предоставить Заказчику копии документов, подтверждающих специальные знания и профессиональные навыки Разработчика, для предоставления Услуг;</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.2.3</span>Соблюдать Законы РК при предоставлении Услуг;</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.2.4</span>Не нарушать авторское право третьих лиц при предоставлении Услуг в том числе не копировать тестовые вопросы и/или тексты с официальных источников организаций образования;</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">4.2.5</span>Качественно предоставить Услуги Заказчику согласно техническому заданию (Приложение);</p>
<p class="text-justify text-normal mb-10"><span class="text-left mr-5">4.2.6</span>Передать авторские права на предоставляемые Услуги Заказчику.</p>

<h6 class="text-center">5. ОТВЕТСТВЕННОСТЬ СТОРОН И ПОРЯДОК РАЗРЕШЕНИЯ СПОРОВ</h6>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.1</span>Заказчик несет полную ответственность за достоверность данных указанных в заявке на участие в пробном тестировании.</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">5.2</span>За исключением обстоятельств непреодолимой силы (форс-мажор) за неисполнение или ненадлежащее исполнение обязательств по настоящему Договору Стороны несут ответственность в соответствии с действующим законодательством Республики Казахстан.</p>
<p class="text-justify text-normal mb-10"><span class="text-left mr-5">5.3</span>Споры и разногласия, которые могут возникать при исполнении настоящего Договора, будут по возможности разрешаться путем переговоров между Сторонами.</p>

<h6 class="text-center">6. ФОРС-МАЖОР</h6>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">6.1</span>Стороны не несут ответственность за неисполнение условий Договора, если оно явилось результатом форс-мажорных обстоятельств.</p>
<p class="text-justify text-normal mb-10"><span class="text-left mr-5">6.2</span>«Форс-мажор» означает событие, неподвластное контролю Сторон, и имеющее непредвиденный характер. Такие события могут включать: военные действия, природные или стихийные бедствия и другие.</p>

<h6 class="text-center">7. ПРОЧИЕ УСЛОВИЯ</h6>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.1</span>Договор вступает в силу с момента принятия настоящей Оферты Разработчиком путем регистрации на Веб-сайте и действует до полного его исполнения Сторонами своих обязательств.</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">7.2</span>Разработчик не вправе привлекать для выполнения своих обязательств по Договору третьих лиц без согласования с Заказчиком.</p>
<p class="text-justify text-normal mb-10"><span class="text-left mr-5">7.3</span>В случае возникновения вопросов Разработчик вправе обратиться к Заказчику через Веб-сайт.</p>

<h6 class="text-center">8. ЗАКЛЮЧИТЕЛЬНЫЕ ПОЛОЖЕНИЯ</h6>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.1</span>Настоящая Оферта вступает в силу с момента регистрации Разработчика на Веб-сайте и действует до оказания Услуг Разработчиком.</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.2</span>Заказчик оставляет за собой право внести изменения в условия настоящей Оферты или отозвать Оферту в любой момент по своему усмотрению. Датой вступления в силу изменений настоящей Оферты является дата опубликования на Веб-сайте Оферты или информации об отзыве Оферты.</p>
<p class="text-justify text-normal mb-0"><span class="text-left mr-5">8.3</span>Принимая условия настоящей Оферты путем ее акцепта, Заказчик подтверждает, что заключает Договор добровольно и соглашается со всеми условиями, изложенными в Оферте.</p>
<p class="text-justify text-normal mb-10"><span class="text-left mr-5">8.4</span>Настоящая Оферта составлена в единственном экземпляре и опубликована на Веб-сайте.</p>
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

class AcknowledgementView(DeveloperPermissionRequiredMixin, DeveloperUnacceptedAcknowledgementRequiredMixin, UserContextMixin, FormView):
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
