class ChartDashboard extends React.Component {
    constructor(props) {
        super(props);
        // this.props.students
        // this.props.scores_data
        // this.props.subject_list
        // this.props.mean_subj
        // this.props.subject_topics
        // this.props.subject_scores
        // this.props.subject_chart_height
        this.state = {
            current_subject: "Total",
        };
    }

    componentDidMount() {
        const option_select = $("#subject-select");
        option_select.select2({
            width: '20vw',
        });
        option_select.on('select2:select', (event) => this._selectSubject(event));
    }

    render() {
        const subject_list = this.props.subject_list;


        const options = [];
        for (let i = 0; i < subject_list.length; i++) {
            options.push(<option key={`option ${i + 1}`} value={i + 1} >{subject_list[i]}</option>)
        }

        const selected_subject_topics = this.props.subject_topics[this.state.current_subject];
        const selected_subject_average = this.props.mean_subj[this.state.current_subject];

        const topic_list_html = []
        for (let i = 0; i < selected_subject_topics.length; i++) {
            topic_list_html.push(<li key={`option ${i + 1}`} value={i + 1} >{selected_subject_topics[i]}</li>)
        }
        // console.log("topic_list_html", topic_list_html)


        return <React.Fragment>
            <div className="selector" style={{ textAlign: "center" }}>
                <label htmlFor="subject-select">Select Subject:</label>
                <select className="select_v2" id="subject-select">
                    <option key="option 0" value="0">Total</option>
                    {options}
                </select>
            </div>
            <div className="row">
                <div className="col-lg-3" />
                <div className="col-xs-12 col-lg-6" style={{ minWidth: "600px" }}>
                    <div className="row panel panel-default">
                        <p className="h3" style={{ textAlign: "center" }}>Результаты учеников</p>
                        <ChartTotal
                            subject_list={this.props.subject_list}
                            scores_data={this.props.scores_data}
                            selected_subject={this.state.current_subject}
                            students={this.props.students}
                        />
                    </div>
                    <div className="row panel panel-default">
                        <p className="h3" style={{ textAlign: "center" }}>Усредненные результаты учеников</p>
                        <div className="col-xs-12 col-lg-6">
                            <ChartPolarArea
                                subject_list={this.props.subject_list}
                                scores_data={this.props.scores_data}
                                subject_topics={this.props.subject_topics}
                                subject_scores={this.props.subject_scores}
                                selected_subject={this.state.current_subject}
                                students={this.props.students}
                            />
                        </div>
                        <div className="col-xs-12 col-lg-6">
                            <p>
                                <strong>{`Ученики в среднем ответили набрали ${selected_subject_average} баллов`}</strong>
                            </p>
                            <ul>
                                {topic_list_html}
                            </ul>
                        </div>
                    </div>
                    <div className="panel panel-default" style={{ minHeight: "300px" }}>
                        <ChartProgressBar
                            scores_data={[200, 250, 180, 220, 0, 0, 0, 0, 0, 0]}
                            averageScore={195}
                        />
                    </div>
                </div>
                <div className="col-lg-3" />
            </div>

        </React.Fragment>
    }

    _selectSubject(e) {
        const data = e.params.data;
        const selectedIndex = parseInt(data.id);

        if (selectedIndex == 0) {
            this.setState({
                current_subject: "Total"
            });
            return;
        }


        console.log(data, this.props.subject_list[selectedIndex - 1])

        this.setState({
            current_subject: this.props.subject_list[selectedIndex - 1]
        });
    }


}