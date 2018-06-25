StudentBuyTestsPageModule.prototype = Object.create(Module.prototype);
function StudentBuyTestsPageModule(data) {
    this._url = data.url;
    this._$xhr;

    this._$spinner = $("[data-spinner]");
    this._$overlay_language = $("[data-overlay-language]");
    this._$overlay_sections = $("[data-overlay-sections]");
    this._$overlay_totals = $("[data-overlay-totals]");

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

    this._boundSelectLanguage = this._selectLanguage.bind(this);
    this._boundSelectSection = this._selectSection.bind(this);

    this._$test_language.on("click", this._boundSelectLanguage);
    this._$test_section.on("click", this._boundSelectSection);
    this._$xhr = $.get({
        url: this._url,
        success: this._ajaxSuccess.bind(this),
        error: this._ajaxError.bind(this)
    });

    Module.call(this);
}
StudentBuyTestsPageModule.prototype.unMount = function() {
    this._$test_language.off("click", this._boundSelectLanguage);
    this._$test_section.off("click", this._boundSelectSection);
    if (this._$xhr !== undefined) {
        this._$xhr.abort();
        this._$xhr = undefined;
    }
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
StudentBuyTestsPageModule.prototype._ajaxSuccess = function(data, status, $xhr) {
    this._$xhr = undefined;
    this._apply(data);
    this._curtainsUp();
}
StudentBuyTestsPageModule.prototype._ajaxError = function($xhr, status, error) {
    // DARK_TODO  alert that something is wrong?
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

    this._$totals.removeClass("hidden");
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
        url: this._url,
        headers: {"X-CSRFToken": Cookies.get("csrftoken")},
        data: {
            data: JSON.stringify(data)
        },
        success: this._ajaxSuccess.bind(this),
        error: this._ajaxError.bind(this)
    });
}
