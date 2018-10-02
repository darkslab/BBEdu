SuperUsersPageModule.prototype = Object.create(Module.prototype);
function SuperUsersPageModule() {
    this._$form = $("[data-impersonate-form]");
    this._$impersonateButtons = $("[data-impersonate-url]");

    this._boundUpdateFormAction = this._updateFormAction.bind(this);

    this._$impersonateButtons.on("click", this._boundUpdateFormAction);

    Module.call(this);
}
SuperUsersPageModule.prototype.unMount = function() {
    this._$impersonateButtons.off("click", this._boundUpdateFormAction);
}
SuperUsersPageModule.prototype._updateFormAction = function(event) {
    var $button = $(event.currentTarget);
    this._$form.attr("action", $button.data("impersonate-url"));
}
