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
var MultichoiceOneAnswer = /*#__PURE__*/function (_React$Component) {
  function MultichoiceOneAnswer(props) {
    var _this;
    _classCallCheck(this, MultichoiceOneAnswer);
    _this = _callSuper(this, MultichoiceOneAnswer, [props]);
    _this._alphabet = "ABCDEFGH";
    return _this;
  }
  _inherits(MultichoiceOneAnswer, _React$Component);
  return _createClass(MultichoiceOneAnswer, [{
    key: "render",
    value: function render() {
      var choices = [];
      for (var i = 0; i < this.props.data.choices.length; i++) {
        var ChoiceClass = eval(this.props.data.choices[i].choice_class);
        var chosen = false;
        if (this.props.answer && this.props.answer.correct_id === this.props.data.choices[i].id) {
          chosen = true;
        }
        var isCorrect = false;
        if (this.props.showCorrectAnswer) {
          if (this.props.data.correct_id !== null && this.props.data.correct_id === this.props.data.choices[i].id) {
            isCorrect = true;
          }
        }
        choices.push( /*#__PURE__*/React.createElement(ChoiceClass, {
          key: this.props.data.choices[i].id,
          data: this.props.data.choices[i].meta_data,
          label: this._alphabet[i],
          chosen: chosen,
          isMulti: false,
          onChoose: this._handleChoose.bind(this, this.props.data.choices[i].id),
          texts: this.props.texts,
          forDevelopers: false,
          showCorrectAnswer: this.props.showCorrectAnswer,
          isCorrect: isCorrect
        }));
      }
      return /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12"
      }, /*#__PURE__*/React.createElement("div", {
        className: "mb-15"
      }, /*#__PURE__*/React.createElement("div", {
        className: "panel-body"
      }, /*#__PURE__*/React.createElement("div", {
        className: "mb-15"
      }, choices)))));
    }
  }, {
    key: "_handleChoose",
    value: function _handleChoose(choiceId) {
      console.log(choiceId);
      if (!this.props.canAnswer) {
        return;
      }
      var data = {
        answer: {
          correct_id: choiceId
        },
        observation: {}
      };
      this.props.onUpdate(data);
    }
  }], [{
    key: "isCorrect",
    value: function isCorrect(answerMetaData, report) {
      if (!report) {
        return false;
      }
      if (answerMetaData.correct_id == report.correct_id) {
        return true;
      }
      return false;
    }
  }]);
}(React.Component);