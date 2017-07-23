function SVGChart($container) {
    this._$container = $container;
    this._$svg = null;
    this._active = false;

    var last_width = this._$container.width();
    var timer = null;

    $(window).resize((function() {
        if (this._$container.width() != last_width) {
            clearTimeout(timer);
            last_width = this._$container.width();

            if (this._active) {
                this._destroy();
                timer = setTimeout((function() {
                    this._create();
                }).bind(this), 250);
            }
        }
    }).bind(this));
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
}
SVGChart.prototype.destroy = function() {
    this._destroy();
    this._active = false;
}
