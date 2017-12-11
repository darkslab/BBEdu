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
            update: 0
        };
        return _this;
    }

    _createClass(DeveloperQuestion, [{
        key: "render",
        value: function render() {
            var developerParagraphs = [];
            var paragraphs = [];
            this.props.object.paragraphIds().map(function (id) {
                var data = this.props.object.paragraph(id);
                if (data.paragraph_class === "TextParagraph") {
                    developerParagraphs.push(React.createElement(DeveloperTextParagraph, { key: id,
                        data: data.meta_data,
                        onChange: this._paragraphChange.bind(this, id),
                        placeholder: this.props.texts.sectionTextareaPlaceholder }));
                    paragraphs.push(React.createElement(TextParagraph, { key: id,
                        data: data.meta_data }));
                } else if (data.paragraph_class === "SplitTextParagraph") {
                    developerParagraphs.push(React.createElement(DeveloperSplitTextParagraph, { key: id,
                        data: data.meta_data,
                        onChange: this._paragraphChange.bind(this, id),
                        placeholder: this.props.texts.sectionTextareaPlaceholder }));
                    paragraphs.push(React.createElement(SplitTextParagraph, { key: id,
                        data: data.meta_data }));
                }
            }.bind(this));
            if (!paragraphs.length) {
                paragraphs.push(React.createElement(
                    "div",
                    { key: 'empty', className: "bb-test-paragraph" },
                    React.createElement(
                        "p",
                        { className: "lead text-center mb-0" },
                        this.props.texts.emptyParagraph
                    )
                ));
            }

            return React.createElement(
                "div",
                { className: "col-xs-12 bb-developer-container" },
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
                            null,
                            developerParagraphs,
                            React.createElement(
                                "div",
                                { className: "form-group text-center mt-23" },
                                React.createElement(
                                    "button",
                                    { type: "button", className: "btn btn-success" },
                                    this.props.texts.addSection
                                )
                            )
                        ),
                        React.createElement("hr", { className: "bb-separator" }),
                        React.createElement(
                            "div",
                            null,
                            paragraphs
                        )
                    )
                )
            );
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
            this.setState(function (prevState) {
                return {
                    update: prevState.update + 1
                };
            });
        }
    }, {
        key: "_paragraphChange",
        value: function _paragraphChange(id, data) {
            this.props.object.updateParagraph(id, data);
            this.setState(function (prevState) {
                return {
                    update: prevState.update + 1
                };
            });
        }
    }]);

    return DeveloperQuestion;
}(React.Component);