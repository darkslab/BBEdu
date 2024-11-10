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
        // this.props.topic_to_subtopic_map
        this.state = {
            current_subject: "Total",
            current_topic: "Чтение",
        };
    }

    updateParentTopicState(newTopic) {
        console.log(this.state);
        this.setState({ current_topic: newTopic });
    }

    componentDidMount() {
        const option_select = $("#subject-select");
        option_select.select2({
            width: '20vw',
        });
        option_select.on('select2:select', (event) => this._selectSubject(event));


        // const topic_option_select = $("#subject-topic-select");
        // topic_option_select.select2({
        //     width: '20vw',
        // });
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
        const topic_options = [];

        

        for (let i = 0; i < selected_subject_topics.length; i++) {
            topic_list_html.push(<li key={`option ${i + 1}`} value={i + 1} >{selected_subject_topics[i]}</li>)
            topic_options.push(<option key={`topic_option ${i + 1}`} value={i + 1} >{selected_subject_topics[i]}</option>)
        }
        // console.log("topic_list_html", topic_list_html)

        const current_subtopic_list = this.props.topic_to_subtopic_map[this.state.current_topic];
        const subtopic_list_html = []
        for (let i = 0; i < current_subtopic_list.length; i++) {
            subtopic_list_html.push(<li key={`option ${i + 1}`} value={i + 1} >{current_subtopic_list[i]}</li>)
        }

        return <React.Fragment>
            <FloatingSelector 
                    options={options}
                />
            {this.state.current_topic}
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

                                updateParentTopicState={this.updateParentTopicState.bind(this)}
                            />
                        </div>
                        <div className="col-xs-12 col-lg-6">
                            <select className="select_v2" id="subject-topic-select" style={{maxWidth: "300px"}}>
                                {topic_options}
                            </select>

                            <p>
                                <strong>{`Ученики в среднем ответили набрали ${selected_subject_average} баллов`}</strong>
                            </p>
                            <ul>
                                {/* {topic_list_html} */}
                                {subtopic_list_html}
                            </ul>
                        </div>
                    </div>
                    <div className="panel panel-default" style={{ minHeight: "300px" }}>
                        <div className="row" style={{textAlign: "center"}}>
                            <h3 style={{textAlign: "center"}}>Мониторинг прогресса участника тестирования</h3>
                            <div className="text-center" style={{textAlign: "center"}}>
                                <p>В графике показаны Ваши результаты по данному предмету. Здесь Вы сможете отслеживать результаты каждого теста и траекторию прогресса.</p>
                                <ChartProgressBar
                                    scores_data={[200, 250, 180, 220, 0, 0, 0, 0, 0, 0]}
                                    averageScore={195}
                                />
                                <p style={{ fontStyle: 'italic', fontSize: '14px', color: '#666' }}>
                                    Для сравнения Ваших результатов мы указали средний балл (красная линия) всех участников на сайте по данному предмету.
                                </p>
                            </div>
                        </div>
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