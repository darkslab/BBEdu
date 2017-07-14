function RadialChart($container, value, max_value, options) {
    this._options = {};
    this._options["duration"] = (options && options["duration"]) || 2000;
    this._options["stroke-width"] = (options && options["stroke-width"]) || 6;
    this._options["circle-stroke"] = (options && options["circle-stroke"]) || "#cae6fc";
    this._options["arc-stroke"] = (options && options["arc-stroke"]) || "#2196f3";
    this._options["arc-stroke-linecap"] = (options && options["arc-stroke-linecap"]) || "round";
    this._options["text-fill"] = (options && options["text-fill"]) || "#444444";
    this._$arc = null;
    this._max = ((Math.PI * 2) * value / max_value) - 0.001;
    this._value = value;

    this._render($container);
}
RadialChart.prototype._clear = function($container) {
    this._$arc = null;
    $container.children("svg").remove();
}
RadialChart.prototype._render = function($container) {
    var namespace = "http://www.w3.org/2000/svg";
    var size = Math.min($container.width(), $container.height());
    this._radius = (size - this._options["stroke-width"]) / 2;

    var svg = document.createElementNS(namespace, "svg");
    svg.setAttributeNS(null, "width", "100%");
    svg.setAttributeNS(null, "height", "100%");

    var group_0 = document.createElementNS(namespace, "g");
    group_0.setAttributeNS(null, "transform", "translate(" + [
        size / 2 + ($container.width() - size) / 2,
        size / 2 + ($container.height() - size) / 2
    ].join() + ")");

    var circle = document.createElementNS(namespace, "circle");
    circle.setAttributeNS(null, "cx", 0);
    circle.setAttributeNS(null, "cy", 0);
    circle.setAttributeNS(null, "r", this._radius);
    circle.setAttributeNS(null, "fill", "none");
    circle.setAttributeNS(null, "stroke", this._options["circle-stroke"]);
    circle.setAttributeNS(null, "stroke-width", this._options["stroke-width"]);
    group_0.appendChild(circle);

    var path = document.createElementNS(namespace, "path");
    this._$arc = $(path);
    path.setAttributeNS(null, "d", "M0 0");
    path.setAttributeNS(null, "fill", "none");
    path.setAttributeNS(null, "stroke", this._options["arc-stroke"]);
    path.setAttributeNS(null, "stroke-width", this._options["stroke-width"]);
    path.setAttributeNS(null, "stroke-linecap", this._options["arc-stroke-linecap"]);
    group_0.appendChild(path);

    var text = document.createElementNS(namespace, "text");
    this._$text = $(text);
    text.setAttributeNS(null, "x", 0);
    text.setAttributeNS(null, "y", 0);
    text.setAttributeNS(null, "text-anchor", "middle");
    text.setAttributeNS(null, "font-size", this._radius * 0.4);
    text.setAttributeNS(null, "fill", this._options["text-fill"]);
    group_0.appendChild(text);

    svg.appendChild(group_0);
    $container.append(svg);

    this._$arc.stop(true).animate({
        "_progress": 1
    }, {
        "duration": this._options["duration"],
        "easing": "easeOutQuart",
        "step": this._render_arc.bind(this)
    });
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
