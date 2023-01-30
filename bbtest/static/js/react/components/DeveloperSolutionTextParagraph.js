"use strict";

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _objectWithoutProperties(obj, keys) { var target = {}; for (var i in obj) { if (keys.indexOf(i) >= 0) continue; if (!Object.prototype.hasOwnProperty.call(obj, i)) continue; target[i] = obj[i]; } return target; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperSolutionTextParagraph = function (_React$Component) {
    _inherits(DeveloperSolutionTextParagraph, _React$Component);

    function DeveloperSolutionTextParagraph(props) {
        _classCallCheck(this, DeveloperSolutionTextParagraph);

        var _this = _possibleConstructorReturn(this, (DeveloperSolutionTextParagraph.__proto__ || Object.getPrototypeOf(DeveloperSolutionTextParagraph)).call(this, props));

        _this.state = {
            confirmModal: false
        };
        return _this;
    }

    _createClass(DeveloperSolutionTextParagraph, [{
        key: "render",
        value: function render() {
            var paragraphClassName = "form-group bb-test-section-movable";

            var buttons = [];
            if (this.props.canDelete) {
                buttons.push(React.createElement(
                    "button",
                    { key: "delete",
                        type: "button",
                        className: "btn btn-danger btn-xs pull-right ml-5",
                        onClick: this._renderModal.bind(this) },
                    React.createElement("i", { className: "fa fa-fw fa-times" })
                ));
            }
            buttons.push(React.createElement(
                "button",
                { key: "formulas",
                    type: "button",
                    className: "btn btn-xs pull-right ml-5" + (this.props.data.has_formulas ? " btn-success active" : " btn-default"),
                    onClick: this._handleFormulas.bind(this) },
                this.props.texts.controlFormulasButton
            ));

            var sharedLabel = null;
            if (this.props.sharedQuestionIds.length > 0) {
                sharedLabel = React.createElement(
                    "p",
                    { className: "text-danger pull-left mb-0" },
                    this.props.texts.paragraphsSharedLabelTextParagraph + "ssdd"
                );
                paragraphClassName += " bb-test-section-background-shared";
            } else {
                paragraphClassName += " bb-test-section-background-solution";
            }

            var textareaClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea-solution";
            if (!this.props.data.text) {
                textareaClassName += " bb-test-paragraph-textarea-empty";
            }

            var modal = null;
            if (this.state.confirmModal) {
                modal = React.createElement(ConfirmModal, { title: this.props.texts.deleteModalTitle,
                    yesCaption: this.props.texts.deleteModalYesCaption,
                    noCaption: this.props.texts.deleteModalNoCaption,
                    isInverse: true,
                    complete: this._completeModal.bind(this) });
            }
            // console.log("ans0", this.props);
            // console.log("dd1", this.props.data);

            return React.createElement(
                React.Fragment,
                null,
                modal,
                React.createElement(
                    "div",
                    { className: paragraphClassName, "data-paragraph-id": this.props.paragraphId },
                    React.createElement(
                        "div",
                        { className: "pt-5 pr-5 pb-5 pl-5 clearfix" },
                        React.createElement(
                            "span",
                            null,
                            this.props.texts.solution
                        ),
                        sharedLabel,
                        buttons,
                        React.createElement(
                            "button",
                            { type: "button", className: "btn btn-default btn-xs pull-right ml-5 invisible" },
                            "Spacer"
                        )
                    ),
                    React.createElement("textarea", { className: textareaClassName,
                        placeholder: this.props.texts.paragraphSolutionTextareaPlaceholder,
                        value: this.props.data.text,
                        onChange: this._handleChange.bind(this)
                    })
                )
            );
        }
    }, {
        key: "_handleChange",
        value: function _handleChange(event) {
            this.props.onChange(_extends({}, this.props.data, {
                text: event.target.value
            }));
        }
    }, {
        key: "_handleFormulas",
        value: function _handleFormulas() {
            var _props$data = this.props.data,
                has_formulas = _props$data.has_formulas,
                data = _objectWithoutProperties(_props$data, ["has_formulas"]);

            if (has_formulas === undefined) {
                data.has_formulas = true;
            }
            this.props.onChange(data);
        }
    }, {
        key: "_renderModal",
        value: function _renderModal() {
            this.setState({
                confirmModal: true
            });
        }
    }, {
        key: "_completeModal",
        value: function _completeModal(data) {
            if (data) {
                this.props.onDelete();
            } else {
                this.setState({
                    confirmModal: false
                });
            }
        }
    }]);

    return DeveloperSolutionTextParagraph;
}(React.Component);