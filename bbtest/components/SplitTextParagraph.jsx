function SplitTextParagraph(props) {
    let leftClassName = "bb-test-paragraph";
    let leftContent = null;
    if (props.data.left.text) {
        leftContent = props.data.left.text;
    } else if (props.optionalTexts) {
        leftClassName += " bb-placeholder";
        leftContent = props.optionalTexts.paragraphEmptyPlaceholder;
    }

    let rightClassName = "bb-test-paragraph";
    let rightContent = null;
    if (props.data.right.text) {
        rightContent = props.data.right.text;
    } else if (props.optionalTexts) {
        rightClassName += " bb-placeholder";
        rightContent = props.optionalTexts.paragraphEmptyPlaceholder;
    }

    return (
        <div className="row">
            <div className="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                <div className="row">
                    <div className="col-xs-6 pr-5">
                        <div className={leftClassName}>{leftContent}</div>
                    </div>
                    <div className="col-xs-6 pl-5">
                        <div className={rightClassName}>{rightContent}</div>
                    </div>
                </div>
            </div>
        </div>
    );
}
