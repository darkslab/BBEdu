function TextParagraph(props) {
    let className = "bb-test-paragraph";
    let content = null;
    if (props.data.text) {
        content = SimpleFormattedFragment(props.data.text);
    } else if (props.optionalTexts) {
        className += " bb-placeholder";
        content = props.optionalTexts.paragraphEmptyPlaceholder;
    }

    return (
        <div className={className}>{content}</div>
    );
}
