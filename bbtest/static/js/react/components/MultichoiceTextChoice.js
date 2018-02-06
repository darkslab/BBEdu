"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var MultichoiceTextChoice = function (_React$Component) {
    _inherits(MultichoiceTextChoice, _React$Component);

    function MultichoiceTextChoice(props) {
        _classCallCheck(this, MultichoiceTextChoice);

        var _this = _possibleConstructorReturn(this, (MultichoiceTextChoice.__proto__ || Object.getPrototypeOf(MultichoiceTextChoice)).call(this, props));

        _this.state = {
            originalText: "",
            rawHtml: ""
        };
        _this._processor;
        return _this;
    }

    _createClass(MultichoiceTextChoice, [{
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
            var choiceClassName = "bb-test-answer-choice";
            if (this.props.chosen) {
                choiceClassName += " bb-test-answer-choice-selected";
            }

            var content = null;
            var contentClassName = "bb-test-answer";

            if (!this.props.data.text) {
                var _content = null;
                if (this.props.optionalTexts) {
                    contentClassName += " bb-placeholder";
                    _content = this.props.optionalTexts.paragraphEmptyPlaceholder;
                }
                content = React.createElement(
                    "div",
                    { className: contentClassName },
                    _content
                );
            } else if (this.props.data.has_formulas) {
                content = React.createElement("div", { className: contentClassName,
                    dangerouslySetInnerHTML: { __html: this.state.rawHtml } });
            } else {
                content = React.createElement(
                    "div",
                    { className: contentClassName },
                    SimpleFormattedFragment(this.props.data.text)
                );
            }

            return React.createElement(
                "div",
                { className: "row" },
                React.createElement(
                    "div",
                    { className: "col-xs-2 col-sm-3 pr-0" },
                    React.createElement(
                        "div",
                        { className: "bb-rel bb-test-answer" },
                        React.createElement(
                            "div",
                            { className: choiceClassName,
                                onClick: this._handleClick.bind(this) },
                            this.props.label
                        )
                    )
                ),
                React.createElement(
                    "div",
                    { className: "col-xs-10 col-sm-7 pl-0" },
                    content
                )
            );
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
    }, {
        key: "_handleClick",
        value: function _handleClick() {
            if (this.props.onChoose) {
                this.props.onChoose();
            }
        }
    }]);

    return MultichoiceTextChoice;
}(React.Component);