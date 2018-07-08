"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var NewTest = function (_React$Component) {
    _inherits(NewTest, _React$Component);

    function NewTest(props) {
        _classCallCheck(this, NewTest);

        var _this = _possibleConstructorReturn(this, (NewTest.__proto__ || Object.getPrototypeOf(NewTest)).call(this, props));

        _this.state = {
            isErrored: false,
            status: undefined,
            toggleFlag: true
        };
        _this._xhrStartTime;
        _this._$xhr;
        _this._statusData;
        return _this;
    }

    _createClass(NewTest, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            this._continue(true);
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            this._stop();
        }
    }, {
        key: "render",
        value: function render() {
            var content = null;
            switch (this.state.status) {
                case "queued":
                    content = React.createElement(
                        "div",
                        { className: "panel panel-default" },
                        React.createElement(
                            "div",
                            { className: "panel-body" },
                            React.createElement(
                                "h3",
                                { className: "text-center mb-15" },
                                this._statusData.section
                            ),
                            React.createElement(
                                "p",
                                { className: "lead" },
                                this._statusData.instructions
                            ),
                            React.createElement(
                                "div",
                                { className: "text-center" },
                                React.createElement(
                                    "button",
                                    { type: "button",
                                        className: "btn btn-primary btn-lg mb-23",
                                        onClick: this._continue.bind(this) },
                                    this.props.texts.startButton
                                )
                            )
                        )
                    );
                    break;
                case "started":
                    var bottomPaginationLeft = null;
                    var bottomPaginationRight = null;
                    if (this._statusData.questionIndex > 0) {
                        bottomPaginationLeft = React.createElement(
                            "li",
                            { className: "previous" },
                            React.createElement(
                                "a",
                                { href: "javascript:void(0);",
                                    onClick: this._setQuestionIndex.bind(this, this._statusData.questionIndex - 1) },
                                "\u2190 ",
                                this.props.texts.previousPager
                            )
                        );
                    } else {
                        bottomPaginationLeft = React.createElement(
                            "li",
                            { className: "previous disabled" },
                            React.createElement(
                                "a",
                                { href: "javascript:void(0);" },
                                "\u2190 ",
                                this.props.texts.previousPager
                            )
                        );
                    }
                    if (this._statusData.questionIndex < this._statusData.questionsCount - 1) {
                        bottomPaginationRight = React.createElement(
                            "li",
                            { className: "next" },
                            React.createElement(
                                "a",
                                { href: "javascript:void(0);",
                                    onClick: this._setQuestionIndex.bind(this, this._statusData.questionIndex + 1) },
                                this.props.texts.nextPager,
                                " \u2192"
                            )
                        );
                    } else {
                        bottomPaginationRight = React.createElement(
                            "li",
                            { className: "next disabled" },
                            React.createElement(
                                "a",
                                { href: "javascript:void(0);" },
                                this.props.texts.nextPager,
                                " \u2192"
                            )
                        );
                    }

                    content = React.createElement(
                        React.Fragment,
                        null,
                        React.createElement(
                            "div",
                            { className: "row" },
                            React.createElement(
                                "div",
                                { className: "col-xs-12 text-center hidden-xs" },
                                React.createElement(
                                    "ul",
                                    { className: "pagination mt-0 mb-0" },
                                    this._paginationElements(13)
                                )
                            ),
                            React.createElement(
                                "div",
                                { className: "col-xs-12 text-center visible-xs-block" },
                                React.createElement(
                                    "ul",
                                    { className: "pagination pagination-sm mt-0 mb-0" },
                                    this._paginationElements(6)
                                )
                            )
                        ),
                        React.createElement(Question, { count: this._statusData.questionIndex + 1,
                            object: this._statusData.testObject.question(this._statusData.questionIndex),
                            answerData: this._statusData.testObject.answer(this._statusData.questionIndex),
                            onAnswerUpdate: this._statusData.testObject.updateAnswer.bind(this._statusData.testObject, this._statusData.questionIndex),
                            secondsLeft: this._statusData.seconds,
                            texts: this.props.texts }),
                        React.createElement(
                            "div",
                            { className: "row" },
                            React.createElement(
                                "div",
                                { className: "col-xs-12" },
                                React.createElement(
                                    "ul",
                                    { className: "pager mt-0 mb-0" },
                                    bottomPaginationLeft,
                                    bottomPaginationRight
                                )
                            )
                        )
                    );
                    break;
                case "expired":
                    // DARK_TODO  implement this!
                    break;
                case "concluded":
                // DARK_TODO  implement this!
                default:
                    content = React.createElement("img", { className: "bb-spinner", src: this.props.spinnerLogo });
                    break;
            }

            var modal = null;
            if (this.state.isErrored) {
                modal = React.createElement(RefreshModal, { message: this.props.texts.error,
                    refreshUrl: this.props.refreshUrl,
                    cancelUrl: this.props.cancelRefreshUrl,
                    refreshCaption: this.props.texts.refreshButton,
                    cancelCaption: this.props.texts.cancelRefreshButton });
            }

            return React.createElement(
                React.Fragment,
                null,
                modal,
                React.createElement(
                    "div",
                    { className: "row" },
                    React.createElement(
                        "div",
                        { className: "col-xs-12 bb-test-container" },
                        content
                    )
                )
            );
        }
    }, {
        key: "reportFailed",
        value: function reportFailed() {
            if (this.state.status !== "started") {
                return;
            }
            if (this._statusData.seconds > 1) {
                this._errorOut();
            }
        }
    }, {
        key: "_errorOut",
        value: function _errorOut() {
            this._stop();
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
        }
    }, {
        key: "_ajaxSuccess",
        value: function _ajaxSuccess(data, status, $xhr) {
            if (!data.success) {
                this._errorOut();
                return;
            }
            var msecs = new Date().getTime() - this._xhrStartTime;
            this.setState({
                status: data.status
            });
            switch (data.status) {
                case "queued":
                    this._statusData = {
                        section: data.section,
                        instructions: data.instructions
                    };
                    break;
                case "started":
                    this._statusData = {
                        seconds: Math.max(data.seconds - Math.round(msecs / 1000), 0),
                        testObject: new (eval(this.props.objectClass))(this, data.questions, data.report),
                        questionIndex: 0,
                        questionsCount: data.questions.length,
                        timer: setTimeout(this._tick.bind(this), 1000)
                    };
                    break;
                case "expired":
                    break;
                case "concluded":
                    break;
            }
        }
    }, {
        key: "_ajaxError",
        value: function _ajaxError($xhr, status, error) {
            if (status === "abort") {
                return;
            }
            this._errorOut();
        }
    }, {
        key: "_tick",
        value: function _tick() {
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
            this._end();
        }
    }, {
        key: "_request",
        value: function _request(idempotent, url, $xhrMethod) {
            if (idempotent && this.state.status === undefined) {
                return;
            }
            this._stop();
            this._xhrStartTime = new Date().getTime();
            var xhrData = {
                url: url,
                success: this._ajaxSuccess.bind(this),
                error: this._ajaxError.bind(this)
            };
            if ($xhrMethod === $.post) {
                xhrData.headers = { "X-CSRFToken": Cookies.get("csrftoken") };
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

            this._request(!force, this.props.continueUrl, $.get);
        }
    }, {
        key: "_start",
        value: function _start() {
            this._request(true, this.props.startUrl, $.post);
        }
    }, {
        key: "_skip",
        value: function _skip() {
            this._request(true, this.props.skipUrl, $.post);
        }
    }, {
        key: "_end",
        value: function _end() {
            this._request(true, this.props.endUrl, $.post);
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
                paginationElements.push(React.createElement(
                    "li",
                    { key: "left" },
                    React.createElement(
                        "a",
                        { href: "javascript:void(0);",
                            onClick: this._setQuestionIndex.bind(this, this._statusData.questionIndex - 1) },
                        "\xAB"
                    )
                ));
            } else {
                paginationElements.push(React.createElement(
                    "li",
                    { key: "left", className: "disabled" },
                    React.createElement(
                        "a",
                        { href: "javascript:void(0);" },
                        "\xAB"
                    )
                ));
            }
            for (var _i2 = 0; _i2 < indexes.length; _i2++) {
                if (indexes[_i2] === this._statusData.questionIndex) {
                    paginationElements.push(React.createElement(
                        "li",
                        { key: indexes[_i2].toString(), className: "active" },
                        React.createElement(
                            "a",
                            { href: "javascript:void(0);" },
                            indexes[_i2] + 1
                        )
                    ));
                } else {
                    paginationElements.push(React.createElement(
                        "li",
                        { key: indexes[_i2].toString() },
                        React.createElement(
                            "a",
                            { href: "javascript:void(0);",
                                onClick: this._setQuestionIndex.bind(this, indexes[_i2]),
                                className: this._statusData.testObject.answer(indexes[_i2]) ? "bb-pagination-success" : "" },
                            indexes[_i2] + 1
                        )
                    ));
                }
            }
            if (this._statusData.questionIndex < this._statusData.questionsCount - 1) {
                paginationElements.push(React.createElement(
                    "li",
                    { key: "right" },
                    React.createElement(
                        "a",
                        { href: "javascript:void(0);",
                            onClick: this._setQuestionIndex.bind(this, this._statusData.questionIndex + 1) },
                        "\xBB"
                    )
                ));
            } else {
                paginationElements.push(React.createElement(
                    "li",
                    { key: "right", className: "disabled" },
                    React.createElement(
                        "a",
                        { href: "javascript:void(0);" },
                        "\xBB"
                    )
                ));
            }
            return paginationElements;
        }
    }]);

    return NewTest;
}(React.Component);