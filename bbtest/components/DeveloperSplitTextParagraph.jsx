class DeveloperSplitTextParagraph extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        let buttons = [];
        buttons.push(
            <button key="delete"
                    type="button"
                    className="btn btn-danger btn-xs pull-right ml-5"
                    onClick={this.props.onDelete}>
                <i className="fa fa-fw fa-times"></i>
            </button>
        );

        let leftClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
        if (!this.props.data.left.text) {
            leftClassName += " bb-test-paragraph-textarea-empty";
        }
        let rightClassName = "form-control bb-test-paragraph bb-test-paragraph-textarea";
        if (!this.props.data.right.text) {
            rightClassName += " bb-test-paragraph-textarea-empty";
        }

        return (
            <div className="form-group bb-test-section-movable bb-test-section-background" data-paragraph-id={this.props.paragraphId}>
                <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                    {buttons}
                    <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                </div>
                <div className="row">
                    <div className="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                        <div className="row">
                            <div className="col-xs-6 pr-5">
                                <textarea className={leftClassName}
                                          placeholder={this.props.texts.paragraphTextareaPlaceholder}
                                          value={this.props.data.left.text}
                                          onChange={this._handleChange.bind(this, "left")} />
                            </div>
                            <div className="col-xs-6 pl-5">
                                <textarea className={rightClassName}
                                          placeholder={this.props.texts.paragraphTextareaPlaceholder}
                                          value={this.props.data.right.text}
                                          onChange={this._handleChange.bind(this, "right")} />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
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
}
