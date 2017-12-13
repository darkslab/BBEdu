"use strict";

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperMultichoiceOneAnswer = function (_React$Component) {
    _inherits(DeveloperMultichoiceOneAnswer, _React$Component);

    function DeveloperMultichoiceOneAnswer(props) {
        _classCallCheck(this, DeveloperMultichoiceOneAnswer);

        var _this = _possibleConstructorReturn(this, (DeveloperMultichoiceOneAnswer.__proto__ || Object.getPrototypeOf(DeveloperMultichoiceOneAnswer)).call(this, props));

        _this.state = _extends({}, _this.props.data);
        return _this;
    }

    _createClass(DeveloperMultichoiceOneAnswer, [{
        key: "render",
        value: function render() {
            var _this2 = this;

            var developerAnswers = [];
            var answers = [];
            this.state.choices.map(function (choice) {
                developerAnswers.push(React.createElement(DeveloperMultichoiceTextChoice, { key: choice.id,
                    answerId: choice.id,
                    data: choice.text,
                    onChange: _this2._choiceChange.bind(_this2, choice.id),
                    texts: _this2.props.texts }));
                answers.push(React.createElement(MultichoiceTextChoice, { key: choice.id,
                    data: choice.text }));
            });

            return React.createElement(
                "div",
                { className: "row" },
                React.createElement(
                    "div",
                    { className: "col-xs-12" },
                    React.createElement(
                        "div",
                        { className: "panel panel-default" },
                        React.createElement(
                            "div",
                            { className: "panel-heading" },
                            React.createElement(
                                "h4",
                                { className: "text-center" },
                                this.props.texts.multichoiceOneAnswerTitle
                            )
                        ),
                        React.createElement(
                            "div",
                            { className: "panel-body" },
                            React.createElement(
                                "div",
                                { "data-answers": true },
                                developerAnswers
                            ),
                            React.createElement(
                                "div",
                                { className: "form-group text-center mt-15" },
                                React.createElement(
                                    "button",
                                    { type: "button", className: "btn btn-success" },
                                    this.props.texts.addAnswerChoice
                                )
                            ),
                            React.createElement("hr", { className: "bb-separator" }),
                            answers
                        )
                    )
                )
            );
        }
    }, {
        key: "_choiceChange",
        value: function _choiceChange(choiceId, data) {
            // DARK_TODO
        }
    }]);

    return DeveloperMultichoiceOneAnswer;
}(React.Component);