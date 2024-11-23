class ChartMultiBarHorizontal extends React.Component {
    constructor(props) {
        super(props);
        // student_name_list
        // selected_parent
        // selected_children_list
        // parent_student_scores

        // map_id_to_key
        // subject_chart_height
    }
    componentDidMount() {

        const subject_list = this.props.selected_children_list;
        const scores_data = this.props.parent_student_scores;

        const ctx = document.getElementById('studentChart').getContext('2d');
        
        this.myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: this.props.student_name_list,
                datasets: []
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        stacked: false,  // Default not stacked
                        max: this.props.selected_children_list.length * 100
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
        this._update_chart(this.myChart, this.props.selected_parent, this.props.selected_children_list, this.props.parent_student_scores, this.props.map_id_to_key, this.props.student_name_list);
        
    }

    componentDidUpdate(prevProps) {
        // Check if subject_list has changed
        if (prevProps.selected_parent !== this.props.selected_parent | prevProps.selected_language !== this.props.selected_language) {
            
            // const selected_subject = this.props.selected_subject ? this.props.selected_subject : "Total";
            // const subject_list = this.props.subject_list;
            // const scores_data = this.props.scores_data;
            // console.log("ChartTotal.componentDidUpdate", this.props, selected_subject)

            this._update_chart(this.myChart, this.props.selected_parent, this.props.selected_children_list, this.props.parent_student_scores, this.props.map_id_to_key, this.props.student_name_list);
        }
    }

    render() {
        return <canvas id="studentChart" width="800" height={ this.props.subject_chart_height }></canvas>
    }

    _update_chart(myChart, selected_parent, selected_children_list, parent_student_scores, map_id_to_key, student_name_list) {
        console.log("ChartTotal._update_chart", selected_parent, selected_children_list, parent_student_scores)
        const getAverage = (array) =>
            array.reduce((sum, currentValue) => sum + currentValue, 0) / array.length;

        const averageScore = getAverage(parent_student_scores[selected_parent]);
        myChart.options.plugins.annotation.annotations.line1.xMin = averageScore;
        myChart.options.plugins.annotation.annotations.line1.xMax = averageScore;

        const colors = [
            'rgba(52, 152, 219, 0.8)',  // #3498db
            'rgba(26, 188, 156, 0.8)',  // #1abc9c
            'rgba(155, 89, 182, 0.8)',  // #9b59b6
            'rgba(243, 156, 18, 0.8)',  // #f39c12
            'rgba(231, 76, 60,  0.8)',  // #e74c3c
            'rgba(46, 204, 113, 0.8)'   // #2ecc71
        ];

        myChart.data.labels = student_name_list;

        if (selected_parent === "0rus" || selected_parent === "0kaz") {
            myChart.options.scales.y.stacked = true;
            myChart.data.datasets = [];
            // Loop through each subject in subject_list
            for (let i = 0; i < selected_children_list.length; i++) {
                const selected_children_id = selected_children_list[i]
                const selected_children_key = map_id_to_key[selected_children_id]
                // Create dataset for the subject
                const dataset = {
                    label: selected_children_key.charAt(0).toUpperCase() + selected_children_key.slice(1), 
                    data: parent_student_scores[selected_children_id], // Get the scores for the subject
                    backgroundColor: colors[i % colors.length],
                    stack: 'Stack 0'
                };

                // Push the dataset to myChart.data.datasets
                myChart.data.datasets.push(dataset);
            }
            myChart.options.scales.y.max = selected_children_list.length * 100;
        } else {
            const selected_parent_id = selected_parent
            const selected_parent_key = map_id_to_key[selected_parent]
            const selected_parent_text = selected_parent_key.charAt(0).toUpperCase() + selected_parent_key.slice(1) // Capitalize the label

            myChart.options.scales.y.stacked = false;
            myChart.data.datasets = [{
                label: selected_parent_text,
                data: parent_student_scores[selected_parent],
                backgroundColor: 'rgba(54, 162, 235, 0.6)'
            }];
            myChart.options.scales.y.max = 100;
        }
        myChart.update();
    }

}