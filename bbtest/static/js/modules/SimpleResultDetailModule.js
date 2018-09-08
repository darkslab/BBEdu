SimpleResultDetailModule.prototype = Object.create(Module.prototype);
function SimpleResultDetailModule(data) {
    this._$collapse = $(data.collapse_selector);
    this._charts = [];
    this._charts.push(new RadialChart($(data.detail_selector), data.score, data.max, {
        "line-width": 16,
        "arc-color": data.colors[0],
        "circle-color": data.colors[1],
        "font-size": 52
    }));
    this._charts.push(new ColumnChart($(data.progress_selector), data.progress, data.max, {
        "avg_value": data.avg,
        "padding-width": 4,
        "line-color": data.colors[0],
        "line-background-color": data.colors[1],
        "font-size": 14
    }));

    this._boundUncollapsed = this._uncollapsed.bind(this);
    this._boundCollapsed = this._collapsed.bind(this);

    this._$collapse.on("shown.bs.collapse", this._boundUncollapsed);
    this._$collapse.on("hidden.bs.collapse", this._boundCollapsed);

    Module.call(this);
}
SimpleResultDetailModule.prototype._uncollapsed = function() {
    var i;
    for (i = 0; i < this._charts.length; i++) {
        this._charts[i].create();
    }
}
SimpleResultDetailModule.prototype._collapsed = function() {
    var i;
    for (i = 0; i < this._charts.length; i++) {
        this._charts[i].destroy();
    }
}
SimpleResultDetailModule.prototype.unMount = function() {
    this._$collapse.off("shown.bs.collapse", this._boundUncollapsed);
    this._$collapse.off("hidden.bs.collapse", this._boundCollapsed);

    this._collapsed();
    this._charts = [];
}
SimpleResultDetailModule.prototype.isMultiMount = true;
