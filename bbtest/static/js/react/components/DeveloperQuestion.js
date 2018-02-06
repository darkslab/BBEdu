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
        _this._saveTimeout = 4000;
        _this._timer = null;
        _this._$quickModal;
        _this._quickModalIsClosing = false;
        _this._quickModalTimer = null;
        _this._quickModalTimeout = 1500; // this time should be at least twice less than this._saveTimeout

        _this._boundQuickModalTransitioned = _this._quickModalTransitioned.bind(_this);
        return _this;
    }

    _createClass(DeveloperQuestion, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            this._$paragraphsContainer = $("[data-paragraphs]");
            this._$paragraphsContainer.sortable({
                axis: "y",
                cancel: "input,textarea,button,select,option,[data-bb-non-sortable]",
                forceHelperSize: true,
                forcePlaceholderSize: true,
                items: "> [data-paragraph-id]",
                placeholder: "bb-test-paragraph-placeholder",
                tolerance: "pointer",

                create: function () {
                    this._$paragraphsContainer.height(this._$paragraphsContainer.height());
                }.bind(this),
                update: this._paragraphsSorted.bind(this)
            });

            this._$quickModal = $("[data-quick-modal]");
            this._$quickModal.on("webkitTransitionEnd otransitionend transitionend", this._boundQuickModalTransitioned);
        }
    }, {
        key: "componentWillUpdate",
        value: function componentWillUpdate() {
            this._$paragraphsContainer.css("height", "");
        }
    }, {
        key: "componentDidUpdate",
        value: function componentDidUpdate() {
            this._$paragraphsContainer.height(this._$paragraphsContainer.height());
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            this._$paragraphsContainer.sortable("destroy");

            clearTimeout(this._timer);
            this.props.object.stop("question");

            this._$quickModal.off("webkitTransitionEnd otransitionend transitionend", this._boundQuickModalTransitioned);
            clearTimeout(this._quickModalTimer);
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
                    canDelete: _this2.props.ability.canDeleteParagraph(id),
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
                    ability: this.props.ability,
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
                var paragraphClassData = [];
                if (this.props.ability.canChooseTextParagraph()) {
                    paragraphClassData.push({
                        class: "TextParagraph",
                        caption: this.props.texts.paragraphsModalButtonTextParagraph
                    });
                }
                if (this.props.ability.canChooseSplitTextParagraph()) {
                    paragraphClassData.push({
                        class: "SplitTextParagraph",
                        caption: this.props.texts.paragraphsModalButtonSplitTextParagraph
                    });
                }
                if (this.props.ability.canChooseImageParagraph()) {
                    paragraphClassData.push({
                        class: "ImageParagraph",
                        caption: this.props.texts.paragraphsModalButtonImageParagraph
                    });
                }
                modal = React.createElement(DeveloperSelectorModal, { title: this.props.texts.paragraphsModalTitle,
                    complete: this._completeModal.bind(this, "paragraphs"),
                    classData: paragraphClassData });
            } else if (this.state.answersModal) {
                modal = React.createElement(DeveloperSelectorModal, { title: this.props.texts.answersModalTitle,
                    complete: this._completeModal.bind(this, "answers"),
                    classData: [{
                        class: "MultichoiceOneAnswer",
                        caption: this.props.texts.multichoiceOneAnswerTitle
                    }] });
            }

            var addParagaphButton = null;
            if (this.props.ability.canAddParagraph() && developerParagraphs.length < this._maxParagraphs) {
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

            var taxonomyContent = null;
            if (this.props.attributes.taxonomies.length > 0) {
                taxonomyContent = React.createElement(DeveloperAttribute, { label: this.props.texts.taxonomy,
                    value: this.props.object.taxonomy(),
                    data: this.props.attributes.taxonomies,
                    onChange: this._attributeChange.bind(this, "taxonomy") });
            }
            var topicContent = null;
            if (this.props.attributes.topics.length > 0) {
                topicContent = React.createElement(DeveloperAttribute, { label: this.props.texts.topic,
                    value: this.props.object.topic(),
                    data: this.props.attributes.topics,
                    onChange: this._attributeChange.bind(this, "topic") });
            }

            return React.createElement(
                React.Fragment,
                null,
                React.createElement(
                    "div",
                    { className: "modal bb-quick-modal fade", "data-quick-modal": true },
                    React.createElement(
                        "div",
                        { className: "modal-dialog" },
                        React.createElement(
                            "div",
                            { className: "modal-content" },
                            React.createElement(
                                "div",
                                { className: "modal-body" },
                                React.createElement(
                                    "p",
                                    { className: "lead text-center mb-0" },
                                    this.props.texts.saved
                                )
                            )
                        )
                    )
                ),
                modal,
                React.createElement(
                    "div",
                    { className: "row" },
                    React.createElement(
                        "div",
                        { className: "col-xs-12" },
                        React.createElement(
                            "div",
                            { className: "panel panel-primary mb-15" },
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
                                    taxonomyContent,
                                    topicContent
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
            this._scheduleSave();
        }
    }, {
        key: "_paragraphChange",
        value: function _paragraphChange(id, data, skipSave) {
            this.props.object.updateParagraph(id, data);
            this._pokeComponent();
            if (skipSave) {
                return;
            }
            this._scheduleSave();
        }
    }, {
        key: "_paragraphDelete",
        value: function _paragraphDelete(id) {
            this.props.object.deleteParagraph(id);
            this._pokeComponent();
            this._scheduleSave();
        }
    }, {
        key: "_paragraphsSorted",
        value: function _paragraphsSorted(event, ui) {
            var paragraphIds = this._$paragraphsContainer.sortable("toArray", {
                attribute: "data-paragraph-id"
            });
            this.props.object.setParagraphOrder(paragraphIds.map(function (id) {
                return parseInt(id, 10);
            }));
            this._pokeComponent();
            this._scheduleSave();
        }
    }, {
        key: "_answerChange",
        value: function _answerChange(data) {
            this.props.object.updateAnswer(data);
            this._pokeComponent();
            this._scheduleSave();
        }
    }, {
        key: "_answerDelete",
        value: function _answerDelete() {
            this.props.object.deleteAnswer();
            this._pokeComponent();
            this._scheduleSave();
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
                        this._scheduleSave();
                    }
                    this.setState({
                        paragraphsModal: false
                    });
                    break;
                case "answers":
                    if (data) {
                        this.props.object.setAnswer(data);
                        this._scheduleSave();
                    }
                    this.setState({
                        answersModal: false
                    });
                    break;
            }
        }
    }, {
        key: "_scheduleSave",
        value: function _scheduleSave() {
            var _this3 = this;

            clearTimeout(this._timer);
            this._timer = setTimeout(function () {
                _this3.props.object.save("question", _this3._saveCallback.bind(_this3));
            }, this._saveTimeout);
        }
    }, {
        key: "_saveCallback",
        value: function _saveCallback(result) {
            var _this4 = this;

            if (!result) {
                this.props.errorOut();
                return;
            }
            this._$quickModal.css("display", "block");
            this._quickModalTimer = setTimeout(function () {
                _this4._$quickModal.addClass("in");
                _this4._quickModalTimer = setTimeout(function () {
                    _this4._$quickModal.removeClass("in");
                    _this4._quickModalIsClosing = true;
                }, _this4._quickModalTimeout);
            });
        }
    }, {
        key: "_quickModalTransitioned",
        value: function _quickModalTransitioned(event) {
            if (event.currentTarget !== event.target) {
                return;
            }
            if (!this._quickModalIsClosing) {
                return;
            }
            this._quickModalIsClosing = false;
            this._$quickModal.css("display", "");
        }
    }]);

    return DeveloperQuestion;
}(React.Component);