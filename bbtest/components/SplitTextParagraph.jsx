function SplitTextParagraph(props) {
    return (
        <div className="row">
            <div className="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                <div className="row">
                    <div className="col-xs-6 pr-5">
                        <div className="bb-test-paragraph">{props.data.left_text}</div>
                    </div>
                    <div className="col-xs-6 pl-5">
                        <div className="bb-test-paragraph">{props.data.right_text}</div>
                    </div>
                </div>
            </div>
        </div>
    );
}
