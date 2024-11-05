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
var BuyCreditKaspiQRPage = /*#__PURE__*/function (_React$Component) {
  function BuyCreditKaspiQRPage(props) {
    var _this;
    _classCallCheck(this, BuyCreditKaspiQRPage);
    _this = _callSuper(this, BuyCreditKaspiQRPage, [props]);
    /* props pass from django template */
    // props.qr_code_base64
    // props.secondsLeft
    // props.secondsTotal
    _this.state = {
      secondsLeft: props.secondsLeft || 60 * 5,
      // Default to 100 if not provided
      minutes: Math.floor(Math.max(props.secondsLeft - 1, 0) / 60),
      seconds: Math.max(props.secondsLeft - 1, 0) % 60
    };
    return _this;
  }
  _inherits(BuyCreditKaspiQRPage, _React$Component);
  return _createClass(BuyCreditKaspiQRPage, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this2 = this;
      // Set interval to decrease `secondsLeft` every 2 seconds
      this.interval = setInterval(function () {
        _this2.setState(function (prevState) {
          return {
            secondsLeft: Math.max(prevState.secondsLeft - 1, 0),
            // Ensure it doesn’t go below 0
            minutes: Math.floor(Math.max(prevState.secondsLeft - 1, 0) / 60),
            seconds: Math.max(prevState.secondsLeft - 1, 0) % 60
          };
        });
      }, 1000);
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      clearInterval(this.interval); // Clear interval when the component unmounts
    }
  }, {
    key: "calculateProgressWidth",
    value: function calculateProgressWidth() {
      var secondsTotal = this.props.secondsTotal || 100;
      var widthPercentage = this.state.secondsLeft / secondsTotal * 100;
      return "".concat(widthPercentage, "%");
    }
  }, {
    key: "render",
    value: function render() {
      var progressWidth = this.calculateProgressWidth();
      return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3"
      }, /*#__PURE__*/React.createElement("div", {
        className: "panel panel-default"
      }, /*#__PURE__*/React.createElement("div", {
        className: "panel-body text-center"
      }, /*#__PURE__*/React.createElement("p", {
        className: "text-center"
      }, /*#__PURE__*/React.createElement("strong", null, "\u0418\u043D\u0441\u0442\u0440\u0443\u043A\u0446\u0438\u044F \u043F\u043E \u043E\u043F\u043B\u0430\u0442\u0435"), " "), /*#__PURE__*/React.createElement("img", {
        src: "data:image/png;base64,".concat(this.props.qr_code_base64),
        alt: "QR Code",
        className: "img-responsive center-block"
      }), /*#__PURE__*/React.createElement("div", {
        style: {
          height: "5px",
          backgroundColor: "red",
          width: progressWidth,
          margin: "10px auto",
          // Centers the line
          transition: "width 1s linear" // Smoothly update width every second
        }
      }), /*#__PURE__*/React.createElement("p", {
        style: {
          marginTop: "10px",
          fontSize: "16px",
          fontWeight: "bold"
        }
      }, "\u041F\u043E\u0436\u0430\u043B\u0443\u0439\u0441\u0442\u0430, \u043E\u043F\u043B\u0430\u0442\u0438\u0442\u0435 \u0432 \u0442\u0435\u0447\u0435\u043D\u0438\u0435 ", this.state.minutes, " \u043C\u0438\u043D\u0443\u0442 \u0438 ", this.state.seconds, " \u0441\u0435\u043A\u0443\u043D\u0434")), /*#__PURE__*/React.createElement("div", {
        className: "text-center pb-10"
      }, /*#__PURE__*/React.createElement("a", {
        onClick: function onClick() {
          return window.location.reload();
        },
        className: "btn btn-primary"
      }, "\u041E\u0431\u043D\u043E\u0432\u0438\u0442\u044C"))))));
    }
  }]);
}(React.Component);