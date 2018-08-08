ColumnChart.prototype = Object.create(SVGChart.prototype);
function ColumnChart($container, values, max_value, options) {
    this._options = {};

    this._options["avg_value"] = this._optionValue(options, "avg_value", 0);

    this._options["duration"] = this._optionValue(options, "duration", 2000);
    this._options["chain-duration"] = this._optionValue(options, "chain-duration", 100);
    this._options["line-width"] = this._optionValue(options, "line-width", 6);
    this._options["line-color"] = this._optionValue(options, "line-color", "#2196f3");
    this._options["line-background-color"] = this._optionValue(options, "line-background-color", "#cae6fc");
    this._options["font-size"] = this._optionValue(options, "font-size", 20);
    this._options["font-weight"] = this._optionValue(options, "font-weight", "normal");
    this._options["font-color"] = this._optionValue(options, "font-color", "#444444");
    this._options["padding-right"] = this._optionValue(options, "padding-right", 15);
    this._options["padding-left"] = this._optionValue(options, "padding-left", 15);
    this._options["round-linecap"] = false;

    this._values = values;
    this._max_value = max_value;
    this._shift_y = 0;
    if (this._options["round-linecap"]) {
        this._shift_y = this._options["line-width"] / 2;
    }
    this._timers = [];
    this._helpers = [];

    SVGChart.call(this, $container);
}
ColumnChart.prototype._afterCreate = function(svg) {
    var texts = [];

    var text = this._createElement("text", {
        "x": 0,
        "y": 0,
        "text-anchor": "end",
        "dominant-baseline": "text-before-edge",
        "font-size": this._options["font-size"],
        "font-weight": this._options["font-weight"],
        "fill": this._options["font-color"]
    });
    text.appendChild(document.createTextNode(this._max_value.toString()));
    svg.appendChild(text);
    texts.push(text);

    var text_num = parseInt(($(svg).height() / text.getBBox().height + 2) / 3);
    var text_step = $(svg).height() / (text_num - 1);
    var text_value_step = this._max_value / (text_num - 1);
    for (var i = text_num - 2; i > 0; i--) {
        text = this._createElement("text", {
            "x": 0,
            "y": text_step * (text_num - 1 - i),
            "text-anchor": "end",
            "dominant-baseline": "central",
            "font-size": this._options["font-size"],
            "font-weight": this._options["font-weight"],
            "fill": this._options["font-color"]
        });
        text.appendChild(document.createTextNode(Math.round(text_value_step * i)));
        svg.appendChild(text);
        texts.push(text);
    }

    text = this._createElement("text", {
        "x": 0,
        "y": $(svg).height(),
        "text-anchor": "end",
        "dominant-baseline": "text-after-edge",
        "font-size": this._options["font-size"],
        "font-weight": this._options["font-weight"],
        "fill": this._options["font-color"]
    });
    text.appendChild(document.createTextNode("0"));
    svg.appendChild(text);
    texts.push(text);

    var max_text_width = 0;
    for (var i = 0; i < texts.length; i++) {
        max_text_width = Math.max(texts[i].getBBox().width, max_text_width);
    }
    for (var i = 0; i < texts.length; i++) {
        texts[i].setAttributeNS(null, "x", max_text_width);
    }

    var current_x = max_text_width + this._options["padding-left"] + this._options["line-width"] / 2;
    var step_x = ($(svg).width() - this._options["padding-right"] - this._options["line-width"] / 2 - current_x) / (this._values.length - 1);
    for (var i = 0; i < this._values.length; i++) {
        var group = this._createElement("g", {
            "transform": "translate(" + [
                current_x,
                $(svg).height()
            ].join() + ") rotate(180)"
        });

        group.appendChild(this._createElement("path", {
            "d": this._d([
                [ "M", [ 0, this._shift_y ] ],
                [ "L", [ 0, $(svg).height() - this._shift_y ] ]
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
            this._helpers.push(new _ColumnChartHelper(this, $(path), this._values[i], $(svg)));
            group.appendChild(path);
        }

        svg.append(group);
        current_x += step_x;
    }

    if (this._options["avg_value"] > 0) {
        var avg_y = $(svg).height() - Math.min(this._options["avg_value"], this._max_value) * $(svg).height() / this._max_value;
        var avg_start_x = max_text_width + this._options["padding-left"] / 2;
        var avg_end_x = $(svg).width() - this._options["padding-right"] / 2;
        if (this._options["round-linecap"]) {
            avg_start_x += 1;
            avg_end_x -= 1;
        }
        svg.append(this._createElement("path", {
            "d": this._d([
                [ "M", [ avg_start_x, avg_y ] ],
                [ "L", [ avg_end_x, avg_y ] ]
            ]),
            "fill": "none",
            "stroke": "#ff0000",
            "stroke-width": 2,
            "stroke-opacity": 0.4,
            "stroke-linecap": this._options["round-linecap"] ? "round" : "butt"
        }));
    }

    if (this._helpers.length > 0) {
        this._scheduleNextHelper(0);
    }
}
ColumnChart.prototype._beforeDestroy = function(svg) {
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
