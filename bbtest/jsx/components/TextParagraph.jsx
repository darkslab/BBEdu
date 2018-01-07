class TextParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            rawHtml: ""
        };
        this._processor;
    }
    componentDidMount() {
        // if (!this.props.data.hasFormulas) {
        if (false) {
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
        if (this._processor) {
            return;
        }
        this._setupProcessor();
    }
    render() {
        let className = "bb-test-paragraph";
        // if (!this.props.data.hasFormulas) {
        if (false) {
            let content = null;
            if (this.props.data.text) {
                content = SimpleFormattedFragment(this.props.data.text);
            } else if (this.props.optionalTexts) {
                className += " bb-placeholder";
                content = this.props.optionalTexts.paragraphEmptyPlaceholder;
            }
            return (
                <div className={className}>{content}</div>
            );
        }

        return (
            <div className={className}
                 dangerouslySetInnerHTML={{ __html: this.state.rawHtml }}></div>
        );
    }

    _setupProcessor() {
        this._processor = new MathJaxAsyncProcessor(this._doneProcessing.bind(this), this.props.data.text);
    }
    _doneProcessing(rawHtml, originalText) {
        this.setState({
            rawHtml: rawHtml
        });
        this._processor = undefined;
        if (originalText !== this.props.data.text) {
            this._setupProcessor();
        }
    }
}
