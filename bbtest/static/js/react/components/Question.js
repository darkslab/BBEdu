"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Question = function (_React$Component) {
    _inherits(Question, _React$Component);

    function Question(props) {
        _classCallCheck(this, Question);

        return _possibleConstructorReturn(this, (Question.__proto__ || Object.getPrototypeOf(Question)).call(this, props));
    }

    _createClass(Question, [{
        key: "render",
        value: function render() {
            var paragraphs = [];
            for (var i = 0; i < this.props.object.paragraphs.length; i++) {
                var ParagraphClass = eval(this.props.object.paragraphs[i].paragraph_class);
                paragraphs.push(React.createElement(ParagraphClass, { key: i,
                    data: this.props.object.paragraphs[i].meta_data,
                    texts: this.props.texts,
                    forDevelopers: false }));
            }

            var timer = null;
            if (this.props.hasTimer) {
                var countDown = parseInt(this.props.secondsLeft / 60, 10) + ":" + ("0" + this.props.secondsLeft % 60).substr(-2);
                var countDownClassName = "bb-test-timer label mt-0 mb-0 pull-right";
                if (this.props.secondsLeft > 10) {
                    countDownClassName += " label-success";
                } else {
                    countDownClassName += " label-danger";
                }

                timer = React.createElement(
                    "span",
                    { className: countDownClassName },
                    React.createElement("i", { className: "fa fa-clock-o mr-10" }),
                    countDown
                );
            }

            var answerContent = null;
            if (this.props.object.answer_class) {
                var AnswerClass = eval(this.props.object.answer_class);
                answerContent = React.createElement(AnswerClass, { data: this.props.object.meta_data,
                    answer: this.props.answerData,
                    onUpdate: this.props.onAnswerUpdate,
                    canAnswer: this.props.canAnswer,
                    showCorrectAnswer: this.props.showCorrectAnswer,
                    texts: this.props.texts });
            }

            return React.createElement(
                React.Fragment,
                null,
                React.createElement(
                    "div",
                    { className: "row" },
                    React.createElement(
                        "div",
                        { className: "col-xs-12" },
                        React.createElement(
                            "div",
                            { className: "panel mb-15 panel-primary" },
                            React.createElement(
                                "div",
                                { className: "panel-heading bb-rel clearfix" },
                                React.createElement(
                                    "div",
                                    { className: "bb-test-number" },
                                    this.props.count
                                ),
                                React.createElement(
                                    "h4",
                                    { className: "panel-title bb-test-title mt-15 mb-15 pull-left" },
                                    this.props.texts.question
                                ),
                                timer
                            ),
                            React.createElement(
                                "div",
                                { className: "panel-body" },
                                React.createElement(
                                    "div",
                                    { className: "mb-15" },
                                    paragraphs
                                )
                            )
                        )
                    )
                ),
                answerContent
            );
        }
    }]);

    return Question;
}(React.Component);