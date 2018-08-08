(function() {
    function ModuleStack() {
        this._modules = [];
    }
    ModuleStack.prototype.load = function() {
        var moduleClasses = [];
        var moduleData;
        while ((moduleData = moduleDataStack.shift()) !== undefined) {
            var moduleClass = eval(moduleData.module);
            if (moduleClasses.indexOf(moduleClass) !== -1 && !moduleClass.prototype.isMultiMount) {
                continue;
            }
            this._modules.push(new moduleClass(moduleData.data));
            moduleClasses.push(moduleClass);
        }
    }
    ModuleStack.prototype.unLoad = function() {
        var module;
        while ((module = this._modules.shift()) !== undefined) {
            module.unMount();
        }
    }

    var stack = new ModuleStack();

    $(document).on("turbolinks:request-start", function() {
        $(document.documentElement).addClass("bb-loading");
    });
    $(document).on("turbolinks:request-end", function() {
        stack.unLoad();
    });
    $(document).on("turbolinks:render", function() {
        $(document.documentElement).removeClass("bb-loading");
        stack.load();
    });
    $(function() {
        stack.load();
    });
})();
