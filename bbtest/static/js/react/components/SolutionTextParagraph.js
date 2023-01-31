"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var SolutionTextParagraph = function (_React$Component) {
    _inherits(SolutionTextParagraph, _React$Component);

    function SolutionTextParagraph(props) {
        _classCallCheck(this, SolutionTextParagraph);

        var _this = _possibleConstructorReturn(this, (SolutionTextParagraph.__proto__ || Object.getPrototypeOf(SolutionTextParagraph)).call(this, props));

        _this.state = {
            originalText: "",
            rawHtml: ""
        };
        _this._processor;
        return _this;
    }

    _createClass(SolutionTextParagraph, [{
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
            var content = null;
            var className = "bb-test-paragraph";
            var sharedAddon = null;

            // let youtube_links = text.match(/^(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=([a-zA-Z0-9_]+)|youtu\.be\/([a-zA-Z\d_]+))(?:&.*)?$/gm)

            var regexp = /(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=([a-zA-Z0-9_]+)|youtu\.be\/([a-zA-Z\d_]+))(?:&.*)?/gm;

            if (this.props.isShared) {
                className += " bb-test-paragraph-shared";
                sharedAddon = React.createElement(
                    "h5",
                    { className: "text-center mt-0 mb-5" },
                    React.createElement(
                        "em",
                        null,
                        this.props.testTexts.shared_paragraph_header
                    )
                );
            }

            if (!this.props.data.text) {
                var _content = null;
                if (this.props.forDevelopers) {
                    className += " bb-placeholder";
                    _content = this.props.texts.paragraphEmptyPlaceholder;
                }
                content = React.createElement(
                    React.Fragment,
                    null,
                    sharedAddon,
                    React.createElement(
                        "div",
                        { className: className },
                        _content
                    )
                );
            } else if (this.props.data.has_formulas) {
                var youtube = [];
                var matches = this.props.data.text.matchAll(regexp);
                var _iteratorNormalCompletion = true;
                var _didIteratorError = false;
                var _iteratorError = undefined;

                try {
                    for (var _iterator = matches[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
                        var match = _step.value;

                        console.log(match);
                        // this.props.data.text = this.props.data.text.replace(match[0], "");
                        this.state.rawHtml = this.state.rawHtml.replace(match[0], "");
                        youtube.push(React.createElement(
                            "div",
                            { className: "embed-responsive embed-responsive-16by9", key: "you" + match.index },
                            React.createElement("iframe", { src: "https://www.youtube.com/embed/" + match[1], frameBorder: "0", allow: "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; allowfullscreen" })
                        ));
                    }
                    // console.log(this.state.rawHtml);
                } catch (err) {
                    _didIteratorError = true;
                    _iteratorError = err;
                } finally {
                    try {
                        if (!_iteratorNormalCompletion && _iterator.return) {
                            _iterator.return();
                        }
                    } finally {
                        if (_didIteratorError) {
                            throw _iteratorError;
                        }
                    }
                }

                content = React.createElement(
                    React.Fragment,
                    null,
                    sharedAddon,
                    React.createElement("div", { className: className,
                        dangerouslySetInnerHTML: { __html: this.state.rawHtml } }),
                    youtube.length > 0 && youtube
                );
            } else {
                content = React.createElement(
                    React.Fragment,
                    null,
                    sharedAddon,
                    React.createElement(
                        "div",
                        { className: className },
                        SimpleFormattedFragment(this.props.data.text)
                    )
                );
            }

            return content;
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
    }]);

    return SolutionTextParagraph;
}(React.Component);