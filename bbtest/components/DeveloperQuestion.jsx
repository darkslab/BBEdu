class DeveloperQuestion extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            toggleFlag: true,
            paragraphsModal: false
        };
        this._$paragraphsContainer;
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
                                data={paragraphData.meta_data} />
            );
        });
        if (!paragraphs.length) {
            paragraphs.push(
                <div key={'empty'} className="bb-test-paragraph">
                    <p className="lead text-center mb-0">{this.props.texts.emptyParagraph}</p>
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
                             texts={this.props.texts} />
            );
        } else {
            answerContent = (
                <div className="row mb-23">
                    <div className="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                        <button type="button" className="btn btn-primary btn-lg btn-block">{this.props.texts.addAnswer}</button>
                    </div>
                </div>
            );
        }

        let modal = null;
        if (this.state.paragraphsModal) {
            modal = (
                <DeveloperParagraphsModal complete={this._completeParagraphsModal.bind(this)}
                                          texts={this.props.texts} />
            );
        }

        return (
            <React.Fragment>
                {modal}
                <div className="row">
                    <div className="col-xs-12">
                        <div className="panel panel-primary">
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
                                <div className="form-group text-center mt-23">
                                    <button type="button"
                                            className="btn btn-success"
                                            onClick={this._renderParagraphsModal.bind(this)}>{this.props.texts.addParagraph}</button>
                                </div>
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
    }
    _paragraphChange(id, data) {
        this.props.object.updateParagraph(id, data);
        this._pokeComponent();
    }
    _paragraphDelete(id) {
        this.props.object.deleteParagraph(id);
        this._pokeComponent();
    }
    _paragraphsSorted(event, ui) {
        let paragraphIds = this._$paragraphsContainer.sortable("toArray", {
            attribute: "data-paragraph-id"
        });
        this.props.object.setParagraphOrder(paragraphIds);
        this._pokeComponent();
    }
    _answerChange(data) {
        this.props.object.updateAnswer(data);
        this._pokeComponent();
    }
    _renderParagraphsModal() {
        this.setState({
            paragraphsModal: true
        });
    }
    _completeParagraphsModal(data) {
        if (data) {
            this.props.object.addParagraph(data);
        }
        this.setState({
            paragraphsModal: false
        });
    }
}
