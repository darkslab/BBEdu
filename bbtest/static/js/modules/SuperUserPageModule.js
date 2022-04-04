SuperUserPageModule.prototype = Object.create(Module.prototype);
function SuperUserPageModule() {
    this._$form = $("[data-give-credits-form]");
    this._$form_pass = $("[data-change-pass-manual-form]");
    this._$giveCreditsConfirmButtons = $("[data-give-credits-confirm]");
    this._$changePassManualConfirmButtons = $("[data-change-pass-manual-confirm]");

    this._boundUpdateFormAction = this._updateFormAction.bind(this);
    this._boundUpdateChangePassFormAction = this._updateChangePassFormAction.bind(this);

    this._$giveCreditsConfirmButtons.on("click", this._boundUpdateFormAction);
    this._$changePassManualConfirmButtons.on("click", this._boundUpdateChangePassFormAction);

    Module.call(this);
}
SuperUserPageModule.prototype.unMount = function() {
    this._$giveCreditsConfirmButtons.off("click", this._boundUpdateFormAction);
    this._$changePassManualConfirmButtons.off("click", this._boundUpdateChangePassFormAction);
}
SuperUserPageModule.prototype._updateFormAction = function(event) {
    var $button = $(event.currentTarget);
    if (!$button.data("give-credits-confirm")) {
        return;
    }
    this._$giveCreditsConfirmButtons.attr("disabled", true);
    this._$form.submit();
}
SuperUserPageModule.prototype._updateChangePassFormAction = function(event) {
    var $button = $(event.currentTarget);
    if (!$button.data("change-pass-manual-confirm")) {
        return;
    }
    this._$changePassManualConfirmButtons.attr("disabled", true);
    this._$form_pass.submit();
}
