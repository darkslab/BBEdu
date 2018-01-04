RadialChart.prototype = Object.create(SVGChart.prototype);
function RadialChart($container, value, max_value, options) {
    this._options = {};

    this._options["duration"] = this._optionValue(options, "duration", 2000);
    this._options["line-width"] = this._optionValue(options, "line-width", 6);
    this._options["circle-color"] = this._optionValue(options, "circle-color", "#cae6fc");
    this._options["arc-color"] = this._optionValue(options, "arc-color", "#2196f3");
    this._options["font-size"] = this._optionValue(options, "font-size", "auto");
    this._options["font-weight"] = this._optionValue(options, "font-weight", "normal");
    this._options["font-color"] = this._optionValue(options, "font-color", "#444444");
    this._options["percentage-first"] = this._optionValue(options, "percentage-first", false);
    this._options["round-linecap"] = true;

    this._value = value;
    this._max_value = max_value;
    this._$arc = null;
    this._$text = null;

    this._boundToggleText = this._toggleText.bind(this);

    SVGChart.call(this, $container);
}
RadialChart.prototype._afterCreate = function(svg) {
    var size = Math.min($(svg).width(), $(svg).height());
    this._radius = (size - this._options["line-width"]) / 2;
    this._max_angle = 2 * Math.PI * this._value / this._max_value - 0.001;
    if (this._options["round-linecap"]) {
        this._max_angle = ((2 * Math.PI * this._radius - this._options["line-width"]) / this._radius) * this._value / this._max_value;
    }

    var group = this._createElement("g", {
        "transform": "translate(" + [
            size / 2 + ($(svg).width() - size) / 2,
            size / 2 + ($(svg).height() - size) / 2
        ].join() + ")"
    });

    group.appendChild(this._createElement("circle", {
        "cx": 0,
        "cy": 0,
        "r": this._radius,
        "fill": "none",
        "stroke": this._options["circle-color"],
        "stroke-width": this._options["line-width"]
    }));

    var path = this._createElement("path", {
        "d": "M0 0",
        "fill": "none",
        "stroke": this._options["arc-color"],
        "stroke-width": this._options["line-width"],
        "stroke-linecap": this._options["round-linecap"] ? "round" : "butt"
    });
    this._$arc = $(path);
    group.appendChild(path);

    var text = this._createElement("text", {
        "x": 0,
        "y": 0,
        "text-anchor": "middle",
        "dominant-baseline": "central",
        "font-size": this._options["font-size"] === "auto" ? this._radius * 0.4 : this._options["font-size"],
        "font-weight": this._options["font-weight"],
        "fill": this._options["font-color"],
        "cursor": "pointer"
    });
    this._$text = $(text);
    group.appendChild(text);

    svg.appendChild(group);

    this._$text.on("click", this._boundToggleText);

    this._animation_complete = false;
    this._$arc.animate({
        "_progress": 1
    }, {
        "duration": this._options["duration"],
        "easing": "easeOutQuart",
        "step": this._render_arc.bind(this),
        "complete": function() {
            this._animation_complete = true;
        }.bind(this)
    });
}
RadialChart.prototype._beforeDestroy = function(svg) {
    this._$arc.stop(true);
    this._$text.off("click", this._boundToggleText);
    this._$arc = null;
}
RadialChart.prototype._render_arc = function(percentage) {
    var angle = -(this._max_angle * percentage + Math.PI / 2);
    this._$arc.attr("d", this._d([
        [ "M", [ 0, this._radius ] ],
        [ "A", [
            this._radius,
            this._radius,
            0,
            angle >= -(3 / 2 * Math.PI) ? 0 : 1,
            1,
            this._radius * Math.cos(angle),
            -(this._radius * Math.sin(angle))
        ] ]
    ]));
    this._$text.text(this._getText(percentage));
}
RadialChart.prototype._getText = function(percentage) {
    var text = "";
    if (this._options["percentage-first"]) {
        text += Math.round(this._value / this._max_value * 100 * percentage) + "%";
    } else {
        text += Math.round(this._value * percentage);
    }
    return text;
}
RadialChart.prototype._toggleText = function(event) {
    event.stopPropagation();
    this._options["percentage-first"] = !this._options["percentage-first"];
    if (this._animation_complete) {
        this._$text.text(this._getText(1));
    }
}
