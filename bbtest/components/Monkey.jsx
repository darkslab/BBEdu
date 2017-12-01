class Monkey extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            counter: 0
        };
    }
    handleClick() {
        this.setState(prevState => ({
            counter: prevState.counter + 1
        }));
    }
    render() {
        return (
            <Shmonkey title={this.props.title}
                      counter={this.state.counter}
                      handleClick={this.handleClick.bind(this)} />
        );
    }
}
