ProgressPieChart.prototype = Object.create(SVGChart.prototype);
function ProgressPieChart($container, values, options) {
    this._options = {};

    this._options["duration"] = this._optionValue(options, "duration", 2000);
    this._options["chain-duration"] = this._optionValue(options, "chain-duration", 100);
    this._options["activate-duration"] = this._optionValue(options, "activate-duration", 500);
    this._options["active-radius"] = this._optionValue(options, "active-radius", "20%");
    this._options["font-size"] = this._optionValue(options, "font-size", 20);
    this._options["font-weight"] = this._optionValue(options, "font-weight", "normal");
    this._options["font-color"] = this._optionValue(options, "font-color", "#ffffff");

    this._values = [];
    var value;
    var total = 0;
    while (value = values.shift()) {
        var _value = {};
        _value["max-value"] = this._optionValue(value, "max-value", 100);
        _value["value"] = Math.min(Math.max(this._optionValue(value, "value", _value["max-value"]), 0), _value["max-value"]);
        _value["foreground-color"] = this._optionValue(value, "foreground-color", "#888888");
        _value["background-color"] = this._optionValue(value, "background-color", "#cccccc");
        _value["active-callback"] = this._optionValue(value, "active-callback", null);
        this._values.push(_value);
        total += _value["max-value"];
    }
    this._angles = [];
    for (var i = 0; i < this._values.length; i++) {
        this._angles.push(this._values[i]["max-value"] / total * 360);
    }

    this._timers = [];
    this._helpers = [];

    SVGChart.call(this, $container);
}
ProgressPieChart.prototype.activate = function(index) {
    if (index >= 0 && index < this._helpers.length) {
        this._helpers[index].activate();
    }
}
ProgressPieChart.prototype._afterCreate = function(svg) {
    var size = Math.min($(svg).width(), $(svg).height());
    var outer_radius = size / 2;
    this._inner_radius = 0;
    var inner_radius_set = false;
    if (isNaN(parseInt(this._options["active-radius"]))) {
        inner_radius_set = true;
    }
    if (!inner_radius_set && typeof this._options["active-radius"] === "string") {
        if (this._options["active-radius"][this._options["active-radius"].length-1] === "%") {
            this._inner_radius = parseInt(this._options["active-radius"].slice(0, this._options["active-radius"].length-1)) / 100 * outer_radius;
            inner_radius_set = true;
        }
    }
    if (!inner_radius_set) {
        this._inner_radius = parseInt(this._options["active-radius"]);
    }
    this._inner_radius = Math.min(Math.max(this._inner_radius, 0), outer_radius);
    this._radius = outer_radius - this._inner_radius;

    var group1 = this._createElement("g", {
        "transform": "translate(" + [
            size / 2 + ($(svg).width() - size) / 2,
            size / 2 + ($(svg).height() - size) / 2
        ].join() + ")"
    });

    var current_angle = -90;
    for (var i = 0; i < this._values.length; i++) {
        var group2 = this._createElement("g", {
            "transform": "rotate(" + current_angle + ")"
        });

        var group3 = this._createElement("g", {
            "transform": "translate(0,0)",
            "cursor": "pointer"
        });

        group3.appendChild(this._createElement("path", {
            "d": this._d([
                [ "M", [ 0, 0 ] ],
                [ "L", [ this._radius, 0 ] ],
                [ "A", [
                    this._radius,
                    this._radius,
                    0,
                    this._angles[i] >= 180 ? 1 : 0,
                    1,
                    this._radius * Math.cos(this._deg2rad(this._angles[i])),
                    this._radius * Math.sin(this._deg2rad(this._angles[i]))
                ] ],
                [ "L", [ 0, 0 ] ],
                [ "Z", [] ]
            ]),
            "fill": this._values[i]["background-color"]
        }));

        var path = this._createElement("path", {
            "d": this._d([
                [ "M", [ 0, 0 ] ],
                [ "L", [ 0, 0 ] ],
                [ "A", [
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0
                ] ],
                [ "L", [ 0, 0 ] ],
                [ "Z", [] ]
            ]),
            "fill": this._values[i]["foreground-color"]
        });
        group3.appendChild(path);

        var text_x = (this._radius * 0.75) * Math.cos(this._deg2rad(this._angles[i] / 2));
        var text_y = (this._radius * 0.75) * Math.sin(this._deg2rad(this._angles[i] / 2));
        var group4 = this._createElement("g", {
            "transform": "rotate(" + [
                -current_angle,
                text_x,
                text_y
            ].join(" ") + ")"
        });
        var text = this._createElement("text", {
            "x": text_x,
            "y": text_y,
            "text-anchor": "middle",
            "dominant-baseline": "central",
            "font-size": this._options["font-size"],
            "font-weight": this._options["font-weight"],
            "fill": this._options["font-color"]
        });
        text.appendChild(document.createTextNode("Monkey!"));
        group4.appendChild(text);
        group3.appendChild(group4);

        group2.appendChild(group3);
        group1.appendChild(group2);

        current_angle += this._angles[i];
        this._helpers.push(new _ProgressPieChartHelper(this, i, $(path), $(group3)));
    }

    svg.appendChild(group1);

    if (this._helpers.length > 0) {
        this._scheduleNextHelper(0);
    }
}
ProgressPieChart.prototype._beforeDestroy = function(svg) {
    var obj;
    while (obj = this._timers.pop()) {
        clearTimeout(obj);
    }
    while (obj = this._helpers.pop()) {
        obj.stop_animation();
    }
}
ProgressPieChart.prototype._scheduleNextHelper = function(index) {
    if (index >= this._helpers.length) {
        return;
    }
    this._timers.push(setTimeout((function() {
        this._helpers[index].start_animation();
        this._scheduleNextHelper(index + 1);
    }).bind(this), this._options["chain-duration"]));
}

