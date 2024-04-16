class Question extends React.Component {
    constructor(props) {
        super(props);
    }

    // componentDidMount() {
    //     _load_calculator()
    //     console.log("Question componentDidMount")
    // }
    // componentWillUnmount() {
    //     _unload_calculator()
    //     console.log("Question componentWillUnmount")
    // }

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
                                <h4 className="panel-title bb-test-title mt-15 mb-15 pull-left">{this.props.username}</h4>
                                <TestTimer
                                    secondsLeft={this.props.secondsLeft}
                                    hasTimer={this.props.hasTimer}
                                />
                                <TestPeriodicTable 
                                    hasPeriodicTable={this.props.hasPeriodicTable} 
                                    periodicTableIconUrl={this.props.periodicTableIconUrl}
                                    periodicTableUrl={this.props.periodicTableUrl}
                                />
                                <TestCalculator
                                    hasCalculator={this.props.hasCalculator}
                                    calculatorIconUrl={this.props.calculatorIconUrl}
                                />
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
