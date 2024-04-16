class RefreshModal extends React.Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        let modal = $("[data-modal]");
        if (modal.length) {
            modal.modal({
                backdrop: "static",
                keyboard: false
            });
        }
    }
    render() {
        
        const error_display = this.props.error_msg ? <>
            <button data-toggle="collapse" data-target="#demo">Show error message</button>
            <div id="demo" class="collapse">
                {this.props.error_msg}
            </div>
        </> : null


        return (
            <div className="modal fade" data-modal>
                <div className="modal-dialog">
                    <div className="modal-content">
                        <div className="modal-body">
                            <p className="lead mt-15 mb-0 text-center">{this.props.message}</p>
                        </div>
                        <div className="modal-footer">
                            <div className="text-center">
                                <a href={this.props.refreshUrl} className="btn btn-primary">{this.props.refreshCaption}</a>
                                <a href={this.props.cancelUrl} className="btn btn-default">{this.props.cancelCaption}</a>
                            </div>
                        </div>
                        {error_display}
                    </div>
                </div>
            </div>
        );
    }
}
