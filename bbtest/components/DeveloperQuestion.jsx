class DeveloperQuestion extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            update: 0
        };
    }
    render() {
        let developerParagraphs = [];
        let paragraphs = [];
        this.props.object.paragraphIds().map(function(id) {
            let data = this.props.object.paragraph(id);
            if (data.paragraph_class === "TextParagraph") {
                developerParagraphs.push(
                    <DeveloperTextParagraph key={id}
                                            data={data.meta_data}
                                            onChange={this._paragraphChange.bind(this, id)}
                                            placeholder={this.props.texts.sectionTextareaPlaceholder} />
                );
                paragraphs.push(
                    <TextParagraph key={id}
                                   data={data.meta_data} />
                );
            } else if (data.paragraph_class === "SplitTextParagraph") {
                developerParagraphs.push(
                    <DeveloperSplitTextParagraph key={id}
                                                 data={data.meta_data}
                                                 onChange={this._paragraphChange.bind(this, id)}
                                                 placeholder={this.props.texts.sectionTextareaPlaceholder} />
                );
                paragraphs.push(
                    <SplitTextParagraph key={id}
                                        data={data.meta_data} />
                );
            }
        }.bind(this));

        return (
            <div className="col-xs-12 bb-developer-container">
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
                        <div>
                            {developerParagraphs}
                            <div className="form-group text-center mt-15">
                                <button type="button" className="btn btn-success">{this.props.texts.addSection}</button>
                            </div>
                        </div>
                        <hr className="bb-separator" />
                        <div>
                            {paragraphs}
                        </div>
                        {/*
                        <div>
                            <div class="form-group bb-test-section-movable bb-test-section-background">
                                <div class="pt-5 pr-5 pb-5 pl-5 clearfix">
                                    <button type="button" class="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                                </div>
                                <div class="bb-test-paragraph bb-test-paragraph-upload">
                                    <div class="row">
                                        <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                                            <div class="row">
                                                <div class="col-xs-12">
                                                    <label for="monkey" class="btn btn-success btn-lg btn-block mt-23">Upload Image</label>
                                                    <input id="monkey" class="hidden" type="file">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr class="bb-separator">
                        <div>
                            <div class="bb-test-paragraph">
                                <p class="lead text-center mb-0">Please add a Section above to preview it here.</p>
                            </div>
                            <div class="bb-test-paragraph">
                                <img class="img-responsive center-block bb-test-paragraph-image" src="{% static 'img/sample.png' %}">
                            </div>
                        </div>
                        */}
                    </div>
                </div>
            </div>
        );
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
        this.setState(prevState => ({
            update: prevState.update + 1
        }));
    }
    _paragraphChange(id, data) {
        this.props.object.updateParagraph(id, data);
        this.setState(prevState => ({
            update: prevState.update + 1
        }));
    }
}
