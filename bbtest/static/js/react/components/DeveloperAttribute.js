"use strict";

function DeveloperAttribute(props) {
  var caption = "";
  var options = [];
  for (var i = 0; i < props.data.length; i++) {
    var fullCaption = props.data[i].caption;
    var truncatedCaption = fullCaption.length > 100 ? "".concat(fullCaption.slice(0, 100), "...") : fullCaption;
    if (props.value === props.data[i].value) {
      caption = fullCaption;
      options.push( /*#__PURE__*/React.createElement("li", {
        key: props.data[i].value,
        className: "active"
      }, /*#__PURE__*/React.createElement("a", {
        href: "javascript:void(0);",
        title: fullCaption
      }, truncatedCaption)));
    } else {
      options.push( /*#__PURE__*/React.createElement("li", {
        key: props.data[i].value
      }, /*#__PURE__*/React.createElement("a", {
        href: "javascript:void(0);",
        onClick: props.onChange.bind(null, props.data[i].value),
        title: fullCaption
      }, truncatedCaption)));
    }
  }
  return /*#__PURE__*/React.createElement("div", {
    className: props.value ? "form-group" : "form-group has-error"
  }, /*#__PURE__*/React.createElement("label", {
    className: "control-label col-sm-3 text-uppercase"
  }, props.label), /*#__PURE__*/React.createElement("div", {
    className: "col-sm-9"
  }, /*#__PURE__*/React.createElement("div", {
    className: "input-group"
  }, /*#__PURE__*/React.createElement("input", {
    type: "text",
    className: "form-control bb-test-section-background pl-10",
    readOnly: true,
    value: caption
  }), /*#__PURE__*/React.createElement("div", {
    className: "input-group-btn"
  }, /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn btn-default dropdown-toggle",
    "data-toggle": "dropdown"
  }, /*#__PURE__*/React.createElement("span", {
    className: "caret"
  })), /*#__PURE__*/React.createElement("ul", {
    className: "dropdown-menu dropdown-menu-right"
  }, options)))));
}