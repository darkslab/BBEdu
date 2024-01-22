class DeveloperPeriodicTableParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            confirmModal: false
        };
    }
    render() {
        let paragraphClassName = "form-group bb-test-section-movable";

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

        let sharedLabel = null;
        if (this.props.sharedQuestionIds.length > 0) {
            sharedLabel = (
                <p className="text-danger pull-left mb-0">{this.props.texts.paragraphsSharedLabelTextParagraph}</p>
            );
            paragraphClassName += " bb-test-section-background-shared";
        } else {
            paragraphClassName += " bb-test-section-background";
        }

        // let textareaClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
        // if (!this.props.data.text) {
        //     textareaClassName += " bb-test-paragraph-textarea-empty";
        // }

        let modal = null;
        if (this.state.confirmModal) {
            modal = (
                <ConfirmModal title={this.props.texts.deleteModalTitle}
                              yesCaption={this.props.texts.deleteModalYesCaption}
                              noCaption={this.props.texts.deleteModalNoCaption}
                              isInverse={true}
                              complete={this._completeModal.bind(this)} />
            );
        }
        console.log("this.props", this.props)
        return (
            <React.Fragment>
                {modal}
                <div className={paragraphClassName} data-paragraph-id={this.props.paragraphId}>
                    <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                        {sharedLabel}
                        {buttons}
                        <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                    </div>
                    
                </div>
                <div>
                    <img class="periodicTableThumbnail" src={this.props.data.periodicTableUrl} width="100px" alt="PeriodicTableThumbnail" onClick={this._openOverlay.bind(this)}></img>

                    <div id="periodicTableOverlay" class="periodicTableOverlay" onClick={this._closeOverlay.bind(this)}>
                        <img id="overlayPeriodicTableImage" src="" alt="PeriodicTableLarge"></img>
                    </div>
                </div>
            </React.Fragment>
        );
    }

    _openOverlay() {
        // console.log("_openOverlay", document.getElementById('overlayImage'));
        document.getElementById('overlayPeriodicTableImage').src = this.props.data.periodicTableUrl;
        document.getElementById('periodicTableOverlay').style.display = 'flex';
    }

    _closeOverlay() {
        document.getElementById('periodicTableOverlay').style.display = 'none';
    }

    // _handleChange(event) {
    //     this.props.onChange({
    //         ...this.props.data,
    //         text: event.target.value
    //     });
    // }
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
