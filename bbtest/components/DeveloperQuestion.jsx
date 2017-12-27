class DeveloperQuestion extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            toggleFlag: true,
            paragraphsModal: false,
            answersModal: false
        };
        this._$paragraphsContainer;
        this._maxParagraphs = 8;
        this._saveTimeout = 2000;
        this._timer = null;
    }
    componentDidMount() {
        this._$paragraphsContainer = $("[data-paragraphs]");
        if (this._$paragraphsContainer.length) {
            this._$paragraphsContainer.sortable({
                axis: "y",
                forceHelperSize: true,
                forcePlaceholderSize: true,
                placeholder: "bb-test-paragraph-placeholder",
                tolerance: "pointer",

                create: function() {
                    this._$paragraphsContainer.height(this._$paragraphsContainer.height());
                }.bind(this),
                update: this._paragraphsSorted.bind(this)
            });
        } else {
            this._$paragraphsContainer = undefined;
        }

        this._reScheduleSave();
    }
    componentWillUpdate() {
        if (this._$paragraphsContainer) {
            this._$paragraphsContainer.css("height", "");
        }
    }
    componentDidUpdate() {
        if (this._$paragraphsContainer) {
            this._$paragraphsContainer.height(this._$paragraphsContainer.height());
        }
    }
    componentWillUnmount() {
        if (this._$paragraphsContainer) {
            this._$paragraphsContainer.sortable("destroy");
            this._$paragraphsContainer = undefined;
        }

        clearTimeout(this._timer);
        this.props.object.stop("question");
    }
    render() {
        let developerParagraphs = [];
        let paragraphs = [];
        this.props.object.paragraphIds().map(id => {
            let paragraphData = this.props.object.paragraph(id);

            let DeveloperParagraphClass = eval("Developer" + paragraphData.paragraph_class);
            let ParagraphClass = eval(paragraphData.paragraph_class);

            developerParagraphs.push(
                <DeveloperParagraphClass key={id}
                                         paragraphId={id}
                                         data={paragraphData.meta_data}
                                         onChange={this._paragraphChange.bind(this, id)}
                                         onDelete={this._paragraphDelete.bind(this, id)}
                                         texts={this.props.texts} />
            );
            paragraphs.push(
                <ParagraphClass key={id}
                                data={paragraphData.meta_data}
                                optionalTexts={this.props.texts} />
            );
        });
        if (!paragraphs.length) {
            paragraphs.push(
                <div key="empty" className="bb-test-paragraph">
                    <p className="lead text-center mb-0">{this.props.texts.noParagraphs}</p>
                </div>
            );
        }

        let answerContent = null;
        let answerData = this.props.object.answer();
        if (answerData.answer_class) {
            let AnswerClass = eval("Developer" + answerData.answer_class);
            answerContent = (
                <AnswerClass data={answerData.meta_data}
                             onChange={this._answerChange.bind(this)}
                             onDelete={this._answerDelete.bind(this)}
                             texts={this.props.texts} />
            );
        } else {
            answerContent = (
                <div className="row mb-23">
                    <div className="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                        <button type="button"
                                className="btn btn-primary btn-lg btn-block"
                                onClick={this._renderModal.bind(this, "answers")}>{this.props.texts.addAnswer}</button>
                    </div>
                </div>
            );
        }

        let modal = null;
        if (this.state.paragraphsModal) {
            modal = (
                <DeveloperSelectorModal title={this.props.texts.paragraphsModalTitle}
                                        complete={this._completeModal.bind(this, "paragraphs")}
                                        classData={[
                                            {
                                                class: "TextParagraph",
                                                caption: this.props.texts.paragraphsModalButtonTextParagraph
                                            },
                                            {
                                                class: "SplitTextParagraph",
                                                caption: this.props.texts.paragraphsModalButtonSplitTextParagraph
                                            }
                                        ]} />
            );
        } else if (this.state.answersModal) {
            modal = (
                <DeveloperSelectorModal title={this.props.texts.answersModalTitle}
                                        complete={this._completeModal.bind(this, "answers")}
                                        classData={[
                                            {
                                                class: "MultichoiceOneAnswer",
                                                caption: this.props.texts.multichoiceOneAnswerTitle
                                            }
                                        ]} />
            );
        }

        let addParagaphButton = null;
        if (developerParagraphs.length < this._maxParagraphs) {
            addParagaphButton = (
                <div className="form-group text-center mt-23">
                    <button type="button"
                            className="btn btn-success"
                            onClick={this._renderModal.bind(this, "paragraphs")}>{this.props.texts.addParagraph}</button>
                </div>
            );
        }

        let panelClassName = "panel";
        if (this.props.object.isSaved()) {
            panelClassName += " panel-success";
        } else {
            panelClassName += " panel-primary";
        }

        return (
            <React.Fragment>
                {modal}
                <div className="row">
                    <div className="col-xs-12">
                        <div className={panelClassName}>
                            <div className="panel-heading bb-rel">
                                <div className="bb-test-number">{this.props.count}</div>
                                <h4 className="panel-title bb-test-title mt-15 mb-15">{this.props.texts.question}</h4>
                            </div>
                            <div className="panel-body">
                                <div className="form-horizontal">
                                    <DeveloperAttribute label={this.props.texts.difficulty}
                                                        value={this.props.object.difficulty()}
                                                        data={this.props.attributes.difficulties}
                                                        onChange={this._attributeChange.bind(this, "difficulty")} />
                                    <DeveloperAttribute label={this.props.texts.taxonomy}
                                                        value={this.props.object.taxonomy()}
                                                        data={this.props.attributes.taxonomies}
                                                        onChange={this._attributeChange.bind(this, "taxonomy")} />
                                    <DeveloperAttribute label={this.props.texts.topic}
                                                        value={this.props.object.topic()}
                                                        data={this.props.attributes.topics}
                                                        onChange={this._attributeChange.bind(this, "topic")} />
                                </div>
                                <div data-paragraphs>
                                    {developerParagraphs}
                                </div>
                                {addParagaphButton}
                                <hr className="bb-separator" />
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
    _pokeComponent() {
        this.setState(prevState => ({
            toggleFlag: !prevState.toggleFlag
        }));
    }
    _attributeChange(type, value) {
        switch (type) {
            case "difficulty":
                this.props.object.setDifficulty(value);
                break;
            case "taxonomy":
                this.props.object.setTaxonomy(value);
                break;
            case "topic":
                this.props.object.setTopic(value);
                break;
        }
        this._pokeComponent();
        this._reScheduleSave();
    }
    _paragraphChange(id, data) {
        this.props.object.updateParagraph(id, data);
        this._pokeComponent();
        this._reScheduleSave();
    }
    _paragraphDelete(id) {
        this.props.object.deleteParagraph(id);
        this._pokeComponent();
        this._reScheduleSave();
    }
    _paragraphsSorted(event, ui) {
        let paragraphIds = this._$paragraphsContainer.sortable("toArray", {
            attribute: "data-paragraph-id"
        });
        this.props.object.setParagraphOrder(paragraphIds);
        this._pokeComponent();
        this._reScheduleSave();
    }
    _answerChange(data) {
        this.props.object.updateAnswer(data);
        this._pokeComponent();
        this._reScheduleSave();
    }
    _answerDelete() {
        this.props.object.deleteAnswer();
        this._pokeComponent();
        this._reScheduleSave();
    }
    _renderModal(type) {
        switch (type) {
            case "paragraphs":
                this.setState({
                    paragraphsModal: true
                });
                break;
            case "answers":
                this.setState({
                    answersModal: true
                });
                break;
        }
    }
    _completeModal(type, data) {
        switch (type) {
            case "paragraphs":
                if (data) {
                    this.props.object.addParagraph(data);
                }
                this.setState({
                    paragraphsModal: false
                });
                break;
            case "answers":
                if (data) {
                    this.props.object.setAnswer(data);
                }
                this.setState({
                    answersModal: false
                });
                break;
        }
    }
    _reScheduleSave() {
        clearTimeout(this._timer);
        this._timer = setTimeout(() => {
            this.props.object.save("question", this._saveCallback.bind(this));
        }, this._saveTimeout);
    }
    _saveCallback(result) {
        if (!result) {
            this.props.errorOut();
            return;
        }
        this._pokeComponent();
    }
}
