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
var ChartPolarArea = /*#__PURE__*/function (_React$Component) {
  function ChartPolarArea(props) {
    _classCallCheck(this, ChartPolarArea);
    return _callSuper(this, ChartPolarArea, [props]); // polar_area_chart_labels_id
    // polar_area_chart_labels
    // polar_area_chart_data
    // map_id_to_key
    // updateParentTopicState
  }
  _inherits(ChartPolarArea, _React$Component);
  return _createClass(ChartPolarArea, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this = this;
      var ctx = document.getElementById('myDoughnutChart').getContext('2d');
      var polarAreaData = {
        labels: [],
        mylabels_ids: [],
        datasets: [{
          data: [],
          backgroundColor: ['rgba(52, 152, 219, 0.8)',
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
          ],
          borderColor: '#ffffff',
          borderWidth: 2
        }]
      };
      var polarAreaOptions = {
        responsive: true,
        scale: {
          min: 0,
          // max: 100,
          weight: 1000
        },
        plugins: {
          legend: {
            display: false // Hide default legend
          },
          tooltip: {
            callbacks: {
              label: function label(tooltipItem) {
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
            formatter: function formatter(value) {
              return value + '%';
            }
          }
        },
        onClick: function onClick(event, elements) {
          // Check if a segment was clicked
          if (elements.length > 0) {
            // Get the clicked element (first in the array)
            var element = elements[0];
            var segmentIndex = element.index; // Get the index of the clicked segment

            // Retrieve the label and value of the clicked segment
            var label = _this.myChart.data.labels[segmentIndex];
            var label_id = _this.myChart.data.mylabels_ids[segmentIndex];
            var value = _this.myChart.data.datasets[0].data[segmentIndex];
            _this.props.updateParentTopicState(label_id);

            // Do something with the clicked segment information
            console.log("Clicked on segment: ".concat(label, ", Value: ").concat(value, ", label_id: ").concat(label_id));
            // alert(`Clicked on ${label} with value ${value}`);
          }
        }
      };
      this.myChart = new Chart(ctx, {
        type: 'polarArea',
        data: polarAreaData,
        options: polarAreaOptions
        // plugins: [ChartDataLabels] // Add the data labels plugin
      });

      // --------------------------------------------------------------------------------------------------------------------------

      this._update_doughnut_chart2(this.myChart, this.props.polar_area_chart_labels_id, this.props.polar_area_chart_labels, this.props.polar_area_chart_data);
    }
  }, {
    key: "componentDidUpdate",
    value: function componentDidUpdate(prevProps) {
      // Check if subject_list has changed
      if (prevProps.selected_parent !== this.props.selected_parent) {
        this._update_doughnut_chart2(this.myChart, this.props.polar_area_chart_labels_id, this.props.polar_area_chart_labels, this.props.polar_area_chart_data);
      }
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      if (this.myChart) {
        this.myChart.destroy();
      }
    }
  }, {
    key: "render",
    value: function render() {
      return /*#__PURE__*/React.createElement("canvas", {
        id: "myDoughnutChart",
        width: "400",
        height: "400"
      });
    }

    // Function to update doughnut chart based on selected subject
  }, {
    key: "_update_doughnut_chart2",
    value: function _update_doughnut_chart2(myChart, labels_id, labels, scores) {
      // Update labels and data for the doughnut chart
      myChart.data.labels = labels;
      myChart.data.mylabels_ids = labels_id;
      myChart.data.datasets[0].data = scores;
      // Update the doughnut chart display
      myChart.update();
    }
  }]);
}(React.Component);