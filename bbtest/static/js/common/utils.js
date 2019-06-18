function ga_report_pageview() {
    if (typeof gtag === "undefined") {
        return;
    }
    gtag("config", "UA-112252952-1", {
        "page_title": document.title,
        "page_path": location.pathname + location.search
    });
}

function ga_report_event(args) {
    if (typeof gtag === "undefined") {
        return;
    }
    var _args = args.slice(0);
    _args.unshift("event");
    gtag.apply(null, _args);
}
