"use strict";

function SplitTextParagraph(props) {
    var leftClassName = "bb-test-paragraph";
    var leftContent = null;
    if (props.data.left.text) {
        leftContent = props.data.left.text;
    } else if (props.optionalTexts) {
        leftClassName += " bb-placeholder";
        leftContent = props.optionalTexts.paragraphEmptyPlaceholder;
    }

    var rightClassName = "bb-test-paragraph";
    var rightContent = null;
    if (props.data.right.text) {
        rightContent = props.data.right.text;
    } else if (props.optionalTexts) {
        rightClassName += " bb-placeholder";
        rightContent = props.optionalTexts.paragraphEmptyPlaceholder;
    }

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
                        { className: leftClassName },
                        leftContent
                    )
                ),
                React.createElement(
                    "div",
                    { className: "col-xs-6 pl-5" },
                    React.createElement(
                        "div",
                        { className: rightClassName },
                        rightContent
                    )
                )
            )
        )
    );
}