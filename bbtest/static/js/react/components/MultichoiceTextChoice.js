"use strict";

function MultichoiceTextChoice(props) {
    return React.createElement(
        "div",
        { className: "row" },
        React.createElement(
            "div",
            { className: "col-xs-2 col-sm-3 pr-0" },
            React.createElement(
                "div",
                { className: "bb-rel bb-test-answer" },
                React.createElement(
                    "div",
                    { className: "bb-test-answer-choice" },
                    "A"
                )
            )
        ),
        React.createElement(
            "div",
            { className: "col-xs-10 col-sm-7 pl-0" },
            React.createElement(
                "div",
                { className: "bb-test-answer" },
                "Answer example 1"
            )
        )
    );
}