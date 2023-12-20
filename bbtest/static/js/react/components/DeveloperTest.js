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
var DeveloperTest = /*#__PURE__*/function (_React$Component) {
  _inherits(DeveloperTest, _React$Component);
  var _super = _createSuper(DeveloperTest);
  function DeveloperTest(props) {
    var _this;
    _classCallCheck(this, DeveloperTest);
    _this = _super.call(this, props);
    _this.state = {
      isTestLoading: true,
      isQuestionLoading: true,
      isQuestionSaving: false,
      isErrored: false,
      questionIndex: 0
    };
    _this._questionObject = null;
    _this._abilityObject = null;
    _this._oldQuestionObjects = [];
    _this._questionAttributes = null;
    _this._$xhrs = {
      question: null,
      attributes: null
    };
    _this._finalSave = false;
    _this._boundConfirmIsSaved = _this._confirmIsSaved.bind(_assertThisInitialized(_this));
    _this._boundConfirmIsSavedTurbolinks = _this._confirmIsSavedTurbolinks.bind(_assertThisInitialized(_this));
    return _this;
  }
  _createClass(DeveloperTest, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      var questionNumber = 1;
      if (location.hash) {
        questionNumber = parseInt(location.hash.substr(1), 10);
        if (isNaN(questionNumber) || questionNumber < 1 || questionNumber > this.props.questionIds.length) {
          questionNumber = 1;
        }
      }
      this._getQuestionData(questionNumber - 1, false);
      this._$xhrs["attributes"] = $.get({
        url: this.props.attributesUrl,
        success: this._ajaxSuccess.bind(this, "attributes", false),
        error: this._ajaxError.bind(this, "attributes")
      });
      $(window).on("beforeunload", this._boundConfirmIsSaved);
      $(document).on("turbolinks:before-visit", this._boundConfirmIsSavedTurbolinks);
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      this._cleanUp();
      $(window).off("beforeunload", this._boundConfirmIsSaved);
      $(document).off("turbolinks:before-visit", this._boundConfirmIsSavedTurbolinks);
    }
  }, {
    key: "render",
    value: function render() {
      var content = null;
      if (this.state.isErrored) {
        content = /*#__PURE__*/React.createElement("h4", {
          className: "text-center text-danger mt-100 mb-0"
        }, this.props.texts.error);
      } else if (!this.state.isTestLoading && !this.state.isQuestionLoading && !this.state.isQuestionSaving) {
        content = /*#__PURE__*/React.createElement(DeveloperQuestion, {
          count: this.state.questionIndex + 1,
          attributes: this._questionAttributes,
          object: this._questionObject,
          ability: this._abilityObject,
          texts: this.props.texts,
          errorOut: this._errorOut.bind(this)
        });
      } else {
        content = /*#__PURE__*/React.createElement("img", {
          className: "bb-spinner",
          src: this.props.spinnerLogo
        });
      }
      var pagination = null;
      if (this.props.questionIds.length > 1 && !this.state.isErrored && !this.state.isTestLoading && !this._finalSave) {
        var width = 6;
        if (width < 1) {
          width = 1;
        } else if (width > this.props.questionIds.length) {
          width = this.props.questionIds.length;
        }
        var padding = parseInt((width - 1) / 2, 10);
        var rightPadding = (width - 1) % 2;
        var indexes = [this.state.questionIndex];
        for (var i = 0; i < padding; i++) {
          indexes.unshift(indexes[0] - 1);
          indexes.push(indexes[indexes.length - 1] + 1);
        }
        for (var _i = 0; _i < rightPadding; _i++) {
          indexes.push(indexes[indexes.length - 1] + 1);
        }
        if (indexes[0] < 0) {
          while (true) {
            if (indexes[0] >= 0) {
              break;
            }
            indexes.shift();
            indexes.push(indexes[indexes.length - 1] + 1);
          }
        } else if (indexes[indexes.length - 1] >= this.props.questionIds.length) {
          while (true) {
            if (indexes[indexes.length - 1] < this.props.questionIds.length) {
              break;
            }
            indexes.pop();
            indexes.unshift(indexes[0] - 1);
          }
        }
        var paginationElements = [];
        if (this.state.questionIndex > 0) {
          paginationElements.push( /*#__PURE__*/React.createElement("li", {
            key: "left"
          }, /*#__PURE__*/React.createElement("a", {
            href: "javascript:void(0);",
            onClick: this._nextQuestion.bind(this, this.state.questionIndex - 1)
          }, "\xAB")));
        } else {
          paginationElements.push( /*#__PURE__*/React.createElement("li", {
            key: "left",
            className: "disabled"
          }, /*#__PURE__*/React.createElement("a", {
            href: "javascript:void(0);"
          }, "\xAB")));
        }
        for (var _i2 = 0; _i2 < indexes.length; _i2++) {
          if (indexes[_i2] === this.state.questionIndex) {
            paginationElements.push( /*#__PURE__*/React.createElement("li", {
              key: indexes[_i2].toString(),
              className: "active"
            }, /*#__PURE__*/React.createElement("a", {
              href: "javascript:void(0);"
            }, indexes[_i2] + 1)));
          } else {
            paginationElements.push( /*#__PURE__*/React.createElement("li", {
              key: indexes[_i2].toString()
            }, /*#__PURE__*/React.createElement("a", {
              href: "javascript:void(0);",
              onClick: this._nextQuestion.bind(this, indexes[_i2])
            }, indexes[_i2] + 1)));
          }
        }
        if (this.state.questionIndex < this.props.questionIds.length - 1) {
          paginationElements.push( /*#__PURE__*/React.createElement("li", {
            key: "right"
          }, /*#__PURE__*/React.createElement("a", {
            href: "javascript:void(0);",
            onClick: this._nextQuestion.bind(this, this.state.questionIndex + 1)
          }, "\xBB")));
        } else {
          paginationElements.push( /*#__PURE__*/React.createElement("li", {
            key: "right",
            className: "disabled"
          }, /*#__PURE__*/React.createElement("a", {
            href: "javascript:void(0);"
          }, "\xBB")));
        }
        pagination = /*#__PURE__*/React.createElement("div", {
          className: "col-xs-12 col-sm-6 text-center"
        }, /*#__PURE__*/React.createElement("ul", {
          className: "pagination pagination-sm mt-0 mb-0"
        }, paginationElements));
      }
      return /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-sm-6"
      }, /*#__PURE__*/React.createElement("button", {
        type: "button",
        "class": "btn btn-info mr-5 mb-5",
        "data-toggle": "modal",
        "data-target": "[data-specification-modal]"
      }, this.props.texts.testSpec), /*#__PURE__*/React.createElement("button", {
        type: "button",
        disabled: this.state.isQuestionSaving,
        className: "btn btn-success mr-5 mb-5",
        onClick: this._saveAndExit.bind(this, this.props.dashboardUrl)
      }, this.props.texts.saveAndExitButton), /*#__PURE__*/React.createElement("button", {
        type: "button",
        disabled: this.state.isQuestionSaving,
        className: "btn btn-success mr-5 mb-5",
        onClick: this._saveAndExit.bind(this, this.props.previewUrl)
      }, this.props.texts.saveAndPreviewButton)), pagination, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 bb-test-container"
      }, content));
    }
  }, {
    key: "_saveAndExit",
    value: function _saveAndExit(followUrl) {
      if (!this._questionObject) {
        return;
      }
      this.setState({
        isQuestionSaving: true
      });
      this._finalSave = true;
      var object = this._questionObject;
      this._questionObject = null;
      this._abilityObject = null;
      object.save("test", this._questionLastSave.bind(this, followUrl));
      this._oldQuestionObjects.push(object);
    }
  }, {
    key: "_nextQuestion",
    value: function _nextQuestion(index) {
      this.setState({
        isQuestionLoading: true
      });
      if (this._questionObject) {
        this.setState({
          isQuestionSaving: true
        });
        var object = this._questionObject;
        this._questionObject = null;
        this._abilityObject = null;
        object.save("test", this._questionSave.bind(this));
        this._oldQuestionObjects.push(object);
      }
      this._getQuestionData(index, true);
    }
  }, {
    key: "_ajaxSuccess",
    value: function _ajaxSuccess(type, pageview, data, status, $xhr) {
      if (pageview) {
        ga_report_pageview();
      }
      if (type === "question") {
        this._questionObject = new DeveloperQuestionObject(data.id, data.data, data.paragraphs, data.texts, this.props.questionUrl, this.props.paragraphsUrl, this.props.uploadStartUrl, this.props.spinnerLogo);
        this._abilityObject = new (eval(this.props.ability))(this._questionObject);
        this.setState({
          isQuestionLoading: false
        });
      } else if (type === "attributes") {
        this._questionAttributes = data;
      }
      if (this._questionObject && this._questionAttributes) {
        this.setState({
          isTestLoading: false
        });
      }
    }
  }, {
    key: "_ajaxError",
    value: function _ajaxError(type, $xhr, status, error) {
      if (status === "abort") {
        return;
      }
      this._errorOut();
    }
  }, {
    key: "_cleanUp",
    value: function _cleanUp() {
      var object;
      while (object = this._oldQuestionObjects.shift()) {
        object.stop("test");
      }
      this._$xhrs["question"].abort();
      this._$xhrs["attributes"].abort();
    }
  }, {
    key: "_questionSave",
    value: function _questionSave(success, object) {
      var index = this._oldQuestionObjects.indexOf(object);
      if (index > -1) {
        this._oldQuestionObjects.splice(index, 1);
      }
      if (!success) {
        this._errorOut();
        return;
      }
      this.setState({
        isQuestionSaving: false
      });
    }
  }, {
    key: "_questionLastSave",
    value: function _questionLastSave(followUrl, success, object) {
      var index = this._oldQuestionObjects.indexOf(object);
      if (index > -1) {
        this._oldQuestionObjects.splice(index, 1);
      }
      if (!success || this._oldQuestionObjects.length) {
        this._errorOut();
        return;
      }
      $(document).off("turbolinks:before-visit", this._boundConfirmIsSavedTurbolinks);
      Turbolinks.visit(followUrl);
    }
  }, {
    key: "_getQuestionData",
    value: function _getQuestionData(index, pageview) {
      this.setState({
        questionIndex: index
      });
      history.replaceState(history.state, "", location.pathname + "#" + (index + 1).toString());
      if (this._$xhrs["question"]) {
        this._$xhrs["question"].abort();
      }
      this._$xhrs["question"] = $.get({
        url: this.props.questionUrl + this.props.questionIds[index] + "/",
        success: this._ajaxSuccess.bind(this, "question", pageview),
        error: this._ajaxError.bind(this, "question")
      });
    }
  }, {
    key: "_errorOut",
    value: function _errorOut() {
      this.setState({
        isErrored: true
      });
      this._cleanUp();
    }
  }, {
    key: "_confirmIsSaved",
    value: function _confirmIsSaved(event) {
      if (this.state.isErrored) {
        return;
      }
      if (this.state.isQuestionSaving || !this._questionObject.isSaved()) {
        var confirmationMessage = "\o/";
        event.returnValue = confirmationMessage;
        return confirmationMessage;
      }
    }
  }, {
    key: "_confirmIsSavedTurbolinks",
    value: function _confirmIsSavedTurbolinks(event) {
      if (this.state.isErrored) {
        return;
      }
      if (this.state.isQuestionSaving || !this._questionObject.isSaved()) {
        event.preventDefault();
      }
    }
  }]);
  return DeveloperTest;
}(React.Component);