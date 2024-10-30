class Question extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let paragraphs_left_side = [];
        let paragraphs_right_side = [];

        for (let i = 0; i < this.props.object.paragraphs.length; i++) {
            let ParagraphClass = eval(this.props.object.paragraphs[i].paragraph_class);
            let left_side = this.props.object.paragraphs[i].meta_data["left_side"] | this.props.object.paragraphs[i].meta_data["left_side"] === undefined

            let parag = <ParagraphClass key={i}
                data={this.props.object.paragraphs[i].meta_data}
                isShared={this.props.object.paragraphs[i].is_shared}
                texts={this.props.texts}
                testTexts={this.props.testTexts}
                forDevelopers={false} />

            if (left_side) {
                paragraphs_left_side.push(parag);
            } else {
                paragraphs_right_side.push(parag);
            }
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
                    <div className="row row-eq-height">
                        <div className="col-xs-12 col-md-5 border" style={{"borderRight": "solid"}}>
                            <div className="">
                                <div className="">
                                    <div className="">
                                        {paragraphs_left_side}
                                    </div>
                                    {answerContent}
                                </div>
                            </div>
                        </div>
                        <div className="col-xs-12 col-md-7">
                            {paragraphs_right_side}
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}
