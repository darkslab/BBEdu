"use strict";

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _objectWithoutProperties(obj, keys) { var target = {}; for (var i in obj) { if (keys.indexOf(i) >= 0) continue; if (!Object.prototype.hasOwnProperty.call(obj, i)) continue; target[i] = obj[i]; } return target; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperSplitTextParagraph = function (_React$Component) {
    _inherits(DeveloperSplitTextParagraph, _React$Component);

    function DeveloperSplitTextParagraph(props) {
        _classCallCheck(this, DeveloperSplitTextParagraph);

        var _this = _possibleConstructorReturn(this, (DeveloperSplitTextParagraph.__proto__ || Object.getPrototypeOf(DeveloperSplitTextParagraph)).call(this, props));

        _this.state = {
            confirmModal: false
        };
        return _this;
    }

    _createClass(DeveloperSplitTextParagraph, [{
        key: "render",
        value: function render() {
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

            var leftClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
            if (!this.props.data.left.text) {
                leftClassName += " bb-test-paragraph-textarea-empty";
            }
            var rightClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
            if (!this.props.data.right.text) {
                rightClassName += " bb-test-paragraph-textarea-empty";
            }

            var modal = null;
            if (this.state.confirmModal) {
                modal = React.createElement(ConfirmModal, { title: this.props.texts.deleteModalTitle,
                    yesCaption: this.props.texts.deleteModalYesCaption,
                    noCaption: this.props.texts.deleteModalNoCaption,
                    isInverse: true,
                    complete: this._completeModal.bind(this) });
            }

            return React.createElement(
                React.Fragment,
                null,
                modal,
                React.createElement(
                    "div",
                    { className: "form-group bb-test-section-movable bb-test-section-background", "data-paragraph-id": this.props.paragraphId },
                    React.createElement(
                        "div",
                        { className: "pt-5 pr-5 pb-5 pl-5 clearfix" },
                        buttons,
                        React.createElement(
                            "button",
                            { type: "button", className: "btn btn-default btn-xs pull-right ml-5 invisible" },
                            "Spacer"
                        )
                    ),
                    React.createElement(
                        "div",
                        { className: "row" },
                        React.createElement(
                            "div",
                            { className: "col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2" },
                            React.createElement(
                                "div",
                                { className: "row" },
                                React.createElement(
                                    "div",
                                    { className: "col-xs-6 pr-5" },
                                    React.createElement(
                                        "h5",
                                        { className: "text-center mt-0 mb-10" },
                                        React.createElement(
                                            "em",
                                            null,
                                            this.props.texts.columnACaption
                                        )
                                    ),
                                    React.createElement("textarea", { className: leftClassName,
                                        placeholder: this.props.texts.paragraphTextareaPlaceholder,
                                        value: this.props.data.left.text,
                                        onChange: this._handleChange.bind(this, "left") })
                                ),
                                React.createElement(
                                    "div",
                                    { className: "col-xs-6 pl-5" },
                                    React.createElement(
                                        "h5",
                                        { className: "text-center mt-0 mb-10" },
                                        React.createElement(
                                            "em",
                                            null,
                                            this.props.texts.columnBCaption
                                        )
                                    ),
                                    React.createElement("textarea", { className: rightClassName,
                                        placeholder: this.props.texts.paragraphTextareaPlaceholder,
                                        value: this.props.data.right.text,
                                        onChange: this._handleChange.bind(this, "right") })
                                )
                            )
                        )
                    )
                )
            );
        }
    }, {
        key: "_handleChange",
        value: function _handleChange(side, event) {
            var data = _extends({}, this.props.data);
            data.left = _extends({}, data.left);
            data.right = _extends({}, data.right);
            switch (side) {
                case "left":
                case "right":
                    data[side].text = event.target.value;
                    break;
            }
            this.props.onChange(data);
        }
    }, {
        key: "_handleFormulas",
        value: function _handleFormulas() {
            var _props$data = this.props.data,
                has_formulas = _props$data.has_formulas,
                data = _objectWithoutProperties(_props$data, ["has_formulas"]);

            data.left = _extends({}, this.props.data.left);
            data.right = _extends({}, this.props.data.right);
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

    return DeveloperSplitTextParagraph;
}(React.Component);