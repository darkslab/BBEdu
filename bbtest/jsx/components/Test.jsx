class Test extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isErrored: false,
            status: undefined,
            toggleFlag: true,
            confirmationFor: undefined
        };
        this._xhrStartTime;
        this._$xhr;
        this._statusData;
        this._lingerTimer = null;
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
                let instructions = [];
                for (let i = 0; i < this._statusData.instructions.length; i++) {
                    let className = "lead";
                    let isLastGroup = true;
                    if (i < this._statusData.instructions.length - 1) {
                        isLastGroup = false;
                    }
                    for (let j = 0; j < this._statusData.instructions[i].length; j++) {
                        let innerClassName = "";
                        if (j < this._statusData.instructions[i].length - 1) {
                            innerClassName += " mb-0";
                        } else if (!isLastGroup) {
                            innerClassName += " mb-10";
                        }
                        instructions.push(
                            <p key={i + "-" + j} className={className + innerClassName}>{this._statusData.instructions[i][j]}</p>
                        );
                    }
                }
                content = (
                    <div className="panel panel-default">
                        <div className="panel-body">
                            <h3 className="text-center mb-15">{this._statusData.section}</h3>
                            {instructions}
                            <div className="text-center mb-23">
                                <div className="visible-xs-block">
                                    <button type="button"
                                            className="btn btn-primary btn-block"
                                            onClick={this._renderModal.bind(this, "start")}>{this.props.texts.startButton}</button>
                                    {/*
                                    <button type="button"
                                            className="btn btn-danger btn-block"
                                            onClick={this._renderModal.bind(this, "skip")}>{this.props.texts.skipButton}</button>
                                    */}
                                </div>
                                <div className="hidden-xs">
                                    <button type="button"
                                            className="btn btn-primary btn-lg"
                                            onClick={this._renderModal.bind(this, "start")}>{this.props.texts.startButton}</button>
                                    {/*
                                    <button type="button"
                                            className="btn btn-danger btn-lg ml-5"
                                            onClick={this._renderModal.bind(this, "skip")}>{this.props.texts.skipButton}</button>
                                    */}
                                </div>
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

                let endControl = null;
                if (this.props.canEnd) {
                    endControl = (
                        <div className="row">
                            <div className="col-xs-12 text-center">
                                <button type="button"
                                        className="btn btn-danger btn-sm"
                                        onClick={this._renderModal.bind(this, "end")}>{this.props.texts.endButton}</button>
                            </div>
                        </div>
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
                                  canAnswer={this._statusData.testObject.canAnswer()}
                                  showCorrectAnswer={this._statusData.testObject.showCorrectAnswer()}
                                  secondsLeft={this._statusData.seconds}
                                  texts={this.props.texts}
                                  hasTimer={this.props.hasTimer} />
                        <div className="row">
                            <div className="col-xs-12">
                                <ul className="pager mt-0 mb-0">
                                    {bottomPaginationLeft}
                                    {bottomPaginationRight}
                                </ul>
                            </div>
                        </div>
                        {endControl}
                    </React.Fragment>
                );
                break;
            case "expired":
                content = (
                    <div className="panel panel-default">
                        <div className="panel-body">
                            <h3 className="text-center mb-15 text-danger">{this.props.texts.expiredTitle}</h3>
                            <p className="lead text-center">{this.props.texts.expiredExplanation}</p>
                            <div className="text-center mb-23">
                                <div className="visible-xs-block">
                                    <button type="button"
                                            className="btn btn-primary btn-block"
                                            onClick={this._end.bind(this)}>{this.props.texts.continueButton}</button>
                                </div>
                                <div className="hidden-xs">
                                    <button type="button"
                                            className="btn btn-primary btn-lg"
                                            onClick={this._end.bind(this)}>{this.props.texts.continueButton}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                );
                break;
            case "concluded":
                content = (
                    <div className="panel panel-default">
                        <div className="panel-body">
                            <h3 className="text-center mb-15 text-success">{this.props.texts.concludedTitle}</h3>
                            <p className="lead text-center">{this.props.texts.concludedExplanation}</p>
                            <div className="text-center mb-23">
                                <div className="visible-xs-block">
                                    <a href={this.props.resultsUrl}
                                       className="btn btn-success btn-block">{this.props.texts.resultsButton}</a>
                                    <a href={this.props.buyUrl}
                                       className="btn btn-primary btn-block">{this.props.texts.buyButton}</a>
                                </div>
                                <div className="hidden-xs">
                                    <a href={this.props.resultsUrl}
                                       className="btn btn-success btn-lg">{this.props.texts.resultsButton}</a>
                                    <a href={this.props.buyUrl}
                                       className="btn btn-primary btn-lg ml-5">{this.props.texts.buyButton}</a>
                                </div>
                            </div>
                        </div>
                    </div>
                );
                break;
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
        } else if (this.state.confirmationFor !== undefined) {
            var isInverse = true;
            if (this.state.confirmationFor === "start") {
                isInverse = false;
            }
            modal = (
                <ConfirmModal title={this.props.texts.confirmModalTitle}
                              yesCaption={this.props.texts.confirmModalYesCaption}
                              noCaption={this.props.texts.confirmModalNoCaption}
                              isInverse={isInverse}
                              complete={this._completeModal.bind(this)} />
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
        clearTimeout(this._lingerTimer);
    }
    _ajaxSuccess(data, status, $xhr) {
        if (!data.success) {
            this._errorOut();
            return;
        }
        let msecs = (new Date()).getTime() - this._xhrStartTime;
        switch (data.status) {
            case "queued":
                this._statusData = {
                    section: data.section,
                    instructions: data.instructions
                };
                break;
            case "started":
                let seconds = Math.max(data.seconds - Math.round(msecs / 1000), 0);
                if (seconds <= 1) {
                    data.status = undefined;
                    this._lingerTimer = setTimeout(function() {
                        this._continue(true);
                    }.bind(this), 2000);
                } else {
                    this._statusData = {
                        seconds: seconds,
                        testObject: new (eval(this.props.objectClass))(this, this.props.reportUrl, data.questions, data.report),
                        questionIndex: 0,
                        questionsCount: data.questions.length,
                        timer: setTimeout(this._tick.bind(this), 1000)
                    };
                }
                break;
            case "expired":
                break;
            case "concluded":
                break;
        }
        this.setState({
            status: data.status
        });
    }
    _ajaxError($xhr, status, error) {
        if (status === "abort") {
            return;
        }
        this._errorOut();
    }
    _tick() {
        if (!this.props.hasTimer) {
            return;
        }
        this._statusData.seconds -= 1;
        if (this._statusData.seconds >= 0) {
            this._statusData.timer = setTimeout(this._tick.bind(this), 1000);
            this.setState(prevState => ({
                toggleFlag: !prevState.toggleFlag
            }));
            return;
        }
        this._continue();
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
    _completeModal(data) {
        if (data) {
            switch (this.state.confirmationFor) {
                case "skip":
                    this._skip();
                    break;
                case "end":
                    this._end();
                    break;
                case "start":
                    this._start();
                    break;
            }
        }
        this.setState({
            confirmationFor: undefined
        });
    }
    _renderModal(type) {
        if (this.state.confirmationFor !== undefined) {
            return;
        }
        this.setState({
            confirmationFor: type
        });
    }
}
