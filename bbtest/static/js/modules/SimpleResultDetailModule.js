SimpleResultDetailModule.prototype = Object.create(Module.prototype);
function SimpleResultDetailModule(data) {
    this._$collapse = $(data.collapse_selector);
    this._chart = new RadialChart($(data.selector), data.score, data.max, {
        "line-width": 16,
        "arc-color": "#dc3912",
        "font-size": 52
    });

    this._boundUncollapsed = this._uncollapsed.bind(this);
    this._boundCollapsed = this._collapsed.bind(this);

    this._$collapse.on("shown.bs.collapse", this._boundUncollapsed);
    this._$collapse.on("hidden.bs.collapse", this._boundCollapsed);

    Module.call(this);
}
SimpleResultDetailModule.prototype._uncollapsed = function() {
    this._chart.create();
}
SimpleResultDetailModule.prototype._collapsed = function() {
    this._chart.destroy();
}
SimpleResultDetailModule.prototype.unMount = function() {
    this._$collapse.off("shown.bs.collapse", this._boundUncollapsed);
    this._$collapse.off("hidden.bs.collapse", this._boundCollapsed);
}
SimpleResultDetailModule.prototype.isMultiMount = true;
