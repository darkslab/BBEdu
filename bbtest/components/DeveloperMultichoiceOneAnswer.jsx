class DeveloperMultichoiceOneAnswer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {...this.props.data};
    }
    render() {
        let developerAnswers = [];
        let answers = [];
        this.state.choices.map(choice => {
            developerAnswers.push(
                <DeveloperMultichoiceTextChoice key={choice.id}
                                                answerId={choice.id}
                                                data={choice.text}
                                                onChange={this._choiceChange.bind(this, choice.id)}
                                                texts={this.props.texts} />
            );
            answers.push(
                <MultichoiceTextChoice key={choice.id}
                                       data={choice.text} />
            );
        });

        return (
            <div className="row">
                <div className="col-xs-12">
                    <div className="panel panel-default">
                        <div className="panel-heading">
                            <h4 className="text-center">{this.props.texts.multichoiceOneAnswerTitle}</h4>
                        </div>
                        <div className="panel-body">
                            <div data-answers>
                                {developerAnswers}
                            </div>
                            <div className="form-group text-center mt-15">
                                <button type="button" className="btn btn-success">{this.props.texts.addAnswerChoice}</button>
                            </div>
                            <hr className="bb-separator" />
                            {answers}
                        </div>
                    </div>
                </div>
            </div>
        );
    }
    _choiceChange(choiceId, data) {
        // DARK_TODO
    }
}
