GAModule.prototype = Object.create(Module.prototype);
function GAModule(data) {
    ga_report_pageview();

    if (typeof gtag !== "undefined") {
        var i;
        for (i = 0; i < data.events.length; i++) {
            data.events[i].unshift("event");
            gtag.apply(null, data.events[i]);
        }
    }

    Module.call(this);
}
