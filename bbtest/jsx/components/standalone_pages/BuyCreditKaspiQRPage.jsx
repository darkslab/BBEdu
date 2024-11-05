class BuyCreditKaspiQRPage extends React.Component {
    constructor(props) {
        super(props);
        // props.qr_code_base64
        this.state = {
            current_subject: "Total",
        };
    }

    componentDidMount() {

        // setTimeout(() => {
        //     console.log("timeout", this.props.subject_list[1])
        //     this.setState({
        //         current_subject: this.props.subject_list[1]
        //     })
        // }, 2000);
    }

    render() {

        return <React.Fragment>
            <div className="row">
                <div className="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                    <div className="panel panel-default">
                        <div className="panel-body text-center">
                            <p className="text-center">
                                <strong>Manual Payment Message</strong>
                            </p>
                            <img src={`data:image/png;base64,${ this.props.qr_code_base64 }`} alt="QR Code" className="img-responsive center-block" />
                        </div>
                        {/* <!-- Manual Payment Button --> */}
                        <div className="text-center pb-10">
                            {/* <a href="" className="btn btn-primary">'Go to tests'</a> */}
                            <a onClick={() => window.location.reload()} className="btn btn-primary">Refresh</a>
                        </div>
                    </div>
                </div>
            </div>
        </React.Fragment>
    }

    _selectSubject(e) {
        // this.setState({
        //     current_subject: this.props.subject_list[selectedIndex - 1]
        // });
    }

}