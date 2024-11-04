class ChartPolarArea extends React.Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        const subject_list = this.props.subject_list;
        const scoresData = this.props.scoresData;
        const subject_topics = this.props.subject_topics;
        const subject_scores = this.props.subject_scores;

        const selected_subject = this.props.selected_subject ? this.props.selected_subject : "Total";

        const ctx = document.getElementById('myDoughnutChart').getContext('2d');


        const polarAreaData = {
            labels: [],
            datasets: [
                {
                    data: [],
                    backgroundColor: ['#3498db', '#1abc9c', '#9b59b6', '#f39c12', '#e74c3c'],
                    borderColor: '#ffffff',
                    borderWidth: 2
                }
            ]
        };

        const polarAreaOptions = {
            responsive: false,
            scale: {
                min: 0,
                max: 100,
                weight: 1000,
            },
            plugins: {
                legend: {
                    display: false // Hide default legend
                },
                tooltip: {
                    callbacks: {
                        label: function (tooltipItem) {
                            return tooltipItem.raw + '%';
                        }
                    }
                },
                datalabels: {
                    display: true,
                    color: '#ffffff',
                    font: {
                        weight: 'bold',
                        size: 16
                    },
                    formatter: (value) => value + '%'
                }
            },
            onClick: (event, elements) => {
                // Check if a segment was clicked
                if (elements.length > 0) {
                    // Get the clicked element (first in the array)
                    const element = elements[0];
                    const segmentIndex = element.index; // Get the index of the clicked segment

                    // Retrieve the label and value of the clicked segment
                    const label = this.myChart.data.labels[segmentIndex];
                    const value = this.myChart.data.datasets[0].data[segmentIndex];

                    // Do something with the clicked segment information
                    console.log(`Clicked on segment: ${label}, Value: ${value}`);
                    alert(`Clicked on ${label} with value ${value}`);
                }
            }
        };

        this.myChart = new Chart(ctx, {
            type: 'polarArea',
            data: polarAreaData,
            options: polarAreaOptions,
            // plugins: [ChartDataLabels] // Add the data labels plugin
        });
        
        // --------------------------------------------------------------------------------------------------------------------------
        this._update_doughnut_chart2(this.myChart, subject_topics[selected_subject], subject_scores[selected_subject])

    }

    componentDidUpdate(prevProps) {
        // Check if subject_list has changed
        if (prevProps.selected_subject !== this.props.selected_subject) {
            const selected_subject = this.props.selected_subject ? this.props.selected_subject : "Total";

            this._update_doughnut_chart2(this.myChart, this.props.subject_topics[selected_subject], this.props.subject_scores[selected_subject])
        }
    }

    componentWillUnmount() {
        if (this.myChart) {
            this.myChart.destroy();
        }
    }

    render() {

        return <div className="col-xs-12 col-lg-3">
            <canvas id="myDoughnutChart" width="400" height="400"></canvas>
        </div>
    }

    // Function to update doughnut chart based on selected subject
    _update_doughnut_chart2(myChart, subject_topics, subject_scores) {
        // Update labels and data for the doughnut chart
        myChart.data.labels = subject_topics;
        myChart.data.datasets[0].data = subject_scores;

        // Update the doughnut chart display
        myChart.update();
    }

    // Function to update doughnut chart based on selected subject
    _update_doughnut_chart(myChart, selectedSubject, subject_topics, subject_scores) {
        // Update labels and data for the doughnut chart
        myChart.data.labels = subject_topics[selectedSubject];
        myChart.data.datasets[0].data = subject_scores[selectedSubject];

        // Update the doughnut chart display
        myChart.update();
    }

}