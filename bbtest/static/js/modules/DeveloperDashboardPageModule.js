DeveloperDashboardPageModule.prototype = Object.create(Module.prototype);
function DeveloperDashboardPageModule() {
    this._$form = $("[data-delete-test-form]");
    this._$deleteButtons = $("[data-delete-test-url]");

    this._boundUpdateFormAction = this._updateFormAction.bind(this);

    this._$deleteButtons.on("click", this._boundUpdateFormAction);

    Module.call(this);
}
DeveloperDashboardPageModule.prototype.unMount = function() {
    this._$deleteButtons.off("click", this._boundUpdateFormAction);
}
DeveloperDashboardPageModule.prototype._updateFormAction = function(event) {
    var $button = $(event.currentTarget);
    this._$form.attr("action", $button.data("delete-test-url"));
}
