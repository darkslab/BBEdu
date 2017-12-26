"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var MultichoiceTextChoice = function (_React$Component) {
    _inherits(MultichoiceTextChoice, _React$Component);

    function MultichoiceTextChoice(props) {
        _classCallCheck(this, MultichoiceTextChoice);

        return _possibleConstructorReturn(this, (MultichoiceTextChoice.__proto__ || Object.getPrototypeOf(MultichoiceTextChoice)).call(this, props));
    }

    _createClass(MultichoiceTextChoice, [{
        key: "render",
        value: function render() {
            var choiceClassName = "bb-test-answer-choice";
            if (this.props.chosen) {
                choiceClassName += " bb-test-answer-choice-selected";
            }

            var contentClassName = "bb-test-answer";
            var content = null;
            if (this.props.data.text) {
                content = this.props.data.text;
            } else if (this.props.optionalTexts) {
                contentClassName += " bb-placeholder";
                content = this.props.optionalTexts.choiceEmptyPlaceholder;
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
                                onClick: function onClick() {} },
                            this.props.label
                        )
                    )
                ),
                React.createElement(
                    "div",
                    { className: "col-xs-10 col-sm-7 pl-0" },
                    React.createElement(
                        "div",
                        { className: contentClassName },
                        content
                    )
                )
            );
        }
    }]);

    return MultichoiceTextChoice;
}(React.Component);