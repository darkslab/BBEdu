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

        if (!this.props.data.text) {
            let _content = null;
            if (this.props.optionalTexts) {
                className += " bb-placeholder";
                _content = this.props.optionalTexts.paragraphEmptyPlaceholder;
            }
            content = (
                <div className={className}>{_content}</div>
            );
        } else if (this.props.data.has_formulas) {
            content = (
                <div className={className}
                     dangerouslySetInnerHTML={{ __html: this.state.rawHtml }}></div>
            );
        } else {
            content = (
                <div className={className}>{SimpleFormattedFragment(this.props.data.text)}</div>
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
