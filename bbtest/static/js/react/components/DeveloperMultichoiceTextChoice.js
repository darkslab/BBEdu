"use strict";

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperMultichoiceTextChoice = function (_React$Component) {
    _inherits(DeveloperMultichoiceTextChoice, _React$Component);

    function DeveloperMultichoiceTextChoice(props) {
        _classCallCheck(this, DeveloperMultichoiceTextChoice);

        return _possibleConstructorReturn(this, (DeveloperMultichoiceTextChoice.__proto__ || Object.getPrototypeOf(DeveloperMultichoiceTextChoice)).call(this, props));
    }

    _createClass(DeveloperMultichoiceTextChoice, [{
        key: "render",
        value: function render() {
            var buttons = [];
            buttons.push(React.createElement(
                "button",
                { key: "delete",
                    type: "button",
                    className: "btn btn-danger btn-xs pull-right ml-5",
                    onClick: this.props.onDelete },
                React.createElement("i", { className: "fa fa-fw fa-times" })
            ));
            buttons.push(React.createElement(
                "button",
                { key: "chosen",
                    type: "button",
                    className: "btn btn-default btn-xs pull-right ml-5" + (this.props.chosen ? " active" : ""),
                    onClick: this.props.onSelect.bind(null, !this.props.chosen) },
                this.props.texts.answerChoiceSelectButton
            ));
            if (this.props.chosen) {
                buttons.push(React.createElement(
                    "button",
                    { disabled: true,
                        key: "solution",
                        type: "button",
                        className: "btn btn-primary btn-xs pull-right ml-5" },
                    this.props.texts.answerChoiceSolutionButton
                ));
            }

            var className = "form-control bb-test-answer bb-test-answer-textarea";
            if (!this.props.data.text) {
                className += " bb-test-answer-textarea-empty";
            }

            return React.createElement(
                "div",
                { className: "form-group bb-test-section-movable bb-test-section-background", "data-choice-id": this.props.choiceId },
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
                    React.createElement("div", { className: "col-xs-2 col-sm-3 pr-0" }),
                    React.createElement(
                        "div",
                        { className: "col-xs-10 col-sm-7 pl-0" },
                        React.createElement("textarea", { className: className,
                            placeholder: this.props.texts.choiceTextareaPlaceholder,
                            value: this.props.data.text,
                            onChange: this._handleChange.bind(this) })
                    )
                )
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

    return DeveloperMultichoiceTextChoice;
}(React.Component);