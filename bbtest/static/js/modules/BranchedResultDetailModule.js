BranchedResultDetailModule.prototype = Object.create(Module.prototype);
function BranchedResultDetailModule(data) {
    this._$collapse = $(data.collapse_selector);
    this._$dropdown = $(data.dropdown_selector);
    this._$dropdownCaption = this._$dropdown.find(data.dropdown_caption_selector);
    this._tabHandlesDataAttrName = data.tab_handle_data_attr_name;
    this._$tabHandles = $("[data-" + this._tabHandlesDataAttrName + "]");
    this._$tabs = $(data.tab_selector);

    this._boundUncollapsed = this._uncollapsed.bind(this);
    this._boundCollapsed = this._collapsed.bind(this);
    this._boundTabbed = this._tabbed.bind(this);
    this._boundActivated = this._activated.bind(this);

    var max = 0;
    var score = 0;
    var detailChartData = [];
    var i;
    for (i = 0; i < data.branches.length; i++) {
        detailChartData.push({
            "max-value": data.branches[i].max,
            "value": data.branches[i].score,
            "foreground-color": data.branches[i].colors[0],
            "background-color": data.branches[i].colors[1],
            "active-callback-start": this._boundActivated
        });
        max += data.branches[i].max;
        score += data.branches[i].score;
    }

    this._index;
    this._summaryChart = new RadialChart($(data.summary_selector), score, max, {
        "line-width": 16,
        "arc-color": data.colors[0],
        "circle-color": data.colors[1],
        "font-size": 52
    });
    this._detailChart = new ProgressPieChart($(data.detail_selector), detailChartData, {
        "duration": 2000,
        "chain-duration": 0,
        "activate-duration": 150,
        "hole-radius": "20%",
        "active-radius": "10%",
        "font-size": 18,
        "font-weight": "bold",
        "font-color": "#fff",
        "percentage": true
    });
    this._progressChart = new ColumnChart($(data.progress_selector), data.progress, max, {
        "avg_value": data.avg,
        "padding-width": 4,
        "line-color": data.colors[0],
        "line-background-color": data.colors[1],
        "font-size": 14
    });

    this._$collapse.on("shown.bs.collapse", this._boundUncollapsed);
    this._$collapse.on("hidden.bs.collapse", this._boundCollapsed);
    this._$tabHandles.on("click", this._boundTabbed);

    Module.call(this);
}
BranchedResultDetailModule.prototype._uncollapsed = function() {
    this._summaryChart.create();
    this._detailChart.create();
    this._progressChart.create();

    this._detailChart.activate(0);
    this._$dropdown.addClass("in");
}
BranchedResultDetailModule.prototype._collapsed = function() {
    this._summaryChart.destroy();
    this._detailChart.destroy();
    this._progressChart.destroy();
    this._index = undefined;

    this._$dropdown.removeClass("in");
    this._$dropdownCaption.text("");
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
    this._detailChart.activate(this._index);
    this._updateDropdown(this._index);
}
BranchedResultDetailModule.prototype._activated = function(index) {
    if (this._index === index) {
        return;
    }
    this._index = index;
    this._updateDropdown(this._index);
}
BranchedResultDetailModule.prototype._updateDropdown = function(index) {
    var dropdownText = this._$tabHandles.filter("[data-" + this._tabHandlesDataAttrName + "=\"" + index + "\"]").text();
    this._$dropdownCaption.text(dropdownText);
    this._$tabs.each(function(_index) {
        if (_index === index) {
            $(this).addClass("active").addClass("in");
        } else {
            $(this).removeClass("active").removeClass("in");
        }
    });
    this._$tabHandles.each(function(_index, elem) {
        var $tabHandle = $(elem);
        if ($tabHandle.data(this._tabHandlesDataAttrName) === index) {
            $tabHandle.parent().addClass("active");
        } else {
            $tabHandle.parent().removeClass("active");
        }
    }.bind(this));
}
BranchedResultDetailModule.prototype.unMount = function() {
    this._$collapse.off("shown.bs.collapse", this._boundUncollapsed);
    this._$collapse.off("hidden.bs.collapse", this._boundCollapsed);
    this._$tabHandles.off("click", this._boundTabbed);

    this._collapsed();
    this._detailChart = undefined;
    this._progressChart = undefined;
}
BranchedResultDetailModule.prototype.isMultiMount = true;
