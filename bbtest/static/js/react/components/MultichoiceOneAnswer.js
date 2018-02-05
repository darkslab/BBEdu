"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var MultichoiceOneAnswer = function (_React$Component) {
    _inherits(MultichoiceOneAnswer, _React$Component);

    function MultichoiceOneAnswer(props) {
        _classCallCheck(this, MultichoiceOneAnswer);

        var _this = _possibleConstructorReturn(this, (MultichoiceOneAnswer.__proto__ || Object.getPrototypeOf(MultichoiceOneAnswer)).call(this, props));

        _this._alphabet = "ABCDEFGH";
        return _this;
    }

    _createClass(MultichoiceOneAnswer, [{
        key: "render",
        value: function render() {
            var choices = [];
            for (var i = 0; i < this.props.data.choices.length; i++) {
                var ChoiceClass = eval(this.props.data.choices[i].choice_class);
                choices.push(React.createElement(ChoiceClass, { key: this.props.data.choices[i].id,
                    data: this.props.data.choices[i].meta_data,
                    label: this._alphabet[i],
                    chosen: false }));
            }

            return React.createElement(
                "div",
                { className: "row" },
                React.createElement(
                    "div",
                    { className: "col-xs-12" },
                    React.createElement(
                        "div",
                        { className: "panel panel-default mb-15" },
                        React.createElement(
                            "div",
                            { className: "panel-heading" },
                            React.createElement(
                                "h4",
                                { className: "panel-title text-center" },
                                this.props.texts.multichoiceOneAnswerTitle
                            )
                        ),
                        React.createElement(
                            "div",
                            { className: "panel-body" },
                            React.createElement(
                                "div",
                                { className: "mb-15" },
                                choices
                            )
                        )
                    )
                )
            );
        }
    }]);

    return MultichoiceOneAnswer;
}(React.Component);