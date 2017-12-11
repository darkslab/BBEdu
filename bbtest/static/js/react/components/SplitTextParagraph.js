"use strict";

function SplitTextParagraph(props) {
    return React.createElement(
        "div",
        { className: "row" },
        React.createElement(
            "div",
            { className: "col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2" },
            React.createElement(
                "div",
                { className: "row" },
                React.createElement(
                    "div",
                    { className: "col-xs-6 pr-5" },
                    React.createElement(
                        "div",
                        { className: "bb-test-paragraph" },
                        props.data.left_text
                    )
                ),
                React.createElement(
                    "div",
                    { className: "col-xs-6 pl-5" },
                    React.createElement(
                        "div",
                        { className: "bb-test-paragraph" },
                        props.data.right_text
                    )
                )
            )
        )
    );
}