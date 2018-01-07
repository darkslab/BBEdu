"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var TextParagraph = function (_React$Component) {
    _inherits(TextParagraph, _React$Component);

    function TextParagraph(props) {
        _classCallCheck(this, TextParagraph);

        var _this = _possibleConstructorReturn(this, (TextParagraph.__proto__ || Object.getPrototypeOf(TextParagraph)).call(this, props));

        _this.state = {
            rawHtml: ""
        };
        _this._processor;
        return _this;
    }

    _createClass(TextParagraph, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            // if (!this.props.data.hasFormulas) {
            if (false) {
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
            if (this._processor) {
                return;
            }
            this._setupProcessor();
        }
    }, {
        key: "render",
        value: function render() {
            var className = "bb-test-paragraph";
            // if (!this.props.data.hasFormulas) {
            if (false) {
                var content = null;
                if (this.props.data.text) {
                    content = SimpleFormattedFragment(this.props.data.text);
                } else if (this.props.optionalTexts) {
                    className += " bb-placeholder";
                    content = this.props.optionalTexts.paragraphEmptyPlaceholder;
                }
                return React.createElement(
                    "div",
                    { className: className },
                    content
                );
            }

            return React.createElement("div", { className: className,
                dangerouslySetInnerHTML: { __html: this.state.rawHtml } });
        }
    }, {
        key: "_setupProcessor",
        value: function _setupProcessor() {
            this._processor = new MathJaxAsyncProcessor(this._doneProcessing.bind(this), this.props.data.text);
        }
    }, {
        key: "_doneProcessing",
        value: function _doneProcessing(rawHtml, originalText) {
            this.setState({
                rawHtml: rawHtml
            });
            this._processor = undefined;
            if (originalText !== this.props.data.text) {
                this._setupProcessor();
            }
        }
    }]);

    return TextParagraph;
}(React.Component);