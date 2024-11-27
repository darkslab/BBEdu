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
var Question = /*#__PURE__*/function (_React$Component) {
  function Question(props) {
    _classCallCheck(this, Question);
    return _callSuper(this, Question, [props]);
  }
  _inherits(Question, _React$Component);
  return _createClass(Question, [{
    key: "render",
    value: function render() {
      var paragraphs_left_side = [];
      var paragraphs_right_side = [];
      var solutionParagraphs = [];
      // show solutions only if student is in result page
      var regex = new RegExp("^/(en|ru|kk)/student/results/([0-9A-Fa-f]{4,6})/$");
      var regex_dev = new RegExp("^/(en|ru|kk)/build/.+/preview/$");
      var show_solution = regex.test(window.location.pathname);
      var show_solution_dev = regex_dev.test(window.location.pathname);

      // console.log("Question.jsx", this.props.object.paragraphs)
      for (var i = 0; i < this.props.object.paragraphs.length; i++) {
        var paragraph_class = this.props.object.paragraphs[i].paragraph_class;
        var ParagraphClass = eval(paragraph_class);
        var parag = /*#__PURE__*/React.createElement(ParagraphClass, {
          key: i,
          data: this.props.object.paragraphs[i].meta_data,
          isShared: this.props.object.paragraphs[i].is_shared,
          texts: this.props.texts,
          testTexts: this.props.testTexts,
          forDevelopers: false
        });
        if (paragraph_class.includes("Solution")) {
          solutionParagraphs.push(parag);
        } else if (paragraph_class === "CalculatorParagraph" || paragraph_class === "PeriodicTableParagraph") {
          // skip calculator and periodic table paragraph
        } else {
          var left_side = this.props.object.paragraphs[i].meta_data["left_side"] | this.props.object.paragraphs[i].meta_data["left_side"] === undefined;
          if (left_side) {
            paragraphs_left_side.push(parag);
          } else {
            paragraphs_right_side.push(parag);
          }
        }
      }
      var solution = null;
      if ((show_solution || show_solution_dev) && solutionParagraphs.length > 0) {
        solution = /*#__PURE__*/React.createElement("div", {
          className: "border",
          style: {
            "borderTop": "solid"
          }
        }, /*#__PURE__*/React.createElement("h3", {
          key: "sep_sol_h3"
        }, this.props.texts.solution), solutionParagraphs);
      }
      var answerContent = null;
      if (this.props.object.answer_class) {
        var AnswerClass = eval(this.props.object.answer_class);
        answerContent = /*#__PURE__*/React.createElement(AnswerClass, {
          data: this.props.object.meta_data,
          answer: this.props.answerData,
          onUpdate: this.props.onAnswerUpdate,
          canAnswer: this.props.canAnswer,
          showCorrectAnswer: this.props.showCorrectAnswer,
          texts: this.props.texts
        });
      }
      return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("div", {
        className: "panel mb-15 panel-primary"
      }, /*#__PURE__*/React.createElement("div", {
        className: "panel-heading bb-rel clearfix"
      }, /*#__PURE__*/React.createElement("div", {
        className: "bb-test-number"
      }, this.props.count), /*#__PURE__*/React.createElement("h4", {
        className: "panel-title bb-test-title mt-15 mb-15 pull-left"
      }, this.props.texts.question), /*#__PURE__*/React.createElement(TestTimer, {
        secondsLeft: this.props.secondsLeft,
        hasTimer: this.props.hasTimer
      }), /*#__PURE__*/React.createElement(TestPeriodicTable, {
        hasPeriodicTable: this.props.hasPeriodicTable,
        periodicTableIconUrl: this.props.periodicTableIconUrl,
        periodicTableUrl: this.props.periodicTableUrl
      }), /*#__PURE__*/React.createElement(TestCalculator, {
        hasCalculator: this.props.hasCalculator,
        calculatorIconUrl: this.props.calculatorIconUrl
      })), /*#__PURE__*/React.createElement("div", {
        className: "row row-eq-height border",
        style: {
          "borderBottom": "solid"
        }
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-md-5 border pl-5 pr-5 pb-5",
        style: {
          "borderRight": "solid"
        }
      }, /*#__PURE__*/React.createElement("div", {
        className: ""
      }, paragraphs_left_side), answerContent), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-md-7 border pl-5 pr-5 pb-5",
        style: {
          "borderLeft": "solid"
        }
      }, paragraphs_right_side)), solution));
    }
  }]);
}(React.Component);