class MultichoiceMultiAnswer extends React.Component {
    static isCorrect(answerMetaData, report) {
        if (!report) {
            return false;
        }
        if (answerMetaData.correct_ids.length != report.correct_ids.length) {
            return false;
        }
        for (let i = 0; i < answerMetaData.correct_ids.length; i++) {
            if (report.correct_ids.indexOf(answerMetaData.correct_ids[i]) < 0) {
                return false;
            }
        }
        return true;
    }

    constructor(props) {
        super(props);
        this._alphabet = "ABCDEFGH";
        this._correctIds = [];
        this._assignCorrectIds(this.props.answer);
    }
    componentWillReceiveProps(nextProps) {
        this._assignCorrectIds(nextProps.answer);
    }
    render() {
        let choices = [];
        for (let i = 0; i < this.props.data.choices.length; i++) {
            let ChoiceClass = eval(this.props.data.choices[i].choice_class);
            let chosen = false;
            if (this.props.answer && this.props.answer.correct_ids.indexOf(this.props.data.choices[i].id) > -1) {
                chosen = true;
            }
            let isCorrect = false;
            if (this.props.showCorrectAnswer) {
                if (this.props.data.correct_ids.length && this.props.data.correct_ids.indexOf(this.props.data.choices[i].id) > -1) {
                    isCorrect = true;
                }
            }
            choices.push(
                <ChoiceClass key={this.props.data.choices[i].id}
                             data={this.props.data.choices[i].meta_data}
                             label={this._alphabet[i]}
                             chosen={chosen}
                             isMulti={true}
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
                        {/* <div className="panel-heading">
                            <h4 className="panel-title text-center">{this.props.texts.multichoiceMultiAnswerTitle}</h4>
                        </div> */}
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
        let i = this._correctIds.indexOf(choiceId);
        if (i > -1) {
            this._correctIds.splice(i, 1);
        } else {
            this._correctIds.push(choiceId);
        }
        let data = {
            answer: null,
            observation: {}
        };
        if (this._correctIds.length) {
            data.answer = {
                correct_ids: [...this._correctIds]
            };
        }
        this.props.onUpdate(data);
    }
    _assignCorrectIds(answer) {
        this._correctIds = [];
        if (!answer) {
            return;
        }
        for (let i = 0; i < answer.correct_ids.length; i++) {
            this._correctIds.push(answer.correct_ids[i]);
        }
    }
}
