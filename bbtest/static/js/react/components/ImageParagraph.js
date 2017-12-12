"use strict";

function ImageParagraph(props) {
    return React.createElement(
        "div",
        { className: "bb-test-paragraph" },
        React.createElement("img", { className: "img-responsive center-block bb-test-paragraph-image",
            src: props.data.src })
    );
}