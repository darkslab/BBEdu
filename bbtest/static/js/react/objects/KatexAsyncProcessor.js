"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(arg) { var key = _toPrimitive(arg, "string"); return _typeof(key) === "symbol" ? key : String(key); }
function _toPrimitive(input, hint) { if (_typeof(input) !== "object" || input === null) return input; var prim = input[Symbol.toPrimitive]; if (prim !== undefined) { var res = prim.call(input, hint || "default"); if (_typeof(res) !== "object") return res; throw new TypeError("@@toPrimitive must return a primitive value."); } return (hint === "string" ? String : Number)(input); }
var KatexAsyncProcessor = /*#__PURE__*/function () {
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
        delimiters: [{
          left: "$$",
          right: "$$",
          display: true
        }, {
          left: "$",
          right: "$",
          display: false
        }]
      });
      this._callback(this._$container.html(), this._originalText);
    }
  }]);
  return KatexAsyncProcessor;
}();