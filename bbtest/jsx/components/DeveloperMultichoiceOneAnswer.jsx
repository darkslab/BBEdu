class DeveloperMultichoiceOneAnswer extends React.Component {
    constructor(props) {
        super(props);
        this._alphabet = "ABCDEFGH";
        this._$choicesContainer;
        this.state = {
            choicesModal: false,
            confirmModal: false
        };
    }
    componentDidMount() {
        this._$choicesContainer = $("[data-choices]");
        if (this._$choicesContainer.length) {
            this._$choicesContainer.sortable({
                axis: "y",
                cancel: "input,textarea,button,select,option,[data-bb-non-sortable]",
                forceHelperSize: true,
                forcePlaceholderSize: true,
                items: "> [data-choice-id]",
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
    componentWillUpdate() {
        if (this._$choicesContainer) {
            this._$choicesContainer.css("height", "");
        }
    }
    componentDidUpdate() {
        if (this._$choicesContainer) {
            this._$choicesContainer.height(this._$choicesContainer.height());
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
                                      onSelect={this._choiceSelect.bind(this, choice.id)}
                                      onDelete={this._choiceDelete.bind(this, choice.id)}
                                      canEdit={this.props.ability.canEditAnswerChoice(choice.id)}
                                      canDelete={this.props.ability.canDeleteAnswerChoice(choice.id)}
                                      texts={this.props.texts}
                                      chosen={chosen} />
            );
            choices.push(
                <ChoiceClass key={choice.id}
                             data={choice.meta_data}
                             label={this._alphabet[index]}
                             chosen={chosen}
                             isMulti={false}
                             texts={this.props.texts}
                             forDevelopers={true} />
            );
        });
        if (!choices.length) {
            choices.push(
                <div key="empty" className="row">
                    <div className="col-xs-12">
                        <p className="lead text-center mb-0">{this.props.texts.noAnswerChoices}</p>
                    </div>
                </div>
            );
        }

        let modal = null;
        if (this.state.choicesModal) {
            modal = (
                <DeveloperSelectorModal title={this.props.texts.answerChoicesModalTitle}
                                        complete={this._completeModal.bind(this, "choices")}
                                        classData={[
                                            {
                                                class: "MultichoiceTextChoice",
                                                caption: this.props.texts.answerChoicesModalTitleButtonMultichoiceTextChoice
                                            }
                                        ]} />
            );
        } else if (this.state.confirmModal) {
            modal = (
                <ConfirmModal title={this.props.texts.deleteModalTitle}
                              yesCaption={this.props.texts.deleteModalYesCaption}
                              noCaption={this.props.texts.deleteModalNoCaption}
                              isInverse={true}
                              complete={this._completeModal.bind(this, "confirm")} />
            );
        }

        let addAnswerChoiceButton = null;
        if (this.props.ability.canAddAnswerChoice() && developerChoices.length < this._alphabet.length) {
            addAnswerChoiceButton = (
                <div className="form-group text-center mt-23">
                    <button type="button"
                            className="btn btn-success"
                            onClick={this._renderModal.bind(this, "choices")}>{this.props.texts.addAnswerChoice}</button>
                </div>
            );
        }

        let deleteButton = null;
        if (this.props.ability.canDeleteAnswer()) {
            deleteButton = (
                <button type="button"
                        className="btn btn-danger btn-sm"
                        onClick={this._renderModal.bind(this, "confirm")}>
                    <i className="fa fa-fw fa-times"></i>
                </button>
            );
        }

        return (
            <React.Fragment>
                {modal}
                <div className="row">
                    <div className="col-xs-12">
                        <div className="panel panel-default mb-15">
                            <div className="panel-heading">
                                <div className="row">
                                    <h4 className="col-xs-9 col-sm-11 mt-5 mb-5">{this.props.texts.multichoiceOneAnswerTitle}</h4>
                                    <div className="col-xs-3 col-sm-1 text-right pl-0">{deleteButton}</div>
                                </div>
                            </div>
                            <div className="panel-body">
                                <div data-choices>
                                    {developerChoices}
                                </div>
                                {addAnswerChoiceButton}
                                <hr className="bb-separator" />
                                <div className="mb-15">
                                    {choices}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </React.Fragment>
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
    _choiceSelect(choiceId, data) {
        let _data = this._deepCopyData();
        _data.correct_id = data ? choiceId : null;
        this.props.onChange(_data);
    }
    _choiceDelete(choiceId) {
        let data = this._deepCopyData();
        for (let i = 0; i < data.choices.length; i++) {
            if (data.choices[i].id === choiceId) {
                if (data.correct_id === choiceId) {
                    data.correct_id = null;
                }
                data.choices.splice(i, 1);
                break;
            }
        }
        this.props.onChange(data);
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
    _renderModal(type) {
        switch (type) {
            case "choices":
                this.setState({
                    choicesModal: true
                });
                break;
            case "confirm":
                this.setState({
                    confirmModal: true
                });
                break;
        }
    }
    _completeModal(type, data) {
        switch (type) {
            case "choices":
                if (data) {
                    let _data = this._deepCopyData();
                    let choiceIds = _data.choices.map(choice => choice.id).sort((a, b) => a === b ? 0 : (a < b ? -1 : 1));

                    let choice = {
                        choice_class: data,
                        id: null,
                        meta_data: {
                            text: ""
                        }
                    };
                    if (choiceIds.length) {
                        choice.id = choiceIds[choiceIds.length - 1] + 1;
                    } else {
                        choice.id = Math.random() * 0xffff | 0x00;
                    }

                    _data.choices.push(choice);
                    this.props.onChange(_data);
                }
                this.setState({
                    choicesModal: false
                });
                break;
            case "confirm":
                if (data) {
                    this.props.onDelete();
                } else {
                    this.setState({
                        confirmModal: false
                    });
                }
                break;
        }
    }
}
