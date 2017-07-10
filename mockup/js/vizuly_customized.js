vizuly.theme.radial_progress = function(viz) {
    var skins = {
        bb_default: {
            name: "bb_default",
            class: "vz-skin-bb-default"
        }
    }
    var viz = viz;
    var callbacks = [
        { on: "update.theme", callback: applyTheme },
        { on: "mouseover.theme", callback: onMouseOver },
        { on: "mouseout.theme", callback: onMouseOut }
    ];
    theme();
    function theme() {
        applyCallbacks();
    }
    function applyTheme() {
        if (!skin) {
            return;
        }
        var selection = viz.selection();
        selection.attr("class", skin.class);
        selection.selectAll(".vz-radial_progress-label").style("font-size", viz.radius() * 0.25);
    }
    function onMouseOver(e, d, i) {
    }
    function onMouseOut(e, d, i) {
    }
    function applyCallbacks() {
        callbacks.forEach(function(d) {
            viz.on(d.on, d.callback);
        });
    }
    function removeCallbacks() {
        callbacks.forEach(function(d) {
            viz.on(d.on, null);
        });
    }
    theme.apply = function(skin) {
        if (arguments.length > 0) {
            theme.skin(skin);
        }
        applyTheme();
        return theme;
    }
    theme.release = function() {
        if (!viz) {
            return;
        }
        viz.selection().attr("class", null);
        removeCallbacks();
        viz = null;
    };
    theme.viz = function(_) {
        if (!arguments.length) {
            return viz;
        }
        if (viz) {
            removeCallbacks();
        }
        viz = _;
        applyCallbacks();
    }
    theme.skin = function(_) {
        if (arguments.length == 0) {
            return skin;
        }
        if (skins[_]) {
            skin = skins[_];
        } else {
            throw new Error("theme/linearea.js - skin " + _ + " does not exist.");
        }
        return theme;
    }
    theme.skins = function() {
        return skins;
    }
    var skin = skins[vizuly.skin.RADIAL_PROGRESS_BB_DEFAULT];

    return theme;
}
vizuly.skin.RADIAL_PROGRESS_BB_DEFAULT = "bb_default";

function VizulyArc($container, current_value, max_value) {
    var arc = vizuly.viz.radial_progress($container[0]);
    arc.data(current_value).min(0).max(max_value + 0.01).capRadius(1).on("tween", function(v, i) {
        v.selection().selectAll(".vz-radial_progress-label").text(v.label()(v.data() * i));
    }).startAngle(250).endAngle(110).arcThickness(0.06).label(function(d, i) {
        return d3.format(".0f")(d);
    });
    var theme = vizuly.theme.radial_progress(arc);
    theme.skin(vizuly.skin.RADIAL_PROGRESS_BB_DEFAULT);
    var timer = null;
    var self = this;

    $(window).resize(function() {
        clearTimeout(timer);
        $container.children("div.vz-skin-bb-default").children("svg.vizuly").css({
            "visibility": "hidden"
        });
        timer = setTimeout(function() {
            self._draw(arc, $container);
            $container.children("div.vz-skin-bb-default").children("svg.vizuly").css({
                "visibility": "visible"
            });
        }, 250);
    });

    this._draw(arc, $container);
}
VizulyArc.prototype._radius = function($container) {
    return $container.width() > $container.height() ? $container.height() : $container.width();
}
VizulyArc.prototype._draw = function(arc, $container) {
    arc.width($container.width()).height($container.height()).radius(this._radius($container)/2.1);
    arc.update();
}
