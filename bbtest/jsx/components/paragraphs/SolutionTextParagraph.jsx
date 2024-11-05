class SolutionTextParagraph extends React.Component {
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

        // let youtube_links = text.match(/^(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=([a-zA-Z0-9_]+)|youtu\.be\/([a-zA-Z\d_]+))(?:&.*)?$/gm)
        
        const regexp = /(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=([a-zA-Z0-9_]+)|youtu\.be\/([a-zA-Z\d_]+))(?:&.*)?/gm;
        

        if (this.props.isShared) {
            className += " bb-test-paragraph-shared";
            sharedAddon = (
                <h5 className="text-center mt-0 mb-5"><em>{this.props.testTexts.shared_paragraph_header}</em></h5>
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
            let youtube = [];
            const matches = this.props.data.text.matchAll(regexp)
            for (const match of matches) {
                console.log(match);
                // this.props.data.text = this.props.data.text.replace(match[0], "");
                // let rep = '<div className="embed-responsive embed-responsive-16by9" key="you'+match.index+'"><iframe src="https://www.youtube.com/embed/' + match[1] +'" frameBorder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; allowfullscreen" ></iframe></div>'
                this.state.rawHtml = this.state.rawHtml.replace(match[0], "");
                youtube.push(
                    <div className="embed-responsive embed-responsive-16by9" key={"you"+match.index}>
                        <iframe src={"https://www.youtube.com/embed/" + match[1]} frameBorder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; allowfullscreen" ></iframe>
                    </div>
                )
            }
            // console.log(this.state.rawHtml);
            content = (
                <React.Fragment>
                    {sharedAddon}
                    <div className={className}
                            dangerouslySetInnerHTML={{ __html: this.state.rawHtml }}></div>
                    {youtube.length > 0 && youtube}
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