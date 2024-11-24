

const chart_colors = [
    'rgba(52, 152, 219, 0.8)',  // #3498db
    'rgba(26, 188, 156, 0.8)',  // #1abc9c
    'rgba(155, 89, 182, 0.8)',  // #9b59b6
    'rgba(243, 156, 18, 0.8)',  // #f39c12
    'rgba(231, 76, 60,  0.8)',  // #e74c3c
    'rgba(46, 204, 113, 0.8)'   // #2ecc71
];


class ChartMultiBarHorizontal extends React.Component {
    constructor(props) {
        super(props);
        // data
        // data_label_list
        // row_label_list

        // props_update_indicator

        // map_id_to_key
        // subject_chart_height
    }
    componentDidMount() {
        const ctx = document.getElementById('graph_1').getContext('2d');

        const chart_struct = {
            type: 'bar',
            data: {
                labels: this.props.row_label_list,
                datasets: []
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        stacked: false,  // Default not stacked
                        max: 100
                    }
                },
                plugins: {
                    legend: { display: true, position: 'top' },
                }
            }
        }

        this.myChart = new Chart(ctx, chart_struct);
        this._update_chart(this.myChart);
    }

    componentDidUpdate(prevProps) {
        // console.log("ChartMultiBarHorizontal.componentDidUpdate", prevProps.data, prevProps.data_label_list)
        // console.log("ChartMultiBarHorizontal.componentDidUpdate", this.props.data, this.props.data_label_list)
        // console.log("ChartMultiBarHorizontal.componentDidUpdate", this.myChart)
        if (prevProps.props_update_indicator != this.props.props_update_indicator) {
            this._update_chart(this.myChart);
        }
    }

    render() {
        return <canvas id="graph_1" width="800" height={this.props.subject_chart_height}></canvas>
    }

    _update_chart(myChart) {
        const data = this.props.data;
        const data_label_list = this.props.data_label_list;
        const row_label_list = this.props.row_label_list; // Labels for rows (corresponding to columns in data)

        // console.log("ChartMultiBarHorizontal._update_chart", data, data_label_list)

        // Calculate the sum for each column
        const columnSums = data[0].map((_, colIndex) => 
            data.reduce((sum, row) => sum + row[colIndex], 0)
        );
        // console.log("ChartMultiBarHorizontal._update_chart", columnSums)

        // Get sorted indices based on the column sums in descending order
        const sortedIndices = columnSums
            .map((sum, index) => ({ sum, index }))
            .sort((a, b) => b.sum - a.sum) // Sort by sum (descending)
            .map(item => item.index);


        // Rearrange data columns and row_label_list based on the sorted indices
        const sortedData = data.map(row => sortedIndices.map(index => row[index]));
        const sortedRowLabels = sortedIndices.map(index => row_label_list[index]);

        // Update the datasets
        const datasets = [];
        for (let i = 0; i < sortedData.length; i++) {
            const dataset = {
                label: data_label_list[i],
                data: sortedData[i], // Columns are now sorted
                backgroundColor: chart_colors[i % chart_colors.length],
                stack: `Stack ${i}`
            };
            datasets.push(dataset);
        }

        myChart.data.datasets = datasets;
        myChart.data.labels = sortedRowLabels; // this.props.row_label_list;
        myChart.update();
    }

}