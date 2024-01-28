"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
var _excluded = ["has_formulas"];
function _objectWithoutProperties(source, excluded) { if (source == null) return {}; var target = _objectWithoutPropertiesLoose(source, excluded); var key, i; if (Object.getOwnPropertySymbols) { var sourceSymbolKeys = Object.getOwnPropertySymbols(source); for (i = 0; i < sourceSymbolKeys.length; i++) { key = sourceSymbolKeys[i]; if (excluded.indexOf(key) >= 0) continue; if (!Object.prototype.propertyIsEnumerable.call(source, key)) continue; target[key] = source[key]; } } return target; }
function _objectWithoutPropertiesLoose(source, excluded) { if (source == null) return {}; var target = {}; var sourceKeys = Object.keys(source); var key, i; for (i = 0; i < sourceKeys.length; i++) { key = sourceKeys[i]; if (excluded.indexOf(key) >= 0) continue; target[key] = source[key]; } return target; }
function ownKeys(e, r) { var t = Object.keys(e); if (Object.getOwnPropertySymbols) { var o = Object.getOwnPropertySymbols(e); r && (o = o.filter(function (r) { return Object.getOwnPropertyDescriptor(e, r).enumerable; })), t.push.apply(t, o); } return t; }
function _objectSpread(e) { for (var r = 1; r < arguments.length; r++) { var t = null != arguments[r] ? arguments[r] : {}; r % 2 ? ownKeys(Object(t), !0).forEach(function (r) { _defineProperty(e, r, t[r]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) { Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r)); }); } return e; }
function _defineProperty(obj, key, value) { key = _toPropertyKey(key); if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
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
var DeveloperSolutionTextParagraph = /*#__PURE__*/function (_React$Component) {
  _inherits(DeveloperSolutionTextParagraph, _React$Component);
  var _super = _createSuper(DeveloperSolutionTextParagraph);
  function DeveloperSolutionTextParagraph(props) {
    var _this;
    _classCallCheck(this, DeveloperSolutionTextParagraph);
    _this = _super.call(this, props);
    _this.state = {
      confirmModal: false
    };
    return _this;
  }
  _createClass(DeveloperSolutionTextParagraph, [{
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
      buttons.push( /*#__PURE__*/React.createElement("button", {
        key: "formulas",
        type: "button",
        className: "btn btn-xs pull-right ml-5" + (this.props.data.has_formulas ? " btn-success active" : " btn-default"),
        onClick: this._handleFormulas.bind(this)
      }, this.props.texts.controlFormulasButton));
      var sharedLabel = null;
      if (this.props.sharedQuestionIds.length > 0) {
        sharedLabel = /*#__PURE__*/React.createElement("p", {
          className: "text-danger pull-left mb-0"
        }, this.props.texts.paragraphsSharedLabelTextParagraph + "ssdd");
        paragraphClassName += " bb-test-section-background-shared";
      } else {
        paragraphClassName += " bb-test-section-background-solution";
      }
      var textareaClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea-solution";
      if (!this.props.data.text) {
        textareaClassName += " bb-test-paragraph-textarea-empty";
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
      // console.log("ans0", this.props);
      // console.log("dd1", this.props.data);

      return /*#__PURE__*/React.createElement(React.Fragment, null, modal, /*#__PURE__*/React.createElement("div", {
        className: paragraphClassName,
        "data-paragraph-id": this.props.paragraphId
      }, /*#__PURE__*/React.createElement("div", {
        className: "pt-5 pr-5 pb-5 pl-5 clearfix"
      }, /*#__PURE__*/React.createElement("span", null, this.props.texts.solution), sharedLabel, buttons, /*#__PURE__*/React.createElement("button", {
        type: "button",
        className: "btn btn-default btn-xs pull-right ml-5 invisible"
      }, "Spacer")), /*#__PURE__*/React.createElement("textarea", {
        className: textareaClassName,
        placeholder: this.props.texts.paragraphSolutionTextareaPlaceholder,
        value: this.props.data.text,
        onChange: this._handleChange.bind(this)
      })));
    }
  }, {
    key: "_handleChange",
    value: function _handleChange(event) {
      this.props.onChange(_objectSpread(_objectSpread({}, this.props.data), {}, {
        text: event.target.value
      }));
    }
  }, {
    key: "_handleFormulas",
    value: function _handleFormulas() {
      var _this$props$data = this.props.data,
        has_formulas = _this$props$data.has_formulas,
        data = _objectWithoutProperties(_this$props$data, _excluded);
      if (has_formulas === undefined) {
        data.has_formulas = true;
      }
      this.props.onChange(data);
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
  return DeveloperSolutionTextParagraph;
}(React.Component);