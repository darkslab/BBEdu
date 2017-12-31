DeveloperAcknowledgementPageModule.prototype = Object.create(Module.prototype);
function DeveloperAcknowledgementPageModule() {
    this._$form = $("[data-agreement-form]");
    this._$planInput = this._$form.find("[data-set-plan]");
    this._$planButtons = $("[data-get-plan]");
    this._$lastPlanButton;

    this._$agreementModal = $("[data-agreement-modal]");
    this._$agreementViewButton = $("[data-agreement-view]");
    this._$agreementReadCheckbox = $("[data-agreement-read]");
    this._$agreementAcceptButton = $("[data-agreement-accept]");

    this._$planButtons.on("click", this._planClick.bind(this));
    this._$agreementModal.on("hide.bs.modal", this._modalHide.bind(this));
    this._$agreementReadCheckbox.on("change", this._readChecked.bind(this));
    this._$agreementAcceptButton.on("click", this._agreementAccepted.bind(this));

    Module.call(this);
}
DeveloperAcknowledgementPageModule.prototype.unMount = function() {
    this._$planButtons.off("click", this._planClick.bind(this));
    this._$agreementModal.off("hide.bs.modal", this._modalHide.bind(this));
    this._$agreementReadCheckbox.off("change", this._readChecked.bind(this));
    this._$agreementAcceptButton.off("click", this._agreementAccepted.bind(this));
}
DeveloperAcknowledgementPageModule.prototype._planClick = function(event) {
    var $button = $(event.currentTarget);

    if (!this._$lastPlanButton) {
        this._$lastPlanButton = $button;
    } else if (this._$lastPlanButton.data("get-plan") === $button.data("get-plan")) {
        $button.removeClass("active");
        this._$lastPlanButton = undefined;
    } else {
        this._$lastPlanButton.removeClass("active");
        this._$lastPlanButton = $button;
    }

    if (this._$lastPlanButton) {
        this._$lastPlanButton.addClass("active");
        this._$planInput.val(this._$lastPlanButton.data("get-plan"));
        this._$agreementViewButton.attr("disabled", false);
    } else {
        this._$planInput.val("");
        this._$agreementViewButton.attr("disabled", true);
    }
}
DeveloperAcknowledgementPageModule.prototype._modalHide = function() {
    if (this._$agreementReadCheckbox.is(":checked")) {
        this._$agreementReadCheckbox.trigger("click");
    }
}
DeveloperAcknowledgementPageModule.prototype._readChecked = function() {
    if (this._$agreementReadCheckbox.is(":checked")) {
        this._$agreementAcceptButton.attr("disabled", false);
    } else {
        this._$agreementAcceptButton.attr("disabled", true);
    }
}
DeveloperAcknowledgementPageModule.prototype._agreementAccepted = function() {
    if (this._$agreementReadCheckbox.is(":checked")) {
        this._$agreementModal.data("bs.modal").options.backdrop = "static";
        this._$agreementModal.data("bs.modal").options.keyboard = false;

        this._$agreementReadCheckbox.attr("disabled", true);

        this._$form.submit();
    }
}
