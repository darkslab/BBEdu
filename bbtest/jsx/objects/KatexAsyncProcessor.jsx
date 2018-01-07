class KatexAsyncProcessor {
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
        renderMathInElement(this._$container[0], {
            throwOnError: false,
            delimiters: [
                { left: "$$", right: "$$", display: true },
                { left: "$", right: "$", display: false },
            ]
        });
        this._callback(this._$container.html(), this._originalText);
    }
}
