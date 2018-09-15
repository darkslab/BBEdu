class TextParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            originalText: "",
            rawHtml: ""
        };
        this._processor;
    }
    componentDidMount() {
        if (!this.props.data.has_formulas) {
            return;
        }
        this._setupProcessor();
    }
    componentWillUnmount() {
        if (this._processor) {
            this._processor.stop();
        }
    }
    componentDidUpdate() {
        if (this._processor || !this.props.data.has_formulas) {
            return;
        }
        if (this.props.data.text !== this.state.originalText) {
            this._setupProcessor();
        }
    }
    render() {
        let content = null;
        let className = "bb-test-paragraph";
        let sharedAddon = null;

        if (this.props.isShared) {
            className += " bb-test-paragraph-shared";
            sharedAddon = (
                <h5 className="text-center mt-0 mb-5"><em>{this.props.texts.sharedTitleTextParagraph}</em></h5>
            );
        }

        if (!this.props.data.text) {
            let _content = null;
            if (this.props.forDevelopers) {
                className += " bb-placeholder";
                _content = this.props.texts.paragraphEmptyPlaceholder;
            }
            content = (
                <React.Fragment>
                    {sharedAddon}
                    <div className={className}>{_content}</div>
                </React.Fragment>
            );
        } else if (this.props.data.has_formulas) {
            content = (
                <React.Fragment>
                    {sharedAddon}
                    <div className={className}
                         dangerouslySetInnerHTML={{ __html: this.state.rawHtml }}></div>
                </React.Fragment>
            );
        } else {
            content = (
                <React.Fragment>
                    {sharedAddon}
                    <div className={className}>{SimpleFormattedFragment(this.props.data.text)}</div>
                </React.Fragment>
            );
        }

        return content;
    }

    _setupProcessor() {
        this._processor = new KatexAsyncProcessor(this._doneProcessing.bind(this), this.props.data.text);
    }
    _doneProcessing(rawHtml, originalText) {
        this.setState({
            originalText: originalText,
            rawHtml: rawHtml
        });
        this._processor = undefined;
    }
}
