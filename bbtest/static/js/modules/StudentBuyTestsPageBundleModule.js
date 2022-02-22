StudentBuyTestsPageBundleModule.prototype = Object.create(Module.prototype);
function StudentBuyTestsPageBundleModule(data) {
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
    this._$bundle_section = $("[bundle-test-section]");
    this._$totals = $("[data-totals]");
    this._$totals_line_items = this._$totals.find("[data-totals-line-items]");
    this._$totals_line_items_row = this._$totals_line_items.find("[data-totals-row]");
    this._$totals_line_items_row.remove();
    this._$totals_subtotals = this._$totals.find("[data-totals-subtotals]");
    this._$totals_subtotals_row = this._$totals_subtotals.find("[data-totals-row]");
    this._$totals_subtotals_row.remove();
    this._$totals_total = this._$totals.find("[data-totals-total]");
    this._$totals_test_language = this._$totals.find("[data-totals-test-language]");
    this._$totals_buy_tests = this._$totals.find("[data-totals-buy-tests]");
    this._$totals_buy_credits = this._$totals.find("[data-totals-buy-credits]");

    this._totalsTop;
    this._totalsTopPadding = 15;
    this._windowActionTimer = null;

    this._boundCheckout = this._checkout.bind(this);
    this._boundSelectLanguage = this._selectLanguage.bind(this);
    this._boundSelectSection = this._selectSection.bind(this);
    this._boundBundleSection = this._selectBundle.bind(this);
    this._boundWindowScroll = this._windowScroll.bind(this);
    this._boundWindowScrollDone = this._windowScrollDone.bind(this);
    this._boundWindowResize = this._windowResize.bind(this);
    this._boundWindowResizeDone = this._windowResizeDone.bind(this);

    this._$totals_buy_tests.on("click", this._boundCheckout);
    this._$test_language.on("click", this._boundSelectLanguage);
    this._$test_section.on("click", this._boundSelectSection);
    this._$bundle_section.on("click", this._boundBundleSection);
    $(window).on("scroll", this._boundWindowScroll);
    $(window).on("resize", this._boundWindowResize);

    this._$xhr = $.get({
        url: this._cartUrl,
        success: this._ajaxSuccess.bind(this, "cart", false),
        error: this._ajaxError.bind(this)
    });

    Module.call(this);
}
StudentBuyTestsPageBundleModule.prototype.unMount = function() {
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
StudentBuyTestsPageBundleModule.prototype._checkout = function(event) {
    if (this._$xhr !== undefined) {
        return;
    }

    this._curtainsDown();
    this._$xhr = $.post({
        url: this._checkoutUrl,
        headers: {"X-CSRFToken": Cookies.get("csrftoken")},
        success: this._ajaxSuccess.bind(this, "checkout", false),
        error: this._ajaxError.bind(this)
    });
}
StudentBuyTestsPageBundleModule.prototype._selectLanguage = function(event) {
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

    this._post(false, -1);
}
StudentBuyTestsPageBundleModule.prototype._selectSection = function(event) {
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
    this._post(true, -1);
}

StudentBuyTestsPageBundleModule.prototype._selectBundle = function(event) {
    
    if (this._$xhr !== undefined) {
        return;
    }
    
    var $bundle = $(event.currentTarget);
    var $pk = $bundle.attr("bundle-test-section");
    if (!$bundle.data("available")) {
        return;
    }
    if ($bundle.data("selected")) {
        $bundle.data("selected", false);
    } else {
        $bundle.data("selected", true);
    }
    this._post(false, $pk);
}

StudentBuyTestsPageBundleModule.prototype._ajaxSuccess = function(type, pageview, data, status, $xhr) {
    if (pageview) {
        ga_report_pageview();
    }
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
StudentBuyTestsPageBundleModule.prototype._ajaxError = function($xhr, status, error) {
    this._$failureModal.modal("show");
}
StudentBuyTestsPageBundleModule.prototype._apply = function(data) {
    var test_language_explanation;

    this._$test_language.each(function() {
        var $test_language = $(this);

        if ($test_language.data("test-language") === data.data.language) {
            $test_language.addClass("active");
            $test_language.data("selected", true);
            test_language_explanation = $test_language.data("test-language-explanation");
        } else {
            $test_language.removeClass("active");
            $test_language.data("selected", false);
        }
    });

    this._$test_section.each(function() {
        var $test_section = $(this);
        var $test_section_variant = $test_section.find("[data-test-section-variant]");
        var $test_section_price = $test_section.find("[data-test-section-price]");
        var $test_section_progress_message = $test_section.find("[data-progress-message]");
        var section_data = data.sections[$test_section.data("test-section").toString()];
        
        if (!section_data.enabled) {
            $test_section.addClass("disabled");
            $test_section.data("available", false);

            $test_section.removeClass("active");
            $test_section.data("selected", false);

            $test_section_variant.text("");
            $test_section_price.text("");
            $test_section_progress_message.removeClass("hidden");
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
        $test_section_variant.text(section_data.variant);
        $test_section_price.text(section_data.price);
        $test_section_progress_message.addClass("hidden");
    });

    this._$bundle_section.each(function() {
        var $bundle_section = $(this);
        var $bundle_pk = $bundle_section.attr("bundle-test-section");
        var $bundle_section_progress_message = $bundle_section.find("[bundle-progress-message]");
        var bundle_data = data.bundles[$bundle_pk];

        if (!bundle_data.enabled.some(function(e){return e;} )){
            $bundle_section.addClass("disabled");
            $bundle_section.data("available", false);

            $bundle_section.removeClass("active");
            $bundle_section.data("selected", false);

            $bundle_section_progress_message.removeClass("hidden");
            return;
        }

        $bundle_section.attr("bundle-sections", "");
        data.bundles[$bundle_pk].enabled.forEach(function(en, i){
            if(en){
                var sects = $bundle_section.attr("bundle-sections");
                var sect_id = 9539 + i;
                if (sects.length > 0){
                    $bundle_section.attr("bundle-sections", String(sects) + "_" + String(sect_id));
                }else{
                    $bundle_section.attr("bundle-sections", String(sect_id));
                }
            }
        });

        $bundle_section.removeClass("disabled");
        $bundle_section.data("available", true);
        if ($bundle_pk == data.selected_bundle_pk) {
            $bundle_section.addClass("active");
            $bundle_section.data("selected", true);
        } else {
            $bundle_section.removeClass("active");
            $bundle_section.data("selected", false);
        }
        $bundle_section_progress_message.addClass("hidden");
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
        if (test_language_explanation) {
            this._$totals_test_language.text(test_language_explanation);
            this._$totals_test_language.removeClass("hidden");
        }
        if (data.affordable) {
            this._$totals_buy_tests.removeClass("hidden");
            this._$totals_buy_credits.addClass("hidden");
        } else {
            this._$totals_buy_tests.addClass("hidden");
            this._$totals_buy_credits.removeClass("hidden");
        }
    } else {
        this._$totals_test_language.addClass("hidden");
        this._$totals_buy_tests.addClass("hidden");
        this._$totals_buy_credits.addClass("hidden");
    }

    this._$totals.removeClass("hidden");

    if (this._totalsTop === undefined) {
        this._totalsTop = this._$totals.offset().top;
    }
    this._hangTotals();
}
StudentBuyTestsPageBundleModule.prototype._curtainsDown = function() {
    this._$spinner.removeClass("hidden");
    this._$overlay_language.removeClass("hidden");
    this._$overlay_sections.removeClass("hidden");
    this._$overlay_totals.removeClass("hidden");
}
StudentBuyTestsPageBundleModule.prototype._curtainsUp = function() {
    this._$spinner.addClass("hidden");
    this._$overlay_language.addClass("hidden");
    this._$overlay_sections.addClass("hidden");
    this._$overlay_totals.addClass("hidden");
}
StudentBuyTestsPageBundleModule.prototype._post = function(include_sections, bundle_id) {
    this._curtainsDown();
    var data = {
        language: undefined,
        sections: [],
        selected_bundle_pk: -1,
        selected_bundle_variant: []
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
    if (bundle_id >= 0){
        this._$bundle_section.each(function() {
            var $bundle_section = $(this);
            if ($bundle_section.data("selected") ) {
                if($bundle_section.attr("bundle-test-section") == bundle_id){

                    var sects = $bundle_section.attr("bundle-sections").split('_');

                    sects.forEach(function(s){
                        data.sections.push(parseInt(s));
                    });

                    data.selected_bundle_pk = bundle_id;
                }
            }
        });
    }
    this._$xhr = $.post({
        url: this._cartUrl,
        headers: {"X-CSRFToken": Cookies.get("csrftoken")},
        data: {
            data: JSON.stringify(data)
        },
        success: this._ajaxSuccess.bind(this, "cart", true),
        error: this._ajaxError.bind(this)
    });
}
StudentBuyTestsPageBundleModule.prototype._hangTotals = function() {
    if (this._totalsTop === undefined) {
        return;
    }
    if ($(window).width() < 768 || $(window).height() < this._$totals.height() + this._totalsTopPadding * 2) {
        this._hangTotalsOff();
    } else {
        this._hangTotalsOn();
    }
}
StudentBuyTestsPageBundleModule.prototype._hangTotalsOn = function() {
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
StudentBuyTestsPageBundleModule.prototype._hangTotalsOff = function() {
    this._$totals.removeClass("bb-totals-hanging");
    this._$totals.css({
        width: "",
        top: ""
    });
}
StudentBuyTestsPageBundleModule.prototype._windowScroll = function() {
    clearTimeout(this._windowActionTimer);
    this._windowActionTimer = setTimeout(this._boundWindowScrollDone, 100);
}
StudentBuyTestsPageBundleModule.prototype._windowScrollDone = function() {
    this._hangTotals();
}
StudentBuyTestsPageBundleModule.prototype._windowResize = function() {
    this._hangTotalsOff();
    clearTimeout(this._windowActionTimer);
    this._windowActionTimer = setTimeout(this._boundWindowResizeDone, 100);
}
StudentBuyTestsPageBundleModule.prototype._windowResizeDone = function() {
    this._totalsTop = this._$totals.offset().top;
    this._hangTotals();
}
