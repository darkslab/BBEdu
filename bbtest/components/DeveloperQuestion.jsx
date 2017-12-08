class DeveloperQuestion extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        // DARK_TODO  implement this
        console.log(this.props.id);
        console.log(this.props.data);
        console.log(this.props.paragraphs);
        return (
            <div className="col-xs-12 bb-developer-container">
                DeveloperQuestion
            </div>
        );
    }
}
