GAModule.prototype = Object.create(Module.prototype);
function GAModule(data) {
    ga_report_pageview();

    var i;
    for (i = 0; i < data.events.length; i++) {
        ga_report_event(data.events[i]);
    }

    this._$inquiryTargets = [
        $("[data-corporate-link]")
    ];

    this._boundInquiryClick = this._inquiryClick.bind(this);

    for (i = 0; i < this._$inquiryTargets.length; i++) {
        this._$inquiryTargets[i].on("click", this._boundInquiryClick);
    }

    Module.call(this);
}
GAModule.prototype.unMount = function() {
    for (i = 0; i < this._$inquiryTargets.length; i++) {
        this._$inquiryTargets[i].off("click", this._boundInquiryClick);
    }
}
GAModule.prototype._inquiryClick = function(event) {
    var $inquiryTarget = $(event.currentTarget);

    if ($inquiryTarget.data("corporate-link")) {
        ga_report_event([ "corporate_click", { "event_category": "inquiry" } ]);
    }
}
