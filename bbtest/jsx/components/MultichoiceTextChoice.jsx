class MultichoiceTextChoice extends React.Component {
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
        let choiceClassName = "bb-test-answer-choice";
        if (this.props.chosen) {
            choiceClassName += " bb-test-answer-choice-selected";
        }

        let content = null;
        let contentClassName = "bb-test-answer";

        if (!this.props.data.text) {
            let _content = null;
            if (this.props.optionalTexts) {
                contentClassName += " bb-placeholder";
                _content = this.props.optionalTexts.paragraphEmptyPlaceholder;
            }
            content = (
                <div className={contentClassName}>{_content}</div>
            );
        } else if (this.props.data.has_formulas) {
            content = (
                <div className={contentClassName}
                     dangerouslySetInnerHTML={{ __html: this.state.rawHtml }}></div>
            );
        } else {
            content = (
                <div className={contentClassName}>{SimpleFormattedFragment(this.props.data.text)}</div>
            );
        }

        return (
            <div className="row">
                <div className="col-xs-2 col-sm-3 pr-0">
                    <div className="bb-rel bb-test-answer">
                        <div className={choiceClassName}
                             onClick={this._handleClick.bind(this)}>{this.props.label}</div>
                    </div>
                </div>
                <div className="col-xs-10 col-sm-7 pl-0">
                    {content}
                </div>
            </div>
        );
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
    _handleClick() {
        if (this.props.onChoose) {
            this.props.onChoose();
        }
    }
}
