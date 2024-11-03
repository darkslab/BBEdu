class ChartPolarArea extends React.Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        // $("#subject-select").select2({
        //     width: '20vw',
        // });

        const subject_list = this.props.subject_list;
        const scoresData = this.props.scoresData;
        const subject_topics = this.props.subject_topics;
        const subject_scores = this.props.subject_scores;

        const ctx_doughnut = document.getElementById('myDoughnutChart').getContext('2d');

        const doughnutData = {
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

        const doughnutOptions = {
            responsive: false,
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
                    const label = myDoughnutChart.data.labels[segmentIndex];
                    const value = myDoughnutChart.data.datasets[0].data[segmentIndex];

                    // Do something with the clicked segment information
                    console.log(`Clicked on segment: ${label}, Value: ${value}`);
                    alert(`Clicked on ${label} with value ${value}`);
                }
            }
        };

        const myDoughnutChart = new Chart(ctx_doughnut, {
            type: 'polarArea',
            data: doughnutData,
            options: doughnutOptions,
            // plugins: [ChartDataLabels] // Add the data labels plugin
        });

        

        // --------------------------------------------------------------------------------------------------------------------------
       this._update_doughnut_chart(myDoughnutChart, "Total", subject_topics, subject_scores)

    }

    render() {
        const subject_list = this.props.subject_list;
        // const options = [];
        // for (let i = 0; i < subject_list.length; i++) {
        //     options.push(<option key={`option ${i}`} value={{ i }} >{subject_list[i]}</option>)
        // }
        // {% for subj in subject_list %}
        //         
        //       {% endfor %}

        return <div className="row">
            <h2 style={{textAlign: "center"}}>Student Average Results</h2>
            <div className="col-lg-3"></div>
            <div className="col-xs-12 col-lg-3">
                <canvas id="myDoughnutChart" width="400" height="400"></canvas>
            </div>
            <div className="col-xs-12 col-lg-3">
                <button style={{backgroundColor: "#3498db", color: "white", padding: "10px 20px", border: "none"}}>РАЦИОНАЛЬНЫЕ ЧИСЛА</button>
                <p>
                    <strong>Вы ответили правильно на 12 вопросов (120 баллов) из 12 по данному разделу</strong>
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
    // Function to update doughnut chart based on selected subject
    _update_doughnut_chart(myChart, selectedSubject, subject_topics, subject_scores) {
        // Update labels and data for the doughnut chart
        myChart.data.labels = subject_topics[selectedSubject];
        myChart.data.datasets[0].data = subject_scores[selectedSubject];

        // Update the doughnut chart display
        myChart.update();
    }

}