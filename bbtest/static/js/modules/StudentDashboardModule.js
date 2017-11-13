StudentDashboardModule.prototype = Object.create(Module.prototype);
function StudentDashboardModule(data) {
    this._radialCharts = [];
    this._columnCharts = [];
    this._chartIndex = 0;

    var i;
    for (i = 0; i < data.radialChartsData.length; i++) {
        data.radialChartsData[i][0] = $(data.radialChartsData[i][0]);
        data.radialChartsData[i].unshift(null);
        var radialChart = new (Function.prototype.bind.apply(RadialChart, data.radialChartsData[i]));
        radialChart.create();
        this._radialCharts.push(radialChart);
    }
    var $container = $(data.columnChartsData.attr);
    for (i = 0; i < data.columnChartsData.data.length; i++) {
        data.columnChartsData.data[i].unshift($container);
        data.columnChartsData.data[i].unshift(null);
        var columnChart = new (Function.prototype.bind.apply(ColumnChart, data.columnChartsData.data[i]));
        this._columnCharts.push(columnChart);
    }
    this._columnCharts[this._chartIndex].create();

    $("[data-dashboard-table-chart-row]").click(function() {
        if ($(this).data("dashboard-table-chart-row") != this._chartIndex) {
            this._columnCharts[this._chartIndex].destroy();
            $("[data-dashboard-table-chart-row=\"" + this._chartIndex + "\"]").removeClass("success");
            this._chartIndex = $(this).data("dashboard-table-chart-row");
            this._columnCharts[this._chartIndex].create();
            $(this).addClass("success");
        }
    });

    Module.call(this);
}
StudentDashboardModule.prototype.unMount = function() {
    var radialChart;
    while ((radialChart = this._radialCharts.shift()) !== undefined) {
        radialChart.destroy();
    }
    this._columnCharts[this._chartIndex].destroy();
}
