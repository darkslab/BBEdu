"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : i + ""; }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
function _callSuper(t, o, e) { return o = _getPrototypeOf(o), _possibleConstructorReturn(t, _isNativeReflectConstruct() ? Reflect.construct(o, e || [], _getPrototypeOf(t).constructor) : o.apply(t, e)); }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { try { var t = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); } catch (t) {} return (_isNativeReflectConstruct = function _isNativeReflectConstruct() { return !!t; })(); }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
var chart_colors = ['rgba(52, 152, 219, 0.8)',
// #3498db
'rgba(26, 188, 156, 0.8)',
// #1abc9c
'rgba(155, 89, 182, 0.8)',
// #9b59b6
'rgba(243, 156, 18, 0.8)',
// #f39c12
'rgba(231, 76, 60,  0.8)',
// #e74c3c
'rgba(46, 204, 113, 0.8)' // #2ecc71
];
var ChartMultiBarHorizontal = /*#__PURE__*/function (_React$Component) {
  function ChartMultiBarHorizontal(props) {
    _classCallCheck(this, ChartMultiBarHorizontal);
    return _callSuper(this, ChartMultiBarHorizontal, [props]); // data
    // data_label_list
    // row_label_list
    // props_update_indicator
    // map_id_to_key
    // subject_chart_height
  }
  _inherits(ChartMultiBarHorizontal, _React$Component);
  return _createClass(ChartMultiBarHorizontal, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      var ctx = document.getElementById('graph_1').getContext('2d');
      var chart_struct = {
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
              stacked: false,
              // Default not stacked
              max: 100
            }
          },
          plugins: {
            legend: {
              display: true,
              position: 'top'
            }
          }
        }
      };
      this.myChart = new Chart(ctx, chart_struct);
      this._update_chart(this.myChart);
    }
  }, {
    key: "componentDidUpdate",
    value: function componentDidUpdate(prevProps) {
      // console.log("ChartMultiBarHorizontal.componentDidUpdate", prevProps.data, prevProps.data_label_list)
      // console.log("ChartMultiBarHorizontal.componentDidUpdate", this.props.data, this.props.data_label_list)
      // console.log("ChartMultiBarHorizontal.componentDidUpdate", this.myChart)
      if (prevProps.props_update_indicator != this.props.props_update_indicator) {
        this._update_chart(this.myChart);
      }
    }
  }, {
    key: "render",
    value: function render() {
      return /*#__PURE__*/React.createElement("canvas", {
        id: "graph_1",
        width: "800",
        height: this.props.subject_chart_height
      });
    }
  }, {
    key: "_update_chart",
    value: function _update_chart(myChart) {
      var data = this.props.data;
      var data_label_list = this.props.data_label_list;
      var row_label_list = this.props.row_label_list; // Labels for rows (corresponding to columns in data)

      // console.log("ChartMultiBarHorizontal._update_chart", data, data_label_list)

      // Calculate the sum for each column
      var columnSums = data[0].map(function (_, colIndex) {
        return data.reduce(function (sum, row) {
          return sum + row[colIndex];
        }, 0);
      });
      // console.log("ChartMultiBarHorizontal._update_chart", columnSums)

      // Get sorted indices based on the column sums in descending order
      var sortedIndices = columnSums.map(function (sum, index) {
        return {
          sum: sum,
          index: index
        };
      }).sort(function (a, b) {
        return b.sum - a.sum;
      }) // Sort by sum (descending)
      .map(function (item) {
        return item.index;
      });

      // Rearrange data columns and row_label_list based on the sorted indices
      var sortedData = data.map(function (row) {
        return sortedIndices.map(function (index) {
          return row[index];
        });
      });
      var sortedRowLabels = sortedIndices.map(function (index) {
        return row_label_list[index];
      });

      // Update the datasets
      var datasets = [];
      for (var i = 0; i < sortedData.length; i++) {
        var dataset = {
          label: data_label_list[i],
          data: sortedData[i],
          // Columns are now sorted
          backgroundColor: chart_colors[i % chart_colors.length],
          stack: "Stack ".concat(i)
        };
        datasets.push(dataset);
      }
      myChart.data.datasets = datasets;
      myChart.data.labels = sortedRowLabels; // this.props.row_label_list;
      myChart.update();
    }
  }]);
}(React.Component);