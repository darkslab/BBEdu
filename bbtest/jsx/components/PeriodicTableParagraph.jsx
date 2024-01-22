class PeriodicTableParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            originalText: "",
            rawHtml: "",
            zoomLevel: 1
        };
    }

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

                <img
                    className="periodicTableThumbnail"
                    src={this.props.data.periodicTableUrl}
                    width="100px"
                    alt="Thumbnail"
                    onClick={this._openOverlay.bind(this)}
                ></img>

                <div id="periodicTableOverlay" className="periodicTableOverlay" onClick={this._closeOverlay.bind(this)} onWheel={this._handleWheel.bind(this)}>
                    <img
                        id="overlayPeriodicTableImage"
                        src={this.props.data.periodicTableUrl}
                        alt="Large Image"
                        style={{ transform: `scale(${this.state.zoomLevel})` }}
                    ></img>
                </div>
            </React.Fragment>
        );
        return content;
    }

    _openOverlay() {
        // console.log("_openOverlay");
        document.getElementById('periodicTableOverlay').style.display = 'flex';
        // this.state.zoomLevel = 1;  // Reset zoom level when opening the overlay
        // this.setState({ zoomLevel: 1 }); 
    }

    _closeOverlay() {
        document.getElementById('periodicTableOverlay').style.display = 'none';
        // this.state.zoomLevel = 1;  // Reset zoom level when opening the overlay
    }

    _handleWheel(event) {
        event.preventDefault();
        // console.log(event)
        // console.log(event.deltaY)
        // console.log(this.state.zoomLevel )
        // const deltaY = event.deltaY;
        const image = document.getElementById('overlayPeriodicTableImage')

        if (event.deltaY > 0) {
            this.state.zoomLevel = this.state.zoomLevel - 0.1;
        } else {
            this.state.zoomLevel = this.state.zoomLevel + 0.1;
        }
            
        if (this.state.zoomLevel  < 0.2) {
            this.state.zoomLevel = 0.2
        }
        image.style.transform = `scale(${this.state.zoomLevel})`
    }
}
