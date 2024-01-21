class PeriodicTableParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            originalText: "",
            rawHtml: ""
        };
        // this._processor;
    }
    // componentDidMount() {
    //     if (!this.props.data.has_formulas) {
    //         return;
    //     }
    //     this._setupProcessor();
    // }
    // componentWillUnmount() {
    //     if (this._processor) {
    //         this._processor.stop();
    //     }
    // }
    // componentDidUpdate() {
    //     if (this._processor || !this.props.data.has_formulas) {
    //         return;
    //     }
    //     if (this.props.data.text !== this.state.originalText) {
    //         this._setupProcessor();
    //     }
    // }
    render() {
        let content = null;
        let className = "bb-test-paragraph";
        let sharedAddon = null;

        if (this.props.isShared) {
            className += " bb-test-paragraph-shared";
            sharedAddon = (
                <h5 className="text-center mt-0 mb-5"><em>{this.props.testTexts.shared_paragraph_header}</em></h5>
            );
        }

        console.log("PeriodicTableParagraph this.props", this.props    )
        content = (
            <React.Fragment>
                {sharedAddon}
                <div className={className}>{SimpleFormattedFragment(this.props.data.text)}</div>
                <div>
                    <img class="periodicTableThumbnail" src={this.props.data.periodicTableUrl} width="100px" alt="Periodic Table Thumbnail" onClick={this._openOverlay.bind(this)}></img>

                    <div id="periodicTableOverlay" class="periodicTableOverlay" onClick={this._closeOverlay.bind(this)}>
                        <img id="overlayPeriodicTableImage" src="" alt="Periodic Table Large"></img>
                    </div>
                </div>
            </React.Fragment>
        );
        return content;
    }

    _openOverlay() {
        // console.log("_openOverlay", document.getElementById('overlayImage'));
        document.getElementById('overlayPeriodicTableImage').src = this.props.data.periodicTableUrl;
        document.getElementById('periodicTableOverlay').style.display = 'flex';
    }

    _closeOverlay() {
        document.getElementById('periodicTableOverlay').style.display = 'none';
    }

    // _setupProcessor() {
    //     this._processor = new KatexAsyncProcessor(this._doneProcessing.bind(this), this.props.data.text);
    // }
    // _doneProcessing(rawHtml, originalText) {
    //     this.setState({
    //         originalText: originalText,
    //         rawHtml: rawHtml
    //     });
    //     this._processor = undefined;
    // }
}
