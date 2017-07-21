function SVGChart($container) {
    this._$container = $container;
    this._$svg = null;

    var last_width = this._$container.width();
    var timer;

    $(window).resize((function() {
        if (this._$container.width() != last_width) {
            clearTimeout(timer);
            last_width = this._$container.width();

            if (this._$svg) {
                this._beforeErase();
                this._$container.css({
                    "visibility": "hidden !important"
                });

                this._$svg.remove();
                this._$svg = null;
            }

            timer = setTimeout((function() {
                this._$container.css({
                    "visibility": "visible"
                });
                this.draw();
            }).bind(this), 250);
        }
    }).bind(this));
}
SVGChart.prototype._createElement = function(element, attributes) {
    var svg_element = document.createElementNS("http://www.w3.org/2000/svg", element);
    if (attributes) {
        var name;
        for (name in attributes) {
            svg_element.setAttributeNS(null, name, attributes[name]);
        }
    }
    return svg_element;
}
SVGChart.prototype._d = function(description) {
    var d = "";
    for (var i = 0; i < description.length; i++) {
        d = [
            d,
            [
                description[i][0],
                description[i][1].join(" "),
            ].join("")
        ].join("");
    }
    return d;
}
SVGChart.prototype._optionValue = function(options, name, default_value) {
    if (typeof options === "undefined" || typeof options[name] === "undefined") {
        return default_value;
    }
    return options[name];
}

/**
 * Extension methods
 */
SVGChart.prototype._svg = function($container) {}
SVGChart.prototype._afterDraw = function() {}
SVGChart.prototype._beforeErase = function() {}

/**
 * Client methods
 */
SVGChart.prototype.draw = function() {
    this._$svg = $(this._svg(this._$container));
    this._$container.append(this._$svg);
    this._afterDraw();
}
