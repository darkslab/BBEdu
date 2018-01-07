"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var MathJaxAsyncProcessor = function () {
    function MathJaxAsyncProcessor(callback, text) {
        _classCallCheck(this, MathJaxAsyncProcessor);

        this._callback = callback;
        this._originalText = text;

        this._isActive = true;
        this._$container = $("<div></div>");
        ReactDOM.render(SimpleFormattedFragment(this._originalText), this._$container[0], this._doneRendering.bind(this));
    }

    _createClass(MathJaxAsyncProcessor, [{
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
            MathJax.Hub.Queue(["Typeset", MathJax.Hub, this._$container[0]], ["_doneTypesetting", this]);
        }
    }, {
        key: "_doneTypesetting",
        value: function _doneTypesetting() {
            if (!this._isActive) {
                return;
            }
            this._callback(this._$container.html(), this._originalText);
        }
    }]);

    return MathJaxAsyncProcessor;
}();