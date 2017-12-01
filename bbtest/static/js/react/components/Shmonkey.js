"use strict";

function Shmonkey(props) {
    var style = {
        cursor: "pointer",
        WebkitUserSelect: "none",
        MozUserSelect: "none",
        MsUserSelect: "none",
        userSelect: "none"
    };
    return React.createElement(
        "h1",
        { style: style, onClick: props.handleClick },
        props.title,
        ": ",
        props.counter
    );
}