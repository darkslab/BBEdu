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
        this._abilityObject = null;
        this._oldQuestionObjects = [];
        this._questionAttributes = null;
        this._$xhrs = {
            question: null,
            attributes: null
        };
        this._finalSave = false;

        this._boundConfirmIsSaved = this._confirmIsSaved.bind(this);
        this._boundConfirmIsSavedTurbolinks = this._confirmIsSavedTurbolinks.bind(this);
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

        $(window).on("beforeunload", this._boundConfirmIsSaved);
        $(document).on("turbolinks:before-visit", this._boundConfirmIsSavedTurbolinks);
    }
    componentWillUnmount() {
        this._cleanUp();

        $(window).off("beforeunload", this._boundConfirmIsSaved);
        $(document).off("turbolinks:before-visit", this._boundConfirmIsSavedTurbolinks);
    }
    render() {
        let content = null;
        if (this.state.isErrored) {
            content = (
                <h4 className="text-center text-danger mt-100 mb-0">{this.props.texts.error}</h4>
            );
        } else if (!this.state.isTestLoading && !this.state.isQuestionLoading && !this.state.isQuestionSaving) {
            content = (
                <DeveloperQuestion count={this.state.questionIndex + 1}
                                   attributes={this._questionAttributes}
                                   object={this._questionObject}
                                   ability={this._abilityObject}
                                   texts={this.props.texts}
                                   errorOut={this._errorOut.bind(this)} />
            );
        } else {
            content = (
                <img className="bb-spinner" src={this.props.spinnerLogo} />
            );
        }

        let pagination = null;
        if (this.props.questionIds.length > 1 && !this.state.isErrored && !this.state.isTestLoading && !this._finalSave) {
            let width = 6;
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
                <div className="col-xs-12 col-sm-6 text-center">
                    <ul className="pagination pagination-sm mt-0 mb-0">{paginationElements}</ul>
                </div>
            );
        }

        return (
            <div className="row">
                <div className="col-xs-12 col-sm-6">
                    <button type="button"
                            disabled={this.state.isQuestionSaving}
                            className="btn btn-success mr-5 mb-5"
                            onClick={this._saveAndExit.bind(this, this.props.dashboardUrl)}>{this.props.texts.saveAndExitButton}</button>
                    <button type="button"
                            disabled={this.state.isQuestionSaving}
                            className="btn btn-success mr-5 mb-5"
                            onClick={this._saveAndExit.bind(this, this.props.previewUrl)}>{this.props.texts.saveAndPreviewButton}</button>
                </div>
                {pagination}
                <div className="col-xs-12 bb-test-container">
                    {content}
                </div>
            </div>
        );
    }
    _saveAndExit(followUrl) {
        if (!this._questionObject) {
            return;
        }
        this.setState({
            isQuestionSaving: true
        });
        this._finalSave = true;
        let object = this._questionObject;
        this._questionObject = null;
        this._abilityObject = null;
        object.save("test", this._questionLastSave.bind(this, followUrl));
        this._oldQuestionObjects.push(object);
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
            this._abilityObject = null;
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
                data.texts,
                this.props.questionUrl,
                this.props.paragraphsUrl,
                this.props.uploadStartUrl,
                this.props.spinnerLogo
            );
            this._abilityObject = new (eval(this.props.ability))(this._questionObject);
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
    _questionLastSave(followUrl, success, object) {
        let index = this._oldQuestionObjects.indexOf(object);
        if (index > -1) {
            this._oldQuestionObjects.splice(index, 1);
        }

        if (!success || this._oldQuestionObjects.length) {
            this._errorOut();
            return;
        }

        $(document).off("turbolinks:before-visit", this._boundConfirmIsSavedTurbolinks);
        Turbolinks.visit(followUrl);
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
    _confirmIsSaved(event) {
        if (this.state.isErrored) {
            return;
        }
        if (this.state.isQuestionSaving || !this._questionObject.isSaved()) {
            let confirmationMessage = "\o/";
            event.returnValue = confirmationMessage;
            return confirmationMessage;
        }
    }
    _confirmIsSavedTurbolinks(event) {
        if (this.state.isErrored) {
            return;
        }
        if (this.state.isQuestionSaving || !this._questionObject.isSaved()) {
            event.preventDefault();
        }
    }
}
