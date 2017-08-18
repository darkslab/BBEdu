<script>
    $(function() {
        var selected_items = [];
        var selected_rows = [];
        var total = 0;
        var $summary_container = $("[data-summary-container]");
        var $summary_row = $summary_container.children("div");

        $summary_container.html("");

        $("[data-line-item]").click(function() {
            var item = $(this).data("line-item");
            var index = selected_items.indexOf(item);
            if (index != -1) {
                selected_items.splice(index, 1);
                $(this).removeClass("active");

                selected_rows[index].remove();
                selected_rows.splice(index, 1);

                total -= $(this).data("line-item-price");
            } else {
                selected_items.push(item);
                $(this).addClass("active");

                var row = $summary_row.clone();
                row.find("[data-summary=\"caption\"]").text($(this).data("line-item-caption"));
                row.find("[data-summary=\"amount\"]").html($(this).data("line-item-price") + " &#8376;");
                $summary_container.append(row);
                selected_rows.push(row);

                total += $(this).data("line-item-price");
            }

            $("[data-total-amount]").html(total + " &#8376;");
            if (total > 0) {
                $("[data-charge-button]").attr("disabled", false);
            } else {
                $("[data-charge-button]").attr("disabled", true);
            }
        });
    });
</script>
<div class="row">
    <div class="col-xs-12">
        <h3 class="mb-23 mt-0">Выберите тесты</h3>
    </div>

    <div class="col-xs-12">
        <div class="row">
            <div class="col-sm-8">
                <div class="list-group">
                    <a href="javascript:void(0);" class="list-group-item" data-line-item="0" data-line-item-caption="Математика" data-line-item-price="200">
                        <div class="row">
                            <div class="col-xs-8 col-sm-9">
                                <h4 class="list-group-item-heading">Математика</h4>
                                <p class="list-group-item-text">Тест проверяет математические знания в области Дробей, Функций, Арифметики, Комбинаторики и Геометрий.</p>
                                <p class="list-group-item-text mt-15">Количество вопросов: 30</p>
                                <p class="list-group-item-text">Время: 60 мин.</p>
                            </div>
                            <div class="col-xs-4 col-sm-3">
                                <h4 class="list-group-item-heading text-right">200 &#8376;</h4>
                                <h1 class="list-group-item-heading bb-list-group-heading-active text-right">
                                    <i class="fa fa-check-circle"></i>
                                </h1>
                            </div>
                        </div>
                    </a>
                    <a href="javascript:void(0);" class="list-group-item" data-line-item="1" data-line-item-caption="Казахский язык" data-line-item-price="150">
                        <div class="row">
                            <div class="col-xs-8 col-sm-9">
                                <h4 class="list-group-item-heading">Казахский язык</h4>
                                <p class="list-group-item-text">Sed eget turpis a pede tempor malesuada. Vivamus quis mi at leo pulvinar hendrerit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
                                <p class="list-group-item-text mt-15">Количество вопросов: 30</p>
                                <p class="list-group-item-text">Время: 60 мин.</p>
                            </div>
                            <div class="col-xs-4 col-sm-3">
                                <h4 class="list-group-item-heading text-right">150 &#8376;</h4>
                                <h1 class="list-group-item-heading bb-list-group-heading-active text-right">
                                    <i class="fa fa-check-circle"></i>
                                </h1>
                            </div>
                        </div>
                    </a>
                    <a href="javascript:void(0);" class="list-group-item" data-line-item="2" data-line-item-caption="Русский язык" data-line-item-price="150">
                        <div class="row">
                            <div class="col-xs-8 col-sm-9">
                                <h4 class="list-group-item-heading">Русский язык</h4>
                                <p class="list-group-item-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                                <p class="list-group-item-text mt-15">Количество вопросов: 30</p>
                                <p class="list-group-item-text">Время: 60 мин.</p>
                            </div>
                            <div class="col-xs-4 col-sm-3">
                                <h4 class="list-group-item-heading text-right">150 &#8376;</h4>
                                <h1 class="list-group-item-heading bb-list-group-heading-active text-right">
                                    <i class="fa fa-check-circle"></i>
                                </h1>
                            </div>
                        </div>
                    </a>
                    <a href="javascript:void(0);" class="list-group-item" data-line-item="3" data-line-item-caption="Английский язык" data-line-item-price="150">
                        <div class="row">
                            <div class="col-xs-8 col-sm-9">
                                <h4 class="list-group-item-heading">Английский язык</h4>
                                <p class="list-group-item-text">Donec dapibus orci sit amet elit. Maecenas rutrum ultrices lectus. Aliquam suscipit, lacus a iaculis adipiscing, eros orci pellentesque nisl, non pharetra dolor urna nec dolor.</p>
                                <p class="list-group-item-text mt-15">Количество вопросов: 30</p>
                                <p class="list-group-item-text">Время: 60 мин.</p>
                            </div>
                            <div class="col-xs-4 col-sm-3">
                                <h4 class="list-group-item-heading text-right">150 &#8376;</h4>
                                <h1 class="list-group-item-heading bb-list-group-heading-active text-right">
                                    <i class="fa fa-check-circle"></i>
                                </h1>
                            </div>
                        </div>
                    </a>
                    <a href="javascript:void(0);" class="list-group-item" data-line-item="4" data-line-item-caption="Количественные характеристики" data-line-item-price="250">
                        <div class="row">
                            <div class="col-xs-8 col-sm-9">
                                <h4 class="list-group-item-heading">Количественные характеристики</h4>
                                <p class="list-group-item-text">Nulla facilisi. Nunc volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut sit amet orci vel mauris blandit vehicula. Nullam quis enim. Integer dignissim viverra velit. Curabitur in odio. In hac habitasse platea dictumst.</p>
                                <p class="list-group-item-text mt-15">Количество вопросов: 30</p>
                                <p class="list-group-item-text">Время: 60 мин.</p>
                            </div>
                            <div class="col-xs-4 col-sm-3">
                                <h4 class="list-group-item-heading text-right">250 &#8376;</h4>
                                <h1 class="list-group-item-heading bb-list-group-heading-active text-right">
                                    <i class="fa fa-check-circle"></i>
                                </h1>
                            </div>
                        </div>
                    </a>
                    <a href="javascript:void(0);" class="list-group-item">
                        <div class="row">
                            <div class="col-xs-12">
                                <h4 class="list-group-item-heading">Поворот поверхностей</h4>
                                <p class="list-group-item-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at ante. Mauris eleifend, quam a vulputate dictum, massa quam dapibus leo, eget vulputate orci purus ut lorem. In fringilla mi in ligula. Pellentesque aliquam quam vel dolor. Nunc adipiscing. Sed quam odio, tempus ac, aliquam molestie, varius ac, tellus. Vestibulum ut nulla aliquam risus rutrum interdum.</p>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
            <div class="col-sm-4">
                <div class="panel panel-default">
                    <div class="panel-body">
                        <h5>Итого:</h5>
                        <div data-summary-container>
                            <div class="row">
                                <div class="col-xs-8">
                                    <h6 class="mt-10 mb-0" data-summary="caption"></h6>
                                </div>
                                <div class="col-xs-4 text-right">
                                    <h6 class="mt-10 mb-0">
                                        <span class="pull-left ml--15">&times;</span>
                                        <span data-summary="amount"></span>
                                    </h6>
                                </div>
                            </div>
                        </div>
                        <hr class="mt-15 mb-15" style="border-color: #ccc;">
                        <h4 class="text-right mt-0 mb-23" data-total-amount>0 &#8376;</h4>
                        <button type="button" class="btn btn-success btn-lg btn-block" disabled data-charge-button>Начать</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
