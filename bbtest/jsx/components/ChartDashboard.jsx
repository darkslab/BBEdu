class ChartDashboard extends React.Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        
    }

    render() {
        const subject_list = this.props.subject_list;


        return <React.Fragment>
            <ChartTotal
                subject_list = {this.props.subject_list}
                scoresData = {this.props.scoresData}
                students = {this.props.students}
            />
        </React.Fragment>
    }


}