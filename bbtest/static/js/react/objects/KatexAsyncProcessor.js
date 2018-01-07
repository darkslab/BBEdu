"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var KatexAsyncProcessor = function () {
    function KatexAsyncProcessor(callback, text) {
        _classCallCheck(this, KatexAsyncProcessor);

        this._callback = callback;
        this._originalText = text;

        this._isActive = true;
        this._$container = $("<div></div>");
        ReactDOM.render(SimpleFormattedFragment(this._originalText), this._$container[0], this._doneRendering.bind(this));
    }

    _createClass(KatexAsyncProcessor, [{
        key: "stop",
        value: function stop() {
            this._isActive = false;
        }
    }, {
        key: "_doneRendering",
        value: function _doneRendering() {
            if (!this._isActive) {
                return;
            }
            renderMathInElement(this._$container[0], {
                throwOnError: false,
                delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }]
            });
            this._callback(this._$container.html(), this._originalText);
        }
    }]);

    return KatexAsyncProcessor;
}();