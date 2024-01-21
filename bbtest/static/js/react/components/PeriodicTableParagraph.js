"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(arg) { var key = _toPrimitive(arg, "string"); return _typeof(key) === "symbol" ? key : String(key); }
function _toPrimitive(input, hint) { if (_typeof(input) !== "object" || input === null) return input; var prim = input[Symbol.toPrimitive]; if (prim !== undefined) { var res = prim.call(input, hint || "default"); if (_typeof(res) !== "object") return res; throw new TypeError("@@toPrimitive must return a primitive value."); } return (hint === "string" ? String : Number)(input); }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
var PeriodicTableParagraph = /*#__PURE__*/function (_React$Component) {
  _inherits(PeriodicTableParagraph, _React$Component);
  var _super = _createSuper(PeriodicTableParagraph);
  function PeriodicTableParagraph(props) {
    var _this;
    _classCallCheck(this, PeriodicTableParagraph);
    _this = _super.call(this, props);
    _this.state = {
      originalText: "",
      rawHtml: ""
    };
    _this._processor;
    return _this;
  }
  _createClass(PeriodicTableParagraph, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      if (!this.props.data.has_formulas) {
        return;
      }
      this._setupProcessor();
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      if (this._processor) {
        this._processor.stop();
      }
    }
  }, {
    key: "componentDidUpdate",
    value: function componentDidUpdate() {
      if (this._processor || !this.props.data.has_formulas) {
        return;
      }
      if (this.props.data.text !== this.state.originalText) {
        this._setupProcessor();
      }
    }
  }, {
    key: "render",
    value: function render() {
      var content = null;
      var className = "bb-test-paragraph";
      var sharedAddon = null;
      if (this.props.isShared) {
        className += " bb-test-paragraph-shared";
        sharedAddon = /*#__PURE__*/React.createElement("h5", {
          className: "text-center mt-0 mb-5"
        }, /*#__PURE__*/React.createElement("em", null, this.props.testTexts.shared_paragraph_header));
      }
      if (!this.props.data.text) {
        var _content = null;
        if (this.props.forDevelopers) {
          className += " bb-placeholder";
          _content = this.props.texts.paragraphEmptyPlaceholder;
        }
        content = /*#__PURE__*/React.createElement(React.Fragment, null, sharedAddon, /*#__PURE__*/React.createElement("div", {
          className: className
        }, _content));
      } else if (this.props.data.has_formulas) {
        content = /*#__PURE__*/React.createElement(React.Fragment, null, sharedAddon, /*#__PURE__*/React.createElement("div", {
          className: className,
          dangerouslySetInnerHTML: {
            __html: this.state.rawHtml
          }
        }));
      } else {
        content = /*#__PURE__*/React.createElement(React.Fragment, null, sharedAddon, /*#__PURE__*/React.createElement("div", {
          className: className
        }, SimpleFormattedFragment(this.props.data.text)));
      }
      return content;
    }
  }, {
    key: "_setupProcessor",
    value: function _setupProcessor() {
      this._processor = new KatexAsyncProcessor(this._doneProcessing.bind(this), this.props.data.text);
    }
  }, {
    key: "_doneProcessing",
    value: function _doneProcessing(rawHtml, originalText) {
      this.setState({
        originalText: originalText,
        rawHtml: rawHtml
      });
      this._processor = undefined;
    }
  }]);
  return PeriodicTableParagraph;
}(React.Component);