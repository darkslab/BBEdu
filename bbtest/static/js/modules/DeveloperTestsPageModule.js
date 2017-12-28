DeveloperTestsPageModule.prototype = Object.create(Module.prototype);
function DeveloperTestsPageModule() {
    this._$form = $("[data-test-form]");
    this._$sectionInput = this._$form.find("[data-set-section]");
    this._$languageInput = this._$form.find("[data-set-language]");

    this._sectionIsSet = false;
    this._languageIsSet = false;

    $("[data-get-section]").on("click", this._sectionClick.bind(this));
    $("[data-get-language]").on("click", this._languageClick.bind(this));

    Module.call(this);
}
DeveloperTestsPageModule.prototype.unMount = function() {
    $("[data-get-section]").off("click", this._sectionClick.bind(this));
    $("[data-get-language]").off("click", this._languageClick.bind(this));
}
DeveloperTestsPageModule.prototype._sectionClick = function(event) {
    var $button = $(event.currentTarget);
    this._$sectionInput.val($button.data("get-section"));
    this._sectionIsSet = true;
    this._submitForm();
}
DeveloperTestsPageModule.prototype._languageClick = function(event) {
    var $button = $(event.currentTarget);
    this._$languageInput.val($button.data("get-language"));
    this._languageIsSet = true;
    this._submitForm();
}
DeveloperTestsPageModule.prototype._submitForm = function() {
    if (this._sectionIsSet && this._languageIsSet) {
        this._$form.submit();
    }
}
