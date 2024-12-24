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
    // this.props.student_name_list
    // this.props.parent_list
    // this.props.parent_to_children_list
    // this.props.parent_average_scores
    // this.props.parent_student_scores
    // this.props.parent_student_scores_by_difficulty
    // this.props.pisa_average_historic
    // this.props.polar_area_description
    // this.props.map_key_to_id
    // this.props.map_id_to_key
    // this.props.lang_django
    _this.state = {
      current_parent: "0rus",
      // this.props.map_key_to_id["Total"],
      current_children: _this.props.parent_to_children_list["0rus"][0],
      // this.props.map_key_to_id["Чтение"]
      current_language: "rus"
    };
    return _this;
  }
  _inherits(ChartDashboard, _React$Component);
  return _createClass(ChartDashboard, [{
    key: "updateParentTopicState",
    value: function updateParentTopicState(newTopic) {
      // console.log("updateParentTopicState", this.state);
      this.setState({
        current_children: newTopic
      });
      var topic_option_select = $("#subject-topic-select");
      topic_option_select.val(this.state.current_children).trigger("change");
    }
  }, {
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this2 = this;
      var option_select = $("#subject-select");
      option_select.select2({
        width: '100%'
      });
      option_select.val(this.state.current_parent).trigger("change");
      option_select.on('select2:select', function (event) {
        return _this2._selectParent(event);
      });
      var lang_option_select = $("#language-select");
      lang_option_select.select2({
        width: '100%'
      });
      // lang_option_select.val(this.state.current_children).trigger("change");
      lang_option_select.on('select2:select', function (event) {
        return _this2._selectLanguage(event);
      });
      var topic_option_select = $("#subject-topic-select");
      topic_option_select.select2({
        width: '50%'
      });
      topic_option_select.val(this.state.current_children).trigger("change");
      topic_option_select.on('select2:select', function (event) {
        return _this2._selectChild(event);
      });
    }
  }, {
    key: "render",
    value: function render() {
      var parent_list = this.props.parent_list[this.state.current_language];
      var map_id_to_key = this.props.map_id_to_key;
      console.log("this.props", this.props);
      var map_rus_kaz = {};
      map_rus_kaz["rus"] = {
        "Оқылым": "Чтение",
        "Математика (қазақ тілінде)": "Математика (на казахском)",
        "Жаратылыстану": "Естествознание"
      };
      map_rus_kaz["kaz"] = {
        "Чтение": "Оқылым",
        "Математика (на русском)": "Математика (орыс тілінде)",
        "Естествознание": "Жаратылыстану"
      };
      // console.log(map_rus_kaz)

      var options = [];
      for (var i = 0; i < parent_list.length; i++) {
        var parent_id = parent_list[i];
        var key = map_id_to_key[parent_id];
        var text = key in map_rus_kaz[this.props.lang_django] ? map_rus_kaz[this.props.lang_django][key] : key;
        options.push( /*#__PURE__*/React.createElement("option", {
          key: "option ".concat(parent_id),
          value: parent_id
        }, text));
      }
      var options_lang = [/*#__PURE__*/React.createElement("option", {
        key: "option rus}",
        value: "rus"
      }, this.props.lang_django == "rus" ? "Русский язык" : "Орыс тілі"), /*#__PURE__*/React.createElement("option", {
        key: "option kaz}",
        value: "kaz"
      }, this.props.lang_django == "rus" ? "Казахский язык" : "Қазақ тілі")];

      // Polar Area chart compute
      var polar_area_chart_labels_id = this.props.parent_to_children_list[this.state.current_parent];
      var polar_area_chart_labels = [];
      var polar_area_chart_data = [];
      for (var _i = 0; _i < polar_area_chart_labels_id.length; _i++) {
        var index_id = polar_area_chart_labels_id[_i];
        polar_area_chart_data.push(this.props.parent_average_scores[index_id]);
        polar_area_chart_labels.push(this.props.map_id_to_key[index_id]);
      }
      var selected_children_topic_average = this.props.parent_average_scores[this.state.current_children];
      var selected_parent_average = this.props.parent_average_scores[this.state.current_parent];
      var current_subtopic_list = this.props.parent_to_children_list[this.state.current_children];
      var subtopic_list_html = [];
      for (var _i2 = 0; _i2 < current_subtopic_list.length; _i2++) {
        var subchild_id = current_subtopic_list[_i2];
        subtopic_list_html.push( /*#__PURE__*/React.createElement("li", {
          key: "subchild_option ".concat(subchild_id),
          value: subchild_id
        }, map_id_to_key[subchild_id]));
      }
      var selected_children_list = this.props.parent_to_children_list[this.state.current_parent];
      var child_options = [];
      for (var _i3 = 0; _i3 < selected_children_list.length; _i3++) {
        var child_id = selected_children_list[_i3];
        child_options.push( /*#__PURE__*/React.createElement("option", {
          key: "topic_option ".concat(child_id),
          value: child_id
        }, map_id_to_key[child_id]));
      }
      // console.log("topic_list_html", topic_list_html)

      var recommend = null;
      if (this.state.current_children.length == 5 | this.state.current_children.length == 7) {
        if (parseFloat(selected_children_topic_average) <= 200) {
          recommend = /*#__PURE__*/React.createElement("div", {
            dangerouslySetInnerHTML: {
              __html: this.props.polar_area_recomend_description[this.state.current_language][this.state.current_children][0]
            }
          });
        } else if (parseFloat(selected_children_topic_average) <= 400) {
          recommend = /*#__PURE__*/React.createElement("div", {
            dangerouslySetInnerHTML: {
              __html: this.props.polar_area_recomend_description[this.state.current_language][this.state.current_children][200]
            }
          });
        } else {
          recommend = /*#__PURE__*/React.createElement("div", {
            dangerouslySetInnerHTML: {
              __html: this.props.polar_area_recomend_description[this.state.current_language][this.state.current_children][400]
            }
          });
        }
      }
      // console.log("recommend", this.state.current_children, recommend)

      return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(FloatingSelector, {
        id: ["subject-select", "language-select"],
        title: ["Предмет", "Язык"],
        options: [options, options_lang]
      }), /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12",
        style: {
          minWidth: "900px"
        }
      }, /*#__PURE__*/React.createElement("div", {
        className: "row panel panel-default"
      }, /*#__PURE__*/React.createElement("p", {
        className: "h3",
        style: {
          textAlign: "center"
        }
      }, this.props.texts.graph_total_title), /*#__PURE__*/React.createElement("p", {
        style: {
          textAlign: "center"
        }
      }, this.props.texts.graph_total_description), /*#__PURE__*/React.createElement(ChartTotal, {
        student_name_list: this.props.student_name_list[this.state.current_language],
        selected_parent: this.state.current_parent,
        selected_language: this.state.current_language,
        selected_children_list: selected_children_list,
        parent_student_scores: this.props.parent_student_scores[this.state.current_language],
        map_id_to_key: this.props.map_id_to_key,
        subject_chart_height: this.props.subject_chart_height
      })), this.state.current_parent.length == 5 ? /*#__PURE__*/React.createElement("div", {
        className: "row panel panel-default"
      }, /*#__PURE__*/React.createElement("p", {
        className: "h3",
        style: {
          textAlign: "center"
        }
      }, this.props.texts.graph_difficulty_title), /*#__PURE__*/React.createElement("p", {
        style: {
          textAlign: "center"
        }
      }, this.props.texts.graph_difficulty_description), /*#__PURE__*/React.createElement(ChartMultiBarHorizontal, {
        data: this.props.parent_student_scores_by_difficulty[this.state.current_language][this.state.current_parent],
        data_label_list: ["Базовый", "Средний", "Высокий"],
        row_label_list: this.props.student_name_list[this.state.current_language],
        props_update_indicator: "".concat(this.state.current_parent, "+").concat(this.state.current_language),
        map_id_to_key: this.props.map_id_to_key,
        subject_chart_height: this.props.subject_chart_height
      })) : null, /*#__PURE__*/React.createElement("div", {
        className: "row panel panel-default"
      }, /*#__PURE__*/React.createElement("p", {
        className: "h3",
        style: {
          textAlign: "center"
        }
      }, this.props.texts.graph_polararea_title), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-lg-6"
      }, /*#__PURE__*/React.createElement(ChartPolarArea, {
        selected_parent: this.state.current_parent,
        selected_children: this.state.current_children,
        polar_area_chart_labels_id: polar_area_chart_labels_id,
        polar_area_chart_labels: polar_area_chart_labels,
        polar_area_chart_data: polar_area_chart_data,
        map_id_to_key: this.props.map_id_to_key,
        updateParentTopicState: this.updateParentTopicState.bind(this)
      })), /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12 col-lg-6"
      }, /*#__PURE__*/React.createElement("select", {
        className: "select_v2",
        id: "subject-topic-select",
        style: {
          maxWidth: "300px"
        }
      }, child_options), /*#__PURE__*/React.createElement("div", {
        dangerouslySetInnerHTML: {
          __html: this.props.polar_area_common_description[this.state.current_language][this.state.current_children]
        }
      }), recommend)), /*#__PURE__*/React.createElement("div", {
        className: "panel panel-default",
        style: {
          minHeight: "300px"
        }
      }, /*#__PURE__*/React.createElement("div", {
        className: "row",
        style: {
          textAlign: "center"
        }
      }, /*#__PURE__*/React.createElement("h3", {
        style: {
          textAlign: "center"
        }
      }, this.props.texts.graph_monitoring_title), /*#__PURE__*/React.createElement("div", {
        className: "text-center",
        style: {
          textAlign: "center"
        }
      }, /*#__PURE__*/React.createElement("p", null, this.props.texts.graph_monitoring_description1), /*#__PURE__*/React.createElement(ChartProgressBar, {
        scores_data: [selected_parent_average, 0, 0, 0, 0],
        y_max: this.state.current_parent.length === 4 ? 600 * 3 : 600,
        averageScore: this.props.pisa_average_historic[this.state.current_parent],
        props_update_indicator: "".concat(this.state.current_parent, "+").concat(this.state.current_language)
      }), /*#__PURE__*/React.createElement("p", {
        style: {
          fontStyle: 'italic',
          fontSize: '14px',
          color: '#666'
        }
      }, this.props.texts.graph_monitoring_description2))))), /*#__PURE__*/React.createElement("div", {
        className: "col-lg-3"
      })));
    }
  }, {
    key: "_selectParent",
    value: function _selectParent(e) {
      var data = e.params.data;
      var selectedIndex = data.id;
      var current_language = this.state.current_language;

      // console.log("_selectSubject", data, selectedIndex, this.props.parent_list[this.state.current_language][selectedIndex])
      this.setState({
        current_parent: selectedIndex,
        current_children: this.props.parent_to_children_list[selectedIndex][0]
      });
    }
  }, {
    key: "_selectChild",
    value: function _selectChild(e) {
      var data = e.params.data;
      var selectedIndex = data.id;
      this.setState({
        current_children: selectedIndex
      });
    }
  }, {
    key: "_selectLanguage",
    value: function _selectLanguage(e) {
      var data = e.params.data;
      var new_lang = data.id;
      // const new_parrent = this.state.current_parent.slice(0, -3) + new_lang;
      var new_parrent = "0".concat(new_lang);
      var new_children = this.props.parent_to_children_list[new_parrent][0];
      // const selectedIndex = data.id;
      // console.log(data, data.id)
      // console.log("_selectLanguage", {
      //     current_language: new_lang,
      //     current_parent: new_parrent,
      //     current_children: new_children,
      // })

      this.setState({
        current_language: new_lang,
        current_parent: new_parrent,
        current_children: new_children
      });
    }
  }]);
}(React.Component);