class ChartPolarArea extends React.Component {
    constructor(props) {
        super(props);
        // selected_parent
        // selected_children
        // polar_area_chart_labels_id
        // polar_area_chart_labels
        // polar_area_chart_data

        // map_id_to_key
        // updateParentTopicState
    }
    componentDidMount() {
        const ctx = document.getElementById('myDoughnutChart').getContext('2d');


        const polarAreaData = {
            labels: [],
            mylabels_ids: [],
            datasets: [
                {
                    data: [],
                    backgroundColor: [
                        'rgba(52, 152, 219, 0.8)',  // #3498db
                        'rgba(26, 188, 156, 0.8)',  // #1abc9c
                        'rgba(155, 89, 182, 0.8)',  // #9b59b6
                        'rgba(243, 156, 18, 0.8)',  // #f39c12
                        'rgba(231, 76, 60,  0.8)',  // #e74c3c
                        'rgba(46, 204, 113, 0.8)'   // #2ecc71
                    ],
                    borderColor: '#ffffff',
                    borderWidth: 2
                }
            ]
        };

        const polarAreaOptions = {
            responsive: true,
            scale: {
                min: 0,
                weight: 1000,
            },
            plugins: {
                legend: {
                    display: false, // Hide default legend
                },
                tooltip: {
                    callbacks: {
                        label: function (tooltipItem) {
                            return parseFloat(tooltipItem.raw).toFixed(0);
                        },
                    },
                },
                datalabels: {
                    display: true,
                    color: '#ffffff',
                    font: {
                        weight: 'bold',
                        size: 16,
                    },
                    formatter: (value) => value + '%',
                },
            },
            onClick: (event, elements) => {
                // Check if a segment was clicked
                if (elements.length > 0) {
                    // Get the clicked element (first in the array)
                    const element = elements[0];
                    const segmentIndex = element.index; // Get the index of the clicked segment

                    // Retrieve the label and value of the clicked segment
                    const label = this.myChart.data.labels[segmentIndex];
                    const label_id = this.myChart.data.mylabels_ids[segmentIndex];
                    const value = this.myChart.data.datasets[0].data[segmentIndex];

                    this.props.updateParentTopicState(label_id);

                    // Reset the border colors to their original value
                    const defaultBorderColor = this.props.polar_area_chart_labels_id.map(() => "#ffffff"); // Default border color
                    const defaultBorderWidth = this.props.polar_area_chart_labels_id.map(() => 0); // Default border width

                    this.myChart.data.datasets[0].borderColor = defaultBorderColor;
                    this.myChart.data.datasets[0].borderWidth = defaultBorderWidth;

                    // Set a dark border color and thicker border for the clicked segment
                    this.myChart.data.datasets[0].borderColor[segmentIndex] = "#000000"; // Dark border (black)
                    this.myChart.data.datasets[0].borderWidth[segmentIndex] = 3; // Thicker border for emphasis

                    // Update the chart
                    this.myChart.update();

                    // Log clicked segment details
                    console.log(`Clicked on segment: ${label}, Value: ${value}, label_id: ${label_id}`);
                }
            },
        };

        this.myChart = new Chart(ctx, {
            type: 'polarArea',
            data: polarAreaData,
            options: polarAreaOptions,
            // plugins: [ChartDataLabels] // Add the data labels plugin
        });

        // --------------------------------------------------------------------------------------------------------------------------
        
        this._update_doughnut_chart2(this.myChart, this.props.polar_area_chart_labels_id, this.props.polar_area_chart_labels, this.props.polar_area_chart_data)

    }

    componentDidUpdate(prevProps) {
        // Check if subject_list has changed
        if (prevProps.selected_parent !== this.props.selected_parent || prevProps.selected_children !== this.props.selected_children) {

            this._update_doughnut_chart2(this.myChart, this.props.polar_area_chart_labels_id, this.props.polar_area_chart_labels, this.props.polar_area_chart_data)
        }
    }

    componentWillUnmount() {
        if (this.myChart) {
            this.myChart.destroy();
        }
    }

    render() {
        // console.log("ChartPolarArea.props", this.props)
        return <canvas id="myDoughnutChart" width="400" height="400"></canvas>
    }

    // Function to update doughnut chart based on selected subject
    _update_doughnut_chart2(myChart, label_id_list, labels, scores ) {
        // Update labels and data for the doughnut chart
        myChart.data.labels = labels;
        myChart.data.mylabels_ids = label_id_list;
        myChart.data.datasets[0].data = scores;

        const defaultBorderColor = label_id_list.map(() => "#ffffff"); // Default border color
        const defaultBorderWidth = label_id_list.map(() => 0); // Default border width
        myChart.data.datasets[0].borderColor = defaultBorderColor;
        myChart.data.datasets[0].borderWidth = defaultBorderWidth;

        for (let i=0; i < label_id_list.length; i++) {
            if (label_id_list[i] === this.props.selected_children) {
                // Set a dark border color and thicker border for the clicked segment
                myChart.data.datasets[0].borderColor[i] = "rgba(10, 10, 10, 0.5);"; // Dark border (black)
                myChart.data.datasets[0].borderWidth[i] = 3; // Thicker border for emphasis
            }
        }
        // Update the doughnut chart display
        myChart.update();
    }

}