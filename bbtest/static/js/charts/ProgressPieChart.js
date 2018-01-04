ProgressPieChart.prototype = Object.create(SVGChart.prototype);
function ProgressPieChart($container, values, options) {
    this._options = {};

    this._options["duration"] = this._optionValue(options, "duration", 2000);
    this._options["chain-duration"] = this._optionValue(options, "chain-duration", 100);
    this._options["activate-duration"] = this._optionValue(options, "activate-duration", 500);
    this._options["hole-radius"] = this._optionValue(options, "hole-radius", "10%");
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
        _value["active-callback-start"] = this._optionValue(value, "active-callback-start", null);
        _value["active-callback-complete"] = this._optionValue(value, "active-callback-complete", null);
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
    this._active_radius = Math.min(this._optionalPercentageValue(this._options["active-radius"], outer_radius), outer_radius);
    this._hole_radius = Math.min(this._optionalPercentageValue(this._options["hole-radius"], outer_radius), outer_radius);
    this._radius = outer_radius - this._active_radius;

    var group1 = this._createElement("g", {
        "transform": "translate(" + [
            size / 2 + ($(svg).width() - size) / 2,
            size / 2 + ($(svg).height() - size) / 2
        ].join() + ")"
    });

    var current_angle = -90;
    var texts = [];
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
                [ "M", [ this._hole_radius, 0 ] ],
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
                [ "L", [
                    this._hole_radius * Math.cos(this._deg2rad(this._angles[i])),
                    this._hole_radius * Math.sin(this._deg2rad(this._angles[i]))
                ] ],
                [ "A", [
                    this._hole_radius,
                    this._hole_radius,
                    0,
                    this._angles[i] >= 180 ? 1 : 0,
                    0,
                    this._hole_radius,
                    0
                ] ],
                [ "Z", [] ]
            ]),
            "fill": this._values[i]["background-color"]
        }));

        var path = this._createElement("path", {
            "d": this._d([
                [ "M", [ this._hole_radius, 0 ] ],
                [ "L", [ this._hole_radius, 0 ] ],
                [ "A", [
                    this._hole_radius,
                    this._hole_radius,
                    0,
                    this._angles[i] >= 180 ? 1 : 0,
                    1,
                    this._hole_radius * Math.cos(this._deg2rad(this._angles[i])),
                    this._hole_radius * Math.sin(this._deg2rad(this._angles[i]))
                ] ],
                [ "L", [
                    this._hole_radius * Math.cos(this._deg2rad(this._angles[i])),
                    this._hole_radius * Math.sin(this._deg2rad(this._angles[i]))
                ] ],
                [ "A", [
                    this._hole_radius,
                    this._hole_radius,
                    0,
                    this._angles[i] >= 180 ? 1 : 0,
                    0,
                    this._hole_radius,
                    0
                ] ],
                [ "Z", [] ]
            ]),
            "fill": this._values[i]["foreground-color"]
        });
        group3.appendChild(path);

        var group4 = this._createElement("g", {
            "transform": "translate(" + [
                (this._radius - (this._radius - this._hole_radius) / 2) * Math.cos(this._deg2rad(this._angles[i] / 2)),
                (this._radius - (this._radius - this._hole_radius) / 2) * Math.sin(this._deg2rad(this._angles[i] / 2))
            ].join() + ")" + "rotate(" + (-current_angle) + ")"
        });
        var text1 = this._createElement("text", {
            "x": 0,
            "y": 0,
            "text-anchor": "middle",
            "dominant-baseline": "central",
            "font-size": this._options["font-size"],
            "font-weight": this._options["font-weight"],
            "fill": this._options["font-color"],
            "style": "text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);"
        });
        text1.appendChild(document.createTextNode("0"));
        var text2 = this._createElement("text", {
            "x": 0,
            "y": 0,
            "text-anchor": "middle",
            "dominant-baseline": "central",
            "font-size": Math.max(this._options["font-size"] * 0.75, 1),
            "font-weight": this._options["font-weight"],
            "fill": this._options["font-color"],
            "style": "text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);"
        });
        text2.appendChild(document.createTextNode("──"));
        var text3 = this._createElement("text", {
            "x": 0,
            "y": 0,
            "text-anchor": "middle",
            "dominant-baseline": "central",
            "font-size": Math.max(this._options["font-size"] * 0.75, 1),
            "font-weight": this._options["font-weight"],
            "fill": this._options["font-color"],
            "style": "text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);"
        });
        text3.appendChild(document.createTextNode(this._values[i]["max-value"]));
        group4.appendChild(text1);
        group4.appendChild(text2);
        group4.appendChild(text3);
        texts.push([
            text1,
            text3
        ]);

        group3.appendChild(group4);

        group2.appendChild(group3);
        group1.appendChild(group2);

        current_angle += this._angles[i];
        this._helpers.push(new _ProgressPieChartHelper(this, i, $(path), $(group3), $(text1)));
    }

    svg.appendChild(group1);

    for (var i = 0; i < texts.length; i++) {
        $(texts[i][0]).attr("y", -(texts[i][0].getBBox().height / 2));
        $(texts[i][1]).attr("y", texts[i][1].getBBox().height / 2);
    }

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
ProgressPieChart.prototype._isInspected = function() {
    for (var i = 0; i < this._helpers.length; i++) {
        if (this._helpers[i]._is_active) {
            return true;
        }
    }
    return false;
}

