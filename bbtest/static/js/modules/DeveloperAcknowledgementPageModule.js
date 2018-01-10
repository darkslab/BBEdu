DeveloperAcknowledgementPageModule.prototype = Object.create(Module.prototype);
function DeveloperAcknowledgementPageModule() {
    this._$form = $("[data-agreement-form]");
    this._$planInput = this._$form.find("[data-set-plan]");
    this._$codeInput = this._$form.find("[data-set-code]");
    this._$planButtons = $("[data-get-plan]");
    this._$lastPlanButton;

    this._$agreementViewButton = $("[data-agreement-view]");
    this._$agreementModal = $("[data-agreement-modal]");
    this._$agreementClose = this._$agreementModal.find("[data-agreement-close]");
    this._$agreementReadCheckbox = this._$agreementModal.find("[data-agreement-read]");
    this._$agreementAcceptButton = this._$agreementModal.find("[data-agreement-accept]");
    this._$agreementTexts = this._$agreementModal.find("[data-agreement-text]");

    this._boundPlanClick = this._planClick.bind(this);
    this._boundModalShow = this._modalShow.bind(this);
    this._boundModalHidden = this._modalHidden.bind(this);
    this._boundReadChecked = this._readChecked.bind(this);
    this._boundAgreementAccepted = this._agreementAccepted.bind(this);

    this._$planButtons.on("click", this._boundPlanClick);
    this._$agreementModal.on("show.bs.modal", this._boundModalShow);
    this._$agreementModal.on("hidden.bs.modal", this._boundModalHidden);
    this._$agreementReadCheckbox.on("change", this._boundReadChecked);
    this._$agreementAcceptButton.on("click", this._boundAgreementAccepted);

    Module.call(this);
}
DeveloperAcknowledgementPageModule.prototype.unMount = function() {
    this._$planButtons.off("click", this._boundPlanClick);
    this._$agreementModal.off("show.bs.modal", this._boundModalShow);
    this._$agreementModal.off("hidden.bs.modal", this._boundModalHidden);
    this._$agreementReadCheckbox.off("change", this._boundReadChecked);
    this._$agreementAcceptButton.off("click", this._boundAgreementAccepted);
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
        this._$codeInput.val(this._$lastPlanButton.data("get-code"));
        this._$agreementViewButton.attr("disabled", false);
    } else {
        this._$planInput.val("");
        this._$codeInput.val("");
        this._$agreementViewButton.attr("disabled", true);
    }
}
DeveloperAcknowledgementPageModule.prototype._modalShow = function() {
    var code = this._$codeInput.val().toString();
    this._$agreementTexts.each(function() {
        if ($(this).data("agreement-text").toString() === code) {
            $(this).removeClass("hidden");
            return false;
        }
    });
}
DeveloperAcknowledgementPageModule.prototype._modalHidden = function() {
    if (this._$agreementReadCheckbox.is(":checked")) {
        this._$agreementReadCheckbox.trigger("click");
    }
    this._$agreementTexts.each(function() {
        $(this).addClass("hidden");
    });
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
        this._$agreementClose.attr("disabled", true);

        this._$form.submit();
    }
}
