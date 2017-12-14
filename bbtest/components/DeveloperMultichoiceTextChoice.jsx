class DeveloperMultichoiceTextChoice extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        let buttons = [];
        // <button type="button" className="btn btn-success btn-xs pull-right ml-5">Formulas On</button>
        // <button type="button" className="btn btn-danger btn-xs pull-right ml-5">Incorrect Answer</button>

        return (
            <div className="form-group bb-test-section-movable bb-test-section-background" data-choice-id={this.props.choiceId}>
                <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                    {buttons}
                    <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                </div>
                <div className="row">
                    <div className="col-xs-2 col-sm-3 pr-0"></div>
                    <div className="col-xs-10 col-sm-7 pl-0">
                        <textarea className="form-control bb-test-answer bb-test-answer-textarea"
                                  placeholder={this.props.texts.choiceTextareaPlaceholder}
                                  value={this.props.data.text}
                                  onChange={this._handleChange.bind(this)} />
                    </div>
                </div>
            </div>
        );
    }
    _handleChange(event) {
        this.props.onChange({
            ...this.props.data,
            text: event.target.value
        });
    }
}
