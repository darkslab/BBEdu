class DeveloperQuestion extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            difficulty: this.props.object.difficulty(),
            taxonomy: this.props.object.taxonomy(),
            topic: this.props.object.topic()
        };
    }
    render() {
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
                                                value={this.state.difficulty}
                                                data={this.props.attributes.difficulties}
                                                change={this._attributeChange.bind(this, "difficulty")} />
                            <DeveloperAttribute label={this.props.texts.taxonomy}
                                                value={this.state.taxonomy}
                                                data={this.props.attributes.taxonomies}
                                                change={this._attributeChange.bind(this, "taxonomy")} />
                            <DeveloperAttribute label={this.props.texts.topic}
                                                value={this.state.topic}
                                                data={this.props.attributes.topics}
                                                change={this._attributeChange.bind(this, "topic")} />
                        </div>
                        {/*
                        <div>
                            <div class="form-group bb-test-section-movable bb-test-section-background">
                                <div class="pt-5 pr-5 pb-5 pl-5 clearfix">
                                    <button type="button" class="btn btn-danger btn-xs pull-right ml-5">Formulas Off</button>
                                    <button type="button" class="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                                </div>
                                <textarea class="bb-test-paragraph bb-test-paragraph-textarea" placeholder="Type something!" class="form-control">Main question here...</textarea>
                            </div>

                            <div class="form-group bb-test-section-movable bb-test-section-background">
                                <div class="pt-5 pr-5 pb-5 pl-5 clearfix">
                                    <button type="button" class="btn btn-success btn-xs pull-right ml-5">Formulas On</button>
                                    <button type="button" class="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                                </div>
                                <div class="row">
                                    <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                                        <div class="row">
                                            <div class="col-xs-6 pr-5">
                                                <textarea class="bb-test-paragraph bb-test-paragraph-textarea" placeholder="Type something!" class="form-control">Left quantitative text</textarea>
                                            </div>
                                            <div class="col-xs-6 pl-5">
                                                <textarea class="bb-test-paragraph bb-test-paragraph-textarea" placeholder="Type something!" class="form-control">Right quantitative text</textarea>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

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

                            <div class="form-group text-center mt-15">
                                <button type="button" class="btn btn-success">Add Section</button>
                            </div>
                        </div>
                        <hr class="bb-separator">
                        <div>
                            <div class="bb-test-paragraph">
                                <p class="lead text-center mb-0">Please add a Section above to preview it here.</p>
                            </div>
                            <div class="bb-test-paragraph">Main question here...</div>
                            <div class="row">
                                <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
                                    <div class="row">
                                        <div class="col-xs-6 pr-5">
                                            <div class="bb-test-paragraph">Left quantitative text</div>
                                        </div>
                                        <div class="col-xs-6 pl-5">
                                            <div class="bb-test-paragraph">Right quantitative text</div>
                                        </div>
                                    </div>
                                </div>
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
                this.setState({
                    difficulty: value
                });
                break;
            case "taxonomy":
                this.props.object.setTaxonomy(value);
                this.setState({
                    taxonomy: value
                });
                break;
            case "topic":
                this.props.object.setTopic(value);
                this.setState({
                    topic: value
                });
                break;
        }
    }
}
