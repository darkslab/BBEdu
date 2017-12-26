"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperQuestion = function (_React$Component) {
    _inherits(DeveloperQuestion, _React$Component);

    function DeveloperQuestion(props) {
        _classCallCheck(this, DeveloperQuestion);

        var _this = _possibleConstructorReturn(this, (DeveloperQuestion.__proto__ || Object.getPrototypeOf(DeveloperQuestion)).call(this, props));

        _this.state = {
            toggleFlag: true,
            paragraphsModal: false,
            answersModal: false
        };
        _this._$paragraphsContainer;
        _this._maxParagraphs = 8;
        return _this;
    }

    _createClass(DeveloperQuestion, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            this._$paragraphsContainer = $("[data-paragraphs]");
            if (this._$paragraphsContainer.length) {
                this._$paragraphsContainer.sortable({
                    axis: "y",
                    forceHelperSize: true,
                    forcePlaceholderSize: true,
                    placeholder: "bb-test-paragraph-placeholder",
                    tolerance: "pointer",

                    create: function () {
                        this._$paragraphsContainer.height(this._$paragraphsContainer.height());
                    }.bind(this),
                    update: this._paragraphsSorted.bind(this)
                });
            } else {
                this._$paragraphsContainer = undefined;
            }
        }
    }, {
        key: "componentWillUpdate",
        value: function componentWillUpdate() {
            if (this._$paragraphsContainer) {
                this._$paragraphsContainer.css("height", "");
            }
        }
    }, {
        key: "componentDidUpdate",
        value: function componentDidUpdate() {
            if (this._$paragraphsContainer) {
                this._$paragraphsContainer.height(this._$paragraphsContainer.height());
            }
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            if (this._$paragraphsContainer) {
                this._$paragraphsContainer.sortable("destroy");
                this._$paragraphsContainer = undefined;
            }
        }
    }, {
        key: "render",
        value: function render() {
            var _this2 = this;

            var developerParagraphs = [];
            var paragraphs = [];
            this.props.object.paragraphIds().map(function (id) {
                var paragraphData = _this2.props.object.paragraph(id);

                var DeveloperParagraphClass = eval("Developer" + paragraphData.paragraph_class);
                var ParagraphClass = eval(paragraphData.paragraph_class);

                developerParagraphs.push(React.createElement(DeveloperParagraphClass, { key: id,
                    paragraphId: id,
                    data: paragraphData.meta_data,
                    onChange: _this2._paragraphChange.bind(_this2, id),
                    onDelete: _this2._paragraphDelete.bind(_this2, id),
                    texts: _this2.props.texts }));
                paragraphs.push(React.createElement(ParagraphClass, { key: id,
                    data: paragraphData.meta_data,
                    optionalTexts: _this2.props.texts }));
            });
            if (!paragraphs.length) {
                paragraphs.push(React.createElement(
                    "div",
                    { key: "empty", className: "bb-test-paragraph" },
                    React.createElement(
                        "p",
                        { className: "lead text-center mb-0" },
                        this.props.texts.noParagraphs
                    )
                ));
            }

            var answerContent = null;
            var answerData = this.props.object.answer();
            if (answerData.answer_class) {
                var AnswerClass = eval("Developer" + answerData.answer_class);
                answerContent = React.createElement(AnswerClass, { data: answerData.meta_data,
                    onChange: this._answerChange.bind(this),
                    onDelete: this._answerDelete.bind(this),
                    texts: this.props.texts });
            } else {
                answerContent = React.createElement(
                    "div",
                    { className: "row mb-23" },
                    React.createElement(
                        "div",
                        { className: "col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3" },
                        React.createElement(
                            "button",
                            { type: "button",
                                className: "btn btn-primary btn-lg btn-block",
                                onClick: this._renderModal.bind(this, "answers") },
                            this.props.texts.addAnswer
                        )
                    )
                );
            }

            var modal = null;
            if (this.state.paragraphsModal) {
                modal = React.createElement(DeveloperSelectorModal, { title: this.props.texts.paragraphsModalTitle,
                    complete: this._completeModal.bind(this, "paragraphs"),
                    classData: [{
                        class: "TextParagraph",
                        caption: this.props.texts.paragraphsModalButtonTextParagraph
                    }, {
                        class: "SplitTextParagraph",
                        caption: this.props.texts.paragraphsModalButtonSplitTextParagraph
                    }] });
            } else if (this.state.answersModal) {
                modal = React.createElement(DeveloperSelectorModal, { title: this.props.texts.answersModalTitle,
                    complete: this._completeModal.bind(this, "answers"),
                    classData: [{
                        class: "MultichoiceOneAnswer",
                        caption: this.props.texts.multichoiceOneAnswerTitle
                    }] });
            }

            var addParagaphButton = null;
            if (developerParagraphs.length < this._maxParagraphs) {
                addParagaphButton = React.createElement(
                    "div",
                    { className: "form-group text-center mt-23" },
                    React.createElement(
                        "button",
                        { type: "button",
                            className: "btn btn-success",
                            onClick: this._renderModal.bind(this, "paragraphs") },
                        this.props.texts.addParagraph
                    )
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
                            { className: "panel panel-primary" },
                            React.createElement(
                                "div",
                                { className: "panel-heading bb-rel" },
                                React.createElement(
                                    "div",
                                    { className: "bb-test-number" },
                                    this.props.count
                                ),
                                React.createElement(
                                    "h4",
                                    { className: "panel-title bb-test-title mt-15 mb-15" },
                                    this.props.texts.question
                                )
                            ),
                            React.createElement(
                                "div",
                                { className: "panel-body" },
                                React.createElement(
                                    "div",
                                    { className: "form-horizontal" },
                                    React.createElement(DeveloperAttribute, { label: this.props.texts.difficulty,
                                        value: this.props.object.difficulty(),
                                        data: this.props.attributes.difficulties,
                                        onChange: this._attributeChange.bind(this, "difficulty") }),
                                    React.createElement(DeveloperAttribute, { label: this.props.texts.taxonomy,
                                        value: this.props.object.taxonomy(),
                                        data: this.props.attributes.taxonomies,
                                        onChange: this._attributeChange.bind(this, "taxonomy") }),
                                    React.createElement(DeveloperAttribute, { label: this.props.texts.topic,
                                        value: this.props.object.topic(),
                                        data: this.props.attributes.topics,
                                        onChange: this._attributeChange.bind(this, "topic") })
                                ),
                                React.createElement(
                                    "div",
                                    { "data-paragraphs": true },
                                    developerParagraphs
                                ),
                                addParagaphButton,
                                React.createElement("hr", { className: "bb-separator" }),
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
    }, {
        key: "_pokeComponent",
        value: function _pokeComponent() {
            this.setState(function (prevState) {
                return {
                    toggleFlag: !prevState.toggleFlag
                };
            });
        }
    }, {
        key: "_attributeChange",
        value: function _attributeChange(type, value) {
            switch (type) {
                case "difficulty":
                    this.props.object.setDifficulty(value);
                    break;
                case "taxonomy":
                    this.props.object.setTaxonomy(value);
                    break;
                case "topic":
                    this.props.object.setTopic(value);
                    break;
            }
            this._pokeComponent();
        }
    }, {
        key: "_paragraphChange",
        value: function _paragraphChange(id, data) {
            this.props.object.updateParagraph(id, data);
            this._pokeComponent();
        }
    }, {
        key: "_paragraphDelete",
        value: function _paragraphDelete(id) {
            this.props.object.deleteParagraph(id);
            this._pokeComponent();
        }
    }, {
        key: "_paragraphsSorted",
        value: function _paragraphsSorted(event, ui) {
            var paragraphIds = this._$paragraphsContainer.sortable("toArray", {
                attribute: "data-paragraph-id"
            });
            this.props.object.setParagraphOrder(paragraphIds);
            this._pokeComponent();
        }
    }, {
        key: "_answerChange",
        value: function _answerChange(data) {
            this.props.object.updateAnswer(data);
            this._pokeComponent();
        }
    }, {
        key: "_answerDelete",
        value: function _answerDelete() {
            this.props.object.deleteAnswer();
            this._pokeComponent();
        }
    }, {
        key: "_renderModal",
        value: function _renderModal(type) {
            switch (type) {
                case "paragraphs":
                    this.setState({
                        paragraphsModal: true
                    });
                    break;
                case "answers":
                    this.setState({
                        answersModal: true
                    });
                    break;
            }
        }
    }, {
        key: "_completeModal",
        value: function _completeModal(type, data) {
            switch (type) {
                case "paragraphs":
                    if (data) {
                        this.props.object.addParagraph(data);
                    }
                    this.setState({
                        paragraphsModal: false
                    });
                    break;
                case "answers":
                    if (data) {
                        this.props.object.setAnswer(data);
                    }
                    this.setState({
                        answersModal: false
                    });
                    break;
            }
        }
    }]);

    return DeveloperQuestion;
}(React.Component);