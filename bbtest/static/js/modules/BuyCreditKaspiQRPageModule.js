BuyCreditKaspiQRPageModule.prototype = Object.create(Module.prototype);
function BuyCreditKaspiQRPageModule() {
    this._$form = $("[data-kaspi-qr-form]");
    console.log(this._$form)
    console.log(this._$form.find('input[name="payment_url"]').val())

    if (this._$form.length) {
        // this._$form.submit();
        window.location.href = this._$form.find('input[name="payment_url"]').val();
    }

    Module.call(this);
}
BuyCreditKaspiQRPageModule.prototype.unMount = function() {
}
