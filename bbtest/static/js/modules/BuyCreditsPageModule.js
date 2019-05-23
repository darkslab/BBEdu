BuyCreditsPageModule.prototype = Object.create(Module.prototype);
function BuyCreditsPageModule() {
    this._$form = $("[data-payment-form]");
    this._$paymentChoice = $("[data-payment-choice]");
    this._$buttons = $("[data-payment-type]");

    this._boundSubmit = this._submit.bind(this);

    this._$buttons.on("click", this._boundSubmit);

    Module.call(this);
}
BuyCreditsPageModule.prototype.unMount = function() {
    this._$buttons.off("click", this._boundSubmit);
}
BuyCreditsPageModule.prototype._submit = function(event) {
    this._$paymentChoice.val($(event.currentTarget).data("payment-type"));
    this._$form.submit();
}
