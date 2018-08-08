ResultRowModule.prototype = Object.create(Module.prototype);
function ResultRowModule(data) {
    this._charts = [];
    this._charts.push(new RadialChart($(data.score.selector), data.score.value, data.max, {
        "line-width": 4,
        "arc-color": data.colors[0],
        "circle-color": data.colors[1],
        "font-size": 14
    }));
    this._charts.push(new RadialChart($(data.avg.selector), data.avg.value, data.max, {
        "line-width": 4,
        "arc-color": "#aaaaaa",
        "circle-color": "#cae6fc",
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
