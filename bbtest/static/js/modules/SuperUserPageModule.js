SuperUserPageModule.prototype = Object.create(Module.prototype);
function SuperUserPageModule() {
    this._$form = $("[data-give-credits-form]");
    this._$giveCreditsConfirmButtons = $("[data-give-credits-confirm]");

    this._boundUpdateFormAction = this._updateFormAction.bind(this);

    this._$giveCreditsConfirmButtons.on("click", this._boundUpdateFormAction);

    Module.call(this);
}
SuperUserPageModule.prototype.unMount = function() {
    this._$giveCreditsConfirmButtons.off("click", this._boundUpdateFormAction);
}
SuperUserPageModule.prototype._updateFormAction = function(event) {
    var $button = $(event.currentTarget);
    if (!$button.data("give-credits-confirm")) {
        return;
    }
    this._$giveCreditsConfirmButtons.attr("disabled", true);
    this._$form.submit();
}
