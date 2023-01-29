class DeveloperSolutionTextParagraph extends React.Component {
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
        buttons.push(
            <button key="formulas"
                    type="button"
                    className={"btn btn-xs pull-right ml-5" + (this.props.data.has_formulas ? " btn-success active" : " btn-default")}
                    onClick={this._handleFormulas.bind(this)}>{this.props.texts.controlFormulasButton}</button>
        );

        let sharedLabel = null;
        if (this.props.sharedQuestionIds.length > 0) {
            sharedLabel = (
                <p className="text-danger pull-left mb-0">{this.props.texts.paragraphsSharedLabelTextParagraph + "ssdd"}</p>
            );
            paragraphClassName += " bb-test-section-background-shared";
        } else {
            paragraphClassName += " bb-test-section-background";
        }

        let textareaClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
        if (!this.props.data.text) {
            textareaClassName += " bb-test-paragraph-textarea-empty";
        }

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
        console.log("ans0", this.props);
        // console.log("dd1", this.props.data);

        return (
            <React.Fragment>
                {modal}
                <div className={paragraphClassName} data-paragraph-id={this.props.paragraphId}>
                    <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                        {sharedLabel}
                        {buttons}
                        <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                    </div>
                    <textarea className={textareaClassName}
                              placeholder={this.props.texts.paragraphSolutionTextareaPlaceholder}
                              value={this.props.data.text+"_test"}
                              onChange={this._handleChange.bind(this)}
                               />
                </div>
                <div><p>Dimas answer</p></div>
            </React.Fragment>
        );
    }
    _handleChange(event) {
        this.props.onChange({
            ...this.props.data,
            text: event.target.value
        });
    }
    _handleFormulas() {
        let { has_formulas, ...data } = this.props.data;
        if (has_formulas === undefined) {
            data.has_formulas = true;
        }
        this.props.onChange(data);
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
