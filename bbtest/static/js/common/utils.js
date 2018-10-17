function ga_report_pageview() {
    if (typeof gtag === "undefined") {
        return;
    }
    gtag("config", "UA-112252952-1", {
        "page_title": document.title,
        "page_path": location.pathname + location.search
    });
}
