<script src="js/jquery-ui.min.js"></script>
<script src="js/SVGChart.js"></script>
<script src="js/RadialChart.js"></script>
<script src="js/ColumnChart.js"></script>
<script>
    $(function() {
        $("[data-toggle=\"popover\"]").popover();

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
    });
</script>
<div class="row">
    <div class="col-xs-12">
        <h3 class="mb-23 mt-0">Результаты тестов</h3>
    </div>

    <div class="col-xs-12">
        <div class="panel panel-primary">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <span>Тест #5</span>
                    <span class="label label-danger ml-5 hidden-xs">Не закончен</span>
                    <span class="pull-right">2017-07-26 23:45:56</span>
                </h4>
                <h4 class="panel-title text-center visible-xs-block mt-10">
                    <span class="label label-danger">Не закончен</span>
                </h4>
            </div>
            <div class="bb-accordion-panel-group" id="bb-results-0">
                <div class="panel">
                    <div class="bb-accordion-panel-heading first">
                        <div class="row">
                            <div class="col-xs-12 col-sm-6 bb-result-cell">
                                <span>Математика</span>
                                <a href="#bb-results-0-0" class="bb-accordion-toggle collapsed pull-right visible-xs-block" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                            <div class="col-xs-4 col-xs-offset-2 col-sm-2 col-sm-offset-0 bb-chart bb-result-cell" data-dashboard-table-chart-0></div>
                            <div class="col-xs-4 col-sm-2 bb-chart bb-result-cell" data-dashboard-table-chart-avg-0></div>
                            <div class="col-sm-2 bb-result-cell hidden-xs">
                                <a href="#bb-results-0-0" class="bb-accordion-toggle collapsed pull-right" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="collapse" id="bb-results-0-0">
                        <div class="bb-accordion-panel-body">
                            <div class="row">
                                <div class="col-xs-12 col-sm-5 text-center">
                                    <i class="fa fa-pie-chart" style="font-size: 260px;"></i>
                                </div>
                                <div class="col-xs-12 col-sm-7">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#section-1" data-toggle="tab">Section 1</a></li>
                                        <li><a href="#section-2" data-toggle="tab">Section 2</a></li>
                                        <li><a href="#section-3" data-toggle="tab">Section 3</a></li>
                                        <li><a href="#section-4" data-toggle="tab">Section 5</a></li>
                                    </ul>
                                    <div class="tab-content">
                                        <div class="tab-pane fade active in" id="section-1">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at ante. Mauris eleifend, quam a vulputate dictum, massa quam dapibus leo, eget vulputate orci purus ut lorem. In fringilla mi in ligula. Pellentesque aliquam quam vel dolor. Nunc adipiscing. Sed quam odio, tempus ac, aliquam molestie, varius ac, tellus. Vestibulum ut nulla aliquam risus rutrum interdum. Pellentesque lorem. Curabitur sit amet erat quis risus feugiat viverra. Pellentesque augue justo, sagittis et, lacinia at, venenatis non, arcu. Nunc nec libero. In cursus dictum risus. Etiam tristique nisl a nulla. Ut a orci. Curabitur dolor nunc, egestas at, accumsan at, malesuada nec, magna.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-2">
                                            <p>Nulla facilisi. Nunc volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut sit amet orci vel mauris blandit vehicula. Nullam quis enim. Integer dignissim viverra velit. Curabitur in odio. In hac habitasse platea dictumst. Ut consequat, tellus eu volutpat varius, justo orci elementum dolor, sed imperdiet nulla tellus ut diam. Vestibulum ipsum ante, malesuada quis, tempus ac, placerat sit amet, elit.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-3">
                                            <p>Sed eget turpis a pede tempor malesuada. Vivamus quis mi at leo pulvinar hendrerit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque aliquet lacus vitae pede. Nullam mollis dolor ac nisi. Phasellus sit amet urna. Praesent pellentesque sapien sed lacus. Donec lacinia odio in odio. In sit amet elit. Maecenas gravida interdum urna. Integer pretium, arcu vitae imperdiet facilisis, elit tellus tempor nisi, vel feugiat ante velit sit amet mauris. Vivamus arcu. Integer pharetra magna ac lacus. Aliquam vitae sapien in nibh vehicula auctor. Suspendisse leo mauris, pulvinar sed, tempor et, consequat ac, lacus. Proin velit. Nulla semper lobortis mauris. Duis urna erat, ornare et, imperdiet eu, suscipit sit amet, massa. Nulla nulla nisi, pellentesque at, egestas quis, fringilla eu, diam.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-4">
                                            <p>Donec semper, sem nec tristique tempus, justo neque commodo nisl, ut gravida sem tellus suscipit nunc. Aliquam erat volutpat. Ut tincidunt pretium elit. Aliquam pulvinar. Nulla cursus. Suspendisse potenti. Etiam condimentum hendrerit felis. Duis iaculis aliquam enim. Donec dignissim augue vitae orci. Curabitur luctus felis a metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In varius neque at enim. Suspendisse massa nulla, viverra in, bibendum vitae, tempor quis, lorem.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="panel">
                    <div class="bb-accordion-panel-heading">
                        <div class="row">
                            <div class="col-xs-12 col-sm-6 bb-result-cell">
                                <span>Казахский Язык</span>
                                <a href="#bb-results-0-1" class="bb-accordion-toggle collapsed pull-right visible-xs-block" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                            <div class="col-xs-4 col-xs-offset-2 col-sm-2 col-sm-offset-0 bb-chart bb-result-cell" data-dashboard-table-chart-1></div>
                            <div class="col-xs-4 col-sm-2 bb-chart bb-result-cell" data-dashboard-table-chart-avg-1></div>
                            <div class="col-sm-2 bb-result-cell hidden-xs">
                                <a href="#bb-results-0-1" class="bb-accordion-toggle collapsed pull-right" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="collapse" id="bb-results-0-1">
                        <div class="bb-accordion-panel-body">
                            <div class="row">
                                <div class="col-xs-12 col-sm-5 text-center">
                                    <i class="fa fa-pie-chart" style="font-size: 260px;"></i>
                                </div>
                                <div class="col-xs-12 col-sm-7">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#section-1" data-toggle="tab">Section 1</a></li>
                                        <li><a href="#section-2" data-toggle="tab">Section 2</a></li>
                                        <li><a href="#section-3" data-toggle="tab">Section 3</a></li>
                                        <li><a href="#section-4" data-toggle="tab">Section 5</a></li>
                                    </ul>
                                    <div class="tab-content">
                                        <div class="tab-pane fade active in" id="section-1">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at ante. Mauris eleifend, quam a vulputate dictum, massa quam dapibus leo, eget vulputate orci purus ut lorem. In fringilla mi in ligula. Pellentesque aliquam quam vel dolor. Nunc adipiscing. Sed quam odio, tempus ac, aliquam molestie, varius ac, tellus. Vestibulum ut nulla aliquam risus rutrum interdum. Pellentesque lorem. Curabitur sit amet erat quis risus feugiat viverra. Pellentesque augue justo, sagittis et, lacinia at, venenatis non, arcu. Nunc nec libero. In cursus dictum risus. Etiam tristique nisl a nulla. Ut a orci. Curabitur dolor nunc, egestas at, accumsan at, malesuada nec, magna.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-2">
                                            <p>Nulla facilisi. Nunc volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut sit amet orci vel mauris blandit vehicula. Nullam quis enim. Integer dignissim viverra velit. Curabitur in odio. In hac habitasse platea dictumst. Ut consequat, tellus eu volutpat varius, justo orci elementum dolor, sed imperdiet nulla tellus ut diam. Vestibulum ipsum ante, malesuada quis, tempus ac, placerat sit amet, elit.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-3">
                                            <p>Sed eget turpis a pede tempor malesuada. Vivamus quis mi at leo pulvinar hendrerit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque aliquet lacus vitae pede. Nullam mollis dolor ac nisi. Phasellus sit amet urna. Praesent pellentesque sapien sed lacus. Donec lacinia odio in odio. In sit amet elit. Maecenas gravida interdum urna. Integer pretium, arcu vitae imperdiet facilisis, elit tellus tempor nisi, vel feugiat ante velit sit amet mauris. Vivamus arcu. Integer pharetra magna ac lacus. Aliquam vitae sapien in nibh vehicula auctor. Suspendisse leo mauris, pulvinar sed, tempor et, consequat ac, lacus. Proin velit. Nulla semper lobortis mauris. Duis urna erat, ornare et, imperdiet eu, suscipit sit amet, massa. Nulla nulla nisi, pellentesque at, egestas quis, fringilla eu, diam.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-4">
                                            <p>Donec semper, sem nec tristique tempus, justo neque commodo nisl, ut gravida sem tellus suscipit nunc. Aliquam erat volutpat. Ut tincidunt pretium elit. Aliquam pulvinar. Nulla cursus. Suspendisse potenti. Etiam condimentum hendrerit felis. Duis iaculis aliquam enim. Donec dignissim augue vitae orci. Curabitur luctus felis a metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In varius neque at enim. Suspendisse massa nulla, viverra in, bibendum vitae, tempor quis, lorem.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="panel">
                    <div class="bb-accordion-panel-heading">
                        <div class="row">
                            <div class="col-xs-12 col-sm-6 bb-result-cell">
                                <span>Русский Язык</span>
                                <a href="#bb-results-0-2" class="bb-accordion-toggle collapsed pull-right visible-xs-block" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                            <div class="col-xs-4 col-xs-offset-2 col-sm-2 col-sm-offset-0 bb-chart bb-result-cell" data-dashboard-table-chart-2></div>
                            <div class="col-xs-4 col-sm-2 bb-chart bb-result-cell" data-dashboard-table-chart-avg-2></div>
                            <div class="col-sm-2 bb-result-cell hidden-xs">
                                <a href="#bb-results-0-2" class="bb-accordion-toggle collapsed pull-right" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="collapse" id="bb-results-0-2">
                        <div class="bb-accordion-panel-body">
                            <div class="row">
                                <div class="col-xs-12 col-sm-5 text-center">
                                    <i class="fa fa-pie-chart" style="font-size: 260px;"></i>
                                </div>
                                <div class="col-xs-12 col-sm-7">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#section-1" data-toggle="tab">Section 1</a></li>
                                        <li><a href="#section-2" data-toggle="tab">Section 2</a></li>
                                        <li><a href="#section-3" data-toggle="tab">Section 3</a></li>
                                        <li><a href="#section-4" data-toggle="tab">Section 5</a></li>
                                    </ul>
                                    <div class="tab-content">
                                        <div class="tab-pane fade active in" id="section-1">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at ante. Mauris eleifend, quam a vulputate dictum, massa quam dapibus leo, eget vulputate orci purus ut lorem. In fringilla mi in ligula. Pellentesque aliquam quam vel dolor. Nunc adipiscing. Sed quam odio, tempus ac, aliquam molestie, varius ac, tellus. Vestibulum ut nulla aliquam risus rutrum interdum. Pellentesque lorem. Curabitur sit amet erat quis risus feugiat viverra. Pellentesque augue justo, sagittis et, lacinia at, venenatis non, arcu. Nunc nec libero. In cursus dictum risus. Etiam tristique nisl a nulla. Ut a orci. Curabitur dolor nunc, egestas at, accumsan at, malesuada nec, magna.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-2">
                                            <p>Nulla facilisi. Nunc volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut sit amet orci vel mauris blandit vehicula. Nullam quis enim. Integer dignissim viverra velit. Curabitur in odio. In hac habitasse platea dictumst. Ut consequat, tellus eu volutpat varius, justo orci elementum dolor, sed imperdiet nulla tellus ut diam. Vestibulum ipsum ante, malesuada quis, tempus ac, placerat sit amet, elit.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-3">
                                            <p>Sed eget turpis a pede tempor malesuada. Vivamus quis mi at leo pulvinar hendrerit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque aliquet lacus vitae pede. Nullam mollis dolor ac nisi. Phasellus sit amet urna. Praesent pellentesque sapien sed lacus. Donec lacinia odio in odio. In sit amet elit. Maecenas gravida interdum urna. Integer pretium, arcu vitae imperdiet facilisis, elit tellus tempor nisi, vel feugiat ante velit sit amet mauris. Vivamus arcu. Integer pharetra magna ac lacus. Aliquam vitae sapien in nibh vehicula auctor. Suspendisse leo mauris, pulvinar sed, tempor et, consequat ac, lacus. Proin velit. Nulla semper lobortis mauris. Duis urna erat, ornare et, imperdiet eu, suscipit sit amet, massa. Nulla nulla nisi, pellentesque at, egestas quis, fringilla eu, diam.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-4">
                                            <p>Donec semper, sem nec tristique tempus, justo neque commodo nisl, ut gravida sem tellus suscipit nunc. Aliquam erat volutpat. Ut tincidunt pretium elit. Aliquam pulvinar. Nulla cursus. Suspendisse potenti. Etiam condimentum hendrerit felis. Duis iaculis aliquam enim. Donec dignissim augue vitae orci. Curabitur luctus felis a metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In varius neque at enim. Suspendisse massa nulla, viverra in, bibendum vitae, tempor quis, lorem.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="panel">
                    <div class="bb-accordion-panel-heading">
                        <div class="row">
                            <div class="col-xs-12 col-sm-6 bb-result-cell">
                                <span>Английский Язык</span>
                                <a href="#bb-results-0-3" class="bb-accordion-toggle collapsed pull-right visible-xs-block" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                            <div class="col-xs-4 col-xs-offset-2 col-sm-2 col-sm-offset-0 bb-chart bb-result-cell" data-dashboard-table-chart-3></div>
                            <div class="col-xs-4 col-sm-2 bb-chart bb-result-cell" data-dashboard-table-chart-avg-3></div>
                            <div class="col-sm-2 bb-result-cell hidden-xs">
                                <a href="#bb-results-0-3" class="bb-accordion-toggle collapsed pull-right" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="collapse" id="bb-results-0-3">
                        <div class="bb-accordion-panel-body">
                            <div class="row">
                                <div class="col-xs-12 col-sm-5 text-center">
                                    <i class="fa fa-pie-chart" style="font-size: 260px;"></i>
                                </div>
                                <div class="col-xs-12 col-sm-7">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#section-1" data-toggle="tab">Section 1</a></li>
                                        <li><a href="#section-2" data-toggle="tab">Section 2</a></li>
                                        <li><a href="#section-3" data-toggle="tab">Section 3</a></li>
                                        <li><a href="#section-4" data-toggle="tab">Section 5</a></li>
                                    </ul>
                                    <div class="tab-content">
                                        <div class="tab-pane fade active in" id="section-1">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at ante. Mauris eleifend, quam a vulputate dictum, massa quam dapibus leo, eget vulputate orci purus ut lorem. In fringilla mi in ligula. Pellentesque aliquam quam vel dolor. Nunc adipiscing. Sed quam odio, tempus ac, aliquam molestie, varius ac, tellus. Vestibulum ut nulla aliquam risus rutrum interdum. Pellentesque lorem. Curabitur sit amet erat quis risus feugiat viverra. Pellentesque augue justo, sagittis et, lacinia at, venenatis non, arcu. Nunc nec libero. In cursus dictum risus. Etiam tristique nisl a nulla. Ut a orci. Curabitur dolor nunc, egestas at, accumsan at, malesuada nec, magna.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-2">
                                            <p>Nulla facilisi. Nunc volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut sit amet orci vel mauris blandit vehicula. Nullam quis enim. Integer dignissim viverra velit. Curabitur in odio. In hac habitasse platea dictumst. Ut consequat, tellus eu volutpat varius, justo orci elementum dolor, sed imperdiet nulla tellus ut diam. Vestibulum ipsum ante, malesuada quis, tempus ac, placerat sit amet, elit.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-3">
                                            <p>Sed eget turpis a pede tempor malesuada. Vivamus quis mi at leo pulvinar hendrerit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque aliquet lacus vitae pede. Nullam mollis dolor ac nisi. Phasellus sit amet urna. Praesent pellentesque sapien sed lacus. Donec lacinia odio in odio. In sit amet elit. Maecenas gravida interdum urna. Integer pretium, arcu vitae imperdiet facilisis, elit tellus tempor nisi, vel feugiat ante velit sit amet mauris. Vivamus arcu. Integer pharetra magna ac lacus. Aliquam vitae sapien in nibh vehicula auctor. Suspendisse leo mauris, pulvinar sed, tempor et, consequat ac, lacus. Proin velit. Nulla semper lobortis mauris. Duis urna erat, ornare et, imperdiet eu, suscipit sit amet, massa. Nulla nulla nisi, pellentesque at, egestas quis, fringilla eu, diam.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-4">
                                            <p>Donec semper, sem nec tristique tempus, justo neque commodo nisl, ut gravida sem tellus suscipit nunc. Aliquam erat volutpat. Ut tincidunt pretium elit. Aliquam pulvinar. Nulla cursus. Suspendisse potenti. Etiam condimentum hendrerit felis. Duis iaculis aliquam enim. Donec dignissim augue vitae orci. Curabitur luctus felis a metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In varius neque at enim. Suspendisse massa nulla, viverra in, bibendum vitae, tempor quis, lorem.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="panel">
                    <div class="bb-accordion-panel-heading">
                        <div class="row">
                            <div class="col-xs-12 col-sm-6 bb-result-cell bb-result-cell-total">
                                <strong>Общий балл <i class="fa fa-question-circle text-help" data-toggle="popover" data-container="body" data-content="Общий балл - это сумма 4-х разделов: Математика, Казахский Язык, Русский Язык, Английский Язык" data-placement="auto" data-trigger="hover"></i></strong>
                            </div>
                            <div class="col-xs-4 col-xs-offset-2 col-sm-2 col-sm-offset-0 bb-chart bb-result-cell" data-dashboard-table-chart-total></div>
                            <div class="col-xs-4 col-sm-2 bb-chart bb-result-cell" data-dashboard-table-chart-total-avg></div>
                        </div>
                    </div>
                </div>
                <div class="panel">
                    <div class="bb-accordion-panel-heading">
                        <div class="row">
                            <div class="col-xs-12 col-sm-6 bb-result-cell">
                                <span>Количественные характеристики</span>
                                <a href="#bb-results-0-4" class="bb-accordion-toggle collapsed pull-right visible-xs-block" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                            <div class="col-xs-4 col-xs-offset-2 col-sm-2 col-sm-offset-0 bb-chart bb-result-cell" data-dashboard-table-chart-4></div>
                            <div class="col-xs-4 col-sm-2 bb-chart bb-result-cell" data-dashboard-table-chart-avg-4></div>
                            <div class="col-sm-2 bb-result-cell hidden-xs">
                                <a href="#bb-results-0-4" class="bb-accordion-toggle collapsed pull-right" data-toggle="collapse" data-parent="#bb-results-0">
                                    <i class="fa fa-fw fa-chevron-up"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="collapse" id="bb-results-0-4">
                        <div class="bb-accordion-panel-body">
                            <div class="row">
                                <div class="col-xs-12 col-sm-5 text-center">
                                    <i class="fa fa-pie-chart" style="font-size: 260px;"></i>
                                </div>
                                <div class="col-xs-12 col-sm-7">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#section-1" data-toggle="tab">Section 1</a></li>
                                        <li><a href="#section-2" data-toggle="tab">Section 2</a></li>
                                        <li><a href="#section-3" data-toggle="tab">Section 3</a></li>
                                        <li><a href="#section-4" data-toggle="tab">Section 5</a></li>
                                    </ul>
                                    <div class="tab-content">
                                        <div class="tab-pane fade active in" id="section-1">
                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at ante. Mauris eleifend, quam a vulputate dictum, massa quam dapibus leo, eget vulputate orci purus ut lorem. In fringilla mi in ligula. Pellentesque aliquam quam vel dolor. Nunc adipiscing. Sed quam odio, tempus ac, aliquam molestie, varius ac, tellus. Vestibulum ut nulla aliquam risus rutrum interdum. Pellentesque lorem. Curabitur sit amet erat quis risus feugiat viverra. Pellentesque augue justo, sagittis et, lacinia at, venenatis non, arcu. Nunc nec libero. In cursus dictum risus. Etiam tristique nisl a nulla. Ut a orci. Curabitur dolor nunc, egestas at, accumsan at, malesuada nec, magna.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-2">
                                            <p>Nulla facilisi. Nunc volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut sit amet orci vel mauris blandit vehicula. Nullam quis enim. Integer dignissim viverra velit. Curabitur in odio. In hac habitasse platea dictumst. Ut consequat, tellus eu volutpat varius, justo orci elementum dolor, sed imperdiet nulla tellus ut diam. Vestibulum ipsum ante, malesuada quis, tempus ac, placerat sit amet, elit.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-3">
                                            <p>Sed eget turpis a pede tempor malesuada. Vivamus quis mi at leo pulvinar hendrerit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque aliquet lacus vitae pede. Nullam mollis dolor ac nisi. Phasellus sit amet urna. Praesent pellentesque sapien sed lacus. Donec lacinia odio in odio. In sit amet elit. Maecenas gravida interdum urna. Integer pretium, arcu vitae imperdiet facilisis, elit tellus tempor nisi, vel feugiat ante velit sit amet mauris. Vivamus arcu. Integer pharetra magna ac lacus. Aliquam vitae sapien in nibh vehicula auctor. Suspendisse leo mauris, pulvinar sed, tempor et, consequat ac, lacus. Proin velit. Nulla semper lobortis mauris. Duis urna erat, ornare et, imperdiet eu, suscipit sit amet, massa. Nulla nulla nisi, pellentesque at, egestas quis, fringilla eu, diam.</p>
                                        </div>
                                        <div class="tab-pane fade" id="section-4">
                                            <p>Donec semper, sem nec tristique tempus, justo neque commodo nisl, ut gravida sem tellus suscipit nunc. Aliquam erat volutpat. Ut tincidunt pretium elit. Aliquam pulvinar. Nulla cursus. Suspendisse potenti. Etiam condimentum hendrerit felis. Duis iaculis aliquam enim. Donec dignissim augue vitae orci. Curabitur luctus felis a metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In varius neque at enim. Suspendisse massa nulla, viverra in, bibendum vitae, tempor quis, lorem.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="col-xs-12">
        <div class="panel panel-success">
            <div class="panel-heading">
                <h4 class="panel-title">Тест #4 <span class="pull-right">2017-07-26 23:45:56</span></h4>
            </div>
            <div class="bb-accordion-panel-group" id="bb-results-1">
                <div class="panel">
                    <div class="bb-accordion-panel-heading first">
                        <a href="#bb-results-1-0" class="collapsed" data-toggle="collapse" data-parent="#bb-results-1"><i class="fa fa-fw fa-chevron-down"></i></a>
                    </div>
                    <div class="collapse" id="bb-results-1-0">
                        <div class="bb-accordion-panel-body">
                            <div style="height: 100px;"></div>
                        </div>
                    </div>
                </div>
                <div class="panel">
                    <div class="bb-accordion-panel-heading">
                        <a href="#bb-results-1-1" class="collapsed" data-toggle="collapse" data-parent="#bb-results-1"><i class="fa fa-fw fa-chevron-down"></i></a>
                    </div>
                    <div class="collapse" id="bb-results-1-1">
                        <div class="bb-accordion-panel-body last">
                            <div style="height: 100px;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="col-xs-12">
        <div class="panel panel-success">
            <div class="panel-heading">
                <h4 class="panel-title">Тест #3 <span class="pull-right">2017-07-26 23:45:56</span></h4>
            </div>
            <div class="bb-accordion-panel-group" id="bb-results-2">
                <div class="panel">
                    <div class="bb-accordion-panel-heading first">
                        <a href="#bb-results-2-0" class="collapsed" data-toggle="collapse" data-parent="#bb-results-2"><i class="fa fa-fw fa-chevron-down"></i></a>
                    </div>
                    <div class="collapse" id="bb-results-2-0">
                        <div class="bb-accordion-panel-body">
                            <div style="height: 100px;"></div>
                        </div>
                    </div>
                </div>
                <div class="panel">
                    <div class="bb-accordion-panel-heading">
                        <a href="#bb-results-2-1" class="collapsed" data-toggle="collapse" data-parent="#bb-results-2"><i class="fa fa-fw fa-chevron-down"></i></a>
                    </div>
                    <div class="collapse" id="bb-results-2-1">
                        <div class="bb-accordion-panel-body last">
                            <div style="height: 100px;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="col-xs-12">
        <div class="panel panel-success">
            <div class="panel-heading">
                <h4 class="panel-title">Тест #2 <span class="pull-right">2017-07-26 23:45:56</span></h4>
            </div>
            <div class="bb-accordion-panel-group" id="bb-results-3">
                <div class="panel">
                    <div class="bb-accordion-panel-heading first">
                        <a href="#bb-results-3-0" class="collapsed" data-toggle="collapse" data-parent="#bb-results-3"><i class="fa fa-fw fa-chevron-down"></i></a>
                    </div>
                    <div class="collapse" id="bb-results-3-0">
                        <div class="bb-accordion-panel-body">
                            <div style="height: 100px;"></div>
                        </div>
                    </div>
                </div>
                <div class="panel">
                    <div class="bb-accordion-panel-heading">
                        <a href="#bb-results-3-1" class="collapsed" data-toggle="collapse" data-parent="#bb-results-3"><i class="fa fa-fw fa-chevron-down"></i></a>
                    </div>
                    <div class="collapse" id="bb-results-3-1">
                        <div class="bb-accordion-panel-body last">
                            <div style="height: 100px;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="col-xs-12">
        <div class="panel panel-success">
            <div class="panel-heading">
                <h4 class="panel-title">Тест #1 <span class="pull-right">2017-07-26 23:45:56</span></h4>
            </div>
            <div class="bb-accordion-panel-group" id="bb-results-4">
                <div class="panel">
                    <div class="bb-accordion-panel-heading first">
                        <a href="#bb-results-4-0" class="collapsed" data-toggle="collapse" data-parent="#bb-results-4"><i class="fa fa-fw fa-chevron-down"></i></a>
                    </div>
                    <div class="collapse" id="bb-results-4-0">
                        <div class="bb-accordion-panel-body">
                            <div style="height: 100px;"></div>
                        </div>
                    </div>
                </div>
                <div class="panel">
                    <div class="bb-accordion-panel-heading">
                        <a href="#bb-results-4-1" class="collapsed" data-toggle="collapse" data-parent="#bb-results-4"><i class="fa fa-fw fa-chevron-down"></i></a>
                    </div>
                    <div class="collapse" id="bb-results-4-1">
                        <div class="bb-accordion-panel-body last">
                            <div style="height: 100px;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="col-xs-12">
        <ul class="pagination pull-right mt-0">
            <li class="disabled"><a href="#">&laquo;</a></li>
            <li class="active"><a href="#">1</a></li>
            <li><a href="#">2</a></li>
            <li><a href="#">3</a></li>
            <li><a href="#">4</a></li>
            <li><a href="#">5</a></li>
            <li><a href="#">&raquo;</a></li>
        </ul>
    </div>
</div>
