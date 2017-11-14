PopoverModule.prototype = Object.create(Module.prototype);
function PopoverModule() {
    $("[data-toggle=\"popover\"]").popover();

    Module.call(this);
}
PopoverModule.prototype.unMount = function() {
    $("[data-toggle=\"popover\"]").popover("destroy");
}
