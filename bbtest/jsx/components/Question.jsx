class Question extends React.Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        // _load_calculator()
    }
    componentWillUnmount() {
        // _unload_calculator()
    }
    render() {
        let paragraphs = [];
        for (let i = 0; i < this.props.object.paragraphs.length; i++) {
            let ParagraphClass = eval(this.props.object.paragraphs[i].paragraph_class);
            paragraphs.push(
                <ParagraphClass key={i}
                                data={this.props.object.paragraphs[i].meta_data}
                                isShared={this.props.object.paragraphs[i].is_shared}
                                texts={this.props.texts}
                                testTexts={this.props.testTexts}
                                forDevelopers={false} />
            );
        }

        let timer = null;
        if (this.props.hasTimer) {
            let timerClassName = "fa fa-fw mr-10";
            let countDown = "--:--";
            if (this.props.secondsLeft >= 0) {
                countDown = (parseInt(this.props.secondsLeft / 60, 10)) + ":" + ("0" + (this.props.secondsLeft % 60)).substr(-2);
                timerClassName += " fa-clock-o";
            } else {
                timerClassName += " fa-refresh fa-spin";
            }
            let countDownClassName = "bb-test-timer label mt-0 mb-0 pull-right";
            if (this.props.secondsLeft > 10) {
                countDownClassName += " label-success";
            } else {
                countDownClassName += " label-danger";
            }

            timer = (
                <span className={countDownClassName}>
                    <i className={timerClassName}></i>
                    {countDown}
                </span>
            );
        }

        let answerContent = null;
        if (this.props.object.answer_class) {
            let AnswerClass = eval(this.props.object.answer_class);
            answerContent = (
                <AnswerClass data={this.props.object.meta_data}
                             answer={this.props.answerData}
                             onUpdate={this.props.onAnswerUpdate}
                             canAnswer={this.props.canAnswer}
                             showCorrectAnswer={this.props.showCorrectAnswer}
                             texts={this.props.texts} />
            );
        }
        
        return (
            <React.Fragment>
                <div className="row">
                    <div className="col-xs-12">
                        <div className="panel mb-15 panel-primary">
                            <div className="panel-heading bb-rel clearfix">
                                <div className="bb-test-number">{this.props.count}</div>
                                <h4 className="panel-title bb-test-title mt-15 mb-15 pull-left">{this.props.texts.question} ({this.props.object.meta_data.question_code})</h4>
                                {timer}
                            </div>
                            <div className="panel-body">
                                <div className="mb-15">
                                    {paragraphs}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                {answerContent}
            </React.Fragment>
        );
    }
}
