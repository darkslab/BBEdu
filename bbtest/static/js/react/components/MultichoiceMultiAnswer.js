"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _toConsumableArray(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } else { return Array.from(arr); } }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var MultichoiceMultiAnswer = function (_React$Component) {
    _inherits(MultichoiceMultiAnswer, _React$Component);

    function MultichoiceMultiAnswer(props) {
        _classCallCheck(this, MultichoiceMultiAnswer);

        var _this = _possibleConstructorReturn(this, (MultichoiceMultiAnswer.__proto__ || Object.getPrototypeOf(MultichoiceMultiAnswer)).call(this, props));

        _this._alphabet = "ABCDEFGH";
        _this._correctIds = [];
        _this._assignCorrectIds(_this.props.answer);
        return _this;
    }

    _createClass(MultichoiceMultiAnswer, [{
        key: "componentWillReceiveProps",
        value: function componentWillReceiveProps(nextProps) {
            this._assignCorrectIds(nextProps.answer);
        }
    }, {
        key: "render",
        value: function render() {
            var choices = [];
            for (var i = 0; i < this.props.data.choices.length; i++) {
                var ChoiceClass = eval(this.props.data.choices[i].choice_class);
                var chosen = false;
                if (this.props.answer && this.props.answer.correct_ids.indexOf(this.props.data.choices[i].id) > -1) {
                    chosen = true;
                }
                choices.push(React.createElement(ChoiceClass, { key: this.props.data.choices[i].id,
                    data: this.props.data.choices[i].meta_data,
                    label: this._alphabet[i],
                    chosen: chosen,
                    isMulti: true,
                    onChoose: this._handleChoose.bind(this, this.props.data.choices[i].id),
                    texts: this.props.texts,
                    forDevelopers: false }));
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
                                this.props.texts.multichoiceMultiAnswerTitle
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
    }, {
        key: "_handleChoose",
        value: function _handleChoose(choiceId) {
            var i = this._correctIds.indexOf(choiceId);
            if (i > -1) {
                this._correctIds.splice(i, 1);
            } else {
                this._correctIds.push(choiceId);
            }
            var data = {
                answer: null,
                observation: {}
            };
            if (this._correctIds.length) {
                data.answer = {
                    correct_ids: [].concat(_toConsumableArray(this._correctIds))
                };
            }
            this.props.onUpdate(data);
        }
    }, {
        key: "_assignCorrectIds",
        value: function _assignCorrectIds(answer) {
            this._correctIds = [];
            if (!answer) {
                return;
            }
            for (var i = 0; i < answer.correct_ids.length; i++) {
                this._correctIds.push(answer.correct_ids[i]);
            }
        }
    }]);

    return MultichoiceMultiAnswer;
}(React.Component);