GAModule.prototype = Object.create(Module.prototype);
function GAModule(data) {
    if (typeof gtag !== "undefined") {
        gtag("config", "UA-112252952-1", {
            "page_title": document.title,
            "page_path": location.pathname + location.search
        });

        var i;
        for (i = 0; i < data.events.length; i++) {
            data.events[i].unshift("event");
            gtag.apply(null, data.events[i]);
        }
    }

    Module.call(this);
}
