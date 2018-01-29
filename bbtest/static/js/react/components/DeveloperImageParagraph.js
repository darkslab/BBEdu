"use strict";

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

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
            confirmModal: false,
            isErrored: false
        };
        _this._$fileInput;
        _this._$xhr;
        _this._xhrData = [];
        _this._adoptCheckTimer;
        _this._adoptCheckTimerInterval = 2000;

        _this._boundFileInputChanged = _this._fileInputChanged.bind(_this);
        return _this;
    }

    _createClass(DeveloperImageParagraph, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            this._$fileInput = $("[data-bb-file-input]");
            if (this._$fileInput.length) {
                this._$fileInput.on("change", this._boundFileInputChanged);
            } else {
                this._$fileInput = undefined;
            }
        }
    }, {
        key: "componentWillUnmount",
        value: function componentWillUnmount() {
            if (this._$fileInput) {
                this._$fileInput.off("change", this._boundFileInputChanged);
                this._$fileInput = undefined;
            }
            if (this._$xhr) {
                this._$xhr.abort();
                this._$xhr = undefined;
                this._xhrData.pop();
            }
            clearTimeout(this._adoptCheckTimer);
        }
    }, {
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

            var label = null;
            if (this.props.data.status === "waiting" || this.state.isErrored) {
                var errorMessage = null;
                if (this.state.isErrored) {
                    errorMessage = React.createElement(
                        "p",
                        { className: "text-danger text-center" },
                        this.props.texts.paragraphsImageErrorImageParagraph
                    );
                }
                label = React.createElement(
                    React.Fragment,
                    null,
                    errorMessage,
                    React.createElement(
                        "label",
                        { htmlFor: uploadId,
                            className: "btn btn-success btn-lg btn-block mt-23",
                            "data-bb-non-sortable": true },
                        this.props.texts.paragraphsUploadButtonImageParagraph
                    )
                );
            } else if (this.props.data.status === "starting" || this.props.data.status === "uploading") {
                var labelStyle = {
                    width: this.props.data.progress + "%"
                };
                label = React.createElement(
                    "div",
                    { className: "bb-test-paragraph-progress progress progress-striped active mt-23",
                        "data-bb-non-sortable": true },
                    React.createElement("div", { className: "progress-bar", style: labelStyle })
                );
            } else if (this.props.data.status === "completing" || this.props.data.status === "adopting") {
                label = React.createElement(
                    "div",
                    { className: "mt-23 text-center" },
                    React.createElement("i", { className: "fa fa-fw fa-spin fa-refresh bb-test-paragraph-image-processing-icon",
                        "data-bb-non-sortable": true })
                );
            } else if (this.props.data.status === "staring") {
                label = React.createElement(
                    "p",
                    { className: "lead text-center mt-23 mb-0" },
                    this.props.texts.paragraphsImagePreviewImageParagraph
                );
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
                                label,
                                React.createElement("input", { id: uploadId,
                                    className: "hidden",
                                    type: "file",
                                    accept: "image/*",
                                    "data-bb-file-input": true })
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
    }, {
        key: "_fileInputChanged",
        value: function _fileInputChanged(event) {
            var $fileInput = $(event.currentTarget);
            if (!$fileInput[0].files.length || this._$xhr) {
                return;
            }

            this._$xhr = $.post({
                url: this.props.data.upload_start_url,
                headers: { "X-CSRFToken": Cookies.get("csrftoken") },
                data: {
                    file_name: $fileInput[0].files[0].name,
                    file_size: $fileInput[0].files[0].size,
                    file_type: $fileInput[0].files[0].type,
                    upload_starter: JSON.stringify({
                        name: "image_paragraph_upload_starter"
                    })
                },
                success: this._ajaxSuccess.bind(this, "starting"),
                error: this._ajaxError.bind(this, "starting")
            });
            this._xhrData.push({
                file: $fileInput[0].files[0]
            });

            this.setState({
                isErrored: false
            });
            this._changeStatus("starting");
        }
    }, {
        key: "_ajaxSuccess",
        value: function _ajaxSuccess(type, data, status, $xhr) {
            var xhrData = void 0;
            switch (type) {
                case "starting":
                    xhrData = this._xhrData.pop();
                    this._$xhr = $.ajax({
                        type: "PUT",
                        url: data.upload_url,
                        data: xhrData.file,
                        success: this._ajaxSuccess.bind(this, "uploading"),
                        error: this._ajaxError.bind(this, "uploading"),
                        xhr: function () {
                            var xhr = $.ajaxSettings.xhr();
                            if (xhr.upload) {
                                xhr.upload.addEventListener("progress", this._uploadProgress.bind(this), false);
                            }
                            return xhr;
                        }.bind(this),
                        cache: false,
                        contentType: false,
                        processData: false
                    });
                    this._xhrData.push({
                        complete_url: data.complete_url
                    });
                    this._changeStatus("uploading", 0);
                    break;
                case "uploading":
                    xhrData = this._xhrData.pop();
                    this._$xhr = $.post({
                        url: xhrData.complete_url,
                        headers: { "X-CSRFToken": Cookies.get("csrftoken") },
                        success: this._ajaxSuccess.bind(this, "completing"),
                        error: this._ajaxError.bind(this, "completing")
                    });
                    this._changeStatus("completing");
                    break;
                case "completing":
                    if (!data.success) {
                        this._errorOut();
                        return;
                    }
                    this._xhrData.push({
                        adopt_url: data.adopt_url
                    });
                    this._scheduleAdoptCheck();
                    this._changeStatus("adopting");
                    break;
                case "adopting":
                    if (!data.success) {
                        if (data.broken) {
                            this._errorOut();
                            return;
                        }
                        this._scheduleAdoptCheck();
                        return;
                    }
                    this._changeStatus("staring", data);
                    break;
            }
        }
    }, {
        key: "_ajaxError",
        value: function _ajaxError(type, $xhr, status, error) {
            if (status === "abort") {
                return;
            }
            this._errorOut();
        }
    }, {
        key: "_changeStatus",
        value: function _changeStatus(status, options) {
            var data = _extends({}, this.props.data);
            data.status = status;

            if (options) {
                switch (status) {
                    case "uploading":
                        data.progress = options;
                        break;
                    case "staring":
                        data.asset_uuid = options.asset_uuid;
                        data.asset_url = options.asset_url;
                        break;
                }
            }

            var skipSave = true;
            if (data.status === "staring") {
                skipSave = false;
            }

            this.props.onChange(data, skipSave);
        }
    }, {
        key: "_uploadProgress",
        value: function _uploadProgress(event) {
            if (!event.lengthComputable) {
                return;
            }
            if (this.props.data.status !== "uploading") {
                return;
            }
            this._changeStatus("uploading", Math.min(Math.round(event.loaded / event.total * 100), 100));
        }
    }, {
        key: "_scheduleAdoptCheck",
        value: function _scheduleAdoptCheck() {
            clearTimeout(this._adoptCheckTimer);
            this._adoptCheckTimer = setTimeout(function () {
                var xhrData = this._xhrData.pop();
                this._$xhr = $.post({
                    url: xhrData.adopt_url,
                    headers: { "X-CSRFToken": Cookies.get("csrftoken") },
                    data: {
                        data: JSON.stringify({
                            monkey: "shmonkey!"
                        })
                    },
                    success: this._ajaxSuccess.bind(this, "adopting"),
                    error: this._ajaxError.bind(this, "adopting")
                });
                this._xhrData.push({
                    adopt_url: xhrData.adopt_url
                });
            }.bind(this), this._adoptCheckTimerInterval);
        }
    }, {
        key: "_errorOut",
        value: function _errorOut() {
            this.setState({
                isErrored: true
            });
            this._$xhr = undefined;
            this._xhrData.pop();

            var data = _extends({}, this.props.data);
            data.progress = 0;
            this.props.onChange(data, true);
        }
    }]);

    return DeveloperImageParagraph;
}(React.Component);