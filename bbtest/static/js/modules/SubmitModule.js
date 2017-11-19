SubmitModule.prototype = Object.create(Module.prototype);
function SubmitModule() {
    $("[data-bb-form]").on("submit", this._process.bind(this));

    Module.call(this);
}
SubmitModule.prototype._process = function(event) {
    var $form = $(event.currentTarget);
    $form.find("[data-bb-submit]").attr("disabled", true);
}
SubmitModule.prototype.unMount = function() {
    $("[data-bb-form]").off("submit", this._process.bind(this));
}
