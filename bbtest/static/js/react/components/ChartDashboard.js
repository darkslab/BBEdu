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
var ChartDashboard = /*#__PURE__*/function (_React$Component) {
  function ChartDashboard(props) {
    _classCallCheck(this, ChartDashboard);
    return _callSuper(this, ChartDashboard, [props]);
  }
  _inherits(ChartDashboard, _React$Component);
  return _createClass(ChartDashboard, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      $("#subject-select").select2({
        width: '20vw'
      });
      var update_chart = this._update_chart;
      var subject_list = this.props.subject_list;
      var scoresData = this.props.scoresData;

      // Event listener to update chart when student is selected
      $('#subject-select').on('select2:select', function (e) {
        var data = e.params.data;
        var selectedIndex = parseInt(data.id);
        var selectedSubject = data.text;
        console.log(data, selectedIndex, selectedSubject);
        update_chart(myChart, selectedIndex, selectedSubject, subject_list, scoresData);
        // update_doughnut_chart(selectedSubject); // Update doughnut chart with selected subject
      });
      var ctx = document.getElementById('studentChart').getContext('2d');
      var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.props.students,
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
              max: this.props.subject_list.length * 100
            }
          },
          plugins: {
            legend: {
              display: true,
              position: 'top'
            }
          }
        }
      });
      this._update_chart(myChart, 0, "Total", subject_list, scoresData);
    }
  }, {
    key: "render",
    value: function render() {
      var subject_list = this.props.subject_list;
      var options = [];
      for (var i = 0; i < subject_list.length; i++) {
        options.push( /*#__PURE__*/React.createElement("option", {
          key: "option ".concat(i),
          value: {
            i: i
          }
        }, subject_list[i]));
      }
      // {% for subj in subject_list %}
      //         
      //       {% endfor %}

      return /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-lg-3"
      }), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-lg-6"
      }, /*#__PURE__*/React.createElement("h2", {
        style: {
          textAlign: "center"
        }
      }, "Student Test Results"), /*#__PURE__*/React.createElement("div", {
        className: "selector"
      }, /*#__PURE__*/React.createElement("label", {
        htmlFor: "subject-select"
      }, "Select Subject:"), /*#__PURE__*/React.createElement("select", {
        className: "select_v2",
        id: "subject-select"
      }, /*#__PURE__*/React.createElement("option", {
        value: "0"
      }, "Total"), options)), /*#__PURE__*/React.createElement("canvas", {
        id: "studentChart",
        width: "800",
        height: this.props.subject_chart_height
      })));
    }
  }, {
    key: "_update_chart",
    value: function _update_chart(myChart, selectedIndex, selectedSubject, subject_list, scoresData) {
      if (selectedIndex === 0) {
        myChart.options.scales.y.stacked = true;
        myChart.data.datasets = [];
        // Loop through each subject in subject_list
        for (var i = 0; i < subject_list.length; i++) {
          var subj_key = subject_list[i];
          // Create dataset for the subject
          var dataset = {
            label: subj_key.charAt(0).toUpperCase() + subj_key.slice(1),
            // Capitalize the label
            data: scoresData[subj_key],
            // Get the scores for the subject
            backgroundColor: "rgba(".concat(i * 60 % 255, ", ").concat((i * 100 + 100) % 255, ", ").concat(i * 150 % 255, ", 0.6)"),
            // Example color generation
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
  }]);
}(React.Component);