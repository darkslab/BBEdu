class DeveloperTextParagraph extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        let buttons = [];
        {/*
        <button type="button" class="btn btn-danger btn-xs pull-right ml-5">Formulas Off</button>
        */}

        let className = "form-control bb-test-paragraph bb-test-paragraph-textarea";
        if (!this.props.data.text) {
            className += " bb-test-paragraph-textarea-empty";
        }

        return (
            <div className="form-group bb-test-section-movable bb-test-section-background">
                <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                    {buttons}
                    <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                </div>
                <textarea className={className}
                          placeholder={this.props.placeholder}
                          value={this.props.data.text}
                          onChange={this._handleChange.bind(this)} />
            </div>
        );
    }
    _handleChange(event) {
        this.props.data.text = event.target.value;
        this.props.onChange(this.props.data);
    }
}
