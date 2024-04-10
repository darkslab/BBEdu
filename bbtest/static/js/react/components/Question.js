"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _callSuper(t, o, e) { return o = _getPrototypeOf(o), _possibleConstructorReturn(t, _isNativeReflectConstruct() ? Reflect.construct(o, e || [], _getPrototypeOf(t).constructor) : o.apply(t, e)); }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { try { var t = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); } catch (t) {} return (_isNativeReflectConstruct = function _isNativeReflectConstruct() { return !!t; })(); }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _defineProperty(obj, key, value) { key = _toPropertyKey(key); if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : i + ""; }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
var Question = /*#__PURE__*/function (_React$Component) {
  function Question(props) {
    var _this;
    _classCallCheck(this, Question);
    _this = _callSuper(this, Question, [props]);
    _defineProperty(_this, "_startDrag", function (e) {
      // Assuming this.imageRef is directly the DOM element now
      var img = _this.imageRef;
      _this.setState({
        isDragging: true,
        dragStartX: e.clientX - _this.state.imgPosX,
        dragStartY: e.clientY - _this.state.imgPosY,
        dragStartTime: Date.now()
      });

      // Prevent image dragging behavior to allow custom handling
      if (img) {
        img.addEventListener('dragstart', function (e) {
          return e.preventDefault();
        });
      }
    });
    _defineProperty(_this, "_onDrag", function (e) {
      if (!_this.state.isDragging) return;
      _this.setState({
        imgPosX: e.clientX - _this.state.dragStartX,
        imgPosY: e.clientY - _this.state.dragStartY
      });
    });
    _defineProperty(_this, "_endDrag", function () {
      var dragEndTime = Date.now();
      var dragDuration = dragEndTime - _this.state.dragStartTime;
      // console.log(this.state.dragStartTime, dragEndTime, dragDuration)
      _this.setState({
        isDragging: false,
        dragStartTime: null // Reset the drag start time
      }, function () {
        // If the drag duration is less than 100ms, treat it as a click and close the overlay
        if (dragDuration < 200) {
          _this._closeOverlay();
        }
      });
    });
    _defineProperty(_this, "_openOverlay", function () {
      // Use this.overlayRef directly
      if (_this.overlayRef) {
        _this.overlayRef.style.display = 'flex';
      }
    });
    _defineProperty(_this, "_closeOverlay", function () {
      if (!_this.state.isDragging) {
        if (_this.overlayRef) {
          _this.overlayRef.style.display = 'none';
        }
      }
    });
    _defineProperty(_this, "_handleWheel", function (event) {
      // event.preventDefault();
      var zoomDelta = event.deltaY > 0 ? -0.1 : 0.1;
      _this.setState(function (prevState) {
        return {
          zoomLevel: Math.max(0.2, prevState.zoomLevel + zoomDelta)
        };
      });
    });
    _this.state = {
      originalText: "",
      rawHtml: "",
      zoomLevel: 1,
      isDragging: false,
      dragStartX: 0,
      dragStartY: 0,
      imgPosX: 0,
      imgPosY: 0,
      dragStartTime: null
    };

    // Using callback refs instead of createRef
    _this.overlayRef = null;
    _this.imageRef = null;

    // Set refs
    _this.setOverlayRef = function (element) {
      _this.overlayRef = element;
    };
    _this.setImageRef = function (element) {
      _this.imageRef = element;
    };
    return _this;
  }
  _inherits(Question, _React$Component);
  return _createClass(Question, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      // _load_calculator()
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      // _unload_calculator()
    }
  }, {
    key: "render",
    value: function render() {
      var paragraphs = [];
      for (var i = 0; i < this.props.object.paragraphs.length; i++) {
        var ParagraphClass = eval(this.props.object.paragraphs[i].paragraph_class);
        paragraphs.push( /*#__PURE__*/React.createElement(ParagraphClass, {
          key: i,
          data: this.props.object.paragraphs[i].meta_data,
          isShared: this.props.object.paragraphs[i].is_shared,
          texts: this.props.texts,
          testTexts: this.props.testTexts,
          forDevelopers: false
        }));
      }
      var timer = null;
      if (this.props.hasTimer) {
        var timerClassName = "fa fa-fw mr-10";
        var countDown = "--:--";
        if (this.props.secondsLeft >= 0) {
          countDown = parseInt(this.props.secondsLeft / 60, 10) + ":" + ("0" + this.props.secondsLeft % 60).substr(-2);
          timerClassName += " fa-clock-o";
        } else {
          timerClassName += " fa-refresh fa-spin";
        }
        var countDownClassName = "bb-test-timer label mt-0 mb-0 pull-right";
        if (this.props.secondsLeft > 10) {
          countDownClassName += " label-success";
        } else {
          countDownClassName += " label-danger";
        }
        timer = /*#__PURE__*/React.createElement("span", {
          className: countDownClassName
        }, /*#__PURE__*/React.createElement("i", {
          className: timerClassName
        }), countDown);
      }
      var periodicTable = null;
      console.log(this.prop);
      if (this.props.hasPeriodicTable & this.props.hasPeriodicTable.includes(this.props.count)) {
        var imgClassName = "img-responsive center-block bb-test-paragraph-image";
        periodicTable = /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("img", {
          className: imgClassName,
          src: this.props.periodicTableIconUrl,
          alt: "Thumbnail",
          onClick: this._openOverlay
        }), /*#__PURE__*/React.createElement("div", {
          ref: this.setOverlayRef // Updated to use setOverlayRef
          ,
          className: "periodicTableOverlay"
          // onClick={this._closeOverlay}
          ,
          onWheel: this._handleWheel,
          onMouseDown: this._startDrag,
          onMouseMove: this._onDrag,
          onMouseUp: this._endDrag
          // onMouseLeave={this._endDrag}
          ,
          style: {
            display: 'none'
          }
        }, /*#__PURE__*/React.createElement("img", {
          ref: this.setImageRef // Updated to use setImageRef
          ,
          id: "overlayPeriodicTableImage",
          src: this.props.periodicTableUrl,
          alt: "Large Image",
          style: {
            transform: "scale(".concat(this.state.zoomLevel, ") translate(").concat(this.state.imgPosX, "px, ").concat(this.state.imgPosY, "px)")
          }
        })));
      }
      var answerContent = null;
      if (this.props.object.answer_class) {
        var AnswerClass = eval(this.props.object.answer_class);
        answerContent = /*#__PURE__*/React.createElement(AnswerClass, {
          data: this.props.object.meta_data,
          answer: this.props.answerData,
          onUpdate: this.props.onAnswerUpdate,
          canAnswer: this.props.canAnswer,
          showCorrectAnswer: this.props.showCorrectAnswer,
          texts: this.props.texts
        });
      }
      return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-12"
      }, /*#__PURE__*/React.createElement("div", {
        className: "panel mb-15 panel-primary"
      }, /*#__PURE__*/React.createElement("div", {
        className: "panel-heading bb-rel clearfix"
      }, /*#__PURE__*/React.createElement("div", {
        className: "bb-test-number"
      }, this.props.count), /*#__PURE__*/React.createElement("h4", {
        className: "panel-title bb-test-title mt-15 mb-15 pull-left"
      }, this.props.texts.question, " (", this.props.object.meta_data.question_code, ")"), periodicTable, timer), /*#__PURE__*/React.createElement("div", {
        className: "panel-body"
      }, /*#__PURE__*/React.createElement("div", {
        className: "mb-15"
      }, paragraphs))))), answerContent);
    }
  }]);
}(React.Component);