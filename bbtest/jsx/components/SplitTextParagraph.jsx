class SplitTextParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            toggleFlag: true
        };
        this._left = {
            originalText: "",
            rawHtml: "",
            processor: undefined
        };
        this._right = {
            originalText: "",
            rawHtml: "",
            processor: undefined
        };
    }
    componentDidMount() {
        if (!this.props.data.has_formulas) {
            return;
        }
        this._setupProcessors();
    }
    componentWillUnmount() {
        if (this._left.processor) {
            this._left.processor.stop();
        }
        if (this._right.processor) {
            this._right.processor.stop();
        }
    }
    componentDidUpdate() {
        if (this._left.processor || this._right.processor || !this.props.data.has_formulas) {
            return;
        }
        if (this.props.data.left.text !== this._left.originalText || this.props.data.right.text !== this._right.originalText) {
            this._setupProcessors();
        }
    }
    render() {
        let leftContent = null;
        let rightContent = null;

        let leftClassName = "bb-test-paragraph";
        if (!this.props.data.left.text) {
            let content = null;
            if (this.props.forDevelopers) {
                leftClassName += " bb-placeholder";
                content = this.props.texts.paragraphEmptyPlaceholder;
            }
            leftContent = (
                <div className={leftClassName}>{content}</div>
            );
        } else if (this.props.data.has_formulas) {
            leftContent = (
                <div className={leftClassName}
                     dangerouslySetInnerHTML={{ __html: this._left.rawHtml }}></div>
            );
        } else {
            leftContent = (
                <div className={leftClassName}>{SimpleFormattedFragment(this.props.data.left.text)}</div>
            );
        }

        let rightClassName = "bb-test-paragraph";
        if (!this.props.data.right.text) {
            let content = null;
            if (this.props.forDevelopers) {
                rightClassName += " bb-placeholder";
                content = this.props.texts.paragraphEmptyPlaceholder;
            }
            rightContent = (
                <div className={rightClassName}>{content}</div>
            );
        } else if (this.props.data.has_formulas) {
            rightContent = (
                <div className={rightClassName}
                     dangerouslySetInnerHTML={{ __html: this._right.rawHtml }}></div>
            );
        } else {
            rightContent = (
                <div className={rightClassName}>{SimpleFormattedFragment(this.props.data.right.text)}</div>
            );
        }

        return (
            <div className="row">
                <div className="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                    <div className="row">
                        <div className="col-xs-6 pr-5">
                            <h5 className="text-center mt-0 mb-0"><em>{this.props.texts.columnACaption}</em></h5>
                            {leftContent}
                        </div>
                        <div className="col-xs-6 pl-5">
                            <h5 className="text-center mt-0 mb-0"><em>{this.props.texts.columnBCaption}</em></h5>
                            {rightContent}
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    _setupProcessors() {
        this._left.processor = new KatexAsyncProcessor(this._doneProcessing.bind(this, "left"), this.props.data.left.text);
        this._right.processor = new KatexAsyncProcessor(this._doneProcessing.bind(this, "right"), this.props.data.right.text);
    }
    _doneProcessing(type, rawHtml, originalText) {
        switch (type) {
            case "left":
                this._left.originalText = originalText;
                this._left.rawHtml = rawHtml;
                this._left.processor = undefined;
                break;
            case "right":
                this._right.originalText = originalText;
                this._right.rawHtml = rawHtml;
                this._right.processor = undefined;
                break;
        }
        if (!this._left.processor && !this._right.processor) {
            this.setState(prevState => ({
                toggleFlag: !prevState.toggleFlag
            }));
        }
    }
}
