ColumnChart.prototype = Object.create(SVGChart.prototype);
function ColumnChart($container, values, max_value, options) {
    SVGChart.call(this, $container);

    this._options = {};
    this._options["duration"] = this._optionValue(options, "duration", 2000);
    this._options["chain-duration"] = this._optionValue(options, "chain-duration", 100);
    this._options["line-width"] = this._optionValue(options, "line-width", 6);
    this._options["line-color"] = this._optionValue(options, "line-color", "#2196f3");
    this._options["line-background-color"] = this._optionValue(options, "line-background-color", "#cae6fc");
    this._options["font-size"] = this._optionValue(options, "font-size", 20);
    this._options["font-color"] = this._optionValue(options, "font-color", "#444444");
    this._options["padding-right"] = this._optionValue(options, "padding-right", 15);
    this._options["padding-left"] = this._optionValue(options, "padding-left", 15);
    this._options["round-linecap"] = true;

    this._values = values;
    this._max_value = max_value;
    this._shift_y = 0;
    if (this._options["round-linecap"]) {
        this._shift_y = this._options["line-width"] / 2;
    }
    this._timers = [];
    this._helpers = [];
}
ColumnChart.prototype._svg = function($container) {
    var start_x = this._options["padding-left"] + this._options["line-width"] / 2;
    var end_x = $container.width() - this._options["padding-right"] - this._options["line-width"] / 2;

    var svg = this._createElement("svg", {
        "width": "100%",
        "height": "100%"
    });

    var step_x = (end_x - start_x) / (this._values.length - 1);
    for (var i = 0; i < this._values.length; i++) {
        var group = this._createElement("g", {
            "transform": "translate(" + [
                start_x,
                $container.height()
            ].join() + ") rotate(180)"
        });

        group.appendChild(this._createElement("path", {
            "d": this._d([
                [ "M", [ 0, this._shift_y ] ],
                [ "L", [ 0, $container.height() - this._shift_y ] ]
            ]),
            "fill": "none",
            "stroke": this._options["line-background-color"],
            "stroke-width": this._options["line-width"],
            "stroke-linecap": this._options["round-linecap"] ? "round" : "butt"
        }));

        if (this._values[i] > 0) {
            var path = this._createElement("path", {
                "d": this._d([
                    [ "M", [ 0, this._shift_y ] ],
                    [ "L", [ 0, this._shift_y ] ]
                ]),
                "fill": "none",
                "stroke": this._options["line-color"],
                "stroke-width": this._options["line-width"],
                "stroke-linecap": this._options["round-linecap"] ? "round" : "butt"
            });
            this._helpers.push(new _ColumnChartHelper(this, $(path), this._values[i], $container));
            group.appendChild(path);
        }

        svg.append(group);
        start_x += step_x;
    }

    return svg;
}
ColumnChart.prototype._afterDraw = function() {
    if (this._helpers.length > 0) {
        this._scheduleNextHelper(0);
    }
}
ColumnChart.prototype._beforeErase = function() {
    var obj;
    while (obj = this._timers.pop()) {
        clearTimeout(obj);
    }
    while (obj = this._helpers.pop()) {
        obj.stop_animation();
    }
}
ColumnChart.prototype._scheduleNextHelper = function(index) {
    if (index >= this._helpers.length) {
        return;
    }
    this._timers.push(setTimeout((function() {
        this._helpers[index].start_animation();
        this._scheduleNextHelper(index + 1);
    }).bind(this), this._options["chain-duration"]));
}

function _ColumnChartHelper(column_chart, $path, value, $container) {
    this._column_chart = column_chart;
    this._$path = $path;
    this._value = value;
    this._$container = $container;
}
_ColumnChartHelper.prototype.start_animation = function() {
    this._$path.animate({
        "_progress": 1
    }, {
        "duration": this._column_chart._options["duration"],
        "easing": "easeOutQuart",
        "step": this._render_column.bind(this)
    });
}
_ColumnChartHelper.prototype.stop_animation = function() {
    this._$path.stop(true);
}
_ColumnChartHelper.prototype._render_column = function(percentage) {
    var current_value = this._value * percentage;
    current_value = Math.min(current_value, this._column_chart._max_value) / this._column_chart._max_value * this._$container.height();
    current_value = Math.max(current_value - this._column_chart._shift_y, this._column_chart._shift_y);
    this._$path.attr("d", this._column_chart._d([
        [ "M", [ 0, this._column_chart._shift_y ] ],
        [ "L", [ 0, current_value ] ]
    ]));
}
