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
            <div className="row" style={{textAlign: "center"}}>
                <h3 style={{textAlign: "center"}}>Мониторинг прогресса участника тестирования</h3>
                <div className="col-lg-3"></div>
                <div className="col-xs-12 col-lg-6 text-center" style={{textAlign: "center"}}>
                    <p>В графике показаны Ваши результаты по данному предмету. Здесь Вы сможете отслеживать результаты каждого теста и траекторию прогресса.</p>
                    <canvas id="progressChart" width="400" height="300" style={{maxHeight: "300px"}}></canvas>
                    <p style={{ fontStyle: 'italic', fontSize: '14px', color: '#666' }}>
                        Для сравнения Ваших результатов мы указали средний балл (красная линия) всех участников на сайте по данному предмету.
                    </p>
                </div>
            </div>
        );
    }
}
