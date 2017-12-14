"use strict";

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _toConsumableArray(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } else { return Array.from(arr); } }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperMultichoiceOneAnswer = function (_React$Component) {
    _inherits(DeveloperMultichoiceOneAnswer, _React$Component);

    function DeveloperMultichoiceOneAnswer(props) {
        _classCallCheck(this, DeveloperMultichoiceOneAnswer);

        var _this = _possibleConstructorReturn(this, (DeveloperMultichoiceOneAnswer.__proto__ || Object.getPrototypeOf(DeveloperMultichoiceOneAnswer)).call(this, props));

        _this._alphabet = "ABCDEFGHIJKLMNOP";
        _this._$choicesContainer;
        return _this;
    }

    _createClass(DeveloperMultichoiceOneAnswer, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            this._$choicesContainer = $("[data-choices]");
            if (this._$choicesContainer.length) {
                this._$choicesContainer.sortable({
                    axis: "y",
                    forceHelperSize: true,
                    forcePlaceholderSize: true,
                    placeholder: "bb-test-answer-placeholder",
                    tolerance: "pointer",

                    create: function () {
                        this._$choicesContainer.height(this._$choicesContainer.height());
                    }.bind(this),
                    update: this._choicesSorted.bind(this)
                });
            } else {
                this._$choicesContainer = undefined;
            }
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            if (this._$choicesContainer) {
                this._$choicesContainer.sortable("destroy");
                this._$choicesContainer = undefined;
            }
        }
    }, {
        key: "render",
        value: function render() {
            var _this2 = this;

            var developerChoices = [];
            var choices = [];
            this.props.data.choices.map(function (choice, index) {
                var DeveloperChoiceClass = eval("Developer" + choice.choice_class);
                var ChoiceClass = eval(choice.choice_class);

                var chosen = _this2.props.data.correct_id && _this2.props.data.correct_id === choice.id ? true : false;

                developerChoices.push(React.createElement(DeveloperChoiceClass, { key: choice.id,
                    choiceId: choice.id,
                    data: choice.meta_data,
                    onChange: _this2._choiceChange.bind(_this2, choice.id),
                    texts: _this2.props.texts,
                    chosen: chosen }));
                choices.push(React.createElement(ChoiceClass, { key: choice.id,
                    data: choice.meta_data,
                    label: _this2._alphabet[index],
                    chosen: chosen }));
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
                                { "data-choices": true },
                                developerChoices
                            ),
                            React.createElement(
                                "div",
                                { className: "form-group text-center mt-23" },
                                React.createElement(
                                    "button",
                                    { type: "button", className: "btn btn-success" },
                                    this.props.texts.addAnswerChoice
                                )
                            ),
                            React.createElement("hr", { className: "bb-separator" }),
                            React.createElement(
                                "div",
                                { className: "mb-23" },
                                choices
                            )
                        )
                    )
                )
            );
        }
    }, {
        key: "_choiceChange",
        value: function _choiceChange(choiceId, data) {
            var _data = this._deepCopyData();
            for (var i = 0; i < _data.choices.length; i++) {
                if (_data.choices[i].id === choiceId) {
                    _data.choices[i].meta_data = data;
                    break;
                }
            }
            this.props.onChange(_data);
        }
    }, {
        key: "_deepCopyData",
        value: function _deepCopyData() {
            var data = _extends({}, this.props.data);
            data.choices = [].concat(_toConsumableArray(data.choices));
            for (var i = 0; i < data.choices.length; i++) {
                data.choices[i] = _extends({}, data.choices[i]);
                data.choices[i].meta_data = _extends({}, data.choices[i].meta_data);
            }
            return data;
        }
    }, {
        key: "_choicesSorted",
        value: function _choicesSorted(event, ui) {
            var choicesIds = this._$choicesContainer.sortable("toArray", {
                attribute: "data-choice-id"
            }).map(function (id) {
                return parseInt(id, 10);
            });
            var _data = this._deepCopyData();
            _data.choices.sort(function (a, b) {
                var i = choicesIds.indexOf(a.id);
                var j = choicesIds.indexOf(b.id);
                if (i === j) {
                    return 0;
                }
                return i < j ? -1 : 1;
            });
            this.props.onChange(_data);
        }
    }]);

    return DeveloperMultichoiceOneAnswer;
}(React.Component);