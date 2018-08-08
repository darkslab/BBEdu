StudentResultsPageModule.prototype = Object.create(Module.prototype);
function StudentResultsPageModule() {
    this._timer = setTimeout(function() {
        var $collapseToggles = $("[data-toggle=\"collapse\"]");
        if ($collapseToggles.length) {
            $collapseToggles.eq(0).trigger("click");
        }
    }, 150);

    Module.call(this);
}
StudentResultsPageModule.prototype.unMount = function() {
    clearTimeout(this._timer);
}
