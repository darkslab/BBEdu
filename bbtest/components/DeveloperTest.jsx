class DeveloperTest extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isTestLoading: true,
            isQuestionLoading: true,
            isQuestionSaving: false,
            isErrored: false,
            questionIndex: 0
        };
        this._questionObject = null;
        this._oldQuestionObjects = [];
        this._questionAttributes = null;
        this._$xhrs = {
            question: null,
            attributes: null
        };
    }
    componentDidMount() {
        let questionNumber = 1;
        if (location.hash) {
            questionNumber = parseInt(location.hash.substr(1), 10);
            if (isNaN(questionNumber) || questionNumber < 1 || questionNumber > this.props.questionIds.length) {
                questionNumber = 1;
            }
        }

        this._getQuestionData(questionNumber - 1);
        this._$xhrs["attributes"] = $.get({
            url: this.props.attributesUrl,
            success: this._ajaxSuccess.bind(this, "attributes"),
            error: this._ajaxError.bind(this, "attributes")
        });
    }
    componentWillUnmount() {
        this._cleanUp();
    }
    render() {
        let content = null;
        if (this.state.isErrored) {
            content = (
                <h4 className="text-center text-danger">{this.props.texts.error}</h4>
            );
        } else if (!this.state.isTestLoading && !this.state.isQuestionLoading && !this.state.isQuestionSaving) {
            content = (
                <DeveloperQuestion count={this.state.questionIndex + 1}
                                   attributes={this._questionAttributes}
                                   object={this._questionObject}
                                   texts={this.props.texts}
                                   errorOut={this._errorOut.bind(this)} />
            );
        } else {
            content = (
                <img className="bb-spinner" src={this.props.spinnerLogo} />
            );
        }

        let pagination = null;
        if (!this.state.isErrored && !this.state.isTestLoading) {
            let width = 5;
            if (width < 1) {
                width = 1;
            } else if (width > this.props.questionIds.length) {
                width = this.props.questionIds.length;
            }
            let padding = parseInt((width - 1) / 2, 10);
            let rightPadding = (width - 1) % 2;
            let indexes = [ this.state.questionIndex ];
            for (let i = 0; i < padding; i++) {
                indexes.unshift(indexes[0] - 1);
                indexes.push(indexes[indexes.length - 1] + 1);
            }
            for (let i = 0; i < rightPadding; i++) {
                indexes.push(indexes[indexes.length - 1] + 1);
            }
            if (indexes[0] < 0) {
                while (true) {
                    if (indexes[0] >= 0) {
                        break;
                    }
                    indexes.shift();
                    indexes.push(indexes[indexes.length - 1] + 1);
                }
            } else if (indexes[indexes.length - 1] >= this.props.questionIds.length) {
                while (true) {
                    if (indexes[indexes.length - 1] < this.props.questionIds.length) {
                        break;
                    }
                    indexes.pop();
                    indexes.unshift(indexes[0] - 1);
                }
            }

            let paginationElements = [];
            if (this.state.questionIndex > 0) {
                paginationElements.push(
                    <li key="left">
                        <a href="javascript:void(0);"
                           onClick={this._nextQuestion.bind(this, this.state.questionIndex - 1)}>&laquo;</a>
                    </li>
                );
            } else {
                paginationElements.push(
                    <li key="left" className="disabled">
                        <a href="javascript:void(0);">&laquo;</a>
                    </li>
                );
            }
            for (let i = 0; i < indexes.length; i++) {
                if (indexes[i] === this.state.questionIndex) {
                    paginationElements.push(
                        <li key={indexes[i].toString()} className="active">
                            <a href="javascript:void(0);">{indexes[i] + 1}</a>
                        </li>
                    );
                } else {
                    paginationElements.push(
                        <li key={indexes[i].toString()}>
                            <a href="javascript:void(0);"
                               onClick={this._nextQuestion.bind(this, indexes[i])}>{indexes[i] + 1}</a>
                        </li>
                    );
                }
            }
            if (this.state.questionIndex < this.props.questionIds.length - 1) {
                paginationElements.push(
                    <li key="right">
                        <a href="javascript:void(0);"
                           onClick={this._nextQuestion.bind(this, this.state.questionIndex + 1)}>&raquo;</a>
                    </li>
                );
            } else {
                paginationElements.push(
                    <li key="right" className="disabled">
                        <a href="javascript:void(0);">&raquo;</a>
                    </li>
                );
            }
            pagination = (
                <div className="col-xs-12 text-right">
                    <ul className="pagination mt-5 mb-5">{paginationElements}</ul>
                </div>
            );
        }

        return (
            <div className="row">
                {pagination}
                <div className="col-xs-12 bb-developer-container">
                    {content}
                </div>
            </div>
        );
    }
    _nextQuestion(index) {
        this.setState({
            isQuestionLoading: true
        });
        if (this._questionObject) {
            this.setState({
                isQuestionSaving: true
            });
            let object = this._questionObject;
            this._questionObject = null;
            object.save("test", this._questionSave.bind(this));
            this._oldQuestionObjects.push(object);
        }
        this._getQuestionData(index);
    }
    _ajaxSuccess(type, data, status, $xhr) {
        if (type === "question") {
            this._questionObject = new DeveloperQuestionObject(
                data.id,
                data.data,
                data.paragraphs,
                this.props.questionUrl,
                this.props.paragraphsUrl
            );
            this.setState({
                isQuestionLoading: false
            });
        } else if (type === "attributes") {
            this._questionAttributes = data;
        }
        if (this._questionObject && this._questionAttributes) {
            this.setState({
                isTestLoading: false
            });
        }
    }
    _ajaxError(type, $xhr, status, error) {
        if (status === "abort") {
            return;
        }

        this._errorOut();
    }
    _cleanUp() {
        let object;
        while (object = this._oldQuestionObjects.shift()) {
            object.stop("test");
        }
        this._$xhrs["question"].abort();
        this._$xhrs["attributes"].abort();
    }
    _questionSave(success, object) {
        let index = this._oldQuestionObjects.indexOf(object);
        if (index > -1) {
            this._oldQuestionObjects.splice(index, 1);
        }

        if (!success) {
            this._errorOut();
            return;
        }

        this.setState({
            isQuestionSaving: false
        });
    }
    _getQuestionData(index) {
        this.setState({
            questionIndex: index
        });
        history.replaceState(history.state, "", location.pathname + "#" + (index + 1).toString());

        if (this._$xhrs["question"]) {
            this._$xhrs["question"].abort();
        }
        this._$xhrs["question"] = $.get({
            url: this.props.questionUrl + this.props.questionIds[index] + "/",
            success: this._ajaxSuccess.bind(this, "question"),
            error: this._ajaxError.bind(this, "question")
        });
    }
    _errorOut() {
        this.setState({
            isErrored: true
        });
        this._cleanUp();
    }
}
