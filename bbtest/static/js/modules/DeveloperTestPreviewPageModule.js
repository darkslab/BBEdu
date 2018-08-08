DeveloperTestPreviewPageModule.prototype = Object.create(Module.prototype);
function DeveloperTestPreviewPageModule(data) {
    this._$modal = $("[data-check-modal]");
    this._$waitHeader = this._$modal.find("[data-check-modal-header=\"wait\"]");
    this._$doneHeader = this._$modal.find("[data-check-modal-header=\"done\"]");
    this._$spinner = this._$modal.find("[data-check-modal-body=\"spinner\"]");
    this._$feedback = this._$modal.find("[data-check-modal-body=\"feedback\"]");
    this._$success = this._$modal.find("[data-check-modal-body=\"success\"]");
    this._$error = this._$modal.find("[data-check-modal-body=\"error\"]");
    this._url = data.url;
    this._$xhr;

    this._boundModalShow = this._modalShow.bind(this);
    this._boundModalHide = this._modalHide.bind(this);
    this._boundModalHidden = this._modalHidden.bind(this);

    this._$modal.on("show.bs.modal", this._boundModalShow);
    this._$modal.on("hide.bs.modal", this._boundModalHide);
    this._$modal.on("hidden.bs.modal", this._boundModalHidden);

    Module.call(this);
}
DeveloperTestPreviewPageModule.prototype.unMount = function() {
    this._abort();

    this._$modal.off("show.bs.modal", this._boundModalShow);
    this._$modal.off("hide.bs.modal", this._boundModalHide);
    this._$modal.off("hidden.bs.modal", this._boundModalHidden);
}
DeveloperTestPreviewPageModule.prototype._modalShow = function() {
    this._$xhr = $.post({
        url: this._url,
        headers: {"X-CSRFToken": Cookies.get("csrftoken")},
        success: this._ajaxSuccess.bind(this),
        error: this._ajaxError.bind(this)
    });
}
DeveloperTestPreviewPageModule.prototype._modalHide = function() {
    this._abort();
}
DeveloperTestPreviewPageModule.prototype._modalHidden = function() {
    this._$waitHeader.removeClass("hidden");
    this._$doneHeader.addClass("hidden");
    this._$spinner.removeClass("hidden");
    this._$feedback.addClass("hidden");
    this._$feedback.empty();
    this._$success.addClass("hidden");
    this._$error.addClass("hidden");
}
DeveloperTestPreviewPageModule.prototype._abort = function() {
    if (this._$xhr !== undefined) {
        this._$xhr.abort();
    }
}
DeveloperTestPreviewPageModule.prototype._ajaxSuccess = function(data, status, $xhr) {
    this._$waitHeader.addClass("hidden");
    this._$doneHeader.removeClass("hidden");
    if (data.success) {
        this._$spinner.addClass("hidden");
        this._$success.removeClass("hidden");
        return;
    }
    var $list = $("<ul></ul>").addClass("list-normal");
    var i;
    for (i = 0; i < data.errors.__all__.length; i++) {
        $list.append($("<li></li>").text(data.errors.__all__[i].message));
    }
    this._$spinner.addClass("hidden");
    this._$feedback.append($list).removeClass("hidden");
}
DeveloperTestPreviewPageModule.prototype._ajaxError = function($xhr, status, error) {
    if (status === "abort") {
        return;
    }
    this._$waitHeader.addClass("hidden");
    this._$doneHeader.removeClass("hidden");
    this._$spinner.addClass("hidden");
    this._$error.removeClass("hidden");
}
