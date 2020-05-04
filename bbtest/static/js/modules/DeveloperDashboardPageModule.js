DeveloperDashboardPageModule.prototype = Object.create(Module.prototype);
function DeveloperDashboardPageModule() {
    this._$form = $("[data-form]");
    this._$buttons = $("[data-form-url]");

    this._boundUpdateFormAction = this._updateFormAction.bind(this);

    this._$buttons.on("click", this._boundUpdateFormAction);

    Module.call(this);
}
DeveloperDashboardPageModule.prototype.unMount = function() {
    this._$buttons.off("click", this._boundUpdateFormAction);
}
DeveloperDashboardPageModule.prototype._updateFormAction = function(event) {
    var $button = $(event.currentTarget);
    this._$form.attr("action", $button.data("form-url"));
}
