class DeveloperMultichoiceOneAnswer extends React.Component {
    constructor(props) {
        super(props);
        this._alphabet = "ABCDEFGHIJKLMNOP";
        this._$choicesContainer;
    }
    componentDidMount() {
        this._$choicesContainer = $("[data-choices]");
        if (this._$choicesContainer.length) {
            this._$choicesContainer.sortable({
                axis: "y",
                forceHelperSize: true,
                forcePlaceholderSize: true,
                placeholder: "bb-test-answer-placeholder",
                tolerance: "pointer",

                create: function() {
                    this._$choicesContainer.height(this._$choicesContainer.height());
                }.bind(this),
                update: this._choicesSorted.bind(this)
            });
        } else {
            this._$choicesContainer = undefined;
        }
    }
    componentWillUnmount() {
        if (this._$choicesContainer) {
            this._$choicesContainer.sortable("destroy");
            this._$choicesContainer = undefined;
        }
    }
    render() {
        let developerChoices = [];
        let choices = [];
        this.props.data.choices.map((choice, index) => {
            let DeveloperChoiceClass = eval("Developer" + choice.choice_class);
            let ChoiceClass = eval(choice.choice_class);

            let chosen = (this.props.data.correct_id && this.props.data.correct_id === choice.id) ? true : false;

            developerChoices.push(
                <DeveloperChoiceClass key={choice.id}
                                      choiceId={choice.id}
                                      data={choice.meta_data}
                                      onChange={this._choiceChange.bind(this, choice.id)}
                                      texts={this.props.texts}
                                      chosen={chosen} />
            );
            choices.push(
                <ChoiceClass key={choice.id}
                             data={choice.meta_data}
                             label={this._alphabet[index]}
                             chosen={chosen} />
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
                            <div data-choices>
                                {developerChoices}
                            </div>
                            <div className="form-group text-center mt-23">
                                <button type="button" className="btn btn-success">{this.props.texts.addAnswerChoice}</button>
                            </div>
                            <hr className="bb-separator" />
                            <div className="mb-23">
                                {choices}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
    _choiceChange(choiceId, data) {
        let _data = this._deepCopyData();
        for (let i = 0; i < _data.choices.length; i++) {
            if (_data.choices[i].id === choiceId) {
                _data.choices[i].meta_data = data;
                break;
            }
        }
        this.props.onChange(_data);
    }
    _deepCopyData() {
        let data = {...this.props.data};
        data.choices = [...data.choices];
        for (let i = 0; i < data.choices.length; i++) {
            data.choices[i] = {...data.choices[i]};
            data.choices[i].meta_data = {...data.choices[i].meta_data};
        }
        return data;
    }
    _choicesSorted(event, ui) {
        let choicesIds = this._$choicesContainer.sortable("toArray", {
            attribute: "data-choice-id"
        }).map(id => parseInt(id, 10));
        let _data = this._deepCopyData();
        _data.choices.sort((a, b) => {
            let i = choicesIds.indexOf(a.id);
            let j = choicesIds.indexOf(b.id);
            if (i === j) {
                return 0;
            }
            return i < j ? -1 : 1;
        });
        this.props.onChange(_data);
    }
}
