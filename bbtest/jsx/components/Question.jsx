class Question extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let paragraphs_left_side = [];
        let paragraphs_right_side = [];
        let solutionParagraphs = [];
        // show solutions only if student is in result page
        const regex = new RegExp("^/(en|ru|kk)/student/results/([0-9A-Fa-f]{4,6})/$");
        const regex_dev = new RegExp("^/(en|ru|kk)/build/.+/preview/$");
        const show_solution = regex.test(window.location.pathname);
        const show_solution_dev = regex_dev.test(window.location.pathname);

        // console.log("Question.jsx", this.props.object.paragraphs)
        for (let i = 0; i < this.props.object.paragraphs.length; i++) {
            const paragraph_class = this.props.object.paragraphs[i].paragraph_class
            let ParagraphClass = eval(paragraph_class);
            let parag = <ParagraphClass key={i}
                data={this.props.object.paragraphs[i].meta_data}
                isShared={this.props.object.paragraphs[i].is_shared}
                texts={this.props.texts}
                testTexts={this.props.testTexts}
                forDevelopers={false} />


            if ( paragraph_class.includes("Solution")){
                solutionParagraphs.push(parag);
            } else {
                let left_side = this.props.object.paragraphs[i].meta_data["left_side"] | this.props.object.paragraphs[i].meta_data["left_side"] === undefined
                if (left_side) {
                    paragraphs_left_side.push(parag);
                } else {
                    paragraphs_right_side.push(parag);
                }
            }
        }

        let solution = null;
        if((show_solution || show_solution_dev) && solutionParagraphs.length > 0){
            solution = <div className="border" style={{"borderTop": "solid"}}>
                {/* <hr key="sep_sol" className="bb-separator" /> */}
                <h3 key="sep_sol_h3">{this.props.texts.solution}</h3>
                {solutionParagraphs}
            </div>
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
                    <div className="row row-eq-height border" style={{"borderBottom": "solid"}}>
                        <div className="col-xs-12 col-md-5 border pl-5 pr-5 pb-5" style={{"borderRight": "solid"}}>
                            <div className="">
                                <div className="">
                                    <div className="">
                                        {paragraphs_left_side}
                                    </div>
                                    {answerContent}
                                </div>
                            </div>
                        </div>
                        <div className="col-xs-12 col-md-7 border pl-5 pr-5 pb-5" style={{"borderLeft": "solid"}}>
                            {paragraphs_right_side}
                        </div>
                    </div>
                    {solution}
                </div>
            </React.Fragment>
        );
    }
}
