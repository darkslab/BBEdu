StudentBuyTestsPageModule.prototype = Object.create(Module.prototype);
function StudentBuyTestsPageModule(data) {
    this._cartUrl = data.cartUrl;
    this._checkoutUrl = data.checkoutUrl;
    this._$xhr;

    this._$spinner = $("[data-spinner]");
    this._$overlay_language = $("[data-overlay-language]");
    this._$overlay_sections = $("[data-overlay-sections]");
    this._$overlay_totals = $("[data-overlay-totals]");
    this._$failureModal = $("[data-failure-modal]");
    this._$errorModal = $("[data-error-modal]");
    this._$errorModalBody = this._$errorModal.find("[data-error-modal-body]");

    this._$test_language = $("[data-test-language]");
    this._$test_section = $("[data-test-section]");
    this._$totals = $("[data-totals]");
    this._$totals_line_items = this._$totals.find("[data-totals-line-items]");
    this._$totals_line_items_row = this._$totals_line_items.find("[data-totals-row]");
    this._$totals_line_items_row.remove();
    this._$totals_subtotals = this._$totals.find("[data-totals-subtotals]");
    this._$totals_subtotals_row = this._$totals_subtotals.find("[data-totals-row]");
    this._$totals_subtotals_row.remove();
    this._$totals_total = this._$totals.find("[data-totals-total]");
    this._$totals_buy_tests = this._$totals.find("[data-totals-buy-tests]");
    this._$totals_buy_credits = this._$totals.find("[data-totals-buy-credits]");

    this._totalsTop;
    this._totalsTopPadding = 15;
    this._windowActionTimer = null;

    this._boundCheckout = this._checkout.bind(this);
    this._boundSelectLanguage = this._selectLanguage.bind(this);
    this._boundSelectSection = this._selectSection.bind(this);
    this._boundWindowScroll = this._windowScroll.bind(this);
    this._boundWindowScrollDone = this._windowScrollDone.bind(this);
    this._boundWindowResize = this._windowResize.bind(this);
    this._boundWindowResizeDone = this._windowResizeDone.bind(this);

    this._$totals_buy_tests.on("click", this._boundCheckout);
    this._$test_language.on("click", this._boundSelectLanguage);
    this._$test_section.on("click", this._boundSelectSection);
    $(window).on("scroll", this._boundWindowScroll);
    $(window).on("resize", this._boundWindowResize);

    this._$xhr = $.get({
        url: this._cartUrl,
        success: this._ajaxSuccess.bind(this, "cart"),
        error: this._ajaxError.bind(this)
    });

    Module.call(this);
}
StudentBuyTestsPageModule.prototype.unMount = function() {
    this._$totals_buy_tests.off("click", this._boundCheckout);
    this._$test_language.off("click", this._boundSelectLanguage);
    this._$test_section.off("click", this._boundSelectSection);
    $(window).off("scroll", this._boundWindowScroll);
    $(window).off("resize", this._boundWindowResize);

    clearTimeout(this._windowActionTimer);

    if (this._$xhr !== undefined) {
        this._$xhr.abort();
        this._$xhr = undefined;
    }
}
StudentBuyTestsPageModule.prototype._checkout = function(event) {
    if (this._$xhr !== undefined) {
        return;
    }

    this._curtainsDown();
    this._$xhr = $.post({
        url: this._checkoutUrl,
        headers: {"X-CSRFToken": Cookies.get("csrftoken")},
        success: this._ajaxSuccess.bind(this, "checkout"),
        error: this._ajaxError.bind(this)
    });
}
StudentBuyTestsPageModule.prototype._selectLanguage = function(event) {
    if (this._$xhr !== undefined) {
        return;
    }
    var $language = $(event.currentTarget);
    if ($language.data("selected")) {
        return;
    }
    this._$test_language.each(function() {
        var $test_language = $(this);
        if ($test_language.data("test-language") === $language.data("test-language")) {
            $test_language.data("selected", true);
        } else {
            $test_language.data("selected", false);
        }
    });

    this._post(false);
}
StudentBuyTestsPageModule.prototype._selectSection = function(event) {
    if (this._$xhr !== undefined) {
        return;
    }
    var $section = $(event.currentTarget);
    if (!$section.data("available")) {
        return;
    }
    if ($section.data("selected")) {
        $section.data("selected", false);
    } else {
        $section.data("selected", true);
    }

    this._post(true);
}
StudentBuyTestsPageModule.prototype._ajaxSuccess = function(type, data, status, $xhr) {
    switch (type) {
        case "cart":
            this._$xhr = undefined;
            this._apply(data);
            this._curtainsUp();
            break;
        case "checkout":
            if (data.success) {
                Turbolinks.visit(data.url);
            } else {
                this._$xhr = undefined;
                this._curtainsUp();
                this._$errorModalBody.text(data.message);
                this._$errorModal.modal("show");
            }
            break;
    }
}
StudentBuyTestsPageModule.prototype._ajaxError = function($xhr, status, error) {
    this._$failureModal.modal("show");
}
StudentBuyTestsPageModule.prototype._apply = function(data) {
    this._$test_language.each(function() {
        var $test_language = $(this);

        if ($test_language.data("test-language") === data.data.language) {
            $test_language.addClass("active");
            $test_language.data("selected", true);
        } else {
            $test_language.removeClass("active");
            $test_language.data("selected", false);
        }
    });

    this._$test_section.each(function() {
        var $test_section = $(this);

        if (!data.sections[$test_section.data("test-section").toString()]) {
            $test_section.addClass("disabled");
            $test_section.data("available", false);

            $test_section.removeClass("active");
            $test_section.data("selected", false);
            return;
        }

        $test_section.removeClass("disabled");
        $test_section.data("available", true);
        if (data.data.sections.indexOf($test_section.data("test-section")) > -1) {
            $test_section.addClass("active");
            $test_section.data("selected", true);
        } else {
            $test_section.removeClass("active");
            $test_section.data("selected", false);
        }
    });

    var i;

    this._$totals_line_items.empty();
    if (data.totals.line_items.length) {
        this._$totals_line_items.parent().removeClass("hidden");
        for (i = 0; i < data.totals.line_items.length; i++) {
            var $row = this._$totals_line_items_row.clone();
            $row.find("[data-totals-description]").text(data.totals.line_items[i].description);
            $row.find("[data-totals-amount]").text(data.totals.line_items[i].amount);
            this._$totals_line_items.append($row);
        }
    } else {
        this._$totals_line_items.parent().addClass("hidden");
    }

    this._$totals_subtotals.empty();
    if (data.totals.subtotals.length) {
        this._$totals_subtotals.parent().removeClass("hidden");
        for (i = 0; i < data.totals.subtotals.length; i++) {
            var $row = this._$totals_subtotals_row.clone();
            $row.find("[data-totals-description]").text(data.totals.subtotals[i].description);
            $row.find("[data-totals-amount]").text(data.totals.subtotals[i].amount);
            this._$totals_subtotals.append($row);
        }
    } else {
        this._$totals_subtotals.parent().addClass("hidden");
    }

    this._$totals_total.text(data.totals.total);

    if (data.totals.line_items.length) {
        if (data.affordable) {
            this._$totals_buy_tests.removeClass("hidden");
            this._$totals_buy_credits.addClass("hidden");
        } else {
            this._$totals_buy_tests.addClass("hidden");
            this._$totals_buy_credits.removeClass("hidden");
        }
    } else {
        this._$totals_buy_tests.addClass("hidden");
        this._$totals_buy_credits.addClass("hidden");
    }

    this._$totals.removeClass("hidden");

    if (this._totalsTop === undefined) {
        this._totalsTop = this._$totals.offset().top;
    }
    this._hangTotals();
}
StudentBuyTestsPageModule.prototype._curtainsDown = function() {
    this._$spinner.removeClass("hidden");
    this._$overlay_language.removeClass("hidden");
    this._$overlay_sections.removeClass("hidden");
    this._$overlay_totals.removeClass("hidden");
}
StudentBuyTestsPageModule.prototype._curtainsUp = function() {
    this._$spinner.addClass("hidden");
    this._$overlay_language.addClass("hidden");
    this._$overlay_sections.addClass("hidden");
    this._$overlay_totals.addClass("hidden");
}
StudentBuyTestsPageModule.prototype._post = function(include_sections) {
    this._curtainsDown();
    var data = {
        language: undefined,
        sections: []
    };
    this._$test_language.each(function() {
        var $test_language = $(this);
        if ($test_language.data("selected")) {
            data.language = $test_language.data("test-language");
            return false;
        }
    });
    if (include_sections) {
        this._$test_section.each(function() {
            var $test_section = $(this);
            if ($test_section.data("selected")) {
                data.sections.push($test_section.data("test-section"));
            }
        });
    }
    this._$xhr = $.post({
        url: this._cartUrl,
        headers: {"X-CSRFToken": Cookies.get("csrftoken")},
        data: {
            data: JSON.stringify(data)
        },
        success: this._ajaxSuccess.bind(this, "cart"),
        error: this._ajaxError.bind(this)
    });
}
StudentBuyTestsPageModule.prototype._hangTotals = function() {
    if (this._totalsTop === undefined) {
        return;
    }
    if ($(window).width() < 768 || $(window).height() < this._$totals.height() + this._totalsTopPadding * 2) {
        this._hangTotalsOff();
    } else {
        this._hangTotalsOn();
    }
}
StudentBuyTestsPageModule.prototype._hangTotalsOn = function() {
    this._$totals.css({
        width: this._$totals.width() + "px"
    });
    this._$totals.addClass("bb-totals-hanging");
    var top = 0;
    if ($(window).scrollTop() > this._totalsTop - this._totalsTopPadding) {
        top = $(window).scrollTop() - this._totalsTop + this._totalsTopPadding;
    }
    this._$totals.css({
        top: top + "px"
    });
}
StudentBuyTestsPageModule.prototype._hangTotalsOff = function() {
    this._$totals.removeClass("bb-totals-hanging");
    this._$totals.css({
        width: "",
        top: ""
    });
}
StudentBuyTestsPageModule.prototype._windowScroll = function() {
    clearTimeout(this._windowActionTimer);
    this._windowActionTimer = setTimeout(this._boundWindowScrollDone, 100);
}
StudentBuyTestsPageModule.prototype._windowScrollDone = function() {
    this._hangTotals();
}
StudentBuyTestsPageModule.prototype._windowResize = function() {
    this._hangTotalsOff();
    clearTimeout(this._windowActionTimer);
    this._windowActionTimer = setTimeout(this._boundWindowResizeDone, 100);
}
StudentBuyTestsPageModule.prototype._windowResizeDone = function() {
    this._totalsTop = this._$totals.offset().top;
    this._hangTotals();
}