function _ProgressPieChartHelper(progress_pie_chart, index, $path, $group, $text) {
    this._progress_pie_chart = progress_pie_chart;
    this._index = index;
    this._$path = $path;
    this._$group = $group;
    this._$text = $text;

    this._is_active = false;
    this._activation_timer = null;
    this._$group[0]._progress1 = 1;

    this._boundActivate = this.activate.bind(this);

    this._$group.on("click", this._boundActivate);
}
_ProgressPieChartHelper.prototype.activate = function(event) {
    if (event !== undefined) {
        event.stopPropagation();
    }
    if (this._is_active) {
        this._is_active = false;
    } else {
        this._is_active = true;
    }

    for (var i = 0; i < this._progress_pie_chart._helpers.length; i++) {
        if (i != this._index || (i == this._index && !this._is_active)) {
            this._progress_pie_chart._helpers[i].deactivate();
        }
    }

    if (!this._is_active) {
        return;
    }

    if (this._progress_pie_chart._values[this._index]["active-callback-start"]) {
        this._progress_pie_chart._values[this._index]["active-callback-start"](this._index);
    }
    clearTimeout(this._activation_timer);
    this._activation_timer = setTimeout(function() {
        this._$group.stop(true).animate({
            "_progress0": 1,
            "_progress1": 1
        }, {
            "duration": this._progress_pie_chart._options["activate-duration"],
            "step": this._render_activation.bind(this),
            "complete": this._activation_complete.bind(this)
        });
    }.bind(this));
}
_ProgressPieChartHelper.prototype.deactivate = function() {
    this._is_active = false;

    clearTimeout(this._activation_timer);
    this._activation_timer = setTimeout(function() {
        this._$group.stop(true).animate({
            "_progress0": 0,
            "_progress1": this._progress_pie_chart._isInspected() ? 0 : 1
        }, {
            "duration": this._progress_pie_chart._options["activate-duration"],
            "step": this._render_activation.bind(this)
        });
    }.bind(this));
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
    clearTimeout(this._activation_timer);
    this._$path.stop(true);
    this._$group.stop(true);
    this._$group.off("click", this._boundActivate);
}
_ProgressPieChartHelper.prototype._render_pie = function(percentage) {
    var rad_angle = this._progress_pie_chart._deg2rad(this._progress_pie_chart._angles[this._index]);
    var max_area = rad_angle / 2 * (
        Math.pow(this._progress_pie_chart._radius, 2) - Math.pow(this._progress_pie_chart._hole_radius, 2)
    ) * (
        this._progress_pie_chart._values[this._index]["value"] / this._progress_pie_chart._values[this._index]["max-value"]
    );
    var radius = Math.sqrt(
        (
            2 * max_area * percentage + (rad_angle * Math.pow(this._progress_pie_chart._hole_radius, 2))
        ) / rad_angle
    );

    this._$text.text(Math.round(this._progress_pie_chart._values[this._index]["value"] * percentage));
    this._$path.attr("d", this._progress_pie_chart._d([
        [ "M", [ this._progress_pie_chart._hole_radius, 0 ] ],
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
        [ "L", [
            this._progress_pie_chart._hole_radius * Math.cos(rad_angle),
            this._progress_pie_chart._hole_radius * Math.sin(rad_angle)
        ] ],
        [ "A", [
            this._progress_pie_chart._hole_radius,
            this._progress_pie_chart._hole_radius,
            0,
            rad_angle >= Math.PI ? 1 : 0,
            0,
            this._progress_pie_chart._hole_radius,
            0
        ] ],
        [ "Z", [] ]
    ]));
}
_ProgressPieChartHelper.prototype._render_activation = function(percentage, tween) {
    if (tween.prop == "_progress0") {
        this._$group.attr("transform", "translate(" + [
            Math.cos(this._progress_pie_chart._deg2rad(this._progress_pie_chart._angles[this._index] / 2)) * this._progress_pie_chart._active_radius * percentage,
            Math.sin(this._progress_pie_chart._deg2rad(this._progress_pie_chart._angles[this._index] / 2)) * this._progress_pie_chart._active_radius * percentage
        ] + ")");
    } else if (tween.prop == "_progress1") {
        this._$group.attr("opacity", 0.5 + (0.5 * percentage));
    }
}
_ProgressPieChartHelper.prototype._activation_complete = function() {
    if (this._progress_pie_chart._values[this._index]["active-callback-complete"]) {
        this._progress_pie_chart._values[this._index]["active-callback-complete"](this._index);
    }
}
