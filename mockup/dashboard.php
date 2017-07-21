<script src="js/jquery-ui.min.js"></script>
<script src="js/SVGChart.js"></script>
<script src="js/RadialChart.js"></script>
<script src="js/ColumnChart.js"></script>
<script>
    $(function() {
        var chart_0 = new RadialChart($("[data-dashboard-chart-0]"), 1, 10, {
            "line-width": 16,
            "circle-color": "#c7e7c8",
            "arc-color": "#4caf50"
        });
        var chart_1 = new ColumnChart($("[data-dashboard-chart-1]"), [
            435,
            234,
            412,
            347,
            289,
            500,
            124,
            250,
            179,
            496
        ], 500, {
            // "duration": 5000,
            // "chain-duration": 0,
            "line-width": 16,
            // "padding-right": 0,
            // "padding-left": 0
        });

        chart_0.draw();
        chart_1.draw();
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
        <div class="bb-chart bb-chart-dashboard-1 mb-15" data-dashboard-chart-1 style="height: 200px;">
        </div>
    </div>
    <!-- <div class="col-xs-12 col-sm-8 col-md-7" style="height: 215px;">
        <?php
        $width = 535;
        $height = 200;
        $offset = $width * 0.12 + 15;
        $end_offset = 15;
        $num = 10;

        $col_width = ($width - $offset - $end_offset) / ($num + ($num - 1));
        $col_width = min($col_width, $height * 0.125);
        $col_width = 24;
        $col_shift = $col_width / 2;
        $padding_width = ($width - $offset - $end_offset - ($col_width * $num)) / ($num - 1);
        $current_shift = $col_shift;
        $font_size = 18;
        ?>
        <svg width="100%" height="100%">
            <?php while ($num-- > 0): ?>
                <g transform="translate(<?php echo $current_shift + $offset; ?>,<?php echo $height; ?>) rotate(180)">
                    <path d="<?php echo 'M0 '.$col_shift.'L0 '.($height - $col_shift); ?>" fill="none" stroke="#cae6fc" stroke-width="<?php echo $col_width; ?>" stroke-linecap="round"></path>
                    <path d="<?php echo 'M0 '.$col_shift.'L0 '.rand(10 + $col_shift, $height - $col_shift); ?>" fill="none" stroke="#2196f3" stroke-width="<?php echo $col_width; ?>" stroke-linecap="round"></path>
                </g>
                <?php
                $current_shift += $padding_width + $col_shift * 2;
                ?>
            <?php endwhile; ?>
            <text x="50" y="5" text-anchor="end" font-size="<?php echo $font_size; ?>" font-weight="" dominant-baseline="hanging">500</text>
            <text x="50" y="<?php echo $height / 2; ?>" text-anchor="end" font-size="<?php echo $font_size; ?>" font-weight="" dominant-baseline="middle">xxx</text>
            <text x="50" y="<?php echo $height - 5; ?>" text-anchor="end" font-size="<?php echo $font_size; ?>" font-weight="" dominant-baseline="auto">0</text>
        </svg>
    </div> -->
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
