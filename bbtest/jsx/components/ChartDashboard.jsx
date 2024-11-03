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
            <ChartPolarArea
                subject_list = {this.props.subject_list}
                scoresData = {this.props.scoresData}
                subject_topics = {this.props.subject_topics}
                subject_scores = {this.props.subject_scores}
                students = {this.props.students}
            />
        </React.Fragment>
    }


}