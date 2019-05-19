BuyCreditsBeelinePageModule.prototype = Object.create(Module.prototype);
function BuyCreditsBeelinePageModule(data) {
    this._sendUrl = data.send_url;
    this._resendUrl = data.resend_url;
    this._payUrl = data.pay_url;
    this._completeUrl = data.complete_url;

    this._$overlay = $("[data-beeline-overlay]");
    this._$inputs = $("[data-beeline-input]");
    this._$numberInput = this._$inputs.filter("[data-beeline-input=\"number\"]");
    this._$codeInput = this._$inputs.filter("[data-beeline-input=\"code\"]");
    this._$buttons = $("[data-beeline-action]");
    this._$sendButton = this._$buttons.filter("[data-beeline-action=\"send\"]");
    this._$resendButton = this._$buttons.filter("[data-beeline-action=\"resend\"]");
    this._$payButton = this._$buttons.filter("[data-beeline-action=\"pay\"]");

    this._number = this._$numberInput.val();
    this._paymentId = 0;
    this._code = "";

    this._$xhr;

    this._boundInputChange = this._inputChange.bind(this);
    this._boundButtonClick = this._buttonClick.bind(this);

    this._$inputs.on("input", this._boundInputChange);
    this._$buttons.on("click", this._boundButtonClick);

    this._normalize();

    Module.call(this);
}
BuyCreditsBeelinePageModule.prototype.unMount = function() {
    this._$inputs.off("input", this._boundInputChange);
    this._$buttons.off("click", this._boundButtonClick);

    if (this._$xhr) {
        this._$xhr.abort();
        this._$xhr = undefined;
    }
}
BuyCreditsBeelinePageModule.prototype._inputChange = function(event) {
    var $input = $(event.currentTarget);
    if ($input.data("beeline-input") == "number") {
        if ($input.val().length >= 10) {
            this._number = $input.val();
        } else {
            this._number = "";
            this._paymentId = 0;
            this._code = "";
            this._$codeInput.val(this._code);
        }
        $input.val($input.val());
    } else if ($input.data("beeline-input") == "code") {
        if ($input.val().length >= 6) {
            this._code = $input.val();
        } else {
            this._code = "";
        }
        $input.val($input.val());
    }
    this._normalize();
}
BuyCreditsBeelinePageModule.prototype._normalize = function() {
    if (this._number) {
        this._$numberInput.closest("[data-beeline-group]").removeClass("has-error").addClass("has-success");
    } else {
        this._$numberInput.closest("[data-beeline-group]").removeClass("has-success").addClass("has-error");
    }
    if (this._paymentId) {
        this._$codeInput.closest("[data-beeline-group]").removeClass("hidden");
    } else {
        this._$codeInput.closest("[data-beeline-group]").addClass("hidden");
    }
    if (this._code) {
        this._$codeInput.closest("[data-beeline-group]").removeClass("has-error").addClass("has-success");
    } else {
        this._$codeInput.closest("[data-beeline-group]").removeClass("has-success").addClass("has-error");
    }

    if (this._code) {
        this._$sendButton.prop("disabled", true).addClass("hidden");
        this._$payButton.prop("disabled", false).removeClass("hidden");
        this._$resendButton.prop("disabled", false).removeClass("hidden");
    } else if (this._paymentId) {
        this._$sendButton.prop("disabled", true).addClass("hidden");
        this._$payButton.prop("disabled", true).removeClass("hidden");
        this._$resendButton.prop("disabled", false).removeClass("hidden");
    } else if (this._number) {
        this._$sendButton.prop("disabled", false).removeClass("hidden");
        this._$payButton.prop("disabled", true).addClass("hidden");
        this._$resendButton.prop("disabled", true).addClass("hidden");
    } else {
        this._$sendButton.prop("disabled", true).removeClass("hidden");
        this._$payButton.prop("disabled", true).addClass("hidden");
        this._$resendButton.prop("disabled", true).addClass("hidden");
    }
}
BuyCreditsBeelinePageModule.prototype._buttonClick = function(event) {
    if (this._$xhr) {
        return;
    }

    var $button = $(event.currentTarget);
    if ($button.data("beeline-action") == "send") {
        if (!this._number || this._paymentId || this._code) {
            return;
        }

        this._ajax("send", this._sendUrl, {
            "number": this._number
        });
    } else if ($button.data("beeline-action") == "resend") {
        if (!this._number || !this._paymentId) {
            return;
        }

        this._code = "";
        this._$codeInput.val(this._code);
        this._ajax("resend", this._resendUrl, {
            "payment_id": this._paymentId
        });
    } else if ($button.data("beeline-action") == "pay") {
        if (!this._number || !this._paymentId || !this._code) {
            return;
        }

        this._ajax("pay", this._payUrl, {
            "payment_id": this._paymentId,
            "code": this._code
        });
    }
    this._normalize();
}
BuyCreditsBeelinePageModule.prototype._ajaxSuccess = function(action, data, status, $xhr) {
    this._$xhr = undefined;
    this._$overlay.addClass("hidden");

    switch (action) {
        case "send":
            if (data.success) {
                this._paymentId = data.payment_id;
            } else {
                this._number = "";
                this._$numberInput.val(this._number);
            }
            break;
        case "resend":
            break;
        case "pay":
            if (data.success) {
                Turbolinks.visit(this._completeUrl);
            } else {
                this._code = "";
                this._$codeInput.val(this._code);
            }
            break;
    }
    this._normalize();
}
BuyCreditsBeelinePageModule.prototype._ajaxError = function($xhr, status, error) {
    this._$xhr = undefined;
    this._$overlay.addClass("hidden");
    // DARK_TODO  implement this!
}
BuyCreditsBeelinePageModule.prototype._ajax = function(action, url, data) {
    this._$overlay.removeClass("hidden");
    this._$xhr = $.post({
        url: url,
        headers: {"X-CSRFToken": Cookies.get("csrftoken")},
        data: data,
        success: this._ajaxSuccess.bind(this, action),
        error: this._ajaxError.bind(this)
    });
}
