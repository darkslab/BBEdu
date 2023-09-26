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
var MultichoiceTextChoice = /*#__PURE__*/function (_React$Component) {
  _inherits(MultichoiceTextChoice, _React$Component);
  var _super = _createSuper(MultichoiceTextChoice);
  function MultichoiceTextChoice(props) {
    var _this;
    _classCallCheck(this, MultichoiceTextChoice);
    _this = _super.call(this, props);
    _this.state = {
      originalText: "",
      rawHtml: ""
    };
    _this._processor;
    return _this;
  }
  _createClass(MultichoiceTextChoice, [{
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
      var choiceClassName = "bb-test-answer-choice";
      if (this.props.isMulti) {
        choiceClassName += " bb-test-answer-choice-squared";
      } else {
        choiceClassName += " bb-test-answer-choice-rounded";
      }
      if (this.props.chosen) {
        choiceClassName += " bb-test-answer-choice-selected";
      }
      var content = null;
      var contentClassName = "bb-test-answer";
      if (!this.props.data.text) {
        var _content = null;
        if (this.props.forDevelopers) {
          contentClassName += " bb-placeholder";
          _content = this.props.texts.paragraphEmptyPlaceholder;
        }
        content = /*#__PURE__*/React.createElement("div", {
          className: contentClassName
        }, _content);
      } else if (this.props.data.has_formulas) {
        content = /*#__PURE__*/React.createElement("div", {
          className: contentClassName,
          dangerouslySetInnerHTML: {
            __html: this.state.rawHtml
          }
        });
      } else {
        content = /*#__PURE__*/React.createElement("div", {
          className: contentClassName
        }, SimpleFormattedFragment(this.props.data.text));
      }
      var answer = null;
      if (this.props.showCorrectAnswer) {
        var answerClass = "";
        if (this.props.isMulti) {
          answerClass += " bb-test-answer-choice-squared";
        } else {
          answerClass += " bb-test-answer-choice-rounded";
        }
        if (this.props.isCorrect) {
          answerClass += " bb-test-answer-choice-correct";
          answer = /*#__PURE__*/React.createElement("div", {
            className: answerClass
          });
        } else {
          answerClass += " bb-test-answer-choice-incorrect";
          answer = /*#__PURE__*/React.createElement("div", {
            className: answerClass
          }, /*#__PURE__*/React.createElement("div", {
            className: "bb-test-answer-choice-incorrect-first"
          }), /*#__PURE__*/React.createElement("div", {
            className: "bb-test-answer-choice-incorrect-last"
          }));
        }
      }
      return /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-2 col-sm-3 pr-0"
      }, /*#__PURE__*/React.createElement("div", {
        className: "bb-rel bb-test-answer"
      }, /*#__PURE__*/React.createElement("div", {
        className: choiceClassName,
        onClick: this._handleClick.bind(this)
      }, this.props.label), answer)), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-10 col-sm-7 pl-0"
      }, content));
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
  }, {
    key: "_handleClick",
    value: function _handleClick() {
      if (this.props.onChoose) {
        this.props.onChoose();
      }
    }
  }]);
  return MultichoiceTextChoice;
}(React.Component);