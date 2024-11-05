"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
var _excluded = ["left_side"];
function ownKeys(e, r) { var t = Object.keys(e); if (Object.getOwnPropertySymbols) { var o = Object.getOwnPropertySymbols(e); r && (o = o.filter(function (r) { return Object.getOwnPropertyDescriptor(e, r).enumerable; })), t.push.apply(t, o); } return t; }
function _objectSpread(e) { for (var r = 1; r < arguments.length; r++) { var t = null != arguments[r] ? arguments[r] : {}; r % 2 ? ownKeys(Object(t), !0).forEach(function (r) { _defineProperty(e, r, t[r]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) { Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r)); }); } return e; }
function _defineProperty(obj, key, value) { key = _toPropertyKey(key); if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _objectWithoutProperties(source, excluded) { if (source == null) return {}; var target = _objectWithoutPropertiesLoose(source, excluded); var key, i; if (Object.getOwnPropertySymbols) { var sourceSymbolKeys = Object.getOwnPropertySymbols(source); for (i = 0; i < sourceSymbolKeys.length; i++) { key = sourceSymbolKeys[i]; if (excluded.indexOf(key) >= 0) continue; if (!Object.prototype.propertyIsEnumerable.call(source, key)) continue; target[key] = source[key]; } } return target; }
function _objectWithoutPropertiesLoose(source, excluded) { if (source == null) return {}; var target = {}; var sourceKeys = Object.keys(source); var key, i; for (i = 0; i < sourceKeys.length; i++) { key = sourceKeys[i]; if (excluded.indexOf(key) >= 0) continue; target[key] = source[key]; } return target; }
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
var DeveloperImageParagraph = /*#__PURE__*/function (_React$Component) {
  function DeveloperImageParagraph(props) {
    var _this;
    _classCallCheck(this, DeveloperImageParagraph);
    _this = _callSuper(this, DeveloperImageParagraph, [props]);
    _this.state = {
      confirmModal: false,
      isErrored: false
    };
    _this._fileInput;
    _this._$fileInput;
    _this._$xhr;
    _this._xhrData = [];
    _this._adoptCheckTimer;
    _this._adoptCheckTimerInterval = 2000;
    _this._boundFileInputChanged = _this._fileInputChanged.bind(_this);
    return _this;
  }
  _inherits(DeveloperImageParagraph, _React$Component);
  return _createClass(DeveloperImageParagraph, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      this._$fileInput = $(this._fileInput);
      this._$fileInput.on("change", this._boundFileInputChanged);
    }
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      if (this._$fileInput) {
        this._$fileInput.off("change", this._boundFileInputChanged);
        this._$fileInput = undefined;
      }
      if (this._$xhr) {
        this._$xhr.abort();
        this._$xhr = undefined;
        this._xhrData.pop();
      }
      clearTimeout(this._adoptCheckTimer);
    }
  }, {
    key: "render",
    value: function render() {
      var _this2 = this;
      var uploadId = "upload_" + this.props.paragraphId;
      var buttons = [];
      if (this.props.canDelete) {
        buttons.push( /*#__PURE__*/React.createElement("button", {
          key: "delete",
          type: "button",
          className: "btn btn-danger btn-xs pull-right ml-5",
          onClick: this._renderModal.bind(this)
        }, /*#__PURE__*/React.createElement("i", {
          className: "fa fa-fw fa-times"
        })));
      }
      buttons.push( /*#__PURE__*/React.createElement("button", {
        key: "left_side",
        type: "button",
        className: "btn btn-xs pull-right ml-5 btn-default",
        onClick: this._handleLeftSide.bind(this)
      }, this.props.data.left_side | this.props.data.left_side === undefined ? this.props.texts.controlLeftSideButton : this.props.texts.controlRightSideButton));
      var modal = null;
      if (this.state.confirmModal) {
        modal = /*#__PURE__*/React.createElement(ConfirmModal, {
          title: this.props.texts.deleteModalTitle,
          yesCaption: this.props.texts.deleteModalYesCaption,
          noCaption: this.props.texts.deleteModalNoCaption,
          isInverse: true,
          complete: this._completeModal.bind(this)
        });
      }
      var label = null;
      if (this.props.data.status === "waiting" || this.state.isErrored) {
        var errorMessage = null;
        if (this.state.isErrored) {
          errorMessage = /*#__PURE__*/React.createElement("p", {
            className: "text-danger text-center"
          }, this.props.texts.paragraphsImageErrorImageParagraph);
        }
        label = /*#__PURE__*/React.createElement(React.Fragment, null, errorMessage, /*#__PURE__*/React.createElement("label", {
          htmlFor: uploadId,
          className: "btn btn-success btn-lg btn-block mt-23",
          "data-bb-non-sortable": true
        }, this.props.texts.paragraphsUploadButtonImageParagraph));
      } else if (this.props.data.status === "starting" || this.props.data.status === "uploading") {
        var labelStyle = {
          width: this.props.data.progress + "%"
        };
        label = /*#__PURE__*/React.createElement("div", {
          className: "bb-test-paragraph-progress progress progress-striped active mt-23",
          "data-bb-non-sortable": true
        }, /*#__PURE__*/React.createElement("div", {
          className: "progress-bar",
          style: labelStyle
        }));
      } else if (this.props.data.status === "completing" || this.props.data.status === "adopting") {
        label = /*#__PURE__*/React.createElement("div", {
          className: "mt-23 text-center"
        }, /*#__PURE__*/React.createElement("i", {
          className: "fa fa-fw fa-spin fa-refresh bb-test-paragraph-image-processing-icon",
          "data-bb-non-sortable": true
        }));
      } else if (this.props.data.status === "staring") {
        label = /*#__PURE__*/React.createElement("p", {
          className: "lead text-center mt-23 mb-0"
        }, this.props.texts.paragraphsImagePreviewImageParagraph);
      }
      return /*#__PURE__*/React.createElement(React.Fragment, null, modal, /*#__PURE__*/React.createElement("div", {
        className: "form-group bb-test-section-movable bb-test-section-background",
        "data-paragraph-id": this.props.paragraphId
      }, /*#__PURE__*/React.createElement("div", {
        className: "pt-5 pr-5 pb-5 pl-5 clearfix"
      }, buttons, /*#__PURE__*/React.createElement("button", {
        type: "button",
        className: "btn btn-default btn-xs pull-right ml-5 invisible"
      }, "Spacer")), /*#__PURE__*/React.createElement("div", {
        className: "bb-test-paragraph bb-test-paragraph-upload"
      }, /*#__PURE__*/React.createElement("div", {
        className: "row"
      }, /*#__PURE__*/React.createElement("div", {
        className: "col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3"
      }, label, /*#__PURE__*/React.createElement("input", {
        id: uploadId,
        className: "hidden",
        type: "file",
        accept: "image/*",
        ref: function ref(input) {
          _this2._fileInput = input;
        }
      }))))));
    }
  }, {
    key: "_renderModal",
    value: function _renderModal() {
      this.setState({
        confirmModal: true
      });
    }
  }, {
    key: "_handleLeftSide",
    value: function _handleLeftSide() {
      var _this$props$data = this.props.data,
        left_side = _this$props$data.left_side,
        data = _objectWithoutProperties(_this$props$data, _excluded);
      if (left_side === undefined) {
        data.left_side = false;
      } else {
        data.left_side = !left_side;
      }
      this.props.onChange(data);
    }
  }, {
    key: "_completeModal",
    value: function _completeModal(data) {
      if (data) {
        this.props.onDelete();
      } else {
        this.setState({
          confirmModal: false
        });
      }
    }
  }, {
    key: "_fileInputChanged",
    value: function _fileInputChanged(event) {
      var $fileInput = $(event.currentTarget);
      if (!$fileInput[0].files.length || this._$xhr) {
        return;
      }
      this._$xhr = $.post({
        url: this.props.data.upload_start_url,
        headers: {
          "X-CSRFToken": Cookies.get("csrftoken")
        },
        data: {
          file_name: $fileInput[0].files[0].name,
          file_size: $fileInput[0].files[0].size,
          file_type: $fileInput[0].files[0].type,
          upload_starter: JSON.stringify({
            name: "image_paragraph_upload_starter"
          })
        },
        success: this._ajaxSuccess.bind(this, "starting"),
        error: this._ajaxError.bind(this, "starting")
      });
      this._xhrData.push({
        file: $fileInput[0].files[0]
      });
      this.setState({
        isErrored: false
      });
      this._changeStatus("starting");
    }
  }, {
    key: "_ajaxSuccess",
    value: function _ajaxSuccess(type, data, status, $xhr) {
      var xhrData;
      switch (type) {
        case "starting":
          xhrData = this._xhrData.pop();
          this._$xhr = $.ajax({
            type: "PUT",
            url: data.upload_url,
            data: xhrData.file,
            success: this._ajaxSuccess.bind(this, "uploading"),
            error: this._ajaxError.bind(this, "uploading"),
            xhr: function () {
              var xhr = $.ajaxSettings.xhr();
              if (xhr.upload) {
                xhr.upload.addEventListener("progress", this._uploadProgress.bind(this), false);
              }
              return xhr;
            }.bind(this),
            cache: false,
            contentType: false,
            processData: false
          });
          this._xhrData.push({
            complete_url: data.complete_url
          });
          this._changeStatus("uploading", 0);
          break;
        case "uploading":
          xhrData = this._xhrData.pop();
          this._$xhr = $.post({
            url: xhrData.complete_url,
            headers: {
              "X-CSRFToken": Cookies.get("csrftoken")
            },
            success: this._ajaxSuccess.bind(this, "completing"),
            error: this._ajaxError.bind(this, "completing")
          });
          this._changeStatus("completing");
          break;
        case "completing":
          if (!data.success) {
            this._errorOut();
            return;
          }
          this._xhrData.push({
            adopt_url: data.adopt_url
          });
          this._scheduleAdoptCheck();
          this._changeStatus("adopting");
          break;
        case "adopting":
          if (!data.success) {
            if (data.broken) {
              this._errorOut();
              return;
            }
            this._scheduleAdoptCheck();
            return;
          }
          this._changeStatus("staring", data);
          break;
      }
    }
  }, {
    key: "_ajaxError",
    value: function _ajaxError(type, $xhr, status, error) {
      if (status === "abort") {
        return;
      }
      this._errorOut();
    }
  }, {
    key: "_changeStatus",
    value: function _changeStatus(status, options) {
      var data = _objectSpread({}, this.props.data);
      data.status = status;
      if (options) {
        switch (status) {
          case "uploading":
            data.progress = options;
            break;
          case "staring":
            data.asset_uuid = options.asset_uuid;
            data.asset_url = options.asset_url;
            break;
        }
      }
      var skipSave = true;
      if (data.status === "staring") {
        skipSave = false;
      }
      this.props.onChange(data, skipSave);
    }
  }, {
    key: "_uploadProgress",
    value: function _uploadProgress(event) {
      if (!event.lengthComputable) {
        return;
      }
      if (this.props.data.status !== "uploading") {
        return;
      }
      this._changeStatus("uploading", Math.min(Math.round(event.loaded / event.total * 100), 100));
    }
  }, {
    key: "_scheduleAdoptCheck",
    value: function _scheduleAdoptCheck() {
      clearTimeout(this._adoptCheckTimer);
      this._adoptCheckTimer = setTimeout(function () {
        var xhrData = this._xhrData.pop();
        this._$xhr = $.post({
          url: xhrData.adopt_url,
          headers: {
            "X-CSRFToken": Cookies.get("csrftoken")
          },
          data: {
            data: JSON.stringify({
              monkey: "shmonkey!"
            })
          },
          success: this._ajaxSuccess.bind(this, "adopting"),
          error: this._ajaxError.bind(this, "adopting")
        });
        this._xhrData.push({
          adopt_url: xhrData.adopt_url
        });
      }.bind(this), this._adoptCheckTimerInterval);
    }
  }, {
    key: "_errorOut",
    value: function _errorOut() {
      this.setState({
        isErrored: true
      });
      this._$xhr = undefined;
      this._xhrData.pop();
      var data = _objectSpread({}, this.props.data);
      data.progress = 0;
      this.props.onChange(data, true);
    }
  }]);
}(React.Component);