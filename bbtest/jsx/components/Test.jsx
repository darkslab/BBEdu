class Test extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isTestLoading: true,
            isCompleting: false,
            isErrored: false,
            isTimedOut: false,
            questionIndex: 0,
            secondsLeft: undefined
        };
        this._testObject;
        this._$xhr;
        this._timer;
    }
    componentDidMount() {
        let questionNumber = 1;
        if (location.hash) {
            questionNumber = parseInt(location.hash.substr(1), 10);
            if (isNaN(questionNumber) || questionNumber < 1 || questionNumber > this.props.questionsCount) {
                questionNumber = 1;
            }
        }
        this._setQuestionIndex(questionNumber - 1);

        this._$xhr = $.get({
            url: this.props.testUrl,
            success: this._ajaxSuccess.bind(this),
            error: this._ajaxError.bind(this)
        });
    }
    componentWillUnmount() {
        this._cleanUp();
    }
    render() {
        let content = null;
        if (this.state.isErrored) {
            content = (
                <h4 className="text-center text-danger mt-100 mb-0">{this.props.texts.error}</h4>
            );
        } else if (this.state.isTestLoading || this.state.isCompleting) {
            content = (
                <img className="bb-spinner" src={this.props.spinnerLogo} />
            );
        } else if (this.state.isTimedOut) {
            content = (
                <h4 className="text-center mt-100 mb-0">Time is up!</h4>
            );
        } else {
            content = (
                <Question count={this.state.questionIndex + 1}
                          object={this._testObject.question(this.state.questionIndex)}
                          onAnswerUpdate={this._testObject.answerUpdate.bind(this._testObject, this.state.questionIndex)}
                          secondsLeft={this.state.secondsLeft}
                          texts={this.props.texts} />
            );
        }

        let pagination = null;
        let bottomPagination = null;
        if (this.props.questionsCount > 1 && !this.state.isErrored && !this.state.isTestLoading && !this.state.isCompleting && !this.state.isTimedOut) {
            pagination = (
                <React.Fragment>
                    <div className="col-xs-12 text-center hidden-xs">
                        <ul className="pagination mt-0 mb-0">{this._paginationElements(13)}</ul>
                    </div>
                    <div className="col-xs-12 text-center visible-xs-block">
                        <ul className="pagination pagination-sm mt-0 mb-0">{this._paginationElements(6)}</ul>
                    </div>
                </React.Fragment>
            );

            let bottomPaginationLeft = null;
            let bottomPaginationRight = null;
            if (this.state.questionIndex > 0) {
                bottomPaginationLeft = (
                    <li className="previous">
                        <a href="javascript:void(0);"
                           onClick={this._setQuestionIndex.bind(this, this.state.questionIndex - 1)}>&larr; {this.props.texts.previousPager}</a>
                    </li>
                );
            } else {
                bottomPaginationLeft = (
                    <li className="previous disabled">
                        <a href="javascript:void(0);">&larr; {this.props.texts.previousPager}</a>
                    </li>
                );
            }
            if (this.state.questionIndex < this.props.questionsCount - 1) {
                bottomPaginationRight = (
                    <li className="next">
                        <a href="javascript:void(0);"
                           onClick={this._setQuestionIndex.bind(this, this.state.questionIndex + 1)}>{this.props.texts.nextPager} &rarr;</a>
                    </li>
                );
            } else {
                bottomPaginationRight = (
                    <li className="next disabled">
                        <a href="javascript:void(0);">{this.props.texts.nextPager} &rarr;</a>
                    </li>
                );
            }
            bottomPagination = (
                <ul className="pager mt-0 mb-0">
                    {bottomPaginationLeft}
                    {bottomPaginationRight}
                </ul>
            );
        }

        return (
            <div className="row">
                {pagination}
                <div className="col-xs-12 bb-test-container">
                    {content}
                </div>
                <div className="col-xs-12">
                    {bottomPagination}
                </div>
            </div>
        );
    }

    _ajaxSuccess(data, status, $xhr) {
        this._testObject = new (eval(this.props.objectClass))(data.questions);
        this.setState({
            isTestLoading: false,
            secondsLeft: data.seconds_left
        });
        this._timer = setTimeout(this._tick.bind(this), 1000);
    }
    _ajaxError($xhr, status, error) {
        if (status === "abort") {
            return;
        }
        this._errorOut();
    }
    _errorOut() {
        this.setState({
            isErrored: true
        });
        this._cleanUp();
    }
    _cleanUp() {
        this._$xhr.abort();
        clearTimeout(this._timer);
    }
    _tick() {
        let secondsLeft = this.state.secondsLeft - 1;
        if (secondsLeft >= 0) {
            this._timer = setTimeout(this._tick.bind(this), 1000);
            this.setState({
                secondsLeft: secondsLeft
            });
            return;
        }
        this._testObject.push(this._completed.bind(this));
        this.setState({
            isCompleting: true,
            isTimedOut: true
        });
    }
    _completed(success) {
        if (!success) {
            this._errorOut();
            return;
        }
        this.setState({
            isCompleting: false
        });
    }
    _setQuestionIndex(index) {
        this.setState({
            questionIndex: index
        });
        history.replaceState(history.state, "", location.pathname + "#" + (index + 1).toString());
    }
    _paginationElements(width) {
        if (width < 1) {
            width = 1;
        } else if (width > this.props.questionsCount) {
            width = this.props.questionsCount;
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
        } else if (indexes[indexes.length - 1] >= this.props.questionsCount) {
            while (true) {
                if (indexes[indexes.length - 1] < this.props.questionsCount) {
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
                       onClick={this._setQuestionIndex.bind(this, this.state.questionIndex - 1)}>&laquo;</a>
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
                           onClick={this._setQuestionIndex.bind(this, indexes[i])}>{indexes[i] + 1}</a>
                    </li>
                );
            }
        }
        if (this.state.questionIndex < this.props.questionsCount - 1) {
            paginationElements.push(
                <li key="right">
                    <a href="javascript:void(0);"
                       onClick={this._setQuestionIndex.bind(this, this.state.questionIndex + 1)}>&raquo;</a>
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
