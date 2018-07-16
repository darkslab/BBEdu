ResultRowModule.prototype = Object.create(Module.prototype);
function ResultRowModule() {
    Module.call(this);
}
ResultRowModule.prototype.unMount = function() {
}
ResultRowModule.prototype.isMultiMount = true;
