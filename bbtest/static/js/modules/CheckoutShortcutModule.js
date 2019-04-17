CheckoutShortcutModule.prototype = Object.create(Module.prototype);
function CheckoutShortcutModule() {
    this._$container = $("[data-bb-checkout-shortcut]");
    this._$window = $(window);
    this._$document = $(document);

    this._boundScroll = this._scroll.bind(this);
    this._boundClick = this._click.bind(this);

    this._$window.on("scroll", this._boundScroll);
    this._$container.on("click", this._boundClick);

    Module.call(this);
}
CheckoutShortcutModule.prototype._scroll = function() {
    if (this._shouldShow()) {
        this._$container.addClass("bb-checkout-shortcut-pulled");
    } else {
        this._$container.removeClass("bb-checkout-shortcut-pulled");
    }
}
CheckoutShortcutModule.prototype._click = function() {
    $("html, body").animate({
        scrollTop: (this._$document.height() - this._$window.height()) + "px"
    }, 1000);
}
CheckoutShortcutModule.prototype._shouldShow = function() {
    return this._$document.height() - this._$window.height() - this._$window.scrollTop() > 200;
}
CheckoutShortcutModule.prototype.unMount = function() {
    this._$window.off("scroll", this._boundScroll);
}
