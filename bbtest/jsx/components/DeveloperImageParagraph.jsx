class DeveloperImageParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            confirmModal: false,
            isErrored: false
        };
        this._$fileInput;
        this._$xhr;
        this._xhrData = [];
        this._adoptCheckTimer;
        this._adoptCheckTimerInterval = 2000;

        this._boundFileInputChanged = this._fileInputChanged.bind(this);
    }
    componentDidMount() {
        this._$fileInput = $("[data-bb-file-input]");
        if (this._$fileInput.length) {
            this._$fileInput.on("change", this._boundFileInputChanged);
        } else {
            this._$fileInput = undefined;
        }
    }
    componentWillUnmount () {
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
    render() {
        const uploadId = "upload_" + this.props.paragraphId;

        let buttons = [];
        if (this.props.canDelete) {
            buttons.push(
                <button key="delete"
                        type="button"
                        className="btn btn-danger btn-xs pull-right ml-5"
                        onClick={this._renderModal.bind(this)}>
                    <i className="fa fa-fw fa-times"></i>
                </button>
            );
        }

        let modal = null;
        if (this.state.confirmModal) {
            modal = (
                <DeveloperDeleteConfirmModal title={this.props.texts.deleteModalTitle}
                                             yesCaption={this.props.texts.deleteModalYesCaption}
                                             noCaption={this.props.texts.deleteModalNoCaption}
                                             isInverse={true}
                                             complete={this._completeModal.bind(this)} />
            );
        }

        let label = null;
        if (this.props.data.status === "waiting" || this.state.isErrored) {
            let errorMessage = null;
            if (this.state.isErrored) {
                errorMessage = (
                    <p className="text-danger text-center">{this.props.texts.paragraphsImageErrorImageParagraph}</p>
                );
            }
            label = (
                <React.Fragment>
                    {errorMessage}
                    <label htmlFor={uploadId}
                           className="btn btn-success btn-lg btn-block mt-23"
                           data-bb-non-sortable>{this.props.texts.paragraphsUploadButtonImageParagraph}</label>
                </React.Fragment>
            );
        } else if (this.props.data.status === "starting" || this.props.data.status === "uploading") {
            let labelStyle = {
                width: this.props.data.progress + "%"
            };
            label = (
                <div className="bb-test-paragraph-progress progress progress-striped active mt-23"
                     data-bb-non-sortable>
                    <div className="progress-bar" style={labelStyle} />
                </div>
            );
        } else if (this.props.data.status === "completing" || this.props.data.status === "adopting") {
            let labelStyle = {
                fontSize: "56px"
            };
            label = (
                <div className="mt-23 text-center">
                    <i className="fa fa-fw fa-spin fa-refresh"
                       style={labelStyle}
                       data-bb-non-sortable />
                </div>
            );
        } else if (this.props.data.status === "staring") {
            label = (
                <p className="lead text-center mt-23 mb-0">{this.props.texts.paragraphsImagePreviewImageParagraph}</p>
            );
        }

        return (
            <React.Fragment>
                {modal}
                <div className="form-group bb-test-section-movable bb-test-section-background" data-paragraph-id={this.props.paragraphId}>
                    <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                        {buttons}
                        <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                    </div>
                    <div className="bb-test-paragraph bb-test-paragraph-upload">
                        <div className="row">
                            <div className="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                                {label}
                                <input id={uploadId} className="hidden" type="file" data-bb-file-input />
                            </div>
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }

    _renderModal() {
        this.setState({
            confirmModal: true
        });
    }
    _completeModal(data) {
        if (data) {
            this.props.onDelete();
        } else {
            this.setState({
                confirmModal: false
            });
        }
    }
    _fileInputChanged(event) {
        let $fileInput = $(event.currentTarget);
        if (!$fileInput[0].files.length || this._$xhr) {
            return;
        }

        this._$xhr = $.post({
            url: this.props.data.upload_start_url,
            headers: {"X-CSRFToken": Cookies.get("csrftoken")},
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
    _ajaxSuccess(type, data, status, $xhr) {
        let xhrData;
        switch (type) {
            case "starting":
                xhrData = this._xhrData.pop();
                this._$xhr = $.ajax({
                    type: "PUT",
                    url: data.upload_url,
                    data: xhrData.file,
                    success: this._ajaxSuccess.bind(this, "uploading"),
                    error: this._ajaxError.bind(this, "uploading"),
                    xhr: function() {
                        let xhr = $.ajaxSettings.xhr();
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
                    headers: {"X-CSRFToken": Cookies.get("csrftoken")},
                    success: this._ajaxSuccess.bind(this, "completing"),
                    error: this._ajaxError.bind(this, "completing"),
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
    _ajaxError(type, $xhr, status, error) {
        if (status === "abort") {
            return;
        }
        this._errorOut();
    }
    _changeStatus(status, options) {
        let data = {...this.props.data};
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

        let skipSave = true;
        if (data.status === "staring") {
            skipSave = false;
        }

        this.props.onChange(data, skipSave);
    }
    _uploadProgress(event) {
        if (!event.lengthComputable) {
            return;
        }
        if (this.props.data.status !== "uploading") {
            return;
        }
        this._changeStatus("uploading", Math.min(Math.round(event.loaded / event.total * 100), 100));
    }
    _scheduleAdoptCheck() {
        clearTimeout(this._adoptCheckTimer);
        this._adoptCheckTimer = setTimeout(function() {
            let xhrData = this._xhrData.pop();
            this._$xhr = $.post({
                url: xhrData.adopt_url,
                headers: {"X-CSRFToken": Cookies.get("csrftoken")},
                data: {
                    data: JSON.stringify({
                        monkey: "shmonkey!"
                    })
                },
                success: this._ajaxSuccess.bind(this, "adopting"),
                error: this._ajaxError.bind(this, "adopting"),
            });
            this._xhrData.push({
                adopt_url: xhrData.adopt_url
            });
        }.bind(this), this._adoptCheckTimerInterval);
    }
    _errorOut() {
        this.setState({
            isErrored: true
        });
        this._$xhr = undefined;
        this._xhrData.pop();

        let data = {...this.props.data};
        data.progress = 0;
        this.props.onChange(data, true);
    }
}
