"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperImageParagraph = function (_React$Component) {
    _inherits(DeveloperImageParagraph, _React$Component);

    function DeveloperImageParagraph(props) {
        _classCallCheck(this, DeveloperImageParagraph);

        var _this = _possibleConstructorReturn(this, (DeveloperImageParagraph.__proto__ || Object.getPrototypeOf(DeveloperImageParagraph)).call(this, props));

        _this.state = {
            confirmModal: false
        };
        return _this;
    }

    _createClass(DeveloperImageParagraph, [{
        key: "render",
        value: function render() {
            var uploadId = "upload_" + this.props.paragraphId;

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

            var modal = null;
            if (this.state.confirmModal) {
                modal = React.createElement(DeveloperDeleteConfirmModal, { title: this.props.texts.deleteModalTitle,
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
                        { className: "bb-test-paragraph bb-test-paragraph-upload" },
                        React.createElement(
                            "div",
                            { className: "row" },
                            React.createElement(
                                "div",
                                { className: "col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3" },
                                React.createElement(
                                    "label",
                                    { htmlFor: uploadId, className: "btn btn-success btn-lg btn-block mt-23" },
                                    this.props.texts.paragraphsUploadButtonImageParagraph
                                ),
                                React.createElement("input", { id: uploadId, className: "hidden", type: "file" })
                            )
                        )
                    )
                )
            );
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

    return DeveloperImageParagraph;
}(React.Component);