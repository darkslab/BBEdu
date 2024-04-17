class StandaloneQuestion extends React.Component {
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
        this._currentQuestionIndex = 0;

        this._boundWindowBlur = this._windowBlur.bind(this);
        this._boundWindowFocus = this._windowFocus.bind(this);
    }
    componentDidMount() {
        this._continue(true, false);

        $(window).on("blur", this._boundWindowBlur);
        $(window).on("focus", this._boundWindowFocus);
    }
    componentWillUnmount() {
        this._stop();

        $(window).off("blur", this._boundWindowBlur);
        $(window).off("focus", this._boundWindowFocus);
    }
    render() {
        let content = null;
        switch (this.state.status) {
            case "started":
                let header = null;
                if (this._statusData.section !== undefined) {
                    header = (
                        <div className="row">
                            <div className="col-xs-12">
                                <h4 className="text-center mt-0 mb-23">{this._statusData.section[0]} <span className="label label-default">{this._statusData.section[1]}</span></h4>
                            </div>
                        </div>
                    );
                }

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
                                        className="btn btn-danger btn-sm mt-10"
                                        onClick={this._renderModal.bind(this, "end")}>{this.props.texts.endButton}</button>
                            </div>
                        </div>
                    );
                }

                // const hasPeriodicTableList = JSON.parse(this.props.hasPeriodicTable)
                // const hasCalculatorList = JSON.parse(this.props.hasCalculator)
                // console.log(hasPeriodicTableList, hasCalculatorList)
                content = (
                    <React.Fragment>
                        {header}
                        {/*
                        <div className="row">
                            <div className="col-xs-12 text-center hidden-xs">
                                <ul className="pagination mt-0 mb-0">{this._paginationElements(13)}</ul>
                            </div>
                            <div className="col-xs-12 text-center visible-xs-block">
                                <ul className="pagination pagination-sm mt-0 mb-0">{this._paginationElements(6)}</ul>
                            </div>
                        </div>
                        */}
                        <Question count={this._statusData.questionIndex + 1}
                                  object={this._statusData.testObject.question(this._statusData.questionIndex)}
                                  answerData={this._statusData.testObject.answer(this._statusData.questionIndex)}
                                  onAnswerUpdate={this._statusData.testObject.updateAnswer.bind(this._statusData.testObject, this._statusData.questionIndex)}
                                  canAnswer={this._statusData.testObject.canAnswer()}
                                  showCorrectAnswer={this._statusData.testObject.showCorrectAnswer()}
                                  testTexts={this._statusData.testObject.texts()}
                                  secondsLeft={this._statusData.focused ? this._statusData.seconds : -1}
                                  texts={this.props.texts}
                                  hasTimer={this.props.hasTimer} 
                                  hasPeriodicTable={this._statusData.hasPeriodicTable[this._statusData.questionIndex]} 
                                  periodicTableIconUrl={this.props.periodicTableIconUrl}
                                  periodicTableUrl={this.props.periodicTableUrl}
                                  hasCalculator={this._statusData.hasCalculator[this._statusData.questionIndex]} 
                                  calculatorIconUrl={this.props.calculatorIconUrl}
                                  />
                        {/* <div className="row">
                            <div className="col-xs-12">
                                <ul className="pager mt-0 mb-0">
                                    {bottomPaginationLeft}
                                    {bottomPaginationRight}
                                </ul>
                            </div>
                        </div> */}
                        {endControl}
                    </React.Fragment>
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
    reportFailed(error_msg="") {
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
    _ajaxSuccess(pageview, data, status, $xhr) {
        if (pageview) {
            ga_report_pageview();
        }
        if (!data.success) {
            this._errorOut();
            return;
        }

        this._statusData = {
            seconds: 100000000000000000000000,
            focused: true,
            testObject: new (eval(this.props.objectClass))(this, this.props.reportUrl, data.questions, data.report, data.texts),
            questionIndex: this._currentQuestionIndex,
            questionsCount: data.questions.length,
            timer: setTimeout(this._tick.bind(this), 1000),
            hasCalculator: data.has_calculator,
            hasPeriodicTable: data.has_periodic_table,
        };


        this.setState({
            status: "started"
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
    _request(idempotent, url, $xhrMethod, pageview) {
        if (idempotent && this.state.status === undefined) {
            return;
        }
        this._stop();
        this._xhrStartTime = (new Date()).getTime();
        let xhrData = {
            url: url,
            success: this._ajaxSuccess.bind(this, pageview),
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
    _continue(force = false, pageview = true) {
        this._request(!force, this.props.continueUrl, $.get, pageview);
    }
    _start() {
        this._request(true, this.props.startUrl, $.post, true);
    }
    _skip() {
        this._request(true, this.props.skipUrl, $.post, true);
    }
    _end() {
        this._request(true, this.props.endUrl, $.post, true);
    }
    _setQuestionIndex(index) {
        if (this.state.status !== "started") {
            return;
        }
        this._statusData.questionIndex = index;
        this.setState(prevState => ({
            toggleFlag: !prevState.toggleFlag
        }));
        ga_report_pageview();
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
                let elementClassName = this._statusData.testObject.answer(indexes[i]) ? "bb-pagination-primary" : "";
                if (this._statusData.testObject.showCorrectAnswer()) {
                    elementClassName = this._statusData.testObject.isCorrect(indexes[i]) ? "bb-pagination-success" : "bb-pagination-danger";
                }
                paginationElements.push(
                    <li key={indexes[i].toString()}>
                        <a href="javascript:void(0);"
                           onClick={this._setQuestionIndex.bind(this, indexes[i])}
                           className={elementClassName}>{indexes[i] + 1}</a>
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
    _windowBlur() {
        if (this.state.status !== "started") {
            return;
        }
        this._currentQuestionIndex = this._statusData.questionIndex;
        this._statusData.focused = false;
    }
    _windowFocus() {
        if (this.state.status !== "started") {
            return;
        }
        this._continue();
    }
}
