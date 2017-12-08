class DeveloperTest extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isTestLoading: true,
            isQuestionLoading: true,
            questionIndex: 0
        };
        this._questionData = null;
        this._questionAttributes = null;
        this._$xhrs = [];
    }
    componentDidMount() {
        let questionNumber = 1;
        if (location.hash) {
            questionNumber = parseInt(location.hash.substr(1), 10);
            if (isNaN(questionNumber) || questionNumber < 1 || questionNumber > this.props.questionCount) {
                questionNumber = 1;
            }
            this.setState({
                questionIndex: questionNumber - 1
            });
            location.hash = questionNumber + "";
        }

        this._$xhrs.push($.get({
            url: this.props.indexedQuestionUrl + (questionNumber - 1) + "/",
            success: this._ajaxSuccess.bind(this, "question"),
            error: this._ajaxError.bind(this, "question")
        }));
        this._$xhrs.push($.get({
            url: this.props.attributesUrl,
            success: this._ajaxSuccess.bind(this, "attributes"),
            error: this._ajaxError.bind(this, "attributes")
        }));
    }
    componentWillUnmount() {
        let $xhr;
        while ($xhr = this._$xhrs.shift()) {
            $xhr.abort();
        }
    }
    render() {
        let content = null;
        if (!this.state.isTestLoading && !this.state.isQuestionLoading) {
            content = (
                <DeveloperQuestion id={this._questionData.id}
                                   data={this._questionData.data}
                                   paragraphs={this._questionData.paragraphs}
                                   attributes={this._questionAttributes} />
            );
        } else {
            content = (
                <div className="col-xs-12 bb-developer-container">
                    <img className="bb-spinner" src={this.props.spinnerLogo} />
                </div>
            );
        }

        let pagination = null;
        if (!this.state.isTestLoading) {
            let width = 5;
            if (width < 1) {
                width = 1;
            } else if (width > this.props.questionCount) {
                width = this.props.questionCount;
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
            } else if (indexes[indexes.length - 1] >= this.props.questionCount) {
                while (true) {
                    if (indexes[indexes.length - 1] < this.props.questionCount) {
                        break;
                    }
                    indexes.pop();
                    indexes.unshift(indexes[0] - 1);
                }
            }

            let paginationElements = [];
            paginationElements.push(
                <li key={ 'left' } className={ !indexes[0] ? 'disabled' : '' }>
                    <a href="javascript:void(0);">&laquo;</a>
                </li>
            );
            for (let i = 0; i < indexes.length; i++) {
                paginationElements.push(
                    <li key={ indexes[i].toString() } className={ indexes[i] === this.state.questionIndex ? 'active' : '' }>
                        <a href="javascript:void(0);">{indexes[i] + 1}</a>
                    </li>
                );
            }
            paginationElements.push(
                <li key={ 'right' } className={ indexes[indexes.length - 1] === this.props.questionCount - 1 ? 'disabled' : '' }>
                    <a href="javascript:void(0);">&raquo;</a>
                </li>
            );
            pagination = (
                <div className="col-xs-12 text-right">
                    <ul className="pagination mt-5 mb-5">{paginationElements}</ul>
                </div>
            );
        }

        return (
            <div className="row">
                {pagination}
                {content}
            </div>
        );
    }
    _ajaxSuccess(type, data, status, $xhr) {
        if (type === "question") {
            this._questionData = data;
            this.setState({
                isQuestionLoading: false
            });
        } else if (type === "attributes") {
            this._questionAttributes = data;
        }
        if (this._questionData && this._questionAttributes) {
            this.setState({
                isTestLoading: false
            });
        }
    }
    _ajaxError(type, $xhr, status, error) {
        if (status === "abort") {
            return;
        }
        // DARK_TODO  probably say that something is wrong and ask to reload the page?
    }
}
