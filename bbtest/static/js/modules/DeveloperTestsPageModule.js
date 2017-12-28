DeveloperTestsPageModule.prototype = Object.create(Module.prototype);
function DeveloperTestsPageModule() {
    this._$form = $("[data-test-form]");
    this._$sectionInput = this._$form.find("[data-set-section]");
    this._$languageInput = this._$form.find("[data-set-language]");

    $("[data-get-section]").on("click", this._sectionClick.bind(this));
    $("[data-get-language]").on("click", this._languageClick.bind(this));

    $("[data-language-modal]").on("hide.bs.modal", this._modalHide.bind(this));

    Module.call(this);
}
DeveloperTestsPageModule.prototype.unMount = function() {
    $("[data-get-section]").off("click", this._sectionClick.bind(this));
    $("[data-get-language]").off("click", this._languageClick.bind(this));

    $("[data-language-modal]").off("hide.bs.modal", this._modalHide.bind(this));
}
DeveloperTestsPageModule.prototype._sectionClick = function(event) {
    var $button = $(event.currentTarget);
    $button.addClass("active");
    this._$sectionInput.val($button.data("get-section"));
}
DeveloperTestsPageModule.prototype._languageClick = function(event) {
    var $button = $(event.currentTarget);
    this._$languageInput.val($button.data("get-language"));
    if (this._$sectionInput.val()) {
        this._$form.submit();
    }
}
DeveloperTestsPageModule.prototype._modalHide = function() {
    if (this._$sectionInput.val() && this._$languageInput.val()) {
        return;
    }
    $("[data-get-section=\"" + this._$sectionInput.val() + "\"]").removeClass("active");
}
