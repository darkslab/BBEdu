"use strict";

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _toConsumableArray(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } else { return Array.from(arr); } }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperMultichoiceMultiAnswer = function (_React$Component) {
    _inherits(DeveloperMultichoiceMultiAnswer, _React$Component);

    function DeveloperMultichoiceMultiAnswer(props) {
        _classCallCheck(this, DeveloperMultichoiceMultiAnswer);

        var _this = _possibleConstructorReturn(this, (DeveloperMultichoiceMultiAnswer.__proto__ || Object.getPrototypeOf(DeveloperMultichoiceMultiAnswer)).call(this, props));

        _this._alphabet = "ABCDEFGH";
        _this._$choicesContainer;
        _this.state = {
            choicesModal: false,
            confirmModal: false
        };
        return _this;
    }

    _createClass(DeveloperMultichoiceMultiAnswer, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            this._$choicesContainer = $("[data-choices]");
            if (this._$choicesContainer.length) {
                this._$choicesContainer.sortable({
                    axis: "y",
                    cancel: "input,textarea,button,select,option,[data-bb-non-sortable]",
                    forceHelperSize: true,
                    forcePlaceholderSize: true,
                    items: "> [data-choice-id]",
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
        key: "componentWillUpdate",
        value: function componentWillUpdate() {
            if (this._$choicesContainer) {
                this._$choicesContainer.css("height", "");
            }
        }
    }, {
        key: "componentDidUpdate",
        value: function componentDidUpdate() {
            if (this._$choicesContainer) {
                this._$choicesContainer.height(this._$choicesContainer.height());
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

                var chosen = _this2.props.data.correct_ids.indexOf(choice.id) > -1 ? true : false;

                developerChoices.push(React.createElement(DeveloperChoiceClass, { key: choice.id,
                    choiceId: choice.id,
                    data: choice.meta_data,
                    onChange: _this2._choiceChange.bind(_this2, choice.id),
                    onSelect: _this2._choiceSelect.bind(_this2, choice.id),
                    onDelete: _this2._choiceDelete.bind(_this2, choice.id),
                    canEdit: _this2.props.ability.canEditAnswerChoice(choice.id),
                    canDelete: _this2.props.ability.canDeleteAnswerChoice(choice.id),
                    texts: _this2.props.texts,
                    chosen: chosen }));
                choices.push(React.createElement(ChoiceClass, { key: choice.id,
                    data: choice.meta_data,
                    label: _this2._alphabet[index],
                    chosen: chosen,
                    isMulti: true,
                    texts: _this2.props.texts,
                    forDevelopers: true }));
            });
            if (!choices.length) {
                choices.push(React.createElement(
                    "div",
                    { key: "empty", className: "row" },
                    React.createElement(
                        "div",
                        { className: "col-xs-12" },
                        React.createElement(
                            "p",
                            { className: "lead text-center mb-0" },
                            this.props.texts.noAnswerChoices
                        )
                    )
                ));
            }

            var modal = null;
            if (this.state.choicesModal) {
                modal = React.createElement(DeveloperSelectorModal, { title: this.props.texts.answerChoicesModalTitle,
                    complete: this._completeModal.bind(this, "choices"),
                    classData: [{
                        class: "MultichoiceTextChoice",
                        caption: this.props.texts.answerChoicesModalTitleButtonMultichoiceTextChoice
                    }] });
            } else if (this.state.confirmModal) {
                modal = React.createElement(ConfirmModal, { title: this.props.texts.deleteModalTitle,
                    yesCaption: this.props.texts.deleteModalYesCaption,
                    noCaption: this.props.texts.deleteModalNoCaption,
                    isInverse: true,
                    complete: this._completeModal.bind(this, "confirm") });
            }

            var addAnswerChoiceButton = null;
            if (this.props.ability.canAddAnswerChoice() && developerChoices.length < this._alphabet.length) {
                addAnswerChoiceButton = React.createElement(
                    "div",
                    { className: "form-group text-center mt-23" },
                    React.createElement(
                        "button",
                        { type: "button",
                            className: "btn btn-success",
                            onClick: this._renderModal.bind(this, "choices") },
                        this.props.texts.addAnswerChoice
                    )
                );
            }

            var deleteButton = null;
            if (this.props.ability.canDeleteAnswer()) {
                deleteButton = React.createElement(
                    "button",
                    { type: "button",
                        className: "btn btn-danger btn-sm",
                        onClick: this._renderModal.bind(this, "confirm") },
                    React.createElement("i", { className: "fa fa-fw fa-times" })
                );
            }

            return React.createElement(
                React.Fragment,
                null,
                modal,
                React.createElement(
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
                                    "div",
                                    { className: "row" },
                                    React.createElement(
                                        "h4",
                                        { className: "col-xs-9 col-sm-11 mt-5 mb-5" },
                                        this.props.texts.multichoiceMultiAnswerTitle
                                    ),
                                    React.createElement(
                                        "div",
                                        { className: "col-xs-3 col-sm-1 text-right pl-0" },
                                        deleteButton
                                    )
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
                                addAnswerChoiceButton,
                                React.createElement("hr", { className: "bb-separator" }),
                                React.createElement(
                                    "div",
                                    { className: "mb-15" },
                                    choices
                                )
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
        key: "_choiceSelect",
        value: function _choiceSelect(choiceId, data) {
            var _data = this._deepCopyData();
            var i = _data.correct_ids.indexOf(choiceId);
            if (data) {
                if (i < 0) {
                    _data.correct_ids.push(choiceId);
                }
            } else {
                if (i > -1) {
                    _data.correct_ids.splice(i, 1);
                }
            }
            this.props.onChange(_data);
        }
    }, {
        key: "_choiceDelete",
        value: function _choiceDelete(choiceId) {
            var data = this._deepCopyData();
            for (var i = 0; i < data.choices.length; i++) {
                if (data.choices[i].id === choiceId) {
                    var j = data.correct_ids.indexOf(choiceId);
                    if (j > -1) {
                        data.correct_ids.splice(j, 1);
                    }
                    data.choices.splice(i, 1);
                    break;
                }
            }
            this.props.onChange(data);
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
            data.correct_ids = [].concat(_toConsumableArray(data.correct_ids));
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
    }, {
        key: "_renderModal",
        value: function _renderModal(type) {
            switch (type) {
                case "choices":
                    this.setState({
                        choicesModal: true
                    });
                    break;
                case "confirm":
                    this.setState({
                        confirmModal: true
                    });
                    break;
            }
        }
    }, {
        key: "_completeModal",
        value: function _completeModal(type, data) {
            switch (type) {
                case "choices":
                    if (data) {
                        var _data = this._deepCopyData();
                        var choiceIds = _data.choices.map(function (choice) {
                            return choice.id;
                        }).sort(function (a, b) {
                            return a === b ? 0 : a < b ? -1 : 1;
                        });

                        var choice = {
                            choice_class: data,
                            id: null,
                            meta_data: {
                                text: ""
                            }
                        };
                        if (choiceIds.length) {
                            choice.id = choiceIds[choiceIds.length - 1] + 1;
                        } else {
                            choice.id = Math.random() * 0xffff | 0x00;
                        }

                        _data.choices.push(choice);
                        this.props.onChange(_data);
                    }
                    this.setState({
                        choicesModal: false
                    });
                    break;
                case "confirm":
                    if (data) {
                        this.props.onDelete();
                    } else {
                        this.setState({
                            confirmModal: false
                        });
                    }
                    break;
            }
        }
    }]);

    return DeveloperMultichoiceMultiAnswer;
}(React.Component);