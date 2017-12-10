class DeveloperQuestion extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        // DARK_TODO  implement this
        return (
            <div className="col-xs-12 bb-developer-container">
                Question #{this.props.object.id()}
            </div>
        );
    }
}
