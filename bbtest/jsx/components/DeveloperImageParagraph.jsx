class DeveloperImageParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            confirmModal: false
        };
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
                                <label htmlFor={uploadId} className="btn btn-success btn-lg btn-block mt-23">{this.props.texts.paragraphsUploadButtonImageParagraph}</label>
                                <input id={uploadId} className="hidden" type="file" />
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
}
