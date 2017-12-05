class DeveloperTest extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div className="row">
                <div className="col-xs-12 bb-developer-container">
                    <img className="bb-spinner"
                         src={this.props.spinnerLogo} />
                </div>
            </div>
        );
    }
}
