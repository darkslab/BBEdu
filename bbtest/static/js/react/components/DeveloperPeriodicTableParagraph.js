"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
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
var DeveloperPeriodicTableParagraph = /*#__PURE__*/function (_React$Component) {
  function DeveloperPeriodicTableParagraph(props) {
    var _this;
    _classCallCheck(this, DeveloperPeriodicTableParagraph);
    _this = _callSuper(this, DeveloperPeriodicTableParagraph, [props]);
    _this.state = {
      confirmModal: false
    };
    return _this;
  }
  _inherits(DeveloperPeriodicTableParagraph, _React$Component);
  return _createClass(DeveloperPeriodicTableParagraph, [{
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

      // let textareaClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
      // if (!this.props.data.text) {
      //     textareaClassName += " bb-test-paragraph-textarea-empty";
      // }

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
      console.log("this.props", this.props);
      return /*#__PURE__*/React.createElement(React.Fragment, null, modal, /*#__PURE__*/React.createElement("div", {
        className: paragraphClassName,
        "data-paragraph-id": this.props.paragraphId
      }, /*#__PURE__*/React.createElement("div", {
        className: "pt-5 pr-5 pb-5 pl-5 clearfix"
      }, sharedLabel, buttons, /*#__PURE__*/React.createElement("button", {
        type: "button",
        className: "btn btn-default btn-xs pull-right ml-5 invisible"
      }, "Spacer"))), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("img", {
        "class": "periodicTableThumbnail",
        src: this.props.data.periodicTableUrl,
        width: "100px",
        alt: "PeriodicTableThumbnail",
        onClick: this._openOverlay.bind(this)
      }), /*#__PURE__*/React.createElement("div", {
        id: "periodicTableOverlay",
        "class": "periodicTableOverlay",
        onClick: this._closeOverlay.bind(this)
      }, /*#__PURE__*/React.createElement("img", {
        id: "overlayPeriodicTableImage",
        src: "",
        alt: "PeriodicTableLarge"
      }))));
    }
  }, {
    key: "_openOverlay",
    value: function _openOverlay() {
      // console.log("_openOverlay", document.getElementById('overlayImage'));
      document.getElementById('overlayPeriodicTableImage').src = this.props.data.periodicTableUrl;
      document.getElementById('periodicTableOverlay').style.display = 'flex';
    }
  }, {
    key: "_closeOverlay",
    value: function _closeOverlay() {
      document.getElementById('periodicTableOverlay').style.display = 'none';
    }

    // _handleChange(event) {
    //     this.props.onChange({
    //         ...this.props.data,
    //         text: event.target.value
    //     });
    // }
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