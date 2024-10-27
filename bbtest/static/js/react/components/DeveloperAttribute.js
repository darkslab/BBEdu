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
var DeveloperAttribute = /*#__PURE__*/function (_React$Component) {
  function DeveloperAttribute(props) {
    var _this;
    _classCallCheck(this, DeveloperAttribute);
    _this = _callSuper(this, DeveloperAttribute, [props]);
    _this.attribute_name = props.attribute_name;
    _this.label = props.label;
    _this.value = props.value;
    _this.data = props.data;
    _this.onChange = props.onChange;
    return _this;
  }
  _inherits(DeveloperAttribute, _React$Component);
  return _createClass(DeveloperAttribute, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      console.log(this.label);
      console.log(this.value);
      console.log(this.onChange);
      var label = this.label;
      var onChange = this.onChange;
      $('#' + this.attribute_name).select2({
        width: '50vw'
      });
      $('#' + this.attribute_name).on('select2:select', function (e) {
        var data = e.params.data;
        console.log(label);
        console.log(data);
        console.log(e);
        onChange(parseInt(data.id));
      });
    }
  }, {
    key: "render",
    value: function render() {
      // let caption = "";
      // let options = [];
      // for (let i = 0; i < this.data.length; i++) {
      //     const fullCaption = this.data[i].caption;
      //     const truncatedCaption = fullCaption.length > 100 ? `${fullCaption.slice(0, 100)}...` : fullCaption;

      //     if (this.value === this.data[i].value) {
      //         options.push(
      //             <li key={this.data[i].value} className="active">
      //                 <a href="javascript:void(0);" title={fullCaption}>
      //                     {truncatedCaption}
      //                 </a>
      //             </li>
      //         );
      //     } else {
      //         options.push(
      //             <li key={this.data[i].value}>
      //                 <a
      //                     href="javascript:void(0);"
      //                     onClick={this.onChange.bind(null, this.data[i].value)}
      //                     title={fullCaption}
      //                 >
      //                     {truncatedCaption}
      //                 </a>
      //             </li>
      //         );
      //     }
      // }

      var options_select2 = [];
      for (var i = 0; i < this.data.length; i++) {
        var fullCaption = this.data[i].caption;
        var truncatedCaption = fullCaption.length > 100 ? "".concat(fullCaption.slice(0, 100), "...") : fullCaption;
        options_select2.push( /*#__PURE__*/React.createElement("option", {
          key: this.data[i].value,
          title: fullCaption,
          value: this.data[i].value
        }, truncatedCaption));
      }
      return /*#__PURE__*/React.createElement("div", {
        className: this.value ? "form-group" : "form-group has-error"
      }, /*#__PURE__*/React.createElement("label", {
        className: "control-label col-sm-3 text-uppercase"
      }, this.label), /*#__PURE__*/React.createElement("div", {
        className: "col-sm-9"
      }, /*#__PURE__*/React.createElement("div", {
        className: "input-group"
      }, /*#__PURE__*/React.createElement("select", {
        id: this.attribute_name,
        className: "form-control bb-test-section-background pl-10"
        // data-placeholder={this.label}
        ,
        defaultValue: this.value,
        name: "filter_status",
        onChange: this.onChange.bind(null, function (event) {
          console.log(event);
          event.target.value;
        })
      }, options_select2))));
    }
  }]);
}(React.Component);