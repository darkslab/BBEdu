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
            questionIndex: 0
        };
        _this._questionData = null;
        _this._questionAttributes = null;
        _this._$xhrs = [];
        return _this;
    }

    _createClass(DeveloperTest, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            var questionNumber = 1;
            if (location.hash) {
                questionNumber = parseInt(location.hash.substr(1), 10);
                if (isNaN(questionNumber) || questionNumber < 1 || questionNumber > this.props.questionCount) {
                    questionNumber = 1;
                }
                this.setState({
                    questionIndex: questionNumber - 1
                });
                location.hash = questionNumber + "";
            }

            this._$xhrs.push($.get({
                url: this.props.indexedQuestionUrl + (questionNumber - 1) + "/",
                success: this._ajaxSuccess.bind(this, "question"),
                error: this._ajaxError.bind(this, "question")
            }));
            this._$xhrs.push($.get({
                url: this.props.attributesUrl,
                success: this._ajaxSuccess.bind(this, "attributes"),
                error: this._ajaxError.bind(this, "attributes")
            }));
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            var $xhr = void 0;
            while ($xhr = this._$xhrs.shift()) {
                $xhr.abort();
            }
        }
    }, {
        key: "render",
        value: function render() {
            var content = null;
            if (!this.state.isTestLoading && !this.state.isQuestionLoading) {
                content = React.createElement(DeveloperQuestion, { id: this._questionData.id,
                    data: this._questionData.data,
                    paragraphs: this._questionData.paragraphs,
                    attributes: this._questionAttributes });
            } else {
                content = React.createElement(
                    "div",
                    { className: "col-xs-12 bb-developer-container" },
                    React.createElement("img", { className: "bb-spinner", src: this.props.spinnerLogo })
                );
            }

            var pagination = null;
            if (!this.state.isTestLoading) {
                var width = 5;
                if (width < 1) {
                    width = 1;
                } else if (width > this.props.questionCount) {
                    width = this.props.questionCount;
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
                } else if (indexes[indexes.length - 1] >= this.props.questionCount) {
                    while (true) {
                        if (indexes[indexes.length - 1] < this.props.questionCount) {
                            break;
                        }
                        indexes.pop();
                        indexes.unshift(indexes[0] - 1);
                    }
                }

                var paginationElements = [];
                paginationElements.push(React.createElement(
                    "li",
                    { key: 'left', className: !indexes[0] ? 'disabled' : '' },
                    React.createElement(
                        "a",
                        { href: "javascript:void(0);" },
                        "\xAB"
                    )
                ));
                for (var _i2 = 0; _i2 < indexes.length; _i2++) {
                    paginationElements.push(React.createElement(
                        "li",
                        { key: indexes[_i2].toString(), className: indexes[_i2] === this.state.questionIndex ? 'active' : '' },
                        React.createElement(
                            "a",
                            { href: "javascript:void(0);" },
                            indexes[_i2] + 1
                        )
                    ));
                }
                paginationElements.push(React.createElement(
                    "li",
                    { key: 'right', className: indexes[indexes.length - 1] === this.props.questionCount - 1 ? 'disabled' : '' },
                    React.createElement(
                        "a",
                        { href: "javascript:void(0);" },
                        "\xBB"
                    )
                ));
                pagination = React.createElement(
                    "div",
                    { className: "col-xs-12 text-right" },
                    React.createElement(
                        "ul",
                        { className: "pagination mt-5 mb-5" },
                        paginationElements
                    )
                );
            }

            return React.createElement(
                "div",
                { className: "row" },
                pagination,
                content
            );
        }
    }, {
        key: "_ajaxSuccess",
        value: function _ajaxSuccess(type, data, status, $xhr) {
            if (type === "question") {
                this._questionData = data;
                this.setState({
                    isQuestionLoading: false
                });
            } else if (type === "attributes") {
                this._questionAttributes = data;
            }
            if (this._questionData && this._questionAttributes) {
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
            // DARK_TODO  probably say that something is wrong and ask to reload the page?
        }
    }]);

    return DeveloperTest;
}(React.Component);