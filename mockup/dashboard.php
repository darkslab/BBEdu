<script src="js/jquery-ui.min.js"></script>
<script src="js/SVGChart.js"></script>
<script src="js/RadialChart.js"></script>
<script>
    $(function() {
        var chart = new RadialChart($("[data-dashboard-chart-0]"), 1, 10, {
            "stroke-width": 16,
            "circle-stroke": "#c7e7c8",
            "arc-stroke": "#4caf50"
        });
        chart.draw();
    });
</script>
<div class="row">
    <div class="col-xs-12">
        <div class="alert alert-dismissible alert-success">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <strong>Хорошие новости!</strong> Мы добавили <a href="<?php echo $base; ?>test.html" class="alert-link">8 новые варианты тестов</a>!
        </div>
    </div>
    <div class="col-xs-12 col-sm-4 col-md-5">
        <div class="bb-chart bb-chart-dashboard-0 mb-15" data-dashboard-chart-0>
            <div class="bb-chart-elem bb-chart-elem-dashboard-0 text-center">
                <p class="mb-0">Предметов пройдено!</p>
                <p class="mb-0">Вы можете пройти ещё 9.</p>
            </div>
        </div>
    </div>
    <div class="col-xs-12 col-sm-8 col-md-7">
        <div class="panel panel-primary">
            <div class="panel-heading"><strong>Результаты последнего теста</strong></div>
            <div class="panel-body">
                <div class="row">
                    <div class="col-xs-6">
                    </div>
                    <div class="col-xs-6">
                    </div>
                </div>

                <div class="table-responsive">
                    <table class="table table-hover mb-0">
                        <thead>
                            <tr>
                                <th>Раздел</th>
                                <th style="width: 25%;" class="text-center">Правильные</th>
                                <th style="width: 25%;" class="text-center">Неправильные</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Количественные характеристики</td>
                                <td class="text-center">5</td>
                                <td class="text-center">5</td>
                            </tr>
                            <tr>
                                <td>Развёртка поверхности</td>
                                <td class="text-center">6</td>
                                <td class="text-center">4</td>
                            </tr>
                            <tr class="danger">
                                <td>Поворот блоков</td>
                                <td class="text-center">1</td>
                                <td class="text-center">9</td>
                            </tr>
                            <tr class="success">
                                <td>Зрительная память: Вспоминание</td>
                                <td class="text-center">8</td>
                                <td class="text-center">2</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>
