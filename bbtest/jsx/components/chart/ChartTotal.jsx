class ChartTotal extends React.Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        const subject_list = this.props.subject_list;
        const scores_data = this.props.scores_data;

        const ctx = document.getElementById('studentChart').getContext('2d');
        
        this.myChart = new Chart(ctx, {
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
                    legend: { display: true, position: 'top' },
                    annotation: {
                        annotations: {
                            line1: {
                                type: 'line',
                                xMin: 0,
                                xMax: 0,
                                borderColor: 'red',
                                borderWidth: 2,
                                label: {
                                    content: 'Average Score',
                                    enabled: true,
                                    position: 'end',
                                    backgroundColor: 'rgba(255, 255, 255, 0.8)',
                                    color: 'red'
                                }
                            }
                        }
                    }
                }
            }
        });
        this._update_chart(this.myChart, "Total", subject_list, scores_data);
        
    }

    componentDidUpdate(prevProps) {
        // Check if subject_list has changed
        if (prevProps.selected_subject !== this.props.selected_subject) {
            
            const selected_subject = this.props.selected_subject ? this.props.selected_subject : "Total";
            const subject_list = this.props.subject_list;
            const scores_data = this.props.scores_data;

            console.log("ChartTotal.componentDidUpdate", this.props, selected_subject)

            this._update_chart(this.myChart, selected_subject, subject_list, scores_data)
        }
    }

    render() {
        return <canvas id="studentChart" width="800" height={ this.props.subject_chart_height }></canvas>
    }

    _update_chart(myChart, selected_subject, subject_list, scores_data) {
        console.log("ChartTotal._update_chart", selected_subject, subject_list, scores_data)
        const getAverage = (array) =>
            array.reduce((sum, currentValue) => sum + currentValue, 0) / array.length;

        const averageScore = getAverage(scores_data[selected_subject]);
        myChart.options.plugins.annotation.annotations.line1.xMin = averageScore;
        myChart.options.plugins.annotation.annotations.line1.xMax = averageScore;

        const colors = ['#3498db', '#1abc9c', '#9b59b6', '#f39c12', '#e74c3c'];

        if (selected_subject === "Total") {
            myChart.options.scales.y.stacked = true;
            myChart.data.datasets = [];
            // Loop through each subject in subject_list
            for (let i = 0; i < subject_list.length; i++) {
                const subj_key = subject_list[i]
                // Create dataset for the subject
                const dataset = {
                    label: subj_key.charAt(0).toUpperCase() + subj_key.slice(1), 
                    data: scores_data[subj_key], // Get the scores for the subject
                    backgroundColor: colors[i % 5],
                    // `rgba(${(i * 60) % 255}, ${(i * 100 + 100) % 255}, ${(i * 150) % 255}, 0.6)`, // Example color generation
                    stack: 'Stack 0'
                };

                // Push the dataset to myChart.data.datasets
                myChart.data.datasets.push(dataset);
            }
            myChart.options.scales.y.max = subject_list.length * 100;
        } else {
            const selected_subject_text = selected_subject.charAt(0).toUpperCase() + selected_subject.slice(1) // Capitalize the label
            myChart.options.scales.y.stacked = false;
            myChart.data.datasets = [{
                label: selected_subject_text,
                data: scores_data[selected_subject],
                backgroundColor: 'rgba(54, 162, 235, 0.6)'
            }];
            myChart.options.scales.y.max = 100;
        }
        myChart.update();
    }

}