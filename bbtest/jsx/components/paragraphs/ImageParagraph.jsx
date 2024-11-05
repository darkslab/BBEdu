class ImageParagraph extends React.Component {
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
        let content = null;
        let className = "bb-test-paragraph";
        let sharedAddon = null;

        if (this.props.isShared) {
            className += " bb-test-paragraph-shared";
            sharedAddon = (
                <h5 className="text-center mt-0 mb-5"><em>{this.props.testTexts.shared_paragraph_header}</em></h5>
            );
        }

        let imgClassName;
        let imgSrc;
        if (this.props.data.asset_url) {
            imgClassName = "img-responsive center-block bb-test-paragraph-image";
            imgSrc = this.props.data.asset_url;
        } else {
            className += " bb-test-paragraph-image-waiting";
            imgClassName = "bb-spinner";
            imgSrc = this.props.data.spinner_logo_url;
        }

        content = (
            <React.Fragment>
                {sharedAddon}
                <div className={className}>{/* Your SimpleFormattedFragment rendering here */}</div>

                <img
                    className={imgClassName} 
                    src={imgSrc}
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
                        src={imgSrc}
                        alt="Large Image"
                        style={{
                            transform: `scale(${this.state.zoomLevel}) translate(${this.state.imgPosX}px, ${this.state.imgPosY}px)`
                        }}
                    />
                </div>
            </React.Fragment>
        );

        return content;
    }

}
