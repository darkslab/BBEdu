"use strict";

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperSplitTextParagraph = function (_React$Component) {
    _inherits(DeveloperSplitTextParagraph, _React$Component);

    function DeveloperSplitTextParagraph(props) {
        _classCallCheck(this, DeveloperSplitTextParagraph);

        return _possibleConstructorReturn(this, (DeveloperSplitTextParagraph.__proto__ || Object.getPrototypeOf(DeveloperSplitTextParagraph)).call(this, props));
    }

    _createClass(DeveloperSplitTextParagraph, [{
        key: "render",
        value: function render() {
            var buttons = [];
            buttons.push(React.createElement(
                "button",
                { key: 'delete',
                    type: "button",
                    className: "btn btn-danger btn-xs pull-right ml-5",
                    onClick: this.props.onDelete },
                this.props.texts.deleteParagraphButton
            ));

            var leftClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
            if (!this.props.data.left_text) {
                leftClassName += " bb-test-paragraph-textarea-empty";
            }
            var rightClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
            if (!this.props.data.right_text) {
                rightClassName += " bb-test-paragraph-textarea-empty";
            }

            return React.createElement(
                "div",
                { className: "form-group bb-test-section-movable bb-test-section-background", "data-paragraph-id": this.props.paragraphId },
                React.createElement(
                    "div",
                    { className: "pt-5 pr-5 pb-5 pl-5 clearfix" },
                    buttons,
                    React.createElement(
                        "button",
                        { type: "button", className: "btn btn-default btn-xs pull-right ml-5 invisible" },
                        "Spacer"
                    )
                ),
                React.createElement(
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
                                React.createElement("textarea", { className: leftClassName,
                                    placeholder: this.props.texts.sectionTextareaPlaceholder,
                                    value: this.props.data.left_text,
                                    onChange: this._handleChange.bind(this, "left") })
                            ),
                            React.createElement(
                                "div",
                                { className: "col-xs-6 pl-5" },
                                React.createElement("textarea", { className: rightClassName,
                                    placeholder: this.props.texts.sectionTextareaPlaceholder,
                                    value: this.props.data.right_text,
                                    onChange: this._handleChange.bind(this, "right") })
                            )
                        )
                    )
                )
            );
        }
    }, {
        key: "_handleChange",
        value: function _handleChange(side, event) {
            var data = void 0;
            switch (side) {
                case "left":
                    data = _extends({}, this.props.data, {
                        left_text: event.target.value
                    });
                    break;
                case "right":
                    data = _extends({}, this.props.data, {
                        right_text: event.target.value
                    });
                    break;
            }
            this.props.onChange(data);
        }
    }]);

    return DeveloperSplitTextParagraph;
}(React.Component);