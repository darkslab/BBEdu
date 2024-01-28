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
var SplitTextParagraph = /*#__PURE__*/function (_React$Component) {
  _inherits(SplitTextParagraph, _React$Component);
  var _super = _createSuper(SplitTextParagraph);
  function SplitTextParagraph(props) {
    var _this;
    _classCallCheck(this, SplitTextParagraph);
    _this = _super.call(this, props);
    _this.state = {
      toggleFlag: true
    };
    _this._left = {
      originalText: "",
      rawHtml: "",
      processor: undefined
    };
    _this._right = {
      originalText: "",
      rawHtml: "",
      processor: undefined
    };
    return _this;
  }
  _createClass(SplitTextParagraph, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      if (!this.props.data.has_formulas) {
        return;
      }
      this._setupProcessors();
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      if (this._left.processor) {
        this._left.processor.stop();
      }
      if (this._right.processor) {
        this._right.processor.stop();
      }
    }
  }, {
    key: "componentDidUpdate",
    value: function componentDidUpdate() {
      if (this._left.processor || this._right.processor || !this.props.data.has_formulas) {
        return;
      }
      if (this.props.data.left.text !== this._left.originalText || this.props.data.right.text !== this._right.originalText) {
        this._setupProcessors();
      }
    }
  }, {
    key: "render",
    value: function render() {
      var leftContent = null;
      var rightContent = null;
      var leftClassName = "bb-test-paragraph";
      if (!this.props.data.left.text) {
        var content = null;
        if (this.props.forDevelopers) {
          leftClassName += " bb-placeholder";
          content = this.props.texts.paragraphEmptyPlaceholder;
        }
        leftContent = /*#__PURE__*/React.createElement("div", {
          className: leftClassName
        }, content);
      } else if (this.props.data.has_formulas) {
        leftContent = /*#__PURE__*/React.createElement("div", {
          className: leftClassName,
          dangerouslySetInnerHTML: {
            __html: this._left.rawHtml
          }
        });
      } else {
        leftContent = /*#__PURE__*/React.createElement("div", {
          className: leftClassName
        }, SimpleFormattedFragment(this.props.data.left.text));
      }
      var rightClassName = "bb-test-paragraph";
      if (!this.props.data.right.text) {
        var _content = null;
        if (this.props.forDevelopers) {
          rightClassName += " bb-placeholder";
          _content = this.props.texts.paragraphEmptyPlaceholder;
        }
        rightContent = /*#__PURE__*/React.createElement("div", {
          className: rightClassName
        }, _content);
      } else if (this.props.data.has_formulas) {
        rightContent = /*#__PURE__*/React.createElement("div", {
          className: rightClassName,
          dangerouslySetInnerHTML: {
            __html: this._right.rawHtml
          }
        });
      } else {
        rightContent = /*#__PURE__*/React.createElement("div", {
          className: rightClassName
        }, SimpleFormattedFragment(this.props.data.right.text));
      }
      return /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2"
      }, /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-6 pr-5"
      }, /*#__PURE__*/React.createElement("h5", {
        className: "text-center mt-0 mb-0"
      }, /*#__PURE__*/React.createElement("em", null, this.props.testTexts.column_a)), leftContent), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-6 pl-5"
      }, /*#__PURE__*/React.createElement("h5", {
        className: "text-center mt-0 mb-0"
      }, /*#__PURE__*/React.createElement("em", null, this.props.testTexts.column_b)), rightContent))));
    }
  }, {
    key: "_setupProcessors",
    value: function _setupProcessors() {
      this._left.processor = new KatexAsyncProcessor(this._doneProcessing.bind(this, "left"), this.props.data.left.text);
      this._right.processor = new KatexAsyncProcessor(this._doneProcessing.bind(this, "right"), this.props.data.right.text);
    }
  }, {
    key: "_doneProcessing",
    value: function _doneProcessing(type, rawHtml, originalText) {
      switch (type) {
        case "left":
          this._left.originalText = originalText;
          this._left.rawHtml = rawHtml;
          this._left.processor = undefined;
          break;
        case "right":
          this._right.originalText = originalText;
          this._right.rawHtml = rawHtml;
          this._right.processor = undefined;
          break;
      }
      if (!this._left.processor && !this._right.processor) {
        this.setState(function (prevState) {
          return {
            toggleFlag: !prevState.toggleFlag
          };
        });
      }
    }
  }]);
  return SplitTextParagraph;
}(React.Component);