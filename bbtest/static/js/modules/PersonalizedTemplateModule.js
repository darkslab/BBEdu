PersonalizedTemplateModule.prototype = Object.create(Module.prototype);
function PersonalizedTemplateModule() {
    this._$container = $("[data-bb-container]");
    this._$main = $("[data-bb-main]");
    this._$button = $("[data-bb-bar-button]");
    this._$overlay = $("[data-bb-overlay]");

    this._$button.on("click", this._controlWindow.bind(this));
    $(window).on("resize", this._normalizeScroll.bind(this));

    Module.call(this);
}
PersonalizedTemplateModule.prototype._controlWindow = function() {
    if ($(window).width() < 1200) {
        if (this._$button.hasClass("bb-pushed")) {
            this._$container.removeClass("bb-overlayed");
            this._$container.removeClass("bb-min");
            this._$button.removeClass("bb-pushed");
            this._$main.removeClass("bb-pushed");
            this._$overlay.removeClass("bb-overlayed");
        } else {
            this._$container.animate({
                scrollTop: "0px"
            });
            this._$container.addClass("bb-overlayed");
            this._$container.addClass("bb-min");
            this._$button.addClass("bb-pushed");
            this._$main.addClass("bb-pushed");
            this._$overlay.addClass("bb-overlayed");
        }
    }
}
PersonalizedTemplateModule.prototype._normalizeScroll = function() {
    if ($(window).width() < 1200 && this._$button.hasClass("bb-pushed")) {
        this._$container.animate({
            scrollTop: "0px"
        });
    }
}
PersonalizedTemplateModule.prototype.unMount = function() {
    this._$button.off("click", this._controlWindow.bind(this));
    $(window).off("resize", this._normalizeScroll.bind(this));
}
