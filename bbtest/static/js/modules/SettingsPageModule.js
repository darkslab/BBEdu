SettingsPageModule.prototype = Object.create(Module.prototype);
function SettingsPageModule() {
    this._hidden = true;
    this._$container = $("[data-settings-password-container]");
    this._$button = $("[data-settings-password-button]");

    if (!this._$container.hasClass("hidden")) {
        this._hidden = false;
    }

    this._$button.on("click", this._process.bind(this));

    Module.call(this);
}
SettingsPageModule.prototype._process = function() {
    if (this._hidden) {
        this._hidden = false;
        this._$container.removeClass("hidden");
        this._$button.addClass("active");
    } else {
        this._hidden = true;
        this._$container.addClass("hidden");
        this._$button.removeClass("active");

        this._$container.find("input[type=\"password\"]").val("");
    }
}
SettingsPageModule.prototype.unMount = function() {
    this._$button.off("click", this._process.bind(this));
}
