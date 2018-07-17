ResultRowModule.prototype = Object.create(Module.prototype);
function ResultRowModule(data) {
    this._charts = [];
    this._charts.push(new RadialChart($(data.score.selector), data.score.value, data.max, {
        "line-width": 4,
        "arc-color": data.color,
        "font-size": 14
    }));
    this._charts.push(new ColumnChart($(data.progress.selector), data.progress.value, data.max, {
        "line-color": data.color,
        "avg_value": data.avg.value,
        "line-width": 8,
        "font-size": 14
    }));
    this._charts.push(new RadialChart($(data.avg.selector), data.avg.value, data.max, {
        "line-width": 4,
        "arc-color": "#aaaaaa",
        "font-size": 14
    }));

    var i;
    for (i = 0; i < this._charts.length; i++) {
        this._charts[i].create();
    }

    Module.call(this);
}
ResultRowModule.prototype.unMount = function() {
    var chart;
    while ((chart = this._charts.shift()) !== undefined) {
        chart.destroy();
    }
}
ResultRowModule.prototype.isMultiMount = true;
