"use strict";

function _callSuper(t, o, e) { return o = _getPrototypeOf(o), _possibleConstructorReturn(t, _isNativeReflectConstruct() ? Reflect.construct(o, e || [], _getPrototypeOf(t).constructor) : o.apply(t, e)); }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { try { var t = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); } catch (t) {} return (_isNativeReflectConstruct = function _isNativeReflectConstruct() { return !!t; })(); }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : i + ""; }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
function SimpleFormattedFragment(text) {
  var formats = [{
    regex: /\*{2}(?:(?:[^\s\*][^\*]*?[^\s\*])|[^\s\*])\*{2}/g,
    "class": _BoldFormattedNestedSet
  }, {
    regex: /~{2}(?:(?:[^\s~][^~]*?[^\s~])|[^\s~])~{2}/g,
    "class": _ItalicFormattedNestedSet
  }, {
    regex: /_{2}(?:(?:[^\s_][^_]*?[^\s_])|[^\s_])_{2}/g,
    "class": _UnderlinedFormattedNestedSet
  }];
  var contents = [];
  text = text.replace(/\r/g, "");
  text = $.trim(text);
  text = text.replace(/\n\s+\n/g, "\n\n");
  var paragraphs = text.split("\n\n");
  for (var i = 0; i < paragraphs.length; i++) {
    paragraphs[i] = $.trim(paragraphs[i]);
    var rootNestedSet = new _RootFormattedNestedSet(paragraphs[i], 0, paragraphs[i].length - 1, i + 1 === paragraphs.length);
    for (var j = 0; j < formats.length; j++) {
      var match = void 0;
      while (match = formats[j].regex.exec(paragraphs[i])) {
        var nestedSet = new formats[j]["class"](paragraphs[i], match.index, match.index + match[0].length - 1);
        if (rootNestedSet.canContain(nestedSet)) {
          rootNestedSet.addSet(nestedSet);
        }
      }
    }
    contents.push( /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, rootNestedSet.content()));
  }
  return /*#__PURE__*/React.createElement(React.Fragment, null, contents);
}
var _FormattedNestedSet = /*#__PURE__*/function () {
  function _FormattedNestedSet(string, startPos, endPos) {
    _classCallCheck(this, _FormattedNestedSet);
    this._string = string;
    this._start = startPos;
    this._end = endPos;
    this._innerSets = [];
  }
  return _createClass(_FormattedNestedSet, [{
    key: "start",
    value: function start() {
      return this._start;
    }
  }, {
    key: "end",
    value: function end() {
      return this._end;
    }
  }, {
    key: "content",
    value: function content() {
      var ranges = [];
      ranges.push({
        start: this.start() + this.delimiterLength(),
        end: undefined
      });
      for (var i = 0; i < this._innerSets.length; i++) {
        ranges[ranges.length - 1].end = this._innerSets[i].start();
        ranges.push(this._innerSets[i]);
        ranges.push({
          start: this._innerSets[i].end() + 1,
          end: undefined
        });
        this._innerSets[i];
      }
      ranges[ranges.length - 1].end = this.end() - this.delimiterLength() + 1;
      var elems = [];
      for (var _i = 0; _i < ranges.length; _i++) {
        if (ranges[_i] instanceof _FormattedNestedSet) {
          elems.push( /*#__PURE__*/React.createElement(React.Fragment, {
            key: _i
          }, ranges[_i].content()));
        } else {
          var string = this._string.substring(ranges[_i].start, ranges[_i].end);
          if (string.length) {
            var parts = string.split("  \n");
            if (parts.length > 1) {
              string = [];
              var j = 0;
              string.push( /*#__PURE__*/React.createElement(React.Fragment, {
                key: j++
              }, parts.shift()));
              var part = void 0;
              while (part = parts.shift()) {
                string.push( /*#__PURE__*/React.createElement(React.Fragment, {
                  key: j++
                }, /*#__PURE__*/React.createElement("br", null)));
                string.push( /*#__PURE__*/React.createElement(React.Fragment, {
                  key: j++
                }, part));
              }
            }
            elems.push( /*#__PURE__*/React.createElement(React.Fragment, {
              key: _i
            }, string));
          }
        }
      }
      var Tag = this.tag();
      var className = this.className();
      return /*#__PURE__*/React.createElement(Tag, {
        className: className
      }, elems);
    }
  }, {
    key: "canContain",
    value: function canContain(nestedSet) {
      return this.start() < nestedSet.start() && nestedSet.end() < this.end();
    }
  }, {
    key: "addSet",
    value: function addSet(nestedSet) {
      for (var i = 0; i < this._innerSets.length; i++) {
        if (this._innerSets[i].canContain(nestedSet)) {
          this._innerSets[i].addSet(nestedSet);
          return;
        }
      }
      var deferredSets = [];
      var leftInnerSets = [];
      for (var _i2 = 0; _i2 < this._innerSets.length; _i2++) {
        if (nestedSet.canContain(this._innerSets[_i2])) {
          deferredSets.push(this._innerSets[_i2]);
        } else {
          leftInnerSets.push(this._innerSets[_i2]);
        }
      }
      if (deferredSets.length) {
        leftInnerSets.push(nestedSet);
        this._sortNestedSets(leftInnerSets);
        if (this._doOrderedSetsOverlap(leftInnerSets)) {
          return;
        }
        this._innerSets = leftInnerSets;
        for (var _i3 = 0; _i3 < deferredSets.length; _i3++) {
          nestedSet.addSet(deferredSets[_i3]);
        }
        return;
      }
      var newInnerSets = this._innerSets.slice();
      newInnerSets.push(nestedSet);
      this._sortNestedSets(newInnerSets);
      if (this._doOrderedSetsOverlap(newInnerSets)) {
        return;
      }
      this._innerSets = newInnerSets;
    }
  }, {
    key: "className",
    value: function className() {
      return null;
    }
  }, {
    key: "_doOrderedSetsOverlap",
    value: function _doOrderedSetsOverlap(nestedSets) {
      if (!nestedSets.length) {
        return false;
      }
      for (var lastSet = nestedSets[0], i = 1; i < nestedSets.length; lastSet = nestedSets[i++]) {
        if (nestedSets[i].start() <= lastSet.end()) {
          return true;
        }
      }
      return false;
    }
  }, {
    key: "_sortNestedSets",
    value: function _sortNestedSets(nestedSets) {
      nestedSets.sort(function (a, b) {
        if (a.start() === b.start()) {
          return 0;
        }
        return a.start() < b.start() ? -1 : 1;
      });
    }
  }]);
}();
var _RootFormattedNestedSet = /*#__PURE__*/function (_FormattedNestedSet2) {
  function _RootFormattedNestedSet(string, startPos, endPos, lastParagraph) {
    var _this;
    _classCallCheck(this, _RootFormattedNestedSet);
    _this = _callSuper(this, _RootFormattedNestedSet, [string, startPos, endPos]);
    _this._lastParagraph = !!lastParagraph;
    return _this;
  }
  _inherits(_RootFormattedNestedSet, _FormattedNestedSet2);
  return _createClass(_RootFormattedNestedSet, [{
    key: "canContain",
    value: function canContain(nestedSet) {
      return true;
    }
  }, {
    key: "tag",
    value: function tag() {
      return "p";
    }
  }, {
    key: "delimiterLength",
    value: function delimiterLength() {
      return 0;
    }
  }, {
    key: "className",
    value: function className() {
      if (this._lastParagraph) {
        return "mb-0";
      }
      return "mb-10";
    }
  }]);
}(_FormattedNestedSet);
var _BoldFormattedNestedSet = /*#__PURE__*/function (_FormattedNestedSet3) {
  function _BoldFormattedNestedSet() {
    _classCallCheck(this, _BoldFormattedNestedSet);
    return _callSuper(this, _BoldFormattedNestedSet, arguments);
  }
  _inherits(_BoldFormattedNestedSet, _FormattedNestedSet3);
  return _createClass(_BoldFormattedNestedSet, [{
    key: "tag",
    value: function tag() {
      return "strong";
    }
  }, {
    key: "delimiterLength",
    value: function delimiterLength() {
      return 2;
    }
  }]);
}(_FormattedNestedSet);
var _ItalicFormattedNestedSet = /*#__PURE__*/function (_FormattedNestedSet4) {
  function _ItalicFormattedNestedSet() {
    _classCallCheck(this, _ItalicFormattedNestedSet);
    return _callSuper(this, _ItalicFormattedNestedSet, arguments);
  }
  _inherits(_ItalicFormattedNestedSet, _FormattedNestedSet4);
  return _createClass(_ItalicFormattedNestedSet, [{
    key: "tag",
    value: function tag() {
      return "em";
    }
  }, {
    key: "delimiterLength",
    value: function delimiterLength() {
      return 2;
    }
  }]);
}(_FormattedNestedSet);
var _UnderlinedFormattedNestedSet = /*#__PURE__*/function (_FormattedNestedSet5) {
  function _UnderlinedFormattedNestedSet() {
    _classCallCheck(this, _UnderlinedFormattedNestedSet);
    return _callSuper(this, _UnderlinedFormattedNestedSet, arguments);
  }
  _inherits(_UnderlinedFormattedNestedSet, _FormattedNestedSet5);
  return _createClass(_UnderlinedFormattedNestedSet, [{
    key: "tag",
    value: function tag() {
      return "u";
    }
  }, {
    key: "delimiterLength",
    value: function delimiterLength() {
      return 2;
    }
  }]);
}(_FormattedNestedSet);