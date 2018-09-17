ResultEmptyRowModule.prototype = Object.create(Module.prototype);
function ResultEmptyRowModule(data) {
    this._chart = new RadialChart($(data.selector), data.value, data.max, {
        "line-width": 4,
        "arc-color": "#aaaaaa",
        "circle-color": "#cae6fc",
        "font-size": 14
    });

    this._chart.create();

    Module.call(this);
}
ResultEmptyRowModule.prototype.unMount = function() {
    this._chart.destroy();
}
ResultEmptyRowModule.prototype.isMultiMount = true;
