"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperDeleteConfirmModal = function (_React$Component) {
    _inherits(DeveloperDeleteConfirmModal, _React$Component);

    function DeveloperDeleteConfirmModal(props) {
        _classCallCheck(this, DeveloperDeleteConfirmModal);

        var _this = _possibleConstructorReturn(this, (DeveloperDeleteConfirmModal.__proto__ || Object.getPrototypeOf(DeveloperDeleteConfirmModal)).call(this, props));

        _this._$modal;
        _this._result;
        return _this;
    }

    _createClass(DeveloperDeleteConfirmModal, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            this._$modal = $("[data-modal]");
            if (this._$modal.length) {
                this._$modal.modal({
                    backdrop: "static",
                    keyboard: false
                });
                this._$modal.on("hidden.bs.modal", this._modalHidden.bind(this));
            } else {
                this._$modal = undefined;
            }
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            if (this._$modal) {
                this._$modal.off("hidden.bs.modal", this._modalHidden.bind(this));
                this._$modal = undefined;
            }
        }
    }, {
        key: "render",
        value: function render() {
            var yesClassName = "btn btn-block btn-lg";
            yesClassName += this.props.isInverse ? " btn-danger" : " btn-primary";

            var noClassName = "btn btn-block btn-lg";
            noClassName += this.props.isInverse ? " btn-primary" : " btn-danger";

            return React.createElement(
                "div",
                { className: "modal fade", "data-modal": true },
                React.createElement(
                    "div",
                    { className: "modal-dialog" },
                    React.createElement(
                        "div",
                        { className: "modal-content" },
                        React.createElement(
                            "div",
                            { className: "modal-header" },
                            React.createElement(
                                "h4",
                                { className: "modal-title" },
                                this.props.title
                            )
                        ),
                        React.createElement(
                            "div",
                            { className: "modal-body" },
                            React.createElement(
                                "div",
                                { className: "row" },
                                React.createElement(
                                    "div",
                                    { className: "col-xs-6 col-sm-5 col-sm-offset-1" },
                                    React.createElement(
                                        "button",
                                        { type: "button",
                                            className: yesClassName,
                                            onClick: this._chooseResult.bind(this, true) },
                                        this.props.yesCaption
                                    )
                                ),
                                React.createElement(
                                    "div",
                                    { className: "col-xs-6 col-sm-5" },
                                    React.createElement(
                                        "button",
                                        { type: "button",
                                            className: noClassName,
                                            onClick: this._chooseResult.bind(this, false) },
                                        this.props.noCaption
                                    )
                                )
                            )
                        ),
                        React.createElement("div", { className: "modal-footer" })
                    )
                )
            );
        }
    }, {
        key: "_modalHidden",
        value: function _modalHidden() {
            this.props.complete(this._result);
        }
    }, {
        key: "_chooseResult",
        value: function _chooseResult(result) {
            this._result = result;
            this._$modal.modal("hide");
        }
    }]);

    return DeveloperDeleteConfirmModal;
}(React.Component);