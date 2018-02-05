"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Test = function (_React$Component) {
    _inherits(Test, _React$Component);

    function Test(props) {
        _classCallCheck(this, Test);

        var _this = _possibleConstructorReturn(this, (Test.__proto__ || Object.getPrototypeOf(Test)).call(this, props));

        _this.state = {
            isTestLoading: true,
            isCompleting: false,
            isErrored: false,
            isTimedOut: false,
            questionIndex: 0,
            secondsLeft: undefined,
            toggleFlag: true
        };
        _this._testObject;
        _this._$xhr;
        _this._timer;
        return _this;
    }

    _createClass(Test, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            var questionNumber = 1;
            if (location.hash) {
                questionNumber = parseInt(location.hash.substr(1), 10);
                if (isNaN(questionNumber) || questionNumber < 1 || questionNumber > this.props.questionsCount) {
                    questionNumber = 1;
                }
            }
            this._setQuestionIndex(questionNumber - 1);

            this._$xhr = $.get({
                url: this.props.testUrl,
                success: this._ajaxSuccess.bind(this),
                error: this._ajaxError.bind(this)
            });
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            this._cleanUp();
        }
    }, {
        key: "render",
        value: function render() {
            var content = null;
            if (this.state.isErrored) {
                content = React.createElement(
                    "h4",
                    { className: "text-center text-danger mt-100 mb-0" },
                    this.props.texts.error
                );
            } else if (this.state.isTestLoading || this.state.isCompleting) {
                content = React.createElement("img", { className: "bb-spinner", src: this.props.spinnerLogo });
            } else if (this.state.isTimedOut) {
                content = React.createElement(
                    "h4",
                    { className: "text-center mt-100 mb-0" },
                    "Time is up!"
                );
            } else {
                content = React.createElement(Question, { count: this.state.questionIndex + 1,
                    object: this._testObject.question(this.state.questionIndex),
                    answerData: this._testObject.answerData(this.state.questionIndex),
                    onAnswerUpdate: this._testObject.answerUpdate.bind(this._testObject, this.state.questionIndex),
                    secondsLeft: this.state.secondsLeft,
                    texts: this.props.texts });
            }

            var pagination = null;
            var bottomPagination = null;
            if (this.props.questionsCount > 1 && !this.state.isErrored && !this.state.isTestLoading && !this.state.isCompleting && !this.state.isTimedOut) {
                pagination = React.createElement(
                    React.Fragment,
                    null,
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
                );

                var bottomPaginationLeft = null;
                var bottomPaginationRight = null;
                if (this.state.questionIndex > 0) {
                    bottomPaginationLeft = React.createElement(
                        "li",
                        { className: "previous" },
                        React.createElement(
                            "a",
                            { href: "javascript:void(0);",
                                onClick: this._setQuestionIndex.bind(this, this.state.questionIndex - 1) },
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
                if (this.state.questionIndex < this.props.questionsCount - 1) {
                    bottomPaginationRight = React.createElement(
                        "li",
                        { className: "next" },
                        React.createElement(
                            "a",
                            { href: "javascript:void(0);",
                                onClick: this._setQuestionIndex.bind(this, this.state.questionIndex + 1) },
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
                bottomPagination = React.createElement(
                    "ul",
                    { className: "pager mt-0 mb-0" },
                    bottomPaginationLeft,
                    bottomPaginationRight
                );
            }

            return React.createElement(
                "div",
                { className: "row" },
                pagination,
                React.createElement(
                    "div",
                    { className: "col-xs-12 bb-test-container" },
                    content
                ),
                React.createElement(
                    "div",
                    { className: "col-xs-12" },
                    bottomPagination
                )
            );
        }
    }, {
        key: "_ajaxSuccess",
        value: function _ajaxSuccess(data, status, $xhr) {
            this._testObject = new (eval(this.props.objectClass))(this, data.questions, data.answer_submission);
            this.setState({
                isTestLoading: false,
                secondsLeft: data.seconds_left
            });
            this._timer = setTimeout(this._tick.bind(this), 1000);
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
        key: "_errorOut",
        value: function _errorOut() {
            this.setState({
                isErrored: true
            });
            this._cleanUp();
        }
    }, {
        key: "_cleanUp",
        value: function _cleanUp() {
            this._$xhr.abort();
            clearTimeout(this._timer);
        }
    }, {
        key: "_tick",
        value: function _tick() {
            var secondsLeft = this.state.secondsLeft - 1;
            if (secondsLeft >= 0) {
                this._timer = setTimeout(this._tick.bind(this), 1000);
                this.setState({
                    secondsLeft: secondsLeft
                });
                return;
            }
            this._testObject.push(this._completed.bind(this));
            this.setState({
                isCompleting: true,
                isTimedOut: true
            });
        }
    }, {
        key: "_completed",
        value: function _completed(success) {
            if (!success) {
                this._errorOut();
                return;
            }
            this.setState({
                isCompleting: false
            });
        }
    }, {
        key: "_setQuestionIndex",
        value: function _setQuestionIndex(index) {
            this.setState({
                questionIndex: index
            });
            history.replaceState(history.state, "", location.pathname + "#" + (index + 1).toString());
        }
    }, {
        key: "_paginationElements",
        value: function _paginationElements(width) {
            if (width < 1) {
                width = 1;
            } else if (width > this.props.questionsCount) {
                width = this.props.questionsCount;
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
            } else if (indexes[indexes.length - 1] >= this.props.questionsCount) {
                while (true) {
                    if (indexes[indexes.length - 1] < this.props.questionsCount) {
                        break;
                    }
                    indexes.pop();
                    indexes.unshift(indexes[0] - 1);
                }
            }

            var paginationElements = [];
            if (this.state.questionIndex > 0) {
                paginationElements.push(React.createElement(
                    "li",
                    { key: "left" },
                    React.createElement(
                        "a",
                        { href: "javascript:void(0);",
                            onClick: this._setQuestionIndex.bind(this, this.state.questionIndex - 1) },
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
                if (indexes[_i2] === this.state.questionIndex) {
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
                                className: this._testObject.answerData(indexes[_i2]) ? "bb-pagination-success" : "" },
                            indexes[_i2] + 1
                        )
                    ));
                }
            }
            if (this.state.questionIndex < this.props.questionsCount - 1) {
                paginationElements.push(React.createElement(
                    "li",
                    { key: "right" },
                    React.createElement(
                        "a",
                        { href: "javascript:void(0);",
                            onClick: this._setQuestionIndex.bind(this, this.state.questionIndex + 1) },
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

    return Test;
}(React.Component);