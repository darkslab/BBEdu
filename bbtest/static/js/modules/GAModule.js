GAModule.prototype = Object.create(Module.prototype);
function GAModule(data) {
    if (typeof ga !== "undefined") {
        var i;
        for (i = 0; i < data.events.length; i++) {
            data.events[i].unshift("event");
            data.events[i].unshift("send");
            ga.apply(null, data.events[i]);
        }
    }

    Module.call(this);
}
