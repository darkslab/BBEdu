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
var ChartTotal = /*#__PURE__*/function (_React$Component) {
  function ChartTotal(props) {
    _classCallCheck(this, ChartTotal);
    return _callSuper(this, ChartTotal, [props]); // student_name_list
    // selected_parent
    // selected_children_list
    // parent_student_scores
    // map_id_to_key
    // subject_chart_height
  }
  _inherits(ChartTotal, _React$Component);
  return _createClass(ChartTotal, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      var subject_list = this.props.selected_children_list;
      var scores_data = this.props.parent_student_scores;
      var ctx = document.getElementById('studentChart').getContext('2d');
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
              stacked: true,
              // Default not stacked
              max: this.props.selected_children_list.length * 100
            }
          },
          plugins: {
            legend: {
              display: true,
              position: 'top'
            },
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
  }, {
    key: "componentDidUpdate",
    value: function componentDidUpdate(prevProps) {
      // Check if subject_list has changed
      if (prevProps.selected_parent !== this.props.selected_parent | prevProps.selected_language !== this.props.selected_language) {
        // const selected_subject = this.props.selected_subject ? this.props.selected_subject : "Total";
        // const subject_list = this.props.subject_list;
        // const scores_data = this.props.scores_data;
        // console.log("ChartTotal.componentDidUpdate", this.props, selected_subject)

        this._update_chart(this.myChart, this.props.selected_parent, this.props.selected_children_list, this.props.parent_student_scores, this.props.map_id_to_key, this.props.student_name_list);
      }
    }
  }, {
    key: "render",
    value: function render() {
      return /*#__PURE__*/React.createElement("canvas", {
        id: "studentChart",
        width: "800",
        height: this.props.subject_chart_height
      });
    }
  }, {
    key: "_update_chart",
    value: function _update_chart(myChart, selected_parent, selected_children_list, parent_student_scores, map_id_to_key, student_name_list) {
      console.log("ChartTotal._update_chart", selected_parent, selected_children_list, parent_student_scores);
      var getAverage = function getAverage(array) {
        return array.reduce(function (sum, currentValue) {
          return sum + currentValue;
        }, 0) / array.length;
      };
      var averageScore = getAverage(parent_student_scores[selected_parent]);
      myChart.options.plugins.annotation.annotations.line1.xMin = averageScore;
      myChart.options.plugins.annotation.annotations.line1.xMax = averageScore;
      var colors = ['rgba(52, 152, 219, 0.8)',
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
      myChart.data.labels = student_name_list;
      if (selected_parent === "0rus" || selected_parent === "0kaz") {
        myChart.options.scales.y.stacked = true;
        myChart.data.datasets = [];
        // Loop through each subject in subject_list
        for (var i = 0; i < selected_children_list.length; i++) {
          var selected_children_id = selected_children_list[i];
          var selected_children_key = map_id_to_key[selected_children_id];
          // Create dataset for the subject
          var dataset = {
            label: selected_children_key.charAt(0).toUpperCase() + selected_children_key.slice(1),
            data: parent_student_scores[selected_children_id],
            // Get the scores for the subject
            backgroundColor: colors[i % colors.length],
            stack: 'Stack 0'
          };

          // Push the dataset to myChart.data.datasets
          myChart.data.datasets.push(dataset);
        }
        myChart.options.scales.y.max = selected_children_list.length * 100;
      } else {
        var selected_parent_id = selected_parent;
        var selected_parent_key = map_id_to_key[selected_parent];
        var selected_parent_text = selected_parent_key.charAt(0).toUpperCase() + selected_parent_key.slice(1); // Capitalize the label

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
  }]);
}(React.Component);