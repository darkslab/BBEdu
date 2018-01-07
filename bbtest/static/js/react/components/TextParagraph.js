"use strict";

function TextParagraph(props) {
    var className = "bb-test-paragraph";
    var content = null;
    if (props.data.text) {
        content = SimpleFormattedFragment(props.data.text);
    } else if (props.optionalTexts) {
        className += " bb-placeholder";
        content = props.optionalTexts.paragraphEmptyPlaceholder;
    }

    return React.createElement(
        "div",
        { className: className },
        content
    );
}