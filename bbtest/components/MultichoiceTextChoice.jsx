class MultichoiceTextChoice extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        let choiceClassName = "bb-test-answer-choice";
        if (this.props.chosen) {
            choiceClassName += " bb-test-answer-choice-selected";
        }

        let contentClassName = "bb-test-answer";
        let content = null;
        if (this.props.data.text) {
            content = this.props.data.text;
        } else if (this.props.optionalTexts) {
            contentClassName += " bb-placeholder";
            content = this.props.optionalTexts.choiceEmptyPlaceholder;
        }

        return (
            <div className="row">
                <div className="col-xs-2 col-sm-3 pr-0">
                    <div className="bb-rel bb-test-answer">
                        <div className={choiceClassName}
                             onClick={()=>{}}>{this.props.label}</div>
                    </div>
                </div>
                <div className="col-xs-10 col-sm-7 pl-0">
                    <div className={contentClassName}>{content}</div>
                </div>
            </div>
        );
    }
}
