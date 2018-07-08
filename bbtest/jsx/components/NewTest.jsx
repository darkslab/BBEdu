class NewTest extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isErrored: false,
            status: undefined,
            toggleFlag: true
        };
        this._xhrStartTime;
        this._$xhr;
        this._statusData;
    }
    componentDidMount() {
        this._continue(true);
    }
    componentWillUnmount() {
        this._stop();
    }
    render() {
        let content = null;
        switch (this.state.status) {
            case "queued":
                content = (
                    <div className="panel panel-default">
                        <div className="panel-body">
                            <h3 className="text-center mb-15">{this._statusData.section}</h3>
                            <p className="lead">{this._statusData.instructions}</p>
                            <div className="text-center">
                                <button type="button"
                                        className="btn btn-primary btn-lg mb-23"
                                        onClick={this._continue.bind(this)}>{this.props.texts.startButton}</button>
                            </div>
                        </div>
                    </div>
                );
                break;
            case "started":
                let bottomPaginationLeft = null;
                let bottomPaginationRight = null;
                if (this._statusData.questionIndex > 0) {
                    bottomPaginationLeft = (
                        <li className="previous">
                            <a href="javascript:void(0);"
                               onClick={this._setQuestionIndex.bind(this, this._statusData.questionIndex - 1)}>&larr; {this.props.texts.previousPager}</a>
                        </li>
                    );
                } else {
                    bottomPaginationLeft = (
                        <li className="previous disabled">
                            <a href="javascript:void(0);">&larr; {this.props.texts.previousPager}</a>
                        </li>
                    );
                }
                if (this._statusData.questionIndex < this._statusData.questionsCount - 1) {
                    bottomPaginationRight = (
                        <li className="next">
                            <a href="javascript:void(0);"
                               onClick={this._setQuestionIndex.bind(this, this._statusData.questionIndex + 1)}>{this.props.texts.nextPager} &rarr;</a>
                        </li>
                    );
                } else {
                    bottomPaginationRight = (
                        <li className="next disabled">
                            <a href="javascript:void(0);">{this.props.texts.nextPager} &rarr;</a>
                        </li>
                    );
                }

                content = (
                    <React.Fragment>
                        <div className="row">
                            <div className="col-xs-12 text-center hidden-xs">
                                <ul className="pagination mt-0 mb-0">{this._paginationElements(13)}</ul>
                            </div>
                            <div className="col-xs-12 text-center visible-xs-block">
                                <ul className="pagination pagination-sm mt-0 mb-0">{this._paginationElements(6)}</ul>
                            </div>
                        </div>
                        <Question count={this._statusData.questionIndex + 1}
                                  object={this._statusData.testObject.question(this._statusData.questionIndex)}
                                  answerData={this._statusData.testObject.answer(this._statusData.questionIndex)}
                                  onAnswerUpdate={this._statusData.testObject.updateAnswer.bind(this._statusData.testObject, this._statusData.questionIndex)}
                                  secondsLeft={this._statusData.seconds}
                                  texts={this.props.texts} />
                        <div className="row">
                            <div className="col-xs-12">
                                <ul className="pager mt-0 mb-0">
                                    {bottomPaginationLeft}
                                    {bottomPaginationRight}
                                </ul>
                            </div>
                        </div>
                    </React.Fragment>
                );
                break;
            case "expired":
                // DARK_TODO  implement this!
                break;
            case "concluded":
                // DARK_TODO  implement this!
            default:
                content = (
                    <img className="bb-spinner" src={this.props.spinnerLogo} />
                );
                break;
        }

        let modal = null;
        if (this.state.isErrored) {
            modal = (
                <RefreshModal message={this.props.texts.error}
                              refreshUrl={this.props.refreshUrl}
                              cancelUrl={this.props.cancelRefreshUrl}
                              refreshCaption={this.props.texts.refreshButton}
                              cancelCaption={this.props.texts.cancelRefreshButton} />
            );
        }

        return (
            <React.Fragment>
                {modal}
                <div className="row">
                    <div className="col-xs-12 bb-test-container">
                        {content}
                    </div>
                </div>
            </React.Fragment>
        );
    }
    reportFailed() {
        if (this.state.status !== "started") {
            return;
        }
        if (this._statusData.seconds > 1) {
            this._errorOut();
        }
    }

    _errorOut() {
        this._stop();
        this.setState({
            isErrored: true
        });
    }
    _stop() {
        if (this._$xhr !== undefined) {
            this._$xhr.abort();
        }
        switch (this.state.status) {
            case "queued":
                break;
            case "started":
                this._statusData.testObject.stop();
                clearTimeout(this._statusData.timer);
                break;
            case "expired":
                break;
            case "concluded":
                break;
        }
    }
    _ajaxSuccess(data, status, $xhr) {
        if (!data.success) {
            this._errorOut();
            return;
        }
        let msecs = (new Date()).getTime() - this._xhrStartTime;
        this.setState({
            status: data.status
        });
        switch (data.status) {
            case "queued":
                this._statusData = {
                    section: data.section,
                    instructions: data.instructions
                };
                break;
            case "started":
                this._statusData = {
                    seconds: Math.max(data.seconds - Math.round(msecs / 1000), 0),
                    testObject: new (eval(this.props.objectClass))(this, data.questions, data.report),
                    questionIndex: 0,
                    questionsCount: data.questions.length,
                    timer: setTimeout(this._tick.bind(this), 1000)
                };
                break;
            case "expired":
                break;
            case "concluded":
                break;
        }
    }
    _ajaxError($xhr, status, error) {
        if (status === "abort") {
            return;
        }
        this._errorOut();
    }
    _tick() {
        this._statusData.seconds -= 1;
        if (this._statusData.seconds >= 0) {
            this._statusData.timer = setTimeout(this._tick.bind(this), 1000);
            this.setState(prevState => ({
                toggleFlag: !prevState.toggleFlag
            }));
            return;
        }
        this._end();
    }
    _request(idempotent, url, $xhrMethod) {
        if (idempotent && this.state.status === undefined) {
            return;
        }
        this._stop();
        this._xhrStartTime = (new Date()).getTime();
        let xhrData = {
            url: url,
            success: this._ajaxSuccess.bind(this),
            error: this._ajaxError.bind(this)
        };
        if ($xhrMethod === $.post) {
            xhrData.headers = {"X-CSRFToken": Cookies.get("csrftoken")};
        }
        this._$xhr = $xhrMethod(xhrData);
        this.setState({
            status: undefined
        });
    }
    _continue(force = false) {
        this._request(!force, this.props.continueUrl, $.get);
    }
    _start() {
        this._request(true, this.props.startUrl, $.post);
    }
    _skip() {
        this._request(true, this.props.skipUrl, $.post);
    }
    _end() {
        this._request(true, this.props.endUrl, $.post);
    }
    _setQuestionIndex(index) {
        if (this.state.status !== "started") {
            return;
        }
        this._statusData.questionIndex = index;
        this.setState(prevState => ({
            toggleFlag: !prevState.toggleFlag
        }));
    }
    _paginationElements(width) {
        if (width < 1) {
            width = 1;
        } else if (width > this._statusData.questionsCount) {
            width = this._statusData.questionsCount;
        }
        let padding = parseInt((width - 1) / 2, 10);
        let rightPadding = (width - 1) % 2;
        let indexes = [ this._statusData.questionIndex ];
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
        } else if (indexes[indexes.length - 1] >= this._statusData.questionsCount) {
            while (true) {
                if (indexes[indexes.length - 1] < this._statusData.questionsCount) {
                    break;
                }
                indexes.pop();
                indexes.unshift(indexes[0] - 1);
            }
        }

        let paginationElements = [];
        if (this._statusData.questionIndex > 0) {
            paginationElements.push(
                <li key="left">
                    <a href="javascript:void(0);"
                       onClick={this._setQuestionIndex.bind(this, this._statusData.questionIndex - 1)}>&laquo;</a>
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
            if (indexes[i] === this._statusData.questionIndex) {
                paginationElements.push(
                    <li key={indexes[i].toString()} className="active">
                        <a href="javascript:void(0);">{indexes[i] + 1}</a>
                    </li>
                );
            } else {
                paginationElements.push(
                    <li key={indexes[i].toString()}>
                        <a href="javascript:void(0);"
                           onClick={this._setQuestionIndex.bind(this, indexes[i])}
                           className={this._statusData.testObject.answer(indexes[i]) ? "bb-pagination-success" : ""}>{indexes[i] + 1}</a>
                    </li>
                );
            }
        }
        if (this._statusData.questionIndex < this._statusData.questionsCount - 1) {
            paginationElements.push(
                <li key="right">
                    <a href="javascript:void(0);"
                       onClick={this._setQuestionIndex.bind(this, this._statusData.questionIndex + 1)}>&raquo;</a>
                </li>
            );
        } else {
            paginationElements.push(
                <li key="right" className="disabled">
                    <a href="javascript:void(0);">&raquo;</a>
                </li>
            );
        }
        return paginationElements;
    }
}
