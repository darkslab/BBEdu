class MathJaxAsyncProcessor {
    constructor(callback, text) {
        this._callback = callback;
        this._originalText = text;

        this._isActive = true;
        this._$container = $("<div></div>");
        ReactDOM.render(
            SimpleFormattedFragment(this._originalText),
            this._$container[0],
            this._doneRendering.bind(this)
        );
    }
    stop() {
        this._isActive = false;
    }

    _doneRendering() {
        if (!this._isActive) {
            return;
        }
        MathJax.Hub.Queue(
            ["Typeset", MathJax.Hub, this._$container[0]],
            ["_doneTypesetting", this]
        );
    }
    _doneTypesetting() {
        if (!this._isActive) {
            return;
        }
        this._callback(this._$container.html(), this._originalText);
    }
}
