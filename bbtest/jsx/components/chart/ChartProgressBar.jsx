class ChartProgressBar extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        const { scores_data, averageScore } = this.props;


        console.log(scores_data, averageScore)

        const ctx = document.getElementById('progressChart').getContext('2d');

        const chartData = {
            labels: scores_data.map((_, index) => `Test ${index + 1}`), // Labels like "Test 1", "Test 2", etc.
            datasets: [
                {
                    label: 'Your Scores',
                    data: scores_data,
                    backgroundColor: 'rgba(52, 152, 219, 0.6)', // Bar color
                    borderColor: 'rgba(52, 152, 219, 1)',
                    borderWidth: 1
                }
            ]
        };

        const chartOptions = {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: Math.max(...scores_data) + 50, // Adjust max to fit scores + some margin
                }
            },
            plugins: {
                legend: {
                    display: false, // Hide the legend
                },
                annotation: {
                    annotations: {
                        line1: {
                            type: 'line',
                            yMin: averageScore,
                            yMax: averageScore,
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
        };

        this.chart = new Chart(ctx, {
            type: 'bar',
            data: chartData,
            options: chartOptions
        });
    }

    componentWillUnmount() {
        if (this.chart) {
            this.chart.destroy();
        }
    }

    render() {
        return (
            <canvas id="progressChart" width="400" height="300" style={{ maxHeight: "300px" }}></canvas>
        );
    }
}
