PersonalizedModule.prototype = Object.create(Module.prototype);
function PersonalizedModule() {
    var $main = $("[data-bb-main]");
    var $button = $("[data-bb-bar-button]");

    $button.click(function() {
        if ($(window).width() < 1200) {
            if ($button.hasClass("bb-pushed")) {
                $button.removeClass("bb-pushed");
                $main.removeClass("bb-pushed");
            } else {
                $button.addClass("bb-pushed");
                $main.addClass("bb-pushed");
            }
        }
    });

    Module.call(this);
}
