"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DeveloperSelectorModal = function (_React$Component) {
    _inherits(DeveloperSelectorModal, _React$Component);

    function DeveloperSelectorModal(props) {
        _classCallCheck(this, DeveloperSelectorModal);

        var _this = _possibleConstructorReturn(this, (DeveloperSelectorModal.__proto__ || Object.getPrototypeOf(DeveloperSelectorModal)).call(this, props));

        _this._$modal;
        _this._selectedClass;

        _this._boundModalHidden = _this._modalHidden.bind(_this);
        return _this;
    }

    _createClass(DeveloperSelectorModal, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            this._$modal = $("[data-modal]");
            if (this._$modal.length) {
                this._$modal.modal();
                this._$modal.on("hidden.bs.modal", this._boundModalHidden);
            } else {
                this._$modal = undefined;
            }
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            if (this._$modal) {
                this._$modal.off("hidden.bs.modal", this._boundModalHidden);
                this._$modal = undefined;
            }
        }
    }, {
        key: "render",
        value: function render() {
            var buttons = [];
            for (var i = 0; i < this.props.classData.length; i++) {
                buttons.push(React.createElement(
                    "div",
                    { key: i, className: "col-xs-12 col-sm-10 col-sm-offset-1 mb-10" },
                    React.createElement(
                        "button",
                        { type: "button",
                            className: "btn btn-primary btn-block btn-lg",
                            onClick: this._chooseClass.bind(this, this.props.classData[i].class) },
                        this.props.classData[i].caption
                    )
                ));
            }

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
                                "button",
                                { type: "button", className: "close", "data-dismiss": "modal" },
                                "\xD7"
                            ),
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
                                buttons
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
            this.props.complete(this._selectedClass);
        }
    }, {
        key: "_chooseClass",
        value: function _chooseClass(selectedClass) {
            this._selectedClass = selectedClass;
            this._$modal.modal("hide");
        }
    }]);

    return DeveloperSelectorModal;
}(React.Component);