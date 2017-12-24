"use strict";

function TextParagraph(props) {
    return React.createElement(
        "div",
        { className: "bb-test-paragraph" },
        props.data.text
    );
}