"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperTest = function (_React$Component) {
    _inherits(DeveloperTest, _React$Component);

    function DeveloperTest(props) {
        _classCallCheck(this, DeveloperTest);

        var _this = _possibleConstructorReturn(this, (DeveloperTest.__proto__ || Object.getPrototypeOf(DeveloperTest)).call(this, props));

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

        _this._boundConfirmIsSaved = _this._confirmIsSaved.bind(_this);
        _this._boundConfirmIsSavedTurbolinks = _this._confirmIsSavedTurbolinks.bind(_this);
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

            this._getQuestionData(questionNumber - 1);
            this._$xhrs["attributes"] = $.get({
                url: this.props.attributesUrl,
                success: this._ajaxSuccess.bind(this, "attributes"),
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
                content = React.createElement(
                    "h4",
                    { className: "text-center text-danger mt-100 mb-0" },
                    this.props.texts.error
                );
            } else if (!this.state.isTestLoading && !this.state.isQuestionLoading && !this.state.isQuestionSaving) {
                content = React.createElement(DeveloperQuestion, { count: this.state.questionIndex + 1,
                    attributes: this._questionAttributes,
                    object: this._questionObject,
                    ability: this._abilityObject,
                    texts: this.props.texts,
                    errorOut: this._errorOut.bind(this) });
            } else {
                content = React.createElement("img", { className: "bb-spinner", src: this.props.spinnerLogo });
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
                    paginationElements.push(React.createElement(
                        "li",
                        { key: "left" },
                        React.createElement(
                            "a",
                            { href: "javascript:void(0);",
                                onClick: this._nextQuestion.bind(this, this.state.questionIndex - 1) },
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
                                    onClick: this._nextQuestion.bind(this, indexes[_i2]) },
                                indexes[_i2] + 1
                            )
                        ));
                    }
                }
                if (this.state.questionIndex < this.props.questionIds.length - 1) {
                    paginationElements.push(React.createElement(
                        "li",
                        { key: "right" },
                        React.createElement(
                            "a",
                            { href: "javascript:void(0);",
                                onClick: this._nextQuestion.bind(this, this.state.questionIndex + 1) },
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
                pagination = React.createElement(
                    "div",
                    { className: "col-xs-12 col-sm-6 text-center" },
                    React.createElement(
                        "ul",
                        { className: "pagination pagination-sm mt-0 mb-0" },
                        paginationElements
                    )
                );
            }

            return React.createElement(
                "div",
                { className: "row" },
                React.createElement(
                    "div",
                    { className: "col-xs-12 col-sm-6" },
                    React.createElement(
                        "button",
                        { type: "button",
                            disabled: this.state.isQuestionSaving,
                            className: "btn btn-success mr-5 mb-5",
                            onClick: this._saveAndExit.bind(this, this.props.dashboardUrl) },
                        this.props.texts.saveAndExitButton
                    ),
                    React.createElement(
                        "button",
                        { type: "button",
                            disabled: this.state.isQuestionSaving,
                            className: "btn btn-success mr-5 mb-5",
                            onClick: this._saveAndExit.bind(this, this.props.previewUrl) },
                        this.props.texts.saveAndPreviewButton
                    )
                ),
                pagination,
                React.createElement(
                    "div",
                    { className: "col-xs-12 bb-test-container" },
                    content
                )
            );
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
            this._getQuestionData(index);
        }
    }, {
        key: "_ajaxSuccess",
        value: function _ajaxSuccess(type, data, status, $xhr) {
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
            var object = void 0;
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
        value: function _getQuestionData(index) {
            this.setState({
                questionIndex: index
            });
            history.replaceState(history.state, "", location.pathname + "#" + (index + 1).toString());

            if (this._$xhrs["question"]) {
                this._$xhrs["question"].abort();
            }
            this._$xhrs["question"] = $.get({
                url: this.props.questionUrl + this.props.questionIds[index] + "/",
                success: this._ajaxSuccess.bind(this, "question"),
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