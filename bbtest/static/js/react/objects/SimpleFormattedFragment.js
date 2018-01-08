"use strict";

function SimpleFormattedFragment(text) {
    return React.createElement(
        React.Fragment,
        null,
        $.trim(text)
    );
}