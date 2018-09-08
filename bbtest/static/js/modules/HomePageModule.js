HomePageModule.prototype = Object.create(Module.prototype);
function HomePageModule(data) {
    this._windowActionTimer = null;
    this._chartsAreCreated = false;
    this._progressChartIndex = 0;
    this._scrollThreshold = 300;

    this._boundWindowScroll = this._windowScroll.bind(this);
    this._boundWindowScrollDone = this._windowScrollDone.bind(this);
    this._boundActivated = this._activated.bind(this);

    this._pieChart = new ProgressPieChart($(data.detail_chart_selector), [
        { "max-value": 60, "value": 50, "foreground-color": "#3366cc", "background-color": "#cdd8f1", "active-callback-start": this._boundActivated },
        { "max-value": 40, "value": 25, "foreground-color": "#dc3912", "background-color": "#f6cdc5", "active-callback-start": this._boundActivated },
        { "max-value": 60, "value": 55, "foreground-color": "#ff9900", "background-color": "#ffe6c7", "active-callback-start": this._boundActivated },
        { "max-value": 40, "value": 30, "foreground-color": "#109618", "background-color": "#c5e5c9", "active-callback-start": this._boundActivated },
        { "max-value": 60, "value": 55, "foreground-color": "#990099", "background-color": "#e5bfe5", "active-callback-start": this._boundActivated },
        { "max-value": 60, "value": 40, "foreground-color": "#0099c6", "background-color": "#c5e5f0", "active-callback-start": this._boundActivated },
        { "max-value": 40, "value": 30, "foreground-color": "#dd4477", "background-color": "#f6d0dd", "active-callback-start": this._boundActivated },
        { "max-value": 40, "value": 40, "foreground-color": "#66aa00", "background-color": "#d9eac8", "active-callback-start": this._boundActivated },
    ], {
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
    this._progressCharts = [];
    this._progressCharts.push(new ColumnChart($(data.progress_chart_selector), [ 30, 25, 35, 40, 20, 25, 30, 35, 45, 50 ], 60, {
        "padding-width": 4,
        "line-color": "#3366cc",
        "line-background-color": "#cdd8f1",
        "font-size": 14,
        "percentage": true
    }));
    this._progressCharts.push(new ColumnChart($(data.progress_chart_selector), [ 10, 15, 20, 25, 30, 35, 40, 35, 30, 25 ], 40, {
        "padding-width": 4,
        "line-color": "#dc3912",
        "line-background-color": "#f6cdc5",
        "font-size": 14,
        "percentage": true
    }));
    this._progressCharts.push(new ColumnChart($(data.progress_chart_selector), [ 50, 45, 35, 40, 55, 50, 45, 50, 55, 55 ], 60, {
        "padding-width": 4,
        "line-color": "#ff9900",
        "line-background-color": "#ffe6c7",
        "font-size": 14,
        "percentage": true
    }));
    this._progressCharts.push(new ColumnChart($(data.progress_chart_selector), [ 30, 30, 35, 40, 35, 25, 20, 35, 40, 30 ], 40, {
        "padding-width": 4,
        "line-color": "#109618",
        "line-background-color": "#c5e5c9",
        "font-size": 14,
        "percentage": true
    }));
    this._progressCharts.push(new ColumnChart($(data.progress_chart_selector), [ 30, 40, 45, 50, 55, 60, 50, 45, 50, 55 ], 60, {
        "padding-width": 4,
        "line-color": "#990099",
        "line-background-color": "#e5bfe5",
        "font-size": 14,
        "percentage": true
    }));
    this._progressCharts.push(new ColumnChart($(data.progress_chart_selector), [ 30, 60, 55, 40, 20, 25, 30, 50, 45, 40 ], 60, {
        "padding-width": 4,
        "line-color": "#0099c6",
        "line-background-color": "#c5e5f0",
        "font-size": 14,
        "percentage": true
    }));
    this._progressCharts.push(new ColumnChart($(data.progress_chart_selector), [ 30, 25, 30, 15, 20, 30, 25, 30, 35, 30 ], 40, {
        "padding-width": 4,
        "line-color": "#dd4477",
        "line-background-color": "#f6d0dd",
        "font-size": 14,
        "percentage": true
    }));
    this._progressCharts.push(new ColumnChart($(data.progress_chart_selector), [ 13, 16, 19, 22, 25, 28, 31, 34, 37, 40 ], 40, {
        "padding-width": 4,
        "line-color": "#66aa00",
        "line-background-color": "#d9eac8",
        "font-size": 14,
        "percentage": true
    }));

    $(window).on("scroll", this._boundWindowScroll);

    if ($(window).width() < 768 || $(window).scrollTop() >= this._scrollThreshold) {
        this._createCharts();
    }

    Module.call(this);
}
HomePageModule.prototype.unMount = function() {
    $(window).off("scroll", this._boundWindowScroll);

    clearTimeout(this._windowActionTimer);
    this._pieChart.destroy();
    this._progressCharts[this._progressChartIndex].destroy();
}
HomePageModule.prototype._createCharts = function() {
    if (this._chartsAreCreated) {
        return;
    }
    this._pieChart.create();
    this._progressCharts[this._progressChartIndex].create();
    this._chartsAreCreated = true;
}
HomePageModule.prototype._windowScroll = function() {
    clearTimeout(this._windowActionTimer);
    this._windowActionTimer = setTimeout(this._boundWindowScrollDone, 10);
}
HomePageModule.prototype._windowScrollDone = function() {
    if ($(window).width() < 768) {
        return;
    }
    if ($(window).scrollTop() >= this._scrollThreshold) {
        this._createCharts();
    }
}
HomePageModule.prototype._activated = function(index) {
    if (this._progressChartIndex === index) {
        return;
    }
    this._progressCharts[this._progressChartIndex].destroy();
    this._progressChartIndex = index;
    this._progressCharts[this._progressChartIndex].create();
}
