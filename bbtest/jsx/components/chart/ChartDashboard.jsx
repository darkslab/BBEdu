class ChartDashboard extends React.Component {
    constructor(props) {
        super(props);
        // this.props.student_name_list
        // this.props.parent_list
        // this.props.parent_to_children_list
        // this.props.parent_average_scores
        // this.props.parent_student_scores
        // this.props.parent_student_scores_by_difficulty
        // this.props.pisa_average_historic
        // this.props.polar_area_description
        // this.props.map_key_to_id
        // this.props.map_id_to_key
        this.state = {
            current_parent: "0rus", // this.props.map_key_to_id["Total"],
            current_children: this.props.parent_to_children_list["0rus"][0], // this.props.map_key_to_id["Чтение"]
            current_language: "rus",
        };
    }

    updateParentTopicState(newTopic) {
        // console.log("updateParentTopicState", this.state);
        this.setState({ current_children: newTopic });

        const topic_option_select = $("#subject-topic-select");
        topic_option_select.val(this.state.current_children).trigger("change");
    }

    componentDidMount() {
        const option_select = $("#subject-select");
        option_select.select2({
            width: '100%',
        });
        option_select.val(this.state.current_parent).trigger("change");
        option_select.on('select2:select', (event) => this._selectParent(event));

        const lang_option_select = $("#language-select");
        lang_option_select.select2({
            width: '100%',
        });
        // lang_option_select.val(this.state.current_children).trigger("change");
        lang_option_select.on('select2:select', (event) => this._selectLanguage(event));


        const topic_option_select = $("#subject-topic-select");
        topic_option_select.select2({
            width: '50%',
        });
        topic_option_select.val(this.state.current_children).trigger("change");
        topic_option_select.on('select2:select', (event) => this._selectChild(event));


    }

    render() {
        const parent_list = this.props.parent_list[this.state.current_language];
        const map_id_to_key = this.props.map_id_to_key

        console.log("this.props", this.props)

        const options = [];
        for (let i = 0; i < parent_list.length; i++) {
            const parent_id = parent_list[i]
            options.push(<option key={`option ${parent_id}`} value={parent_id} >{map_id_to_key[parent_id]}</option>)

        }

        const options_lang = [
            <option key={`option rus}`} value={"rus"} >Русский</option>,
            <option key={`option kaz}`} value={"kaz"} >Қазақ тілі</option>,
        ];


        // Polar Area chart compute
        const polar_area_chart_labels_id = this.props.parent_to_children_list[this.state.current_parent];
        const polar_area_chart_labels = []
        const polar_area_chart_data = [];

        for (let i = 0; i < polar_area_chart_labels_id.length; i++) {
            const index_id = polar_area_chart_labels_id[i];
            polar_area_chart_data.push(this.props.parent_average_scores[index_id]);
            polar_area_chart_labels.push(this.props.map_id_to_key[index_id]);
        }



        const selected_children_topic_average = this.props.parent_average_scores[this.state.current_children];
        const selected_parent_average = this.props.parent_average_scores[this.state.current_parent];

        const current_subtopic_list = this.props.parent_to_children_list[this.state.current_children];
        const subtopic_list_html = []
        for (let i = 0; i < current_subtopic_list.length; i++) {
            const subchild_id = current_subtopic_list[i]
            subtopic_list_html.push(<li key={`subchild_option ${subchild_id}`} value={subchild_id} >{map_id_to_key[subchild_id]}</li>)
        }

        const selected_children_list = this.props.parent_to_children_list[this.state.current_parent];
        const child_options = [];
        for (let i = 0; i < selected_children_list.length; i++) {
            const child_id = selected_children_list[i]
            child_options.push(<option key={`topic_option ${child_id}`} value={child_id} >{map_id_to_key[child_id]}</option>)
        }
        // console.log("topic_list_html", topic_list_html)
        
        let recommend = null;
        if (this.state.current_children.length == 5) {
            if (parseFloat(selected_children_topic_average) <= 200) {
                recommend = <div dangerouslySetInnerHTML={{ __html: this.props.polar_area_recomend_description[this.state.current_language][this.state.current_children][0] }} />  
            } else if (parseFloat(selected_children_topic_average) <= 400) {
                recommend = <div dangerouslySetInnerHTML={{ __html: this.props.polar_area_recomend_description[this.state.current_language][this.state.current_children][200] }} />
            } else {
                recommend = <div dangerouslySetInnerHTML={{ __html: this.props.polar_area_recomend_description[this.state.current_language][this.state.current_children][400] }} />  
            }
        }
        

        return <React.Fragment>
            <FloatingSelector
                id={["subject-select", "language-select"]}
                title={["Предмет", "Язык"]}
                options={[options, options_lang]}
            />
            {/* {this.state.current_children} */}
            <div className="row">
                <div className="col-xs-12" style={{ minWidth: "900px" }}>
                    <div className="row panel panel-default">
                        <p className="h3" style={{ textAlign: "center" }}>{this.props.texts.graph_total_title}</p>
                        <p style={{ textAlign: "center" }}>{this.props.texts.graph_total_description}</p>
                        <ChartTotal
                            student_name_list={this.props.student_name_list[this.state.current_language]}
                            selected_parent={this.state.current_parent}
                            selected_language={this.state.current_language}
                            selected_children_list={selected_children_list}
                            parent_student_scores={this.props.parent_student_scores[this.state.current_language]}

                            map_id_to_key={this.props.map_id_to_key}
                            subject_chart_height={this.props.subject_chart_height}
                        />
                    </div>
                    {this.state.current_parent.length == 5 ?
                        <div className="row panel panel-default">
                            <p className="h3" style={{ textAlign: "center" }}>{this.props.texts.graph_difficulty_title}</p>
                            <p style={{ textAlign: "center" }}>{this.props.texts.graph_difficulty_description}</p>
                            <ChartMultiBarHorizontal
                                data={this.props.parent_student_scores_by_difficulty[this.state.current_language][this.state.current_parent]}
                                data_label_list={["Базовый", "Средний", "Высокий"]}
                                row_label_list={this.props.student_name_list[this.state.current_language]}

                                props_update_indicator={`${this.state.current_parent}+${this.state.current_language}`}

                                map_id_to_key={this.props.map_id_to_key}
                                subject_chart_height={this.props.subject_chart_height}
                            />
                        </div>
                        : null
                    }
                    <div className="row panel panel-default">
                        <p className="h3" style={{ textAlign: "center" }}>{this.props.texts.graph_polararea_title}</p>
                        <div className="col-xs-12 col-lg-6">
                            <ChartPolarArea
                                selected_parent={this.state.current_parent}
                                selected_children={this.state.current_children}
                                polar_area_chart_labels_id={polar_area_chart_labels_id}
                                polar_area_chart_labels={polar_area_chart_labels}
                                polar_area_chart_data={polar_area_chart_data}

                                map_id_to_key={this.props.map_id_to_key}
                                updateParentTopicState={this.updateParentTopicState.bind(this)}
                            />
                        </div>
                        <div className="col-xs-12 col-lg-6">
                            <select className="select_v2" id="subject-topic-select" style={{ maxWidth: "300px" }}>
                                {child_options}
                            </select>

                            <div dangerouslySetInnerHTML={{ __html: this.props.polar_area_common_description[this.state.current_language][this.state.current_parent] }} /> 
                            { recommend }
                            {/* <p>
                                <strong>{`Ученики в среднем ответили набрали ${parseFloat(selected_children_topic_average).toFixed(0)} баллов `}</strong>
                            </p> */}
                            <ul>
                                {subtopic_list_html}
                            </ul>
                        </div>
                    </div>
                    <div className="panel panel-default" style={{ minHeight: "300px" }}>
                        <div className="row" style={{ textAlign: "center" }}>
                            <h3 style={{ textAlign: "center" }}>{this.props.texts.graph_monitoring_title}</h3>
                            <div className="text-center" style={{ textAlign: "center" }}>
                                <p>{this.props.texts.graph_monitoring_description1}</p>
                                <ChartProgressBar
                                    scores_data={[selected_parent_average, 0, 0, 0, 0]}
                                    y_max={ this.state.current_parent.length === 4 ? 600 * 3 : 600 }
                                    averageScore={ this.props.pisa_average_historic[this.state.current_parent] }

                                    props_update_indicator={`${this.state.current_parent}+${this.state.current_language}`}
                                />
                                <p style={{ fontStyle: 'italic', fontSize: '14px', color: '#666' }}>
                                    {this.props.texts.graph_monitoring_description2}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="col-lg-3" />
            </div>

        </React.Fragment>
    }

    _selectParent(e) {
        const data = e.params.data;
        const selectedIndex = data.id;
        const current_language = this.state.current_language;

        // console.log("_selectSubject", data, selectedIndex, this.props.parent_list[this.state.current_language][selectedIndex])
        this.setState({
            current_parent: selectedIndex,
            current_children: this.props.parent_to_children_list[selectedIndex][0],
        });
    }

    _selectChild(e) {
        const data = e.params.data;
        const selectedIndex = data.id;

        this.setState({
            current_children: selectedIndex,
        });
    }

    _selectLanguage(e) {
        const data = e.params.data;
        const new_lang = data.id;
        // const new_parrent = this.state.current_parent.slice(0, -3) + new_lang;
        const new_parrent = `0${new_lang}`;
        const new_children = this.props.parent_to_children_list[new_parrent][0];
        // const selectedIndex = data.id;
        // console.log(data, data.id)
        // console.log("_selectLanguage", {
        //     current_language: new_lang,
        //     current_parent: new_parrent,
        //     current_children: new_children,
        // })

        this.setState({
            current_language: new_lang,
            current_parent: new_parrent,
            current_children: new_children,
        });
    }
}