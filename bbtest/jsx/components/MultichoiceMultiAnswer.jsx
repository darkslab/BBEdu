class MultichoiceMultiAnswer extends React.Component {
    constructor(props) {
        super(props);
        this._alphabet = "ABCDEFGH";
        this._correctIds = [...this.props.answer.correct_ids];
    }
    componentWillReceiveProps(nextProps) {
        this._correctIds = [...nextProps.answer.correct_ids];
    }
    render() {
        let choices = [];
        for (let i = 0; i < this.props.data.choices.length; i++) {
            let ChoiceClass = eval(this.props.data.choices[i].choice_class);
            let chosen = false;
            if (this.props.answer.correct_ids.indexOf(this.props.data.choices[i].id) > -1) {
                chosen = true;
            }
            choices.push(
                <ChoiceClass key={this.props.data.choices[i].id}
                             data={this.props.data.choices[i].meta_data}
                             label={this._alphabet[i]}
                             chosen={chosen}
                             isMulti={true}
                             onChoose={this._handleChoose.bind(this, this.props.data.choices[i].id)} />
            );
        }

        return (
            <div className="row">
                <div className="col-xs-12">
                    <div className="panel panel-default mb-15">
                        <div className="panel-heading">
                            <h4 className="panel-title text-center">{this.props.texts.multichoiceMultiAnswerTitle}</h4>
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
        let i = this._correctIds.indexOf(choiceId);
        if (i > -1) {
            this._correctIds.splice(i, 1);
        } else {
            this._correctIds.push(choiceId);
        }
        let data = {
            answer: {
                correct_ids: [...this._correctIds]
            },
            observation: {}
        };
        this.props.onUpdate(data);
    }
}
