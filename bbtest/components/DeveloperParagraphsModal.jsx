class DeveloperParagraphsModal extends React.Component {
    constructor(props) {
        super(props);
        this._$modal;
        this._paragraphClass;
    }
    componentDidMount() {
        this._$modal = $("[data-modal]");
        if (this._$modal.length) {
            this._$modal.modal();
            this._$modal.on("hidden.bs.modal", this._modalHidden.bind(this));
        } else {
            this._$modal = undefined;
        }
    }
    componentWillUnmount() {
        if (this._$modal) {
            this._$modal.off("hidden.bs.modal", this._modalHidden.bind(this));
            this._$modal = undefined;
        }
    }
    render() {
        return (
            <div className="modal fade" data-modal>
                <div className="modal-dialog">
                    <div className="modal-content">
                        <div className="modal-header">
                            <button type="button" className="close" data-dismiss="modal">&times;</button>
                            <h4 className="modal-title">{this.props.texts.paragraphsModalTitle}</h4>
                        </div>
                        <div className="modal-body">
                            <div className="row">
                                <div className="col-xs-12 col-sm-10 col-sm-offset-1 mb-10">
                                    <button type="button"
                                            className="btn btn-primary btn-block btn-lg"
                                            onClick={this._chooseParagraphClass.bind(this, "TextParagraph")}>{this.props.texts.paragraphButtonTextParagraph}</button>
                                </div>
                                <div className="col-xs-12 col-sm-10 col-sm-offset-1 mb-10">
                                    <button type="button"
                                            className="btn btn-primary btn-block btn-lg"
                                            onClick={this._chooseParagraphClass.bind(this, "SplitTextParagraph")}>{this.props.texts.paragraphButtonSplitTextParagraph}</button>
                                </div>
                            </div>
                        </div>
                        <div className="modal-footer"></div>
                    </div>
                </div>
            </div>
        );
    }
    _modalHidden() {
        this.props.complete(this._paragraphClass);
    }
    _chooseParagraphClass(paragraphClass) {
        this._paragraphClass = paragraphClass;
        this._$modal.modal("hide");
    }
}
