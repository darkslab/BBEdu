class Question extends React.Component {
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
        // _load_calculator()
    }
    componentWillUnmount() {
        // _unload_calculator()
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
        let paragraphs = [];
        for (let i = 0; i < this.props.object.paragraphs.length; i++) {
            let ParagraphClass = eval(this.props.object.paragraphs[i].paragraph_class);
            paragraphs.push(
                <ParagraphClass key={i}
                                data={this.props.object.paragraphs[i].meta_data}
                                isShared={this.props.object.paragraphs[i].is_shared}
                                texts={this.props.texts}
                                testTexts={this.props.testTexts}
                                forDevelopers={false} />
            );
        }

        let timer = null;
        if (this.props.hasTimer) {
            let timerClassName = "fa fa-fw mr-10";
            let countDown = "--:--";
            if (this.props.secondsLeft >= 0) {
                countDown = (parseInt(this.props.secondsLeft / 60, 10)) + ":" + ("0" + (this.props.secondsLeft % 60)).substr(-2);
                timerClassName += " fa-clock-o";
            } else {
                timerClassName += " fa-refresh fa-spin";
            }
            let countDownClassName = "bb-test-timer label mt-0 mb-0 pull-right";
            if (this.props.secondsLeft > 10) {
                countDownClassName += " label-success";
            } else {
                countDownClassName += " label-danger";
            }

            timer = (
                <span className={countDownClassName}>
                    <i className={timerClassName}></i>
                    {countDown}
                </span>
            );
        }

        let periodicTable = null;
        console.log(this.props)
        if (this.props.hasPeriodicTable) {
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

        let answerContent = null;
        if (this.props.object.answer_class) {
            let AnswerClass = eval(this.props.object.answer_class);
            answerContent = (
                <AnswerClass data={this.props.object.meta_data}
                             answer={this.props.answerData}
                             onUpdate={this.props.onAnswerUpdate}
                             canAnswer={this.props.canAnswer}
                             showCorrectAnswer={this.props.showCorrectAnswer}
                             texts={this.props.texts} />
            );
        }
        
        return (
            <React.Fragment>
                <div className="row">
                    <div className="col-xs-12">
                        <div className="panel mb-15 panel-primary">
                            <div className="panel-heading bb-rel clearfix">
                                <div className="bb-test-number">{this.props.count}</div>
                                <h4 className="panel-title bb-test-title mt-15 mb-15 pull-left">{this.props.texts.question} ({this.props.object.meta_data.question_code})</h4>
                                {periodicTable}
                                {timer}
                            </div>
                            <div className="panel-body">
                                <div className="mb-15">
                                    {paragraphs}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                {answerContent}
            </React.Fragment>
        );
    }
}