function _ProgressPieChartHelper(progress_pie_chart, index, $path, $group) {
    this._progress_pie_chart = progress_pie_chart;
    this._index = index;
    this._$path = $path;
    this._$group = $group;

    this._is_active = false;
    this._$group.on("click", this.activate.bind(this));
}
_ProgressPieChartHelper.prototype.activate = function() {
    if (this._is_active) {
        return;
    }
    for (var i = 0; i < this._progress_pie_chart._helpers.length; i++) {
        if (i != this._index) {
            this._progress_pie_chart._helpers[i].deactivate();
        }
    }
    this._is_active = true;
    this._$group.animate({
        "_progress": 1
    }, {
        "duration": this._progress_pie_chart._options["activate-duration"],
        "step": this._render_activation.bind(this),
        "complete": this._activation_complete.bind(this)
    });
}
_ProgressPieChartHelper.prototype.deactivate = function() {
    if (!this._is_active) {
        return;
    }
    this._is_active = false;
    this._$group.animate({
        "_progress": 0
    }, {
        "duration": this._progress_pie_chart._options["activate-duration"],
        "step": this._render_activation.bind(this)
    });
}
_ProgressPieChartHelper.prototype.start_animation = function() {
    this._$path.animate({
        "_progress": 1
    }, {
        "duration": this._progress_pie_chart._options["duration"],
        "easing": "easeOutQuart",
        "step": this._render_pie.bind(this)
    });
}
_ProgressPieChartHelper.prototype.stop_animation = function() {
    this._$path.stop(true);
    this._$group.stop(true);
    this._$group.off("click", this.activate.bind(this));
}
_ProgressPieChartHelper.prototype._render_pie = function(percentage) {
    var rad_angle = this._progress_pie_chart._deg2rad(this._progress_pie_chart._angles[this._index]);
    var max_area = rad_angle / 2 * Math.pow(this._progress_pie_chart._radius, 2) * (
        this._progress_pie_chart._values[this._index]["value"] / this._progress_pie_chart._values[this._index]["max-value"]
    );
    var radius = Math.sqrt(2 * max_area * percentage / rad_angle);

    this._$path.attr("d", this._progress_pie_chart._d([
        [ "M", [ 0, 0 ] ],
        [ "L", [ radius, 0 ] ],
        [ "A", [
            radius,
            radius,
            0,
            rad_angle >= Math.PI ? 1 : 0,
            1,
            radius * Math.cos(rad_angle),
            radius * Math.sin(rad_angle)
        ] ],
        [ "L", [ 0, 0 ] ],
        [ "Z", [] ]
    ]));
}
_ProgressPieChartHelper.prototype._render_activation = function(percentage) {
    this._$group.attr("transform", "translate(" + [
        Math.cos(this._progress_pie_chart._deg2rad(this._progress_pie_chart._angles[this._index] / 2)) * this._progress_pie_chart._inner_radius * percentage,
        Math.sin(this._progress_pie_chart._deg2rad(this._progress_pie_chart._angles[this._index] / 2)) * this._progress_pie_chart._inner_radius * percentage
    ] + ")");
}
_ProgressPieChartHelper.prototype._activation_complete = function() {
    if (this._progress_pie_chart._values[this._index]["active-callback"]) {
        this._progress_pie_chart._values[this._index]["active-callback"](this._index);
    }
}
