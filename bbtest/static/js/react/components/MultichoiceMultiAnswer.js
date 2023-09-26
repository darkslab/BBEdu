"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }
function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _iterableToArray(iter) { if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter); }
function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i]; return arr2; }
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
var MultichoiceMultiAnswer = /*#__PURE__*/function (_React$Component) {
  _inherits(MultichoiceMultiAnswer, _React$Component);
  var _super = _createSuper(MultichoiceMultiAnswer);
  function MultichoiceMultiAnswer(props) {
    var _this;
    _classCallCheck(this, MultichoiceMultiAnswer);
    _this = _super.call(this, props);
    _this._alphabet = "ABCDEFGH";
    _this._correctIds = [];
    _this._assignCorrectIds(_this.props.answer);
    return _this;
  }
  _createClass(MultichoiceMultiAnswer, [{
    key: "componentWillReceiveProps",
    value: function componentWillReceiveProps(nextProps) {
      this._assignCorrectIds(nextProps.answer);
    }
  }, {
    key: "render",
    value: function render() {
      var choices = [];
      for (var i = 0; i < this.props.data.choices.length; i++) {
        var ChoiceClass = eval(this.props.data.choices[i].choice_class);
        var chosen = false;
        if (this.props.answer && this.props.answer.correct_ids.indexOf(this.props.data.choices[i].id) > -1) {
          chosen = true;
        }
        var isCorrect = false;
        if (this.props.showCorrectAnswer) {
          if (this.props.data.correct_ids.length && this.props.data.correct_ids.indexOf(this.props.data.choices[i].id) > -1) {
            isCorrect = true;
          }
        }
        choices.push( /*#__PURE__*/React.createElement(ChoiceClass, {
          key: this.props.data.choices[i].id,
          data: this.props.data.choices[i].meta_data,
          label: this._alphabet[i],
          chosen: chosen,
          isMulti: true,
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
        className: "panel panel-default mb-15"
      }, /*#__PURE__*/React.createElement("div", {
        className: "panel-heading"
      }, /*#__PURE__*/React.createElement("h4", {
        className: "panel-title text-center"
      }, this.props.texts.multichoiceMultiAnswerTitle)), /*#__PURE__*/React.createElement("div", {
        className: "panel-body"
      }, /*#__PURE__*/React.createElement("div", {
        className: "mb-15"
      }, choices)))));
    }
  }, {
    key: "_handleChoose",
    value: function _handleChoose(choiceId) {
      if (!this.props.canAnswer) {
        return;
      }
      var i = this._correctIds.indexOf(choiceId);
      if (i > -1) {
        this._correctIds.splice(i, 1);
      } else {
        this._correctIds.push(choiceId);
      }
      var data = {
        answer: null,
        observation: {}
      };
      if (this._correctIds.length) {
        data.answer = {
          correct_ids: _toConsumableArray(this._correctIds)
        };
      }
      this.props.onUpdate(data);
    }
  }, {
    key: "_assignCorrectIds",
    value: function _assignCorrectIds(answer) {
      this._correctIds = [];
      if (!answer) {
        return;
      }
      for (var i = 0; i < answer.correct_ids.length; i++) {
        this._correctIds.push(answer.correct_ids[i]);
      }
    }
  }], [{
    key: "isCorrect",
    value: function isCorrect(answerMetaData, report) {
      if (!report) {
        return false;
      }
      if (answerMetaData.correct_ids.length != report.correct_ids.length) {
        return false;
      }
      for (var i = 0; i < answerMetaData.correct_ids.length; i++) {
        if (report.correct_ids.indexOf(answerMetaData.correct_ids[i]) < 0) {
          return false;
        }
      }
      return true;
    }
  }]);
  return MultichoiceMultiAnswer;
}(React.Component);