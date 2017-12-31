class DeveloperMultichoiceTextChoice extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            confirmModal: false
        };
    }
    render() {
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
        buttons.push(
            <button key="chosen"
                    type="button"
                    className={"btn btn-default btn-xs pull-right ml-5" + (this.props.chosen ? " active" : "")}
                    onClick={this.props.onSelect.bind(null, !this.props.chosen)}>{this.props.texts.answerChoiceSelectButton}</button>
        );
        if (this.props.chosen) {
            buttons.push(
                <button disabled
                        key="solution"
                        type="button"
                        className="btn btn-primary btn-xs pull-right ml-5">{this.props.texts.answerChoiceSolutionButton}</button>
            );
        }

        let className = "form-control bb-test-answer bb-test-answer-textarea";
        if (!this.props.data.text) {
            className += " bb-test-answer-textarea-empty";
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
                <div className="form-group bb-test-section-movable bb-test-section-background" data-choice-id={this.props.choiceId}>
                    <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                        {buttons}
                        <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                    </div>
                    <div className="row">
                        <div className="col-xs-2 col-sm-3 pr-0"></div>
                        <div className="col-xs-10 col-sm-7 pl-0">
                            <textarea className={className}
                                      placeholder={this.props.texts.choiceTextareaPlaceholder}
                                      value={this.props.data.text}
                                      onChange={this._handleChange.bind(this)}
                                      readOnly={this.props.canEdit ? false : true} />
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
    _handleChange(event) {
        this.props.onChange({
            ...this.props.data,
            text: event.target.value
        });
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
