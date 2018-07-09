class ConfirmModal extends React.Component {
    constructor(props) {
        super(props);
        this._$modal;
        this._result;

        this._boundModalHidden = this._modalHidden.bind(this);
    }
    componentDidMount() {
        this._$modal = $("[data-modal]");
        if (this._$modal.length) {
            this._$modal.modal({
                backdrop: "static",
                keyboard: false
            });
            this._$modal.on("hidden.bs.modal", this._boundModalHidden);
        } else {
            this._$modal = undefined;
        }
    }
    componentWillUnmount() {
        if (this._$modal !== undefined) {
            this._$modal.off("hidden.bs.modal", this._boundModalHidden);
            this._$modal = undefined;
        }
    }
    render() {
        let yesClassName = "btn btn-block btn-lg";
        yesClassName += this.props.isInverse ? " btn-danger" : " btn-primary";

        let noClassName = "btn btn-block btn-lg";
        noClassName += this.props.isInverse ? " btn-primary" : " btn-danger";

        return (
            <div className="modal fade" data-modal>
                <div className="modal-dialog modal-sm">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h4 className="modal-title">{this.props.title}</h4>
                        </div>
                        <div className="modal-body">
                            <div className="row">
                                <div className="col-xs-6 pr-5">
                                    <button type="button"
                                            className={yesClassName}
                                            onClick={this._chooseResult.bind(this, true)}>{this.props.yesCaption}</button>
                                </div>
                                <div className="col-xs-6 pl-5">
                                    <button type="button"
                                            className={noClassName}
                                            onClick={this._chooseResult.bind(this, false)}>{this.props.noCaption}</button>
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
        this.props.complete(this._result);
    }
    _chooseResult(result) {
        this._result = result;
        this._$modal.modal("hide");
    }
}
