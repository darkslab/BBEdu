BranchedResultDetailModule.prototype = Object.create(Module.prototype);
function BranchedResultDetailModule(data) {
    this._$collapse = $(data.collapse_selector);
    this._tabHandlesDataAttrName = data.tab_handle_data_attr_name;
    this._$tabHandles = $("[data-" + this._tabHandlesDataAttrName + "]");
    this._$tabs = $(data.tab_selector);

    this._boundUncollapsed = this._uncollapsed.bind(this);
    this._boundCollapsed = this._collapsed.bind(this);
    this._boundTabbed = this._tabbed.bind(this);
    this._boundActivated = this._activated.bind(this);

    this._index;
    var chartData = [];
    var i;
    for (i = 0; i < data.branches.length; i++) {
        chartData.push({
            "max-value": data.branches[i].max,
            "value": data.branches[i].score,
            "foreground-color": data.branches[i].colors[0],
            "background-color": data.branches[i].colors[1],
            "active-callback-start": this._boundActivated
        });
    }
    this._chart = new ProgressPieChart($(data.selector), chartData, {
        "duration": 2000,
        "chain-duration": 0,
        "activate-duration": 150,
        "hole-radius": "30%",
        "active-radius": "15%",
        "font-size": 18,
        "font-weight": "bold",
        "font-color": "#fff"
    });

    this._$collapse.on("shown.bs.collapse", this._boundUncollapsed);
    this._$collapse.on("hidden.bs.collapse", this._boundCollapsed);
    this._$tabHandles.on("click", this._boundTabbed);

    Module.call(this);
}
BranchedResultDetailModule.prototype._uncollapsed = function() {
    this._chart.create();
    this._chart.activate(0);
}
BranchedResultDetailModule.prototype._collapsed = function() {
    this._chart.destroy();
    this._index = undefined;
    this._$tabHandles.each(function() {
        $(this).attr("aria-expanded", false).parent().removeClass("active");
    });
    this._$tabs.each(function() {
        $(this).removeClass("active").removeClass("in");
    });
}
BranchedResultDetailModule.prototype._tabbed = function(event) {
    var $tabHandle = $(event.currentTarget);
    if (this._index === $tabHandle.data(this._tabHandlesDataAttrName)) {
        return;
    }
    this._index = $tabHandle.data(this._tabHandlesDataAttrName);
    this._chart.activate(this._index);
}
BranchedResultDetailModule.prototype._activated = function(index) {
    if (this._index === index) {
        return;
    }
    this._index = index;
    this._$tabHandles.each(function(_index, tabHandle) {
        var $tabHandle = $(tabHandle);
        if ($tabHandle.data(this._tabHandlesDataAttrName) === this._index) {
            $tabHandle.tab("show");
            return false;
        }
    }.bind(this));
}
BranchedResultDetailModule.prototype.unMount = function() {
    this._$collapse.off("shown.bs.collapse", this._boundUncollapsed);
    this._$collapse.off("hidden.bs.collapse", this._boundCollapsed);
    this._$tabHandles.off("click", this._boundTabbed);
}
BranchedResultDetailModule.prototype.isMultiMount = true;
