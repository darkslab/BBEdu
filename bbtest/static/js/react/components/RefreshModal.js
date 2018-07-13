"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var RefreshModal = function (_React$Component) {
    _inherits(RefreshModal, _React$Component);

    function RefreshModal(props) {
        _classCallCheck(this, RefreshModal);

        return _possibleConstructorReturn(this, (RefreshModal.__proto__ || Object.getPrototypeOf(RefreshModal)).call(this, props));
    }

    _createClass(RefreshModal, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            var modal = $("[data-modal]");
            if (modal.length) {
                modal.modal({
                    backdrop: "static",
                    keyboard: false
                });
            }
        }
    }, {
        key: "render",
        value: function render() {
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
                            { className: "modal-body" },
                            React.createElement(
                                "p",
                                { className: "lead mt-15 mb-0 text-center" },
                                this.props.message
                            )
                        ),
                        React.createElement(
                            "div",
                            { className: "modal-footer" },
                            React.createElement(
                                "div",
                                { className: "text-center" },
                                React.createElement(
                                    "a",
                                    { href: this.props.refreshUrl, className: "btn btn-primary" },
                                    this.props.refreshCaption
                                ),
                                React.createElement(
                                    "a",
                                    { href: this.props.cancelUrl, className: "btn btn-default" },
                                    this.props.cancelCaption
                                )
                            )
                        )
                    )
                )
            );
        }
    }]);

    return RefreshModal;
}(React.Component);