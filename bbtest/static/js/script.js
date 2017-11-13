$(function() {
    $(document).on("turbolinks:request-start", function() {
        $(document.body).addClass("bb-loading");
    });
    $(document).on("turbolinks:request-end", function() {
        // unload the current js module
    });
    $(document).on("turbolinks:render", function() {
        // load the current js module
    });
});
