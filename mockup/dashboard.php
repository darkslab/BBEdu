<script src="js/jquery-ui.min.js"></script>
<script src="js/SVGChart.js"></script>
<script src="js/RadialChart.js"></script>
<script src="js/ColumnChart.js"></script>
<script>
    $(function() {
        (new RadialChart($("[data-dashboard-chart-0]"), 4, 10, {
            "line-width": 16,
            "circle-color": "#c7e7c8",
            "arc-color": "#4caf50"
        })).create();

        (new RadialChart($("[data-dashboard-table-chart-0]"), 378, 400, {
            "line-width": 2,
            "arc-color": "#3366cc",
            "font-size": 14
        })).create();
        (new RadialChart($("[data-dashboard-table-chart-avg-0]"), 356, 400, {
            "line-width": 2,
            "arc-color": "#aaaaaa",
            "font-size": 14
        })).create();

        (new RadialChart($("[data-dashboard-table-chart-1]"), 145, 200, {
            "line-width": 2,
            "arc-color": "#dc3912",
            "font-size": 14
        })).create();
        (new RadialChart($("[data-dashboard-table-chart-avg-1]"), 187, 200, {
            "line-width": 2,
            "arc-color": "#aaaaaa",
            "font-size": 14
        })).create();

        (new RadialChart($("[data-dashboard-table-chart-2]"), 128, 200, {
            "line-width": 2,
            "arc-color": "#ff9900",
            "font-size": 14
        })).create();
        (new RadialChart($("[data-dashboard-table-chart-avg-2]"), 167, 200, {
            "line-width": 2,
            "arc-color": "#aaaaaa",
            "font-size": 14
        })).create();

        (new RadialChart($("[data-dashboard-table-chart-3]"), 189, 200, {
            "line-width": 2,
            "arc-color": "#109618",
            "font-size": 14
        })).create();
        (new RadialChart($("[data-dashboard-table-chart-avg-3]"), 156, 200, {
            "line-width": 2,
            "arc-color": "#aaaaaa",
            "font-size": 14
        })).create();

        (new RadialChart($("[data-dashboard-table-chart-4]"), 56, 60, {
            "line-width": 2,
            "arc-color": "#990099",
            "font-size": 14
        })).create();
        (new RadialChart($("[data-dashboard-table-chart-avg-4]"), 50, 60, {
            "line-width": 2,
            "arc-color": "#aaaaaa",
            "font-size": 14
        })).create();

        (new RadialChart($("[data-dashboard-table-chart-total]"), 840, 1000, {
            "line-width": 4,
            "arc-color": "#444444",
            "font-size": 14,
            "font-weight": "bold"
        })).create();
        (new RadialChart($("[data-dashboard-table-chart-total-avg]"), 740, 1000, {
            "line-width": 4,
            "arc-color": "#aaaaaa",
            "font-size": 14,
            "font-weight": "bold"
        })).create();

        var charts = [];
        charts.push(new ColumnChart($("[data-dashboard-chart-1]"), [
            245,
            356,
            378,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ], 400, {
            "line-color": "#3366cc",
            "avg_value": 356,
            "line-width": 16,
            "font-size": 16
        }));
        charts.push(new ColumnChart($("[data-dashboard-chart-1]"), [
            98,
            136,
            145,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ], 200, {
            "line-color": "#dc3912",
            "avg_value": 187,
            "line-width": 16,
            "font-size": 16
        }));
        charts.push(new ColumnChart($("[data-dashboard-chart-1]"), [
            67,
            135,
            128,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ], 200, {
            "line-color": "#ff9900",
            "avg_value": 167,
            "line-width": 16,
            "font-size": 16
        }));
        charts.push(new ColumnChart($("[data-dashboard-chart-1]"), [
            181,
            178,
            189,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ], 200, {
            "line-color": "#109618",
            "avg_value": 156,
            "line-width": 16,
            "font-size": 16
        }));
        charts.push(new ColumnChart($("[data-dashboard-chart-1]"), [
            24,
            45,
            56,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ], 60, {
            "line-color": "#990099",
            "avg_value": 50,
            "line-width": 16,
            "font-size": 16
        }));

        var chart_index = 0;
        charts[chart_index].create();

        $("[data-dashboard-table-chart-row]").click(function() {
            if ($(this).data("dashboard-table-chart-row") != chart_index) {
                charts[chart_index].destroy();
                $("[data-dashboard-table-chart-row=\"" + chart_index + "\"]").removeClass("success");
                chart_index = $(this).data("dashboard-table-chart-row");
                charts[chart_index].create();
                $(this).addClass("success");
            }
        });
    });

    $(function() {
        $("[data-toggle=\"popover\"]").popover();
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
                <p class="mb-0">Вы можете пройти ещё 6.</p>
            </div>
        </div>
    </div>
    <div class="col-xs-12 col-sm-8 col-md-7">
        <div class="bb-chart bb-chart-dashboard-1 mb-15" data-dashboard-chart-1>
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
                                <th style="width: 25%;" class="text-center">Результат</th>
                                <th style="width: 25%;" class="text-center">Средний балл <i class="fa fa-question-circle text-help" data-toggle="popover" data-content="Средний балл по сравнению с другими студентами на bbTest.kz" data-placement="auto" data-trigger="hover"></i></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="data-dashboard-table-chart-row success" data-dashboard-table-chart-row="0">
                                <td><h6>Математика</h6></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-0></div></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-avg-0></div></td>
                            </tr>
                            <tr class="data-dashboard-table-chart-row" data-dashboard-table-chart-row="1">
                                <td><h6>Казахский Язык</h6></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-1></div></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-avg-1></div></td>
                            </tr>
                            <tr class="data-dashboard-table-chart-row" data-dashboard-table-chart-row="2">
                                <td><h6>Русский Язык</h6></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-2></div></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-avg-2></div></td>
                            </tr>
                            <tr class="data-dashboard-table-chart-row" data-dashboard-table-chart-row="3">
                                <td><h6>Английский Язык</h6></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-3></div></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-avg-3></div></td>
                            </tr>
                            <tr class="">
                                <td><h6 class="text-right"><strong>Общий балл <i class="fa fa-question-circle text-help" data-toggle="popover" data-content="Общий балл - это сумма 4-х разделов: Математика, Казахский Язык, Русский Язык, Английский Язык" data-placement="auto" data-trigger="hover"></i></strong></h6></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-total></div></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-total-avg></div></td>
                            </tr>
                            <tr class="data-dashboard-table-chart-row" data-dashboard-table-chart-row="4">
                                <td><h6>Количественные характеристики</h6></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-4></div></td>
                                <td><div class="bb-chart bb-chart-table" data-dashboard-table-chart-avg-4></div></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>
