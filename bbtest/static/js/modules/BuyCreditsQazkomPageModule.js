BuyCreditsQazkomPageModule.prototype = Object.create(Module.prototype);
function BuyCreditsQazkomPageModule() {
    this._$form = $("[data-qazkom-form]");

    if (this._$form.length) {
        this._$form.submit();
    }

    Module.call(this);
}
BuyCreditsQazkomPageModule.prototype.unMount = function() {
}
