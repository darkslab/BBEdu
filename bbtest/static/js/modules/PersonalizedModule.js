PersonalizedModule.prototype = Object.create(Module.prototype);
function PersonalizedModule() {
    this._$main = $("[data-bb-main]");
    this._$button = $("[data-bb-bar-button]");

    this._$button.on("click", this._controlWindow.bind(this));

    Module.call(this);
}
PersonalizedModule.prototype._controlWindow = function() {
    if ($(window).width() < 1200) {
        if (this._$button.hasClass("bb-pushed")) {
            this._$button.removeClass("bb-pushed");
            this._$main.removeClass("bb-pushed");
        } else {
            this._$button.addClass("bb-pushed");
            this._$main.addClass("bb-pushed");
        }
    }
}
PersonalizedModule.prototype.unMount = function() {
    this._$button.off("click", this._controlWindow.bind(this));
}
