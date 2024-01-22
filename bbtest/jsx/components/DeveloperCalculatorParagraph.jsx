class DeveloperCalculatorParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            confirmModal: false
        };
    }
    render() {
        let paragraphClassName = "form-group bb-test-section-movable";

        let buttons = [];
        if (this.props.canDelete) {
            buttons.push(
                <button key="delete"
                        type="button"
                        className="btn btn-danger btn-xs pull-right ml-5"
                        onClick={this._renderModal.bind(this)}>
                    <i className="fa fa-fw fa-times"></i>
                </button>
            );
        }

        let sharedLabel = null;
        if (this.props.sharedQuestionIds.length > 0) {
            sharedLabel = (
                <p className="text-danger pull-left mb-0">{this.props.texts.paragraphsSharedLabelTextParagraph}</p>
            );
            paragraphClassName += " bb-test-section-background-shared";
        } else {
            paragraphClassName += " bb-test-section-background";
        }


        let modal = null;
        if (this.state.confirmModal) {
            modal = (
                <ConfirmModal title={this.props.texts.deleteModalTitle}
                              yesCaption={this.props.texts.deleteModalYesCaption}
                              noCaption={this.props.texts.deleteModalNoCaption}
                              isInverse={true}
                              complete={this._completeModal.bind(this)} />
            );
        }
        return (
            <React.Fragment>
                {modal}
                <div className={paragraphClassName} data-paragraph-id={this.props.paragraphId}>
                    <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                        {sharedLabel}
                        {buttons}
                        <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                    </div>
                    
                </div>
                <script src="https://linangdata.com/calculatorEmbed/linangcalc.js"></script>
                <div style={{ width: "50px", height: "50px", "backgroundImage": "url('https://linangdata.com/calculatorEmbed/icons/48x48.png')", zIndex: 99999}}>
                  <iframe id="linangcalc" src="https://linangdata.com/calculatorEmbed/embeddable.html?placement=right" 
                      width="500" height="500" scrolling="auto" frameBorder="0" allowtransparency="true"
                      style={{border: 0, position: "absolute", opacity: 1.0, zIndex: 99999}}
                      >
                  </iframe>
                </div>
            </React.Fragment>
        );
    }

    _renderModal() {
        this.setState({
            confirmModal: true
        });
    }
    _completeModal(data) {
        if (data) {
            this.props.onDelete();
        } else {
            this.setState({
                confirmModal: false
            });
        }
    }
}
