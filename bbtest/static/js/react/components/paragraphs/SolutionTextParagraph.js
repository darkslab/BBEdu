"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i]; return arr2; }
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
var SolutionTextParagraph = /*#__PURE__*/function (_React$Component) {
  function SolutionTextParagraph(props) {
    var _this;
    _classCallCheck(this, SolutionTextParagraph);
    _this = _callSuper(this, SolutionTextParagraph, [props]);
    _this.state = {
      originalText: "",
      rawHtml: ""
    };
    _this._processor;
    return _this;
  }
  _inherits(SolutionTextParagraph, _React$Component);
  return _createClass(SolutionTextParagraph, [{
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

      // let youtube_links = text.match(/^(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=([a-zA-Z0-9_]+)|youtu\.be\/([a-zA-Z\d_]+))(?:&.*)?$/gm)

      var regexp = /(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=([a-zA-Z0-9_]+)|youtu\.be\/([a-zA-Z\d_]+))(?:&.*)?/gm;
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
        var youtube = [];
        var matches = this.props.data.text.matchAll(regexp);
        var _iterator = _createForOfIteratorHelper(matches),
          _step;
        try {
          for (_iterator.s(); !(_step = _iterator.n()).done;) {
            var match = _step.value;
            console.log(match);
            // this.props.data.text = this.props.data.text.replace(match[0], "");
            // let rep = '<div className="embed-responsive embed-responsive-16by9" key="you'+match.index+'"><iframe src="https://www.youtube.com/embed/' + match[1] +'" frameBorder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; allowfullscreen" ></iframe></div>'
            this.state.rawHtml = this.state.rawHtml.replace(match[0], "");
            youtube.push( /*#__PURE__*/React.createElement("div", {
              className: "embed-responsive embed-responsive-16by9",
              key: "you" + match.index
            }, /*#__PURE__*/React.createElement("iframe", {
              src: "https://www.youtube.com/embed/" + match[1],
              frameBorder: "0",
              allow: "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; allowfullscreen"
            })));
          }
          // console.log(this.state.rawHtml);
        } catch (err) {
          _iterator.e(err);
        } finally {
          _iterator.f();
        }
        content = /*#__PURE__*/React.createElement(React.Fragment, null, sharedAddon, /*#__PURE__*/React.createElement("div", {
          className: className,
          dangerouslySetInnerHTML: {
            __html: this.state.rawHtml
          }
        }), youtube.length > 0 && youtube);
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
}(React.Component);