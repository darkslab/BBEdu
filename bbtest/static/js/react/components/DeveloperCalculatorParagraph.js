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
var DeveloperCalculatorParagraph = /*#__PURE__*/function (_React$Component) {
  _inherits(DeveloperCalculatorParagraph, _React$Component);
  var _super = _createSuper(DeveloperCalculatorParagraph);
  function DeveloperCalculatorParagraph(props) {
    var _this;
    _classCallCheck(this, DeveloperCalculatorParagraph);
    _this = _super.call(this, props);
    _this.state = {
      confirmModal: false
    };
    return _this;
  }
  _createClass(DeveloperCalculatorParagraph, [{
    key: "render",
    value: function render() {
      var paragraphClassName = "form-group bb-test-section-movable";
      var buttons = [];
      if (this.props.canDelete) {
        buttons.push( /*#__PURE__*/React.createElement("button", {
          key: "delete",
          type: "button",
          className: "btn btn-danger btn-xs pull-right ml-5",
          onClick: this._renderModal.bind(this)
        }, /*#__PURE__*/React.createElement("i", {
          className: "fa fa-fw fa-times"
        })));
      }
      var sharedLabel = null;
      if (this.props.sharedQuestionIds.length > 0) {
        sharedLabel = /*#__PURE__*/React.createElement("p", {
          className: "text-danger pull-left mb-0"
        }, this.props.texts.paragraphsSharedLabelTextParagraph);
        paragraphClassName += " bb-test-section-background-shared";
      } else {
        paragraphClassName += " bb-test-section-background";
      }
      var modal = null;
      if (this.state.confirmModal) {
        modal = /*#__PURE__*/React.createElement(ConfirmModal, {
          title: this.props.texts.deleteModalTitle,
          yesCaption: this.props.texts.deleteModalYesCaption,
          noCaption: this.props.texts.deleteModalNoCaption,
          isInverse: true,
          complete: this._completeModal.bind(this)
        });
      }
      return /*#__PURE__*/React.createElement(React.Fragment, null, modal, /*#__PURE__*/React.createElement("div", {
        className: paragraphClassName,
        "data-paragraph-id": this.props.paragraphId
      }, /*#__PURE__*/React.createElement("div", {
        className: "pt-5 pr-5 pb-5 pl-5 clearfix"
      }, sharedLabel, buttons, /*#__PURE__*/React.createElement("button", {
        type: "button",
        className: "btn btn-default btn-xs pull-right ml-5 invisible"
      }, "Spacer"))), /*#__PURE__*/React.createElement("script", {
        src: "https://linangdata.com/calculatorEmbed/linangcalc.js"
      }), /*#__PURE__*/React.createElement("div", {
        style: {
          width: "50px",
          height: "50px",
          "backgroundImage": "url('https://linangdata.com/calculatorEmbed/icons/48x48.png')",
          zIndex: 99999
        }
      }, /*#__PURE__*/React.createElement("iframe", {
        id: "linangcalc",
        src: "https://linangdata.com/calculatorEmbed/embeddable.html?placement=right",
        width: "500",
        height: "500",
        scrolling: "auto",
        frameBorder: "0",
        allowtransparency: "true",
        style: {
          border: 0,
          position: "absolute",
          opacity: 1.0,
          zIndex: 99999
        }
      })));
    }
  }, {
    key: "_renderModal",
    value: function _renderModal() {
      this.setState({
        confirmModal: true
      });
    }
  }, {
    key: "_completeModal",
    value: function _completeModal(data) {
      if (data) {
        this.props.onDelete();
      } else {
        this.setState({
          confirmModal: false
        });
      }
    }
  }]);
  return DeveloperCalculatorParagraph;
}(React.Component);