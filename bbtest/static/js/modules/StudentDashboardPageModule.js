StudentDashboardPageModule.prototype = Object.create(Module.prototype);
function StudentDashboardPageModule(data) {
    this._columnCharts = [];
    this._columnChartIndex;
    var i;
    for (i = 0; i < data.progress_data.length; i++) {
        data.progress_data[i];
        this._columnCharts.push(new ColumnChart($(data.progress_selector), data.progress_data[i].progress, data.progress_data[i].max, {
            "avg_value": data.progress_data[i].avg,
            "padding-width": 4,
            "line-color": data.progress_data[i].colors[0],
            "line-background-color": data.progress_data[i].colors[1],
            "font-size": 14
        }));
    }

    this._rowsAttrName = data.rows_selector_attr_name;
    this._$rows = $("[data-" + this._rowsAttrName + "]");

    this._activateRow(0);

    this._boundSelectRow = this._selectRow.bind(this);

    this._$rows.on("click", this._boundSelectRow);

    Module.call(this);
}
StudentDashboardPageModule.prototype._activateRow = function(index) {
    if (this._columnChartIndex === index) {
        return;
    }
    if (this._columnChartIndex !== undefined) {
        this._deactivateRow(this._columnChartIndex);
    }
    this._columnChartIndex = index;
    this._columnCharts[this._columnChartIndex].create();
    this._$rows.filter("[data-" + this._rowsAttrName + "=\"" + this._columnChartIndex + "\"]").addClass("container-faded");
}
StudentDashboardPageModule.prototype._selectRow = function(event) {
    this._activateRow($(event.currentTarget).data(this._rowsAttrName));
}
StudentDashboardPageModule.prototype._deactivateRow = function(index) {
    this._columnCharts[index].destroy();
    this._$rows.filter("[data-" + this._rowsAttrName + "=\"" + index + "\"]").removeClass("container-faded");
}
StudentDashboardPageModule.prototype.unMount = function() {
    this._deactivateRow(this._columnChartIndex);

    this._$rows.off("click", this._boundSelectRow);
}
