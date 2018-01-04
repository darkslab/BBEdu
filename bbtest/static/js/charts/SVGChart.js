function SVGChart($container) {
    this._$container = $container;
    this._$svg = null;
    this._active = false;
    this._last_width = this._$container.width();
    this._timer = null;

    this._boundResize = this._resize.bind(this);
}
SVGChart.prototype._resize = function() {
    if (this._$container.width() != this._last_width) {
        clearTimeout(this._timer);
        this._last_width = this._$container.width();

        if (this._active) {
            this._destroy();
            this._timer = setTimeout((function() {
                this._create();
            }).bind(this), 250);
        }
    }
}
SVGChart.prototype._create = function() {
    if (this._$svg) {
        return;
    }
    this._$container.css({
        "visibility": "hidden !important"
    });
    this._$svg = $(this._createElement("svg", {
        "width": "100%",
        "height": "100%"
    }));
    this._$container.append(this._$svg);
    this._afterCreate(this._$svg[0]);
    this._$container.css({
        "visibility": "visible"
    });
}
SVGChart.prototype._destroy = function() {
    if (!this._$svg) {
        return;
    }
    this._beforeDestroy(this._$svg[0]);
    this._$container.css({
        "visibility": "hidden !important"
    });
    this._$svg.remove();
    this._$svg = null;
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
SVGChart.prototype._optionalPercentageValue = function(value, whole_value) {
    var _value = 0;
    var is_set = false;
    if (isNaN(parseFloat(value))) {
        is_set = true;
    }
    if (!is_set && typeof value === "string") {
        if (value[value.length-1] === "%") {
            _value = Math.max(parseFloat(value.slice(0, value.length-1)), 0) / 100 * whole_value;
            is_set = true;
        }
    }
    if (!is_set) {
        _value = Math.max(parseFloat(value), 0);
    }
    return _value;
}
SVGChart.prototype._deg2rad = function(deg) {
    return (2 * Math.PI * deg) / 360;
}

/**
 * Extension methods
 */
SVGChart.prototype._afterCreate = function(svg) {}
SVGChart.prototype._beforeDestroy = function(svg) {}

/**
 * Client methods
 */
SVGChart.prototype.create = function() {
    this._active = true;
    this._create();
    $(window).on("resize", this._boundResize);
}
SVGChart.prototype.destroy = function() {
    $(window).off("resize", this._boundResize);
    this._destroy();
    this._active = false;
}
