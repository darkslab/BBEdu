"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
var _excluded = ["has_formulas"],
  _excluded2 = ["left_side"];
function _objectWithoutProperties(source, excluded) { if (source == null) return {}; var target = _objectWithoutPropertiesLoose(source, excluded); var key, i; if (Object.getOwnPropertySymbols) { var sourceSymbolKeys = Object.getOwnPropertySymbols(source); for (i = 0; i < sourceSymbolKeys.length; i++) { key = sourceSymbolKeys[i]; if (excluded.indexOf(key) >= 0) continue; if (!Object.prototype.propertyIsEnumerable.call(source, key)) continue; target[key] = source[key]; } } return target; }
function _objectWithoutPropertiesLoose(source, excluded) { if (source == null) return {}; var target = {}; var sourceKeys = Object.keys(source); var key, i; for (i = 0; i < sourceKeys.length; i++) { key = sourceKeys[i]; if (excluded.indexOf(key) >= 0) continue; target[key] = source[key]; } return target; }
function ownKeys(e, r) { var t = Object.keys(e); if (Object.getOwnPropertySymbols) { var o = Object.getOwnPropertySymbols(e); r && (o = o.filter(function (r) { return Object.getOwnPropertyDescriptor(e, r).enumerable; })), t.push.apply(t, o); } return t; }
function _objectSpread(e) { for (var r = 1; r < arguments.length; r++) { var t = null != arguments[r] ? arguments[r] : {}; r % 2 ? ownKeys(Object(t), !0).forEach(function (r) { _defineProperty(e, r, t[r]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) { Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r)); }); } return e; }
function _defineProperty(obj, key, value) { key = _toPropertyKey(key); if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : i + ""; }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
function _callSuper(t, o, e) { return o = _getPrototypeOf(o), _possibleConstructorReturn(t, _isNativeReflectConstruct() ? Reflect.construct(o, e || [], _getPrototypeOf(t).constructor) : o.apply(t, e)); }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { try { var t = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); } catch (t) {} return (_isNativeReflectConstruct = function _isNativeReflectConstruct() { return !!t; })(); }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
var DeveloperSplitTextParagraph = /*#__PURE__*/function (_React$Component) {
  function DeveloperSplitTextParagraph(props) {
    var _this;
    _classCallCheck(this, DeveloperSplitTextParagraph);
    _this = _callSuper(this, DeveloperSplitTextParagraph, [props]);
    _this.state = {
      confirmModal: false
    };
    return _this;
  }
  _inherits(DeveloperSplitTextParagraph, _React$Component);
  return _createClass(DeveloperSplitTextParagraph, [{
    key: "render",
    value: function render() {
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
      buttons.push( /*#__PURE__*/React.createElement("button", {
        key: "left_side",
        type: "button",
        className: "btn btn-xs pull-right ml-5 btn-default",
        onClick: this._handleLeftSide.bind(this)
      }, this.props.data.left_side | this.props.data.left_side === undefined ? this.props.texts.controlLeftSideButton : this.props.texts.controlRightSideButton));
      var leftClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
      if (!this.props.data.left.text) {
        leftClassName += " bb-test-paragraph-textarea-empty";
      }
      var rightClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
      if (!this.props.data.right.text) {
        rightClassName += " bb-test-paragraph-textarea-empty";
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
        className: "form-group bb-test-section-movable bb-test-section-background",
        "data-paragraph-id": this.props.paragraphId
      }, /*#__PURE__*/React.createElement("div", {
        className: "pt-5 pr-5 pb-5 pl-5 clearfix"
      }, buttons, /*#__PURE__*/React.createElement("button", {
        type: "button",
        className: "btn btn-default btn-xs pull-right ml-5 invisible"
      }, "Spacer")), /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2"
      }, /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-6 pr-5"
      }, /*#__PURE__*/React.createElement("h5", {
        className: "text-center mt-0 mb-10"
      }, /*#__PURE__*/React.createElement("em", null, this.props.testTexts.column_a)), /*#__PURE__*/React.createElement("textarea", {
        className: leftClassName,
        placeholder: this.props.texts.paragraphTextareaPlaceholder,
        value: this.props.data.left.text,
        onChange: this._handleChange.bind(this, "left")
      })), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-6 pl-5"
      }, /*#__PURE__*/React.createElement("h5", {
        className: "text-center mt-0 mb-10"
      }, /*#__PURE__*/React.createElement("em", null, this.props.testTexts.column_b)), /*#__PURE__*/React.createElement("textarea", {
        className: rightClassName,
        placeholder: this.props.texts.paragraphTextareaPlaceholder,
        value: this.props.data.right.text,
        onChange: this._handleChange.bind(this, "right")
      })))))));
    }
  }, {
    key: "_handleChange",
    value: function _handleChange(side, event) {
      var data = _objectSpread({}, this.props.data);
      data.left = _objectSpread({}, data.left);
      data.right = _objectSpread({}, data.right);
      switch (side) {
        case "left":
        case "right":
          data[side].text = event.target.value;
          break;
      }
      this.props.onChange(data);
    }
  }, {
    key: "_handleFormulas",
    value: function _handleFormulas() {
      var _this$props$data = this.props.data,
        has_formulas = _this$props$data.has_formulas,
        data = _objectWithoutProperties(_this$props$data, _excluded);
      data.left = _objectSpread({}, this.props.data.left);
      data.right = _objectSpread({}, this.props.data.right);
      if (has_formulas === undefined) {
        data.has_formulas = true;
      }
      this.props.onChange(data);
    }
  }, {
    key: "_handleLeftSide",
    value: function _handleLeftSide() {
      var _this$props$data2 = this.props.data,
        left_side = _this$props$data2.left_side,
        data = _objectWithoutProperties(_this$props$data2, _excluded2);
      if (left_side === undefined) {
        data.left_side = false;
      } else {
        data.left_side = !left_side;
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
}(React.Component);