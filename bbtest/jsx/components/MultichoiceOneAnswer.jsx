class MultichoiceOneAnswer extends React.Component {
    constructor(props) {
        super(props);
        this._alphabet = "ABCDEFGH";
    }
    render() {
        let choices = [];
        for (let i = 0; i < this.props.data.choices.length; i++) {
            let ChoiceClass = eval(this.props.data.choices[i].choice_class);
            let chosen = false;
            if (this.props.answer && this.props.answer.correct_id === this.props.data.choices[i].id) {
                chosen = true;
            }
            let isCorrect = false;
            if (this.props.showCorrectAnswer) {
                if (this.props.data.correct_id !== null && this.props.data.correct_id === this.props.data.choices[i].id) {
                    isCorrect = true;
                }
            }
            choices.push(
                <ChoiceClass key={this.props.data.choices[i].id}
                             data={this.props.data.choices[i].meta_data}
                             label={this._alphabet[i]}
                             chosen={chosen}
                             isMulti={false}
                             onChoose={this._handleChoose.bind(this, this.props.data.choices[i].id)}
                             texts={this.props.texts}
                             forDevelopers={false}
                             showCorrectAnswer={this.props.showCorrectAnswer}
                             isCorrect={isCorrect} />
            );
        }

        return (
            <div className="row">
                <div className="col-xs-12">
                    <div className="panel panel-default mb-15">
                        <div className="panel-heading">
                            <h4 className="panel-title text-center">{this.props.texts.multichoiceOneAnswerTitle}</h4>
                        </div>
                        <div className="panel-body">
                            <div className="mb-15">
                                {choices}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    _handleChoose(choiceId) {
        if (!this.props.canAnswer) {
            return;
        }
        let data = {
            answer: {
                correct_id: choiceId
            },
            observation: {}
        };
        this.props.onUpdate(data);
    }
}
