/**
 * DARK_TODO
 * - redo linecap, so 100% value would result in 1 pixel touch
 * - use _d() method
 * - .stop(true) is enough
 * - _optionValue
 */

RadialChart.prototype = Object.create(SVGChart.prototype);
function RadialChart($container, value, max_value, options) {
    SVGChart.call(this, $container);

    this._options = {};
    this._options["duration"] = (options && options["duration"]) || 2000;
    this._options["line-width"] = (options && options["line-width"]) || 6;
    this._options["circle-color"] = (options && options["circle-color"]) || "#cae6fc";
    this._options["arc-color"] = (options && options["arc-color"]) || "#2196f3";
    this._options["font-color"] = (options && options["font-color"]) || "#444444";

    this._$arc = null;
    this._value = value;
    this._max = ((Math.PI * 2) * this._value / max_value) - 0.001;
}
RadialChart.prototype._svg = function($container) {
    var size = Math.min($container.width(), $container.height());
    this._radius = (size - this._options["line-width"]) / 2;

    var group = this._createElement("g", {
        "transform": "translate(" + [
            size / 2 + ($container.width() - size) / 2,
            size / 2 + ($container.height() - size) / 2
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
        "stroke-linecap": "round"
    });
    this._$arc = $(path);
    group.appendChild(path);

    var text = this._createElement("text", {
        "x": 0,
        "y": 0,
        "text-anchor": "middle",
        "font-size": this._radius * 0.4,
        "fill": this._options["font-color"]
    });
    this._$text = $(text);
    group.appendChild(text);

    var svg = this._createElement("svg", {
        "width": "100%",
        "height": "100%"
    })
    svg.appendChild(group);

    return svg;
}
RadialChart.prototype._afterDraw = function() {
    this._$arc.stop(true).animate({
        "_progress": 1
    }, {
        "duration": this._options["duration"],
        "easing": "easeOutQuart",
        "step": this._render_arc.bind(this)
    });
}
RadialChart.prototype._beforeErase = function() {
    if (this._$arc) {
        this._$arc.stop(true);
    }
    this._$arc = null;
}
RadialChart.prototype._render_arc = function(percentage) {
    if (!this._$arc) {
        return;
    }
    var angle = -(this._max * percentage + Math.PI / 2);
    var description = "";
    description += "M" + [ 0, this._radius ].join(" ");
    description += "A" + [
        this._radius,
        this._radius,
        0,
        angle >= -(3 / 2 * Math.PI) ? 0 : 1,
        1,
        this._radius * Math.cos(angle),
        -(this._radius * Math.sin(angle))
    ].join(" ");
    this._$arc.attr("d", description);
    this._$text.text(parseInt(this._value * percentage));
}
