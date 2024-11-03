class ChartDashboard extends React.Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        $("#subject-select").select2({
            width: '20vw',
        });
        let update_chart =  this._update_chart;
        const subject_list = this.props.subject_list;
        const scoresData = this.props.scoresData;

        // Event listener to update chart when student is selected
        $('#subject-select').on('select2:select', function (e) {
            var data = e.params.data;
            const selectedIndex = parseInt(data.id);
            const selectedSubject = data.text;
            console.log(data, selectedIndex, selectedSubject);
            update_chart(myChart, selectedIndex, selectedSubject, subject_list, scoresData);
            // update_doughnut_chart(selectedSubject); // Update doughnut chart with selected subject
        });

        const ctx = document.getElementById('studentChart').getContext('2d');
        
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: this.props.students,
                datasets: []
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        stacked: true,  // Default not stacked
                        max: this.props.subject_list.length * 100
                    }
                },
                plugins: {
                    legend: { display: true, position: 'top' }
                }
            }
        });
        this._update_chart(myChart, 0, "Total", subject_list, scoresData);
        
    }

    render() {
        const subject_list = this.props.subject_list;
        const options = [];
        for (let i = 0; i < subject_list.length; i++) {
            options.push(<option key={`option ${i}`} value={{ i }} >{ subject_list[i] }</option>)
        }
        // {% for subj in subject_list %}
        //         
        //       {% endfor %}

        return <div className="row">
            <div className="col-lg-3"></div>
            <div className="col-xs-12 col-lg-6">
                <h2 style={{textAlign: "center"}}>Student Test Results</h2>
                <div className="selector">
                    <label htmlFor="subject-select">Select Subject:</label>
                    <select className="select_v2" id="subject-select">
                        <option value="0">Total</option>
                        {options}
                    </select>
                </div>
                <canvas id="studentChart" width="800" height={ this.props.subject_chart_height }></canvas>
            </div>
        </div>;
    }

    _update_chart(myChart, selectedIndex, selectedSubject, subject_list, scoresData) {
        if (selectedIndex === 0) {
            myChart.options.scales.y.stacked = true;
            myChart.data.datasets = [];
            // Loop through each subject in subject_list
            for (let i = 0; i < subject_list.length; i++) {
                const subj_key = subject_list[i]
                // Create dataset for the subject
                const dataset = {
                    label: subj_key.charAt(0).toUpperCase() + subj_key.slice(1), // Capitalize the label
                    data: scoresData[subj_key], // Get the scores for the subject
                    backgroundColor: `rgba(${(i * 60) % 255}, ${(i * 100 + 100) % 255}, ${(i * 150) % 255}, 0.6)`, // Example color generation
                    stack: 'Stack 0'
                };

                // Push the dataset to myChart.data.datasets
                myChart.data.datasets.push(dataset);
            }
            myChart.options.scales.y.max = subject_list.length * 100;
        } else {
            myChart.options.scales.y.stacked = false;
            myChart.data.datasets = [{
                label: selectedSubject.charAt(0).toUpperCase() + selectedSubject.slice(1),
                data: scoresData[selectedSubject],
                backgroundColor: 'rgba(54, 162, 235, 0.6)'
            }];
            myChart.options.scales.y.max = 100;
        }
        myChart.update();
    }

}