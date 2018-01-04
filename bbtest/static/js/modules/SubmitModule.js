SubmitModule.prototype = Object.create(Module.prototype);
function SubmitModule() {
    this._boundProcess = this._process.bind(this);

    $("[data-bb-form]").on("submit", this._boundProcess);

    Module.call(this);
}
SubmitModule.prototype._process = function(event) {
    var $form = $(event.currentTarget);
    $form.find("[data-bb-submit]").attr("disabled", true);
}
SubmitModule.prototype.unMount = function() {
    $("[data-bb-form]").off("submit", this._boundProcess);
}
