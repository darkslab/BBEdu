GAModule.prototype = Object.create(Module.prototype);
function GAModule(data) {
    ga_report_pageview();

    var i;
    for (i = 0; i < data.events.length; i++) {
        ga_report_event(data.events[i]);
    }

    Module.call(this);
}
