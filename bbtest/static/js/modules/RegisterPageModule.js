RegisterPageModule.prototype = Object.create(Module.prototype);
function RegisterPageModule() {
    this._$form = $("[data-register-form]");
    this._$radio = $("[data-register-radio]");
    this._urls = this._$form.data("register-form");

    this._boundProcess = this._process.bind(this);

    this._$radio.on("change", this._boundProcess);

    Module.call(this);
}
RegisterPageModule.prototype._process = function(event) {
    var $radio = $(event.currentTarget);
    this._$form.attr("action", this._urls[$radio.val()]);
}
RegisterPageModule.prototype.unMount = function() {
    this._$radio.off("change", this._boundProcess);
}
