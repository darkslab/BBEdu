<link href="vendor/css/vizuly.css" rel="stylesheet">
<link href="vendor/css/vizuly_radial_progress.css" rel="stylesheet">
<link href="css/vizuly_customized.css" rel="stylesheet">
<script src="vendor/js/d3.min.js"></script>
<script src="vendor/js/vizuly_core.min.js"></script>
<script src="vendor/js/vizuly_radialprogress.min.js"></script>
<script src="js/vizuly_customized.js"></script>
<script>
    $(function() {
        new VizulyArc($("[data-main-arc]"), 6, 18);
    });
</script>
<div class="row">
    <div class="col-xs-12">
        <div class="alert alert-dismissible alert-success">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <strong>Хорошие новости!</strong> Мы добавили <a href="<?php echo $base; ?>test.html" class="alert-link">8 новые варианты тестов</a>!
        </div>
    </div>
    <div class="col-xs-12 col-sm-6 col-md-5">
        <div class="bb-arc bb-arc-dashboard-main" data-main-arc>
            <div class="bb-arc-caption text-center text-uppercase">Тестов пройдено</div>
        </div>
    </div>
    <div class="col-xs-12 col-sm-6 col-md-7">
        <div class="panel panel-primary">
            <div class="panel-heading"><strong>Результаты последнего теста</strong></div>
            <div class="panel-body">
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
