"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
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
var FloatingSelector = /*#__PURE__*/function (_React$Component) {
  function FloatingSelector(props) {
    var _this;
    _classCallCheck(this, FloatingSelector);
    _this = _callSuper(this, FloatingSelector, [props]);
    // this.props.id
    // this.props.options
    // this.props.title
    _this.state = {
      isSticky: false
    };

    // Define a callback ref
    _this.selectorRef = null;
    _this.setSelectorRef = function (element) {
      _this.selectorRef = element;
    };

    // Bind the handleScroll function
    _this.handleScroll = _this.handleScroll.bind(_this);
    return _this;
  }
  _inherits(FloatingSelector, _React$Component);
  return _createClass(FloatingSelector, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      // Add scroll event listener
      window.addEventListener("scroll", this.handleScroll);
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      // Remove scroll event listener
      window.removeEventListener("scroll", this.handleScroll);
    }
  }, {
    key: "handleScroll",
    value: function handleScroll() {
      if (this.selectorRef) {
        var topPosition = this.selectorRef.getBoundingClientRect().top;
        var shouldBeSticky = topPosition <= 0 && window.scrollY !== 0;
        if (shouldBeSticky !== this.state.isSticky) {
          this.setState({
            isSticky: shouldBeSticky
          });
        }
      }
    }
  }, {
    key: "render",
    value: function render() {
      var option_selector = [];
      for (var i = 0; i < this.props.options.length; i++) {
        var id = this.props.id[i];
        var options = this.props.options[i];
        var title = this.props.title[i];
        option_selector.push( /*#__PURE__*/React.createElement(React.Fragment, {
          key: "asd ".concat(i)
        }, /*#__PURE__*/React.createElement("label", {
          key: "label ".concat(i),
          htmlFor: id,
          className: "h5",
          style: {
            "fontWeight": "bold"
          }
        }, title, ":"), /*#__PURE__*/React.createElement("select", {
          key: "select ".concat(i),
          className: "select_v2",
          id: id
        }, options)));
      }
      return /*#__PURE__*/React.createElement("div", {
        ref: this.setSelectorRef // Set callback ref
        ,
        className: "selector ".concat(this.state.isSticky ? "is-sticky" : ""),
        style: _objectSpread({
          textAlign: "center"
        }, this.state.isSticky ? {
          position: "fixed",
          top: 0,
          left: "50%",
          transform: "translateX(-50%)",
          zIndex: 1000,
          backgroundColor: "white",
          padding: "10px",
          boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.2)"
        } : {})
      }, option_selector);
    }
  }]);
}(React.Component);