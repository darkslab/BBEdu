class DeveloperSplitTextParagraph extends React.Component {
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
            <button key="formulas"
                    type="button"
                    className={"btn btn-xs pull-right ml-5" + (this.props.data.has_formulas ? " btn-success active" : " btn-default")}
                    onClick={this._handleFormulas.bind(this)}>{this.props.texts.controlFormulasButton}</button>
        );

        let leftClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
        if (!this.props.data.left.text) {
            leftClassName += " bb-test-paragraph-textarea-empty";
        }
        let rightClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
        if (!this.props.data.right.text) {
            rightClassName += " bb-test-paragraph-textarea-empty";
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

        return (
            <React.Fragment>
                {modal}
                <div className="form-group bb-test-section-movable bb-test-section-background" data-paragraph-id={this.props.paragraphId}>
                    <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                        {buttons}
                        <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                    </div>
                    <div className="row">
                        <div className="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                            <div className="row">
                                <div className="col-xs-6 pr-5">
                                    <h5 className="text-center mt-0 mb-10"><em>{this.props.texts.columnACaption}</em></h5>
                                    <textarea className={leftClassName}
                                              placeholder={this.props.texts.paragraphTextareaPlaceholder}
                                              value={this.props.data.left.text}
                                              onChange={this._handleChange.bind(this, "left")} />
                                </div>
                                <div className="col-xs-6 pl-5">
                                    <h5 className="text-center mt-0 mb-10"><em>{this.props.texts.columnBCaption}</em></h5>
                                    <textarea className={rightClassName}
                                              placeholder={this.props.texts.paragraphTextareaPlaceholder}
                                              value={this.props.data.right.text}
                                              onChange={this._handleChange.bind(this, "right")} />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
    _handleChange(side, event) {
        let data = {...this.props.data};
        data.left = {...data.left};
        data.right = {...data.right};
        switch (side) {
            case "left":
            case "right":
                data[side].text = event.target.value;
                break;
        }
        this.props.onChange(data);
    }
    _handleFormulas() {
        let { has_formulas, ...data } = this.props.data;
        data.left = {...this.props.data.left};
        data.right = {...this.props.data.right};
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
