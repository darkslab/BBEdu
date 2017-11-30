ReactModule.prototype = Object.create(Module.prototype);
function ReactModule(data) {
    this._$root = $("#root");

    if (this._$root.length) {
        ReactDOM.render(
            React.createElement(eval(data.class), data.props),
            this._$root[0]
        );
    }

    Module.call(this);
}
ReactModule.prototype.unMount = function() {
    if (this._$root.length) {
        ReactDOM.unmountComponentAtNode(this._$root[0]);
    }
}
