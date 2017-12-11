"use strict";

function DeveloperAttribute(props) {
    var caption = "";
    var options = [];
    for (var i = 0; i < props.data.length; i++) {
        if (props.value === props.data[i].value) {
            caption = props.data[i].caption;
            options.push(React.createElement(
                "li",
                { key: props.data[i].value, className: "active" },
                React.createElement(
                    "a",
                    { href: "javascript:void(0);" },
                    caption
                )
            ));
        } else {
            options.push(React.createElement(
                "li",
                { key: props.data[i].value },
                React.createElement(
                    "a",
                    { href: "javascript:void(0);",
                        onClick: props.change.bind(null, props.data[i].value) },
                    props.data[i].caption
                )
            ));
        }
    }

    return React.createElement(
        "div",
        { className: props.value ? "form-group" : "form-group has-error" },
        React.createElement(
            "label",
            { className: "control-label col-sm-3 text-uppercase" },
            props.label
        ),
        React.createElement(
            "div",
            { className: "col-sm-9" },
            React.createElement(
                "div",
                { className: "input-group" },
                React.createElement("input", { type: "text", className: "form-control bb-test-section-background pl-10", readOnly: true, value: caption }),
                React.createElement(
                    "div",
                    { className: "input-group-btn" },
                    React.createElement(
                        "button",
                        { type: "button", className: "btn btn-default dropdown-toggle", "data-toggle": "dropdown" },
                        React.createElement("span", { className: "caret" })
                    ),
                    React.createElement(
                        "ul",
                        { className: "dropdown-menu dropdown-menu-right" },
                        options
                    )
                )
            )
        )
    );
}