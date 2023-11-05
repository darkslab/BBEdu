SuperCreatePackageModule.prototype = Object.create(Module.prototype);
function SuperCreatePackageModule() {
    this._$form = $("[data-create-package-form]");
    this._$createStudentConfirmButtons = $("[data-create-package-confirm]");
    this._boundUpdateFormAction = this._updateFormAction.bind(this);
    this._$createStudentConfirmButtons.on("click", this._boundUpdateFormAction);

    Module.call(this);
}

SuperCreatePackageModule.prototype.unMount = function() {
    this._$createStudentConfirmButtons.off("click", this._boundUpdateFormAction);
};

SuperCreatePackageModule.prototype._updateFormAction = function(event) {
    var $button = $(event.currentTarget);
    // console.log("print");
    if (!$button.data("create-package-confirm")) {
        return;
    }
    this._$form.submit();
    // window.location.href = "/super/export-data/";
    // location.reload();
    $('#modal-asd').modal('toggle');
};
