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
var Test = /*#__PURE__*/function (_React$Component) {
  function Test(props) {
    var _this;
    _classCallCheck(this, Test);
    _this = _callSuper(this, Test, [props]);
    _this.state = {
      isErrored: false,
      status: undefined,
      toggleFlag: true,
      confirmationFor: undefined
    };
    _this.error_msg = "";
    _this._xhrStartTime;
    _this._$xhr;
    _this._statusData;
    _this._lingerTimer = null;
    _this._currentQuestionIndex = 0;
    _this._boundWindowBlur = _this._windowBlur.bind(_this);
    _this._boundWindowFocus = _this._windowFocus.bind(_this);
    return _this;
  }
  _inherits(Test, _React$Component);
  return _createClass(Test, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      this._continue(true, false);
      // _load_calculator()

      $(window).on("blur", this._boundWindowBlur);
      $(window).on("focus", this._boundWindowFocus);
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      this._stop();

      // _unload_calculator()
      $(window).off("blur", this._boundWindowBlur);
      $(window).off("focus", this._boundWindowFocus);
    }
  }, {
    key: "render",
    value: function render() {
      var content = null;
      switch (this.state.status) {
        case "queued":
          var instructions = [];
          for (var i = 0; i < this._statusData.instructions.length; i++) {
            var className = "lead";
            var isLastGroup = true;
            if (i < this._statusData.instructions.length - 1) {
              isLastGroup = false;
            }
            for (var j = 0; j < this._statusData.instructions[i].length; j++) {
              var innerClassName = "";
              if (j < this._statusData.instructions[i].length - 1) {
                innerClassName += " mb-0";
              } else if (!isLastGroup) {
                innerClassName += " mb-10";
              }
              instructions.push( /*#__PURE__*/React.createElement("p", {
                key: i + "-" + j,
                className: className + innerClassName
              }, this._statusData.instructions[i][j]));
            }
          }
          var video = null;
          if (this._statusData.video) {
            video = /*#__PURE__*/React.createElement("div", {
              className: "embed-responsive embed-responsive-16by9 mb-23"
            }, /*#__PURE__*/React.createElement("iframe", {
              src: this._statusData.video,
              frameBorder: "0",
              allow: "accelerometer; encrypted-media; gyroscope; picture-in-picture",
              allowFullScreen: true
            }));
          }
          content = /*#__PURE__*/React.createElement("div", {
            className: "panel panel-default"
          }, /*#__PURE__*/React.createElement("div", {
            className: "panel-body"
          }, /*#__PURE__*/React.createElement("h3", {
            className: "text-center mb-15"
          }, this._statusData.section[0], " ", /*#__PURE__*/React.createElement("span", {
            className: "label label-default"
          }, this._statusData.section[1])), instructions, video, /*#__PURE__*/React.createElement("div", {
            className: "text-center mb-23"
          }, /*#__PURE__*/React.createElement("div", {
            className: "visible-xs-block"
          }, /*#__PURE__*/React.createElement("button", {
            type: "button",
            className: "btn btn-primary btn-block",
            onClick: this._renderModal.bind(this, "start")
          }, this.props.texts.startButton)), /*#__PURE__*/React.createElement("div", {
            className: "hidden-xs"
          }, /*#__PURE__*/React.createElement("button", {
            type: "button",
            className: "btn btn-primary btn-lg",
            onClick: this._renderModal.bind(this, "start")
          }, this.props.texts.startButton)))));
          break;
        case "started":
          var header = null;
          if (this._statusData.section !== undefined) {
            header = /*#__PURE__*/React.createElement("div", {
              className: "row"
            }, /*#__PURE__*/React.createElement("div", {
              className: "col-xs-12"
            }, /*#__PURE__*/React.createElement("h4", {
              className: "text-center mt-0 mb-23"
            }, this._statusData.section[0], " ", /*#__PURE__*/React.createElement("span", {
              className: "label label-default"
            }, this._statusData.section[1]))));
          }
          var bottomPaginationLeft = null;
          var bottomPaginationRight = null;
          if (this._statusData.questionIndex > 0) {
            bottomPaginationLeft = /*#__PURE__*/React.createElement("li", {
              className: "previous"
            }, /*#__PURE__*/React.createElement("a", {
              href: "javascript:void(0);",
              onClick: this._setQuestionIndex.bind(this, this._statusData.questionIndex - 1)
            }, "\u2190 ", this.props.texts.previousPager));
          } else {
            bottomPaginationLeft = /*#__PURE__*/React.createElement("li", {
              className: "previous disabled"
            }, /*#__PURE__*/React.createElement("a", {
              href: "javascript:void(0);"
            }, "\u2190 ", this.props.texts.previousPager));
          }
          if (this._statusData.questionIndex < this._statusData.questionsCount - 1) {
            bottomPaginationRight = /*#__PURE__*/React.createElement("li", {
              className: "next"
            }, /*#__PURE__*/React.createElement("a", {
              href: "javascript:void(0);",
              onClick: this._setQuestionIndex.bind(this, this._statusData.questionIndex + 1)
            }, this.props.texts.nextPager, " \u2192"));
          } else {
            bottomPaginationRight = /*#__PURE__*/React.createElement("li", {
              className: "next disabled"
            }, /*#__PURE__*/React.createElement("a", {
              href: "javascript:void(0);"
            }, this.props.texts.nextPager, " \u2192"));
          }
          var endControl = null;
          if (this.props.canEnd) {
            endControl = /*#__PURE__*/React.createElement("div", {
              className: "row"
            }, /*#__PURE__*/React.createElement("div", {
              className: "col-xs-12 text-center"
            }, /*#__PURE__*/React.createElement("button", {
              type: "button",
              className: "btn btn-danger btn-sm mt-10",
              onClick: this._renderModal.bind(this, "end")
            }, this.props.texts.endButton)));
          }

          // const hasPeriodicTableList = JSON.parse(this.props.hasPeriodicTable)
          // const hasCalculatorList = JSON.parse(this.props.hasCalculator)
          // console.log(hasPeriodicTableList, hasCalculatorList)

          content = /*#__PURE__*/React.createElement(React.Fragment, null, header, /*#__PURE__*/React.createElement("div", {
            className: "row"
          }, /*#__PURE__*/React.createElement("div", {
            className: "col-xs-12 text-center hidden-xs"
          }, /*#__PURE__*/React.createElement("ul", {
            className: "pagination mt-0 mb-0"
          }, this._paginationElements(13))), /*#__PURE__*/React.createElement("div", {
            className: "col-xs-12 text-center visible-xs-block"
          }, /*#__PURE__*/React.createElement("ul", {
            className: "pagination pagination-sm mt-0 mb-0"
          }, this._paginationElements(6)))), /*#__PURE__*/React.createElement(Question, {
            count: this._statusData.questionIndex + 1,
            object: this._statusData.testObject.question(this._statusData.questionIndex),
            answerData: this._statusData.testObject.answer(this._statusData.questionIndex),
            onAnswerUpdate: this._statusData.testObject.updateAnswer.bind(this._statusData.testObject, this._statusData.questionIndex),
            canAnswer: this._statusData.testObject.canAnswer(),
            showCorrectAnswer: this._statusData.testObject.showCorrectAnswer(),
            testTexts: this._statusData.testObject.texts(),
            secondsLeft: this._statusData.focused ? this._statusData.seconds : -1,
            texts: this.props.texts,
            hasTimer: this.props.hasTimer,
            hasPeriodicTable: this._statusData.hasPeriodicTable[this._statusData.questionIndex],
            periodicTableIconUrl: this.props.periodicTableIconUrl,
            periodicTableUrl: this.props.periodicTableUrl,
            hasCalculator: this._statusData.hasCalculator[this._statusData.questionIndex],
            calculatorIconUrl: this.props.calculatorIconUrl,
            username: this._statusData.username
          }), /*#__PURE__*/React.createElement("div", {
            className: "row"
          }, /*#__PURE__*/React.createElement("div", {
            className: "col-xs-12"
          }, /*#__PURE__*/React.createElement("ul", {
            className: "pager mt-0 mb-0"
          }, bottomPaginationLeft, bottomPaginationRight))), endControl);
          break;
        case "expired":
          content = /*#__PURE__*/React.createElement("div", {
            className: "panel panel-default"
          }, /*#__PURE__*/React.createElement("div", {
            className: "panel-body"
          }, /*#__PURE__*/React.createElement("h3", {
            className: "text-center mb-15 text-danger"
          }, this.props.texts.expiredTitle), /*#__PURE__*/React.createElement("p", {
            className: "lead text-center"
          }, this.props.texts.expiredExplanation), /*#__PURE__*/React.createElement("div", {
            className: "text-center mb-23"
          }, /*#__PURE__*/React.createElement("div", {
            className: "visible-xs-block"
          }, /*#__PURE__*/React.createElement("button", {
            type: "button",
            className: "btn btn-primary btn-block",
            onClick: this._end.bind(this)
          }, this.props.texts.continueButton)), /*#__PURE__*/React.createElement("div", {
            className: "hidden-xs"
          }, /*#__PURE__*/React.createElement("button", {
            type: "button",
            className: "btn btn-primary btn-lg",
            onClick: this._end.bind(this)
          }, this.props.texts.continueButton)))));
          break;
        case "concluded":
          content = /*#__PURE__*/React.createElement("div", {
            className: "panel panel-default"
          }, /*#__PURE__*/React.createElement("div", {
            className: "panel-body"
          }, /*#__PURE__*/React.createElement("h3", {
            className: "text-center mb-15 text-success"
          }, this.props.texts.concludedTitle), /*#__PURE__*/React.createElement("p", {
            className: "lead text-center"
          }, this.props.texts.concludedExplanation), /*#__PURE__*/React.createElement("div", {
            className: "text-center mb-23"
          }, /*#__PURE__*/React.createElement("div", {
            className: "visible-xs-block"
          }, /*#__PURE__*/React.createElement("a", {
            href: this.props.resultsUrl,
            className: "btn btn-success btn-block"
          }, this.props.texts.resultsButton)), /*#__PURE__*/React.createElement("div", {
            className: "hidden-xs"
          }, /*#__PURE__*/React.createElement("a", {
            href: this.props.resultsUrl,
            className: "btn btn-success btn-lg"
          }, this.props.texts.resultsButton)))));
          break;
        default:
          content = /*#__PURE__*/React.createElement("img", {
            className: "bb-spinner",
            src: this.props.spinnerLogo
          });
          break;
      }
      var modal = null;
      if (this.state.isErrored) {
        modal = /*#__PURE__*/React.createElement(RefreshModal, {
          message: this.props.texts.error,
          refreshUrl: this.props.refreshUrl,
          cancelUrl: this.props.cancelRefreshUrl,
          refreshCaption: this.props.texts.refreshButton,
          cancelCaption: this.props.texts.cancelRefreshButton,
          error_msg: this.error_msg
        });
      } else if (this.state.confirmationFor !== undefined) {
        var isInverse = true;
        if (this.state.confirmationFor === "start") {
          isInverse = false;
        }
        modal = /*#__PURE__*/React.createElement(ConfirmModal, {
          title: this.props.texts.confirmModalTitle,
          yesCaption: this.props.texts.confirmModalYesCaption,
          noCaption: this.props.texts.confirmModalNoCaption,
          isInverse: isInverse,
          complete: this._completeModal.bind(this)
        });
      }
      return /*#__PURE__*/React.createElement(React.Fragment, null, modal, /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 bb-test-container"
      }, content)));
    }
  }, {
    key: "reportFailed",
    value: function reportFailed() {
      var error_msg = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : "";
      if (this.state.status !== "started") {
        return;
      }
      if (this._statusData.seconds > 1) {
        this._errorOut(error_msg);
      }
    }
  }, {
    key: "_errorOut",
    value: function _errorOut() {
      var error_msg = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : "";
      this._stop();
      this.error_msg = error_msg;
      this.setState({
        isErrored: true
      });
    }
  }, {
    key: "_stop",
    value: function _stop() {
      if (this._$xhr !== undefined) {
        this._$xhr.abort();
      }
      switch (this.state.status) {
        case "queued":
          break;
        case "started":
          this._statusData.testObject.stop();
          clearTimeout(this._statusData.timer);
          break;
        case "expired":
          break;
        case "concluded":
          break;
      }
      clearTimeout(this._lingerTimer);
    }
  }, {
    key: "_ajaxSuccess",
    value: function _ajaxSuccess(pageview, data, status, $xhr) {
      if (pageview) {
        ga_report_pageview();
      }
      if (!data.success) {
        this._errorOut(data.error_msg);
        return;
      }
      var msecs = new Date().getTime() - this._xhrStartTime;
      switch (data.status) {
        case "queued":
          this._statusData = {
            section: data.section,
            instructions: data.instructions
          };
          if (data.video) {
            this._statusData["video"] = data.video;
          }
          this._currentQuestionIndex = 0;
          break;
        case "started":
          var seconds = Math.max(data.seconds - Math.round(msecs / 1000), 0);
          if (seconds <= 1) {
            data.status = undefined;
            this._lingerTimer = setTimeout(function () {
              this._continue(true, false);
            }.bind(this), 2000);
          } else {
            this._statusData = {
              seconds: seconds,
              focused: true,
              testObject: new (eval(this.props.objectClass))(this, this.props.reportUrl, data.questions, data.report, data.texts),
              questionIndex: this._currentQuestionIndex,
              questionsCount: data.questions.length,
              timer: setTimeout(this._tick.bind(this), 1000),
              username: data.username,
              hasCalculator: data.has_calculator,
              hasPeriodicTable: data.has_periodic_table
            };
            if (data.section !== undefined) {
              this._statusData.section = data.section;
            }
          }
          if (data.reload) {
            // location.href = location.href;
            // console.log("reload", data)
            location.reload();
          }
          break;
        case "expired":
          break;
        case "concluded":
          break;
      }
      this.setState({
        status: data.status
      });
    }
  }, {
    key: "_ajaxError",
    value: function _ajaxError($xhr, status, error) {
      if (status === "abort") {
        return;
      }
      this._errorOut("_ajaxError($xhr, status, error)|".concat(error));
    }
  }, {
    key: "_tick",
    value: function _tick() {
      if (!this.props.hasTimer) {
        return;
      }
      this._statusData.seconds -= 1;
      if (this._statusData.seconds >= 0) {
        this._statusData.timer = setTimeout(this._tick.bind(this), 1000);
        this.setState(function (prevState) {
          return {
            toggleFlag: !prevState.toggleFlag
          };
        });
        return;
      }
      this._continue();
    }
  }, {
    key: "_request",
    value: function _request(idempotent, url, $xhrMethod, pageview) {
      if (idempotent && this.state.status === undefined) {
        return;
      }
      this._stop();
      this._xhrStartTime = new Date().getTime();
      var xhrData = {
        url: url,
        success: this._ajaxSuccess.bind(this, pageview),
        error: this._ajaxError.bind(this)
      };
      if ($xhrMethod === $.post) {
        xhrData.headers = {
          "X-CSRFToken": Cookies.get("csrftoken")
        };
      }
      this._$xhr = $xhrMethod(xhrData);
      this.setState({
        status: undefined
      });
    }
  }, {
    key: "_continue",
    value: function _continue() {
      var force = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : false;
      var pageview = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : true;
      this._request(!force, this.props.continueUrl, $.get, pageview);
    }
  }, {
    key: "_start",
    value: function _start() {
      this._request(true, this.props.startUrl, $.post, true);
    }
  }, {
    key: "_skip",
    value: function _skip() {
      this._request(true, this.props.skipUrl, $.post, true);
    }
  }, {
    key: "_end",
    value: function _end() {
      this._request(true, this.props.endUrl, $.post, true);
    }
  }, {
    key: "_setQuestionIndex",
    value: function _setQuestionIndex(index) {
      if (this.state.status !== "started") {
        return;
      }
      this._statusData.questionIndex = index;
      this.setState(function (prevState) {
        return {
          toggleFlag: !prevState.toggleFlag
        };
      });
      ga_report_pageview();
    }
  }, {
    key: "_paginationElements",
    value: function _paginationElements(width) {
      if (width < 1) {
        width = 1;
      } else if (width > this._statusData.questionsCount) {
        width = this._statusData.questionsCount;
      }
      var padding = parseInt((width - 1) / 2, 10);
      var rightPadding = (width - 1) % 2;
      var indexes = [this._statusData.questionIndex];
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
      } else if (indexes[indexes.length - 1] >= this._statusData.questionsCount) {
        while (true) {
          if (indexes[indexes.length - 1] < this._statusData.questionsCount) {
            break;
          }
          indexes.pop();
          indexes.unshift(indexes[0] - 1);
        }
      }
      var paginationElements = [];
      if (this._statusData.questionIndex > 0) {
        paginationElements.push( /*#__PURE__*/React.createElement("li", {
          key: "left"
        }, /*#__PURE__*/React.createElement("a", {
          href: "javascript:void(0);",
          onClick: this._setQuestionIndex.bind(this, this._statusData.questionIndex - 1)
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
        if (indexes[_i2] === this._statusData.questionIndex) {
          paginationElements.push( /*#__PURE__*/React.createElement("li", {
            key: indexes[_i2].toString(),
            className: "active"
          }, /*#__PURE__*/React.createElement("a", {
            href: "javascript:void(0);"
          }, indexes[_i2] + 1)));
        } else {
          var elementClassName = this._statusData.testObject.answer(indexes[_i2]) ? "bb-pagination-primary" : "";
          if (this._statusData.testObject.showCorrectAnswer()) {
            elementClassName = this._statusData.testObject.isCorrect(indexes[_i2]) ? "bb-pagination-success" : "bb-pagination-danger";
          }
          paginationElements.push( /*#__PURE__*/React.createElement("li", {
            key: indexes[_i2].toString()
          }, /*#__PURE__*/React.createElement("a", {
            href: "javascript:void(0);",
            onClick: this._setQuestionIndex.bind(this, indexes[_i2]),
            className: elementClassName
          }, indexes[_i2] + 1)));
        }
      }
      if (this._statusData.questionIndex < this._statusData.questionsCount - 1) {
        paginationElements.push( /*#__PURE__*/React.createElement("li", {
          key: "right"
        }, /*#__PURE__*/React.createElement("a", {
          href: "javascript:void(0);",
          onClick: this._setQuestionIndex.bind(this, this._statusData.questionIndex + 1)
        }, "\xBB")));
      } else {
        paginationElements.push( /*#__PURE__*/React.createElement("li", {
          key: "right",
          className: "disabled"
        }, /*#__PURE__*/React.createElement("a", {
          href: "javascript:void(0);"
        }, "\xBB")));
      }
      return paginationElements;
    }
  }, {
    key: "_completeModal",
    value: function _completeModal(data) {
      if (data) {
        switch (this.state.confirmationFor) {
          case "skip":
            this._skip();
            break;
          case "end":
            this._end();
            break;
          case "start":
            this._start();
            break;
        }
      }
      this.setState({
        confirmationFor: undefined
      });
    }
  }, {
    key: "_renderModal",
    value: function _renderModal(type) {
      if (this.state.confirmationFor !== undefined) {
        return;
      }
      this.setState({
        confirmationFor: type
      });
    }
  }, {
    key: "_windowBlur",
    value: function _windowBlur() {
      if (this.state.status !== "started") {
        return;
      }
      this._currentQuestionIndex = this._statusData.questionIndex;
      this._statusData.focused = false;
    }
  }, {
    key: "_windowFocus",
    value: function _windowFocus() {
      if (this.state.status !== "started") {
        return;
      }
      this._continue();
    }
  }]);
}(React.Component);