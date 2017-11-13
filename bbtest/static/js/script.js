(function() {
    function ModuleStack() {
        this._modules = [];
        this._moduleClasses = [];
    }
    ModuleStack.prototype.load = function() {
        var moduleData;
        while ((moduleData = moduleDataStack.shift()) !== undefined) {
            if (this._moduleClasses.indexOf(moduleData.module) !== -1) {
                continue;
            }
            var moduleClass = eval(moduleData.module);
            this._modules.push(new moduleClass(moduleData.data));
            this._moduleClasses.push(moduleData.module);
        }
    }
    ModuleStack.prototype.unLoad = function() {
        var module;
        while ((module = this._modules.shift()) !== undefined) {
            module.unMount();
            this._moduleClasses.shift();
        }
    }

    var stack = new ModuleStack();

    $(document).on("turbolinks:request-start", function() {
        $(document.body).addClass("bb-loading");
    });
    $(document).on("turbolinks:request-end", function() {
        stack.unLoad();
    });
    $(document).on("turbolinks:render", function() {
        stack.load();
    });
    $(function() {
        stack.load();
    });
})();
