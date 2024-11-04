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
    var _this;
    _classCallCheck(this, ChartDashboard);
    _this = _callSuper(this, ChartDashboard, [props]);
    _this.state = {
      current_subject: "Total"
    };
    return _this;
  }
  _inherits(ChartDashboard, _React$Component);
  return _createClass(ChartDashboard, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this2 = this;
      var option_select = $("#subject-select");
      option_select.select2({
        width: '20vw'
      });
      // option_select.on('select2:select', function (e) {
      //     var data = e.params.data;
      //     const selectedIndex = parseInt(data.id);
      //     const selectedSubject = data.text;
      //     console.log(data, selectedIndex, selectedSubject);
      //     update_chart(myChart, selectedIndex, selectedSubject, subject_list, scores_data);
      //     // update_doughnut_chart(selectedSubject); // Update doughnut chart with selected subject
      // });
      option_select.on('select2:select', function (event) {
        return _this2._selectSubject(event);
      });

      // setTimeout(() => {
      //     console.log("timeout", this.props.subject_list[1])
      //     this.setState({
      //         current_subject: this.props.subject_list[1]
      //     })
      // }, 2000);
    }
  }, {
    key: "render",
    value: function render() {
      var subject_list = this.props.subject_list;
      var options = [];
      for (var i = 0; i < subject_list.length; i++) {
        options.push( /*#__PURE__*/React.createElement("option", {
          key: "option ".concat(i + 1),
          value: i + 1
        }, subject_list[i]));
      }
      return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("div", {
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
        key: "option 0",
        value: "0"
      }, "Total"), options)), /*#__PURE__*/React.createElement(ChartTotal, {
        subject_list: this.props.subject_list,
        scores_data: this.props.scores_data,
        selected_subject: this.state.current_subject,
        students: this.props.students
      }))), ";", /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("h2", {
        style: {
          textAlign: "center"
        }
      }, "Student Average Results"), /*#__PURE__*/React.createElement("div", {
        className: "col-lg-3"
      }), /*#__PURE__*/React.createElement(ChartPolarArea, {
        subject_list: this.props.subject_list,
        scores_data: this.props.scores_data,
        subject_topics: this.props.subject_topics,
        subject_scores: this.props.subject_scores,
        selected_subject: this.state.current_subject,
        students: this.props.students
      }), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-lg-3"
      }, /*#__PURE__*/React.createElement("button", {
        style: {
          backgroundColor: "#3498db",
          color: "white",
          padding: "10px 20px",
          border: "none"
        }
      }, "\u0420\u0410\u0426\u0418\u041E\u041D\u0410\u041B\u042C\u041D\u042B\u0415 \u0427\u0418\u0421\u041B\u0410"), /*#__PURE__*/React.createElement("p", null, /*#__PURE__*/React.createElement("strong", null, "\u0412\u044B \u043E\u0442\u0432\u0435\u0442\u0438\u043B\u0438 \u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u043E \u043D\u0430 12 \u0432\u043E\u043F\u0440\u043E\u0441\u043E\u0432 (120 \u0431\u0430\u043B\u043B\u043E\u0432) \u0438\u0437 12 \u043F\u043E \u0434\u0430\u043D\u043D\u043E\u043C\u0443 \u0440\u0430\u0437\u0434\u0435\u043B\u0443")), /*#__PURE__*/React.createElement("ul", null, /*#__PURE__*/React.createElement("li", null, "\u041F\u043E\u043B\u043E\u0436\u0438\u0442\u0435\u043B\u044C\u043D\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u041E\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043B\u044C\u043D\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u041A\u043E\u043E\u0440\u0434\u0438\u043D\u0430\u0442\u043D\u0430\u044F \u043F\u0440\u044F\u043C\u0430\u044F."), /*#__PURE__*/React.createElement("li", null, "\u041F\u0440\u043E\u0442\u0438\u0432\u043E\u043F\u043E\u043B\u043E\u0436\u043D\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u0426\u0435\u043B\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u0420\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0435 \u0447\u0438\u0441\u043B\u0430. \u041C\u043E\u0434\u0443\u043B\u044C \u0447\u0438\u0441\u043B\u0430."), /*#__PURE__*/React.createElement("li", null, "\u0421\u0440\u0430\u0432\u043D\u0435\u043D\u0438\u0435 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B. \u0421\u043B\u043E\u0436\u0435\u043D\u0438\u0435 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B \u0441 \u043F\u043E\u043C\u043E\u0449\u044C\u044E \u043A\u043E\u043E\u0440\u0434\u0438\u043D\u0430\u0442\u043D\u043E\u0439 \u043F\u0440\u044F\u043C\u043E\u0439."), /*#__PURE__*/React.createElement("li", null, "\u0421\u043B\u043E\u0436\u0435\u043D\u0438\u0435 \u043E\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043B\u044C\u043D\u044B\u0445 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B. \u0421\u043B\u043E\u0436\u0435\u043D\u0438\u0435 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B \u0441 \u0440\u0430\u0437\u043D\u044B\u043C\u0438 \u0437\u043D\u0430\u043A\u0430\u043C\u0438. \u0412\u044B\u0447\u0438\u0442\u0430\u043D\u0438\u0435 \u0440\u0430\u0446\u0438\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0445 \u0447\u0438\u0441\u0435\u043B."), /*#__PURE__*/React.createElement("li", null, "\u0420\u0430\u0441\u0441\u0442\u043E\u044F\u043D\u0438\u0435 \u043C\u0435\u0436\u0434\u0443 \u0442\u043E\u0447\u043A\u0430\u043C\u0438 \u043D\u0430 \u043A\u043E\u043E\u0440\u0434\u0438\u043D\u0430\u0442\u043D\u043E\u0439 \u043F\u0440\u044F\u043C\u043E\u0439.")))), /*#__PURE__*/React.createElement(ChartProgressBar, {
        scores_data: [200, 250, 180, 220, 0, 0, 0, 0, 0, 0],
        averageScore: 200
      }));
    }
  }, {
    key: "_selectSubject",
    value: function _selectSubject(e) {
      var data = e.params.data;
      var selectedIndex = parseInt(data.id);
      if (selectedIndex == 0) {
        this.setState({
          current_subject: "Total"
        });
        return;
      }
      console.log(data, this.props.subject_list[selectedIndex - 1]);
      this.setState({
        current_subject: this.props.subject_list[selectedIndex - 1]
      });
    }
  }]);
}(React.Component);