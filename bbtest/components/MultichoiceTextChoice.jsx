class MultichoiceTextChoice extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        let choiceClassName = "bb-test-answer-choice";
        if (this.props.chosen) {
            choiceClassName += " bb-test-answer-choice-selected";
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
                    <div className="bb-test-answer">{this.props.data.text}</div>
                </div>
            </div>
        );
    }
}
