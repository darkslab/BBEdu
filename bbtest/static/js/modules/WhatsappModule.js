WhatsappModule.prototype = Object.create(Module.prototype);
function WhatsappModule() {
    this._$container = $("[data-bb-whatsapp]");
    this._isHovered = false;

    this._boundMouseOver = this._mouseOver.bind(this);
    this._boundMouseOut = this._mouseOut.bind(this);

    this._$container.on("mouseover", this._boundMouseOver);
    this._$container.on("mouseout", this._boundMouseOut);

    this._$container.addClass("bb-whatsapp-pulled");

    Module.call(this);
}
WhatsappModule.prototype._mouseOver = function(event) {
    if (!this._isHovered) {
        this._$container.addClass("bb-whatsapp-focused");
        this._isHovered = true;
    }
}
WhatsappModule.prototype._mouseOut = function(event) {
    if (this._isHovered) {
        this._$container.removeClass("bb-whatsapp-focused");
        this._isHovered = false;
    }
}
WhatsappModule.prototype.unMount = function() {
    this._$container.off("mouseover", this._boundMouseOver);
    this._$container.off("mouseout", this._boundMouseOut);
}
