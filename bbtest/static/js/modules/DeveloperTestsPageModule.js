DeveloperTestsPageModule.prototype = Object.create(Module.prototype);
function DeveloperTestsPageModule() {
    this._$sectionInput = $("[data-set-section]");
    this._$languageInput = $("[data-set-language]");

    this._$getSections = $("[data-get-section]");
    this._$getLanguages = $("[data-get-language]");

    this._$currentModal;
    this._$pendingModal;
    this._$nextModals = $("[data-next-modal]");
    this._isViewingSpecification = false;

    this._$submitButtons = $("[data-specification-submit]");

    this._boundSectionClick = this._sectionClick.bind(this);
    this._boundLanguageClick = this._languageClick.bind(this);
    this._boundNextModalClick = this._nextModalClick.bind(this);
    this._boundModalShow = this._modalShow.bind(this);
    this._boundModalHidden = this._modalHidden.bind(this);
    this._boundSubmitClick = this._submitClick.bind(this);

    this._$getSections.on("click", this._boundSectionClick);
    this._$getLanguages.on("click", this._boundLanguageClick);
    this._$nextModals.on("click", this._boundNextModalClick);
    this._$submitButtons.on("click", this._boundSubmitClick);

    Module.call(this);
}
DeveloperTestsPageModule.prototype.unMount = function() {
    this._$getSections.off("click", this._boundSectionClick);
    this._$getLanguages.off("click", this._boundLanguageClick);
    this._$nextModals.off("click", this._boundNextModalClick);
    this._$submitButtons.off("click", this._boundSubmitClick);
}
DeveloperTestsPageModule.prototype._sectionClick = function(event) {
    var $button = $(event.currentTarget);
    $button.addClass("active");
    this._$sectionInput.val($button.data("get-section"));
}
DeveloperTestsPageModule.prototype._languageClick = function(event) {
    var $button = $(event.currentTarget);
    this._$languageInput.val($button.data("get-language"));
}
DeveloperTestsPageModule.prototype._nextModalClick = function(event) {
    if (this._$pendingModal) {
        return;
    }
    this._$pendingModal = $($(event.currentTarget).data("next-modal"));
    this._scheduleNextModal();
}
DeveloperTestsPageModule.prototype._modalShow = function() {
    if (this._$sectionInput.val() && this._$languageInput.val()) {
        this._isViewingSpecification = true;
    }
}
DeveloperTestsPageModule.prototype._modalHidden = function() {
    this._$currentModal.off("show.bs.modal", this._boundModalShow);
    this._$currentModal.off("hidden.bs.modal", this._boundModalHidden);
    this._$currentModal = undefined;

    if (this._isViewingSpecification || !this._$pendingModal) {
        var section = this._$sectionInput.val();
        this._$getSections.each(function() {
            if ($(this).data("get-section").toString() === section) {
                $(this).removeClass("active");
                return false;
            }
        });
    }
    if (this._isViewingSpecification) {
        this._$sectionInput.val("");
        this._$languageInput.val("");
        this._isViewingSpecification = false;
    }

    this._scheduleNextModal();
}
DeveloperTestsPageModule.prototype._scheduleNextModal = function() {
    if (this._$currentModal) {
        return;
    }
    this._$currentModal = this._$pendingModal;
    this._$pendingModal = undefined;
    if (!this._$currentModal) {
        return;
    }
    this._$currentModal.on("show.bs.modal", this._boundModalShow);
    this._$currentModal.on("hidden.bs.modal", this._boundModalHidden);
    this._$currentModal.modal();
}
DeveloperTestsPageModule.prototype._submitClick = function() {
    this._$currentModal.data("bs.modal").options.backdrop = "static";
    this._$currentModal.data("bs.modal").options.keyboard = false;
    this._$currentModal.find("[data-specification-close]").attr("disabled", true);
}
