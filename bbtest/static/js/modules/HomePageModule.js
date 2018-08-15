HomePageModule.prototype = Object.create(Module.prototype);
function HomePageModule(data) {
    this._charts = [];
    this._charts.push(new ProgressPieChart($(data.detail_chart_selector), [
        { "max-value": 60, "value": 50, "foreground-color": "#3366cc", "background-color": "#cdd8f1" },
        { "max-value": 40, "value": 25, "foreground-color": "#dc3912", "background-color": "#f6cdc5" },
        { "max-value": 60, "value": 55, "foreground-color": "#ff9900", "background-color": "#ffe6c7" },
        { "max-value": 40, "value": 30, "foreground-color": "#109618", "background-color": "#c5e5c9" },
        { "max-value": 60, "value": 55, "foreground-color": "#990099", "background-color": "#e5bfe5" },
        { "max-value": 60, "value": 40, "foreground-color": "#0099c6", "background-color": "#c5e5f0" },
        { "max-value": 40, "value": 30, "foreground-color": "#dd4477", "background-color": "#f6d0dd" },
        { "max-value": 40, "value": 40, "foreground-color": "#66aa00", "background-color": "#d9eac8" },
    ], {
        "duration": 2000,
        "chain-duration": 0,
        "activate-duration": 150,
        "hole-radius": "30%",
        "active-radius": "15%",
        "font-size": 18,
        "font-weight": "bold",
        "font-color": "#fff"
    }));
    this._charts.push(new ColumnChart($(data.progress_chart_selector), [ 30, 25, 35, 40, 20, 25, 30, 35, 50, 60 ], 60, {
        "line-width": 16,
        "line-color": "#3366cc",
        "line-background-color": "#cdd8f1",
        "font-size": 14
    }));

    this._windowActionTimer = null;
    this._chartsAreCreated = false;

    this._boundWindowScroll = this._windowScroll.bind(this);
    this._boundWindowScrollDone = this._windowScrollDone.bind(this);

    $(window).on("scroll", this._boundWindowScroll);

    if ($(window).width() < 768 || $(window).scrollTop() >= 600) {
        this._createCharts();
    }

    Module.call(this);
}
HomePageModule.prototype.unMount = function() {
    $(window).off("scroll", this._boundWindowScroll);

    clearTimeout(this._windowActionTimer);
    var i;
    for (i = 0; i < this._charts.length; i++) {
        this._charts[i].destroy();
    }
}
HomePageModule.prototype._createCharts = function() {
    if (this._chartsAreCreated) {
        return;
    }
    var i;
    for (i = 0; i < this._charts.length; i++) {
        this._charts[i].create();
    }
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
    if ($(window).scrollTop() >= 600) {
        this._createCharts();
    }
}
