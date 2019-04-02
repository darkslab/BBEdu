function ga_report_pageview() {
    if (typeof gtag === "undefined") {
        return;
    }
    gtag("config", "UA-137493457-1", {
        "page_title": document.title,
        "page_path": location.pathname + location.search
    });
}
