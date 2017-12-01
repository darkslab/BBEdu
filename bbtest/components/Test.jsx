class Test extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <img className="bb-spinner"
                 src={this.props.spinnerLogo} />
        );
    }
}
