class ChartDashboard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            current_subject: "Total",
        };
    }

    componentDidMount() {
        const option_select = $("#subject-select");
        option_select.select2({
            width: '20vw',
        });
        // option_select.on('select2:select', function (e) {
        //     var data = e.params.data;
        //     const selectedIndex = parseInt(data.id);
        //     const selectedSubject = data.text;
        //     console.log(data, selectedIndex, selectedSubject);
        //     update_chart(myChart, selectedIndex, selectedSubject, subject_list, scores_data);
        //     // update_doughnut_chart(selectedSubject); // Update doughnut chart with selected subject
        // });
        option_select.on('select2:select', (event) => this._selectSubject(event));

        // setTimeout(() => {
        //     console.log("timeout", this.props.subject_list[1])
        //     this.setState({
        //         current_subject: this.props.subject_list[1]
        //     })
        // }, 2000);
    }

    render() {
        const subject_list = this.props.subject_list;
        const options = [];
        for (let i = 0; i < subject_list.length; i++) {
            options.push(<option key={`option ${i + 1}`} value={ i + 1 } >{subject_list[i]}</option>)
        }

        return <React.Fragment>
            <div className="row">
                <div className="col-lg-3"></div>
                <div className="col-xs-12 col-lg-6">
                    <h2 style={{ textAlign: "center" }}>Student Test Results</h2>
                    <div className="selector">
                        <label htmlFor="subject-select">Select Subject:</label>
                        <select className="select_v2" id="subject-select">
                            <option key="option 0" value="0">Total</option>
                            {options}
                        </select>
                    </div>
                    <ChartTotal
                        subject_list={this.props.subject_list}
                        scores_data={this.props.scores_data}
                        selected_subject={this.state.current_subject}
                        students={this.props.students}
                    />
                </div>
            </div>;
            <div className="row">
                <h2 style={{ textAlign: "center" }}>Student Average Results</h2>
                <div className="col-lg-3"></div>
                <ChartPolarArea
                    subject_list={this.props.subject_list}
                    scores_data={this.props.scores_data}
                    subject_topics={this.props.subject_topics}
                    subject_scores={this.props.subject_scores}
                    selected_subject={this.state.current_subject}
                    students={this.props.students}
                />
                <div className="col-xs-12 col-lg-3">
                    {/* <button style={{ backgroundColor: "#3498db", color: "white", padding: "10px 20px", border: "none" }}>РАЦИОНАЛЬНЫЕ ЧИСЛА</button> */}
                    <p>
                        <strong>Ученики в среднем ответили правильно на 12 вопросов (120 баллов) из 12 по данному предмету</strong>
                    </p>
                    <ul>
                        <li>Положительные числа. Отрицательные числа. Координатная прямая.</li>
                        <li>Противоположные числа. Целые числа. Рациональные числа. Модуль числа.</li>
                        <li>Сравнение рациональных чисел. Сложение рациональных чисел с помощью координатной прямой.</li>
                        <li>Сложение отрицательных рациональных чисел. Сложение рациональных чисел с разными знаками. Вычитание
                            рациональных чисел.</li>
                        <li>Расстояние между точками на координатной прямой.</li>
                    </ul>
                </div>
            </div>
            <ChartProgressBar
                scores_data={[200, 250, 180, 220, 0, 0, 0, 0, 0, 0]}
                averageScore={195}
            />
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