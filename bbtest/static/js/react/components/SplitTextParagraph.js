"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var SplitTextParagraph = function (_React$Component) {
    _inherits(SplitTextParagraph, _React$Component);

    function SplitTextParagraph(props) {
        _classCallCheck(this, SplitTextParagraph);

        var _this = _possibleConstructorReturn(this, (SplitTextParagraph.__proto__ || Object.getPrototypeOf(SplitTextParagraph)).call(this, props));

        _this.state = {
            toggleFlag: true
        };
        _this._left = {
            originalText: "",
            rawHtml: "",
            processor: undefined
        };
        _this._right = {
            originalText: "",
            rawHtml: "",
            processor: undefined
        };
        return _this;
    }

    _createClass(SplitTextParagraph, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            if (!this.props.data.has_formulas) {
                return;
            }
            this._setupProcessors();
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            if (this._left.processor) {
                this._left.processor.stop();
            }
            if (this._right.processor) {
                this._right.processor.stop();
            }
        }
    }, {
        key: "componentDidUpdate",
        value: function componentDidUpdate() {
            if (this._left.processor || this._right.processor || !this.props.data.has_formulas) {
                return;
            }
            if (this.props.data.left.text !== this._left.originalText || this.props.data.right.text !== this._right.originalText) {
                this._setupProcessors();
            }
        }
    }, {
        key: "render",
        value: function render() {
            var leftContent = null;
            var rightContent = null;

            var leftClassName = "bb-test-paragraph";
            if (!this.props.data.left.text) {
                var content = null;
                if (this.props.forDevelopers) {
                    leftClassName += " bb-placeholder";
                    content = this.props.texts.paragraphEmptyPlaceholder;
                }
                leftContent = React.createElement(
                    "div",
                    { className: leftClassName },
                    content
                );
            } else if (this.props.data.has_formulas) {
                leftContent = React.createElement("div", { className: leftClassName,
                    dangerouslySetInnerHTML: { __html: this._left.rawHtml } });
            } else {
                leftContent = React.createElement(
                    "div",
                    { className: leftClassName },
                    SimpleFormattedFragment(this.props.data.left.text)
                );
            }

            var rightClassName = "bb-test-paragraph";
            if (!this.props.data.right.text) {
                var _content = null;
                if (this.props.forDevelopers) {
                    rightClassName += " bb-placeholder";
                    _content = this.props.texts.paragraphEmptyPlaceholder;
                }
                rightContent = React.createElement(
                    "div",
                    { className: rightClassName },
                    _content
                );
            } else if (this.props.data.has_formulas) {
                rightContent = React.createElement("div", { className: rightClassName,
                    dangerouslySetInnerHTML: { __html: this._right.rawHtml } });
            } else {
                rightContent = React.createElement(
                    "div",
                    { className: rightClassName },
                    SimpleFormattedFragment(this.props.data.right.text)
                );
            }

            return React.createElement(
                "div",
                { className: "row" },
                React.createElement(
                    "div",
                    { className: "col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2" },
                    React.createElement(
                        "div",
                        { className: "row" },
                        React.createElement(
                            "div",
                            { className: "col-xs-6 pr-5" },
                            React.createElement(
                                "h5",
                                { className: "text-center mt-0 mb-0" },
                                React.createElement(
                                    "em",
                                    null,
                                    this.props.texts.columnACaption
                                )
                            ),
                            leftContent
                        ),
                        React.createElement(
                            "div",
                            { className: "col-xs-6 pl-5" },
                            React.createElement(
                                "h5",
                                { className: "text-center mt-0 mb-0" },
                                React.createElement(
                                    "em",
                                    null,
                                    this.props.texts.columnBCaption
                                )
                            ),
                            rightContent
                        )
                    )
                )
            );
        }
    }, {
        key: "_setupProcessors",
        value: function _setupProcessors() {
            this._left.processor = new KatexAsyncProcessor(this._doneProcessing.bind(this, "left"), this.props.data.left.text);
            this._right.processor = new KatexAsyncProcessor(this._doneProcessing.bind(this, "right"), this.props.data.right.text);
        }
    }, {
        key: "_doneProcessing",
        value: function _doneProcessing(type, rawHtml, originalText) {
            switch (type) {
                case "left":
                    this._left.originalText = originalText;
                    this._left.rawHtml = rawHtml;
                    this._left.processor = undefined;
                    break;
                case "right":
                    this._right.originalText = originalText;
                    this._right.rawHtml = rawHtml;
                    this._right.processor = undefined;
                    break;
            }
            if (!this._left.processor && !this._right.processor) {
                this.setState(function (prevState) {
                    return {
                        toggleFlag: !prevState.toggleFlag
                    };
                });
            }
        }
    }]);

    return SplitTextParagraph;
}(React.Component);