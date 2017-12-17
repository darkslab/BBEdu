"use strict";

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperTextParagraph = function (_React$Component) {
    _inherits(DeveloperTextParagraph, _React$Component);

    function DeveloperTextParagraph(props) {
        _classCallCheck(this, DeveloperTextParagraph);

        return _possibleConstructorReturn(this, (DeveloperTextParagraph.__proto__ || Object.getPrototypeOf(DeveloperTextParagraph)).call(this, props));
    }

    _createClass(DeveloperTextParagraph, [{
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

            var className = "form-control bb-test-paragraph bb-test-paragraph-textarea";
            if (!this.props.data.text) {
                className += " bb-test-paragraph-textarea-empty";
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
                React.createElement("textarea", { className: className,
                    placeholder: this.props.texts.sectionTextareaPlaceholder,
                    value: this.props.data.text,
                    onChange: this._handleChange.bind(this) })
            );
        }
    }, {
        key: "_handleChange",
        value: function _handleChange(event) {
            this.props.onChange(_extends({}, this.props.data, {
                text: event.target.value
            }));
        }
    }]);

    return DeveloperTextParagraph;
}(React.Component);