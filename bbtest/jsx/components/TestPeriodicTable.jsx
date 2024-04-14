class TestPeriodicTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            originalText: "",
            rawHtml: "",
            zoomLevel: 1,
            isDragging: false,
            dragStartX: 0,
            dragStartY: 0,
            imgPosX: 0,
            imgPosY: 0,
            dragStartTime: null,
        };

        // Using callback refs instead of createRef
        this.overlayRef = null;
        this.imageRef = null;

        // Set refs
        this.setOverlayRef = element => {
            this.overlayRef = element;
        };
        
        this.setImageRef = element => {
            this.imageRef = element;
        };
    }
    componentDidMount() {
        // let modal = $("[data-modal]");
        // if (modal.length) {
        //     modal.modal({
        //         backdrop: "static",
        //         keyboard: false
        //     });
        // }
    }

    _startDrag = (e) => {
        // Assuming this.imageRef is directly the DOM element now
        const img = this.imageRef;
        this.setState({
            isDragging: true,
            dragStartX: e.clientX - this.state.imgPosX,
            dragStartY: e.clientY - this.state.imgPosY,
            dragStartTime: Date.now(),
        });
    
        // Prevent image dragging behavior to allow custom handling
        if (img) {
            img.addEventListener('dragstart', (e) => e.preventDefault());
        }
    }

    _onDrag = (e) => {
        if (!this.state.isDragging) return;
        this.setState({
            imgPosX: e.clientX - this.state.dragStartX,
            imgPosY: e.clientY - this.state.dragStartY,
        });
    }

    _endDrag = () => {
        const dragEndTime = Date.now();
        const dragDuration = dragEndTime - this.state.dragStartTime;
        // console.log(this.state.dragStartTime, dragEndTime, dragDuration)
        this.setState({
            isDragging: false,
            dragStartTime: null, // Reset the drag start time
        }, () => {
            // If the drag duration is less than 100ms, treat it as a click and close the overlay
            if (dragDuration < 200 ) {
                this._closeOverlay();
            }
        });
    }

    _openOverlay = () => {
        // Use this.overlayRef directly
        if (this.overlayRef) {
            this.overlayRef.style.display = 'flex';
        }
    }

    _closeOverlay = () => {
        if (!this.state.isDragging) {
            if (this.overlayRef) {
                this.overlayRef.style.display = 'none';
            }
        }
    }

    _handleWheel = (event) => {
        // event.preventDefault();
        const zoomDelta = event.deltaY > 0 ? -0.1 : 0.1;
        this.setState(prevState => ({
            zoomLevel: Math.max(0.2, prevState.zoomLevel + zoomDelta)
        }));
    }

    render() {
        let periodicTable = null;
        // console.log(this.props)
        if (this.props.hasPeriodicTable) {
            console.log("Question hasPeriodicTable")
            periodicTable = <React.Fragment>
                <img
                    className="periodicTableThumbnail mt-0 mb-0 pull-right" 
                    src={this.props.periodicTableIconUrl}
                    alt="Thumbnail"
                    onClick={this._openOverlay}
                />

                <div
                    ref={this.setOverlayRef} // Updated to use setOverlayRef
                    className="periodicTableOverlay"
                    // onClick={this._closeOverlay}
                    onWheel={this._handleWheel}
                    onMouseDown={this._startDrag}
                    onMouseMove={this._onDrag}
                    onMouseUp={this._endDrag}
                    // onMouseLeave={this._endDrag}
                    style={{ display: 'none' }}
                >
                    <img
                        ref={this.setImageRef} // Updated to use setImageRef
                        id="overlayPeriodicTableImage"
                        src={this.props.periodicTableUrl}
                        alt="Large Image"
                        style={{
                            transform: `scale(${this.state.zoomLevel}) translate(${this.state.imgPosX}px, ${this.state.imgPosY}px)`
                        }}
                    />
                </div>
            </React.Fragment>
        }

        return periodicTable;
    }
}