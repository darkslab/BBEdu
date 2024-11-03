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
    return _callSuper(this, ChartPolarArea, [props]);
  }
  _inherits(ChartPolarArea, _React$Component);
  return _createClass(ChartPolarArea, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      // $("#subject-select").select2({
      //     width: '20vw',
      // });

      var subject_list = this.props.subject_list;
      var scoresData = this.props.scoresData;
      var subject_topics = this.props.subject_topics;
      var subject_scores = this.props.subject_scores;
      var ctx_doughnut = document.getElementById('myDoughnutChart').getContext('2d');
      var doughnutData = {
        labels: [],
        datasets: [{
          data: [],
          backgroundColor: ['#3498db', '#1abc9c', '#9b59b6', '#f39c12', '#e74c3c'],
          borderColor: '#ffffff',
          borderWidth: 2
        }]
      };
      var doughnutOptions = {
        responsive: false,
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
            var label = myDoughnutChart.data.labels[segmentIndex];
            var value = myDoughnutChart.data.datasets[0].data[segmentIndex];

            // Do something with the clicked segment information
            console.log("Clicked on segment: ".concat(label, ", Value: ").concat(value));
            alert("Clicked on ".concat(label, " with value ").concat(value));
          }
        }
      };
      var myDoughnutChart = new Chart(ctx_doughnut, {
        type: 'polarArea',
        data: doughnutData,
        options: doughnutOptions
        // plugins: [ChartDataLabels] // Add the data labels plugin
      });

      // --------------------------------------------------------------------------------------------------------------------------
      this._update_doughnut_chart(myDoughnutChart, "Total", subject_topics, subject_scores);
    }
  }, {
    key: "render",
    value: function render() {
      var subject_list = this.props.subject_list;
      // const options = [];
      // for (let i = 0; i < subject_list.length; i++) {
      //     options.push(<option key={`option ${i}`} value={{ i }} >{subject_list[i]}</option>)
      // }
      // {% for subj in subject_list %}
      //         
      //       {% endfor %}

      return /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("h2", {
        style: {
          textAlign: "center"
        }
      }, "Student Average Results"), /*#__PURE__*/React.createElement("div", {
        className: "col-lg-3"
      }), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-lg-3"
      }, /*#__PURE__*/React.createElement("canvas", {
        id: "myDoughnutChart",
        width: "400",
        height: "400"
      })), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-lg-3"
      }, /*#__PURE__*/React.createElement("button", {
        style: {
          backgroundColor: "#3498db",
          color: "white",
          padding: "10px 20px",
          border: "none"
        }
      }, "\u0420\u0410\u0426\u0418\u041E\u041D\u0410\u041B\u042C\u041D\u042B\u0415 \u0427\u0418\u0421\u041B\u0410"), /*#__PURE__*/React.createElement("p", null, /*#__PURE__*/React.createElement("strong", null, "\u0412\u044B \u043E\u0442\u0432\u0435\u0442\u0438\u043B\u0438 \u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u043E \u043D\u0430 12 \u0432\u043E\u043F\u0440\u043E\u0441\u043E\u0432 (120 \u0431\u0430\u043B\u043B\u043E\u0432) \u0438\u0437 12 \u043F\u043E \u0434\u0430\u043D\u043D\u043E\u043C\u0443 \u0440\u0430\u0437\u0434\u0435\u043B\u0443")), /*#__PURE__*/React.createElement("ul", null, /*#__PURE__*/React.createElement("li", null, "\u041F\u043E\u043B\u043E\u0436\u0438\u0442\u0435\u043B\u044C\u043D\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u041E\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043B\u044C\u043D\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u041A\u043E\u043E\u0440\u0434\u0438\u043D\u0430\u0442\u043D\u0430\u044F \u043F\u0440\u044F\u043C\u0430\u044F."), /*#__PURE__*/React.createElement("li", null, "\u041F\u0440\u043E\u0442\u0438\u0432\u043E\u043F\u043E\u043B\u043E\u0436\u043D\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u0426\u0435\u043B\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u0420\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u041C\u043E\u0434\u0443\u043B\u044C \u0447\u0438\u0441\u043B\u0430."), /*#__PURE__*/React.createElement("li", null, "\u0421\u0440\u0430\u0432\u043D\u0435\u043D\u0438\u0435 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B. \u0421\u043B\u043E\u0436\u0435\u043D\u0438\u0435 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B \u0441 \u043F\u043E\u043C\u043E\u0449\u044C\u044E \u043A\u043E\u043E\u0440\u0434\u0438\u043D\u0430\u0442\u043D\u043E\u0439 \u043F\u0440\u044F\u043C\u043E\u0439."), /*#__PURE__*/React.createElement("li", null, "\u0421\u043B\u043E\u0436\u0435\u043D\u0438\u0435 \u043E\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043B\u044C\u043D\u044B\u0445 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B. \u0421\u043B\u043E\u0436\u0435\u043D\u0438\u0435 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B \u0441 \u0440\u0430\u0437\u043D\u044B\u043C\u0438 \u0437\u043D\u0430\u043A\u0430\u043C\u0438. \u0412\u044B\u0447\u0438\u0442\u0430\u043D\u0438\u0435 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B."), /*#__PURE__*/React.createElement("li", null, "\u0420\u0430\u0441\u0441\u0442\u043E\u044F\u043D\u0438\u0435 \u043C\u0435\u0436\u0434\u0443 \u0442\u043E\u0447\u043A\u0430\u043C\u0438 \u043D\u0430 \u043A\u043E\u043E\u0440\u0434\u0438\u043D\u0430\u0442\u043D\u043E\u0439 \u043F\u0440\u044F\u043C\u043E\u0439."))));
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
    // Function to update doughnut chart based on selected subject
  }, {
    key: "_update_doughnut_chart",
    value: function _update_doughnut_chart(myChart, selectedSubject, subject_topics, subject_scores) {
      // Update labels and data for the doughnut chart
      myChart.data.labels = subject_topics[selectedSubject];
      myChart.data.datasets[0].data = subject_scores[selectedSubject];

      // Update the doughnut chart display
      myChart.update();
    }
  }]);
}(React.Component);