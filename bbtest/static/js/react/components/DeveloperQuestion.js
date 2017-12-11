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
            difficulty: _this.props.object.difficulty(),
            taxonomy: _this.props.object.taxonomy(),
            topic: _this.props.object.topic()
        };
        return _this;
    }

    _createClass(DeveloperQuestion, [{
        key: "render",
        value: function render() {
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
                                value: this.state.difficulty,
                                data: this.props.attributes.difficulties,
                                change: this._attributeChange.bind(this, "difficulty") }),
                            React.createElement(DeveloperAttribute, { label: this.props.texts.taxonomy,
                                value: this.state.taxonomy,
                                data: this.props.attributes.taxonomies,
                                change: this._attributeChange.bind(this, "taxonomy") }),
                            React.createElement(DeveloperAttribute, { label: this.props.texts.topic,
                                value: this.state.topic,
                                data: this.props.attributes.topics,
                                change: this._attributeChange.bind(this, "topic") })
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
                    this.setState({
                        difficulty: value
                    });
                    break;
                case "taxonomy":
                    this.props.object.setTaxonomy(value);
                    this.setState({
                        taxonomy: value
                    });
                    break;
                case "topic":
                    this.props.object.setTopic(value);
                    this.setState({
                        topic: value
                    });
                    break;
            }
        }
    }]);

    return DeveloperQuestion;
}(React.Component);