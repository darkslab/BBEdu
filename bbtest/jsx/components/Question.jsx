class Question extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        let paragraphs = [];
        for (let i = 0; i < this.props.object.paragraphs.length; i++) {
            let ParagraphClass = eval(this.props.object.paragraphs[i].paragraph_class);
            paragraphs.push(
                <ParagraphClass key={i}
                                data={this.props.object.paragraphs[i].meta_data} />
            );
        }

        let countDown = (parseInt(this.props.secondsLeft / 60, 10)) + ":" + ("0" + (this.props.secondsLeft % 60)).substr(-2);
        let countDownClassName = "bb-test-timer label mt-0 mb-0 pull-right";
        if (this.props.secondsLeft > 10) {
            countDownClassName += " label-success";
        } else {
            countDownClassName += " label-danger";
        }

        return (
            <React.Fragment>
                <div className="row">
                    <div className="col-xs-12">
                        <div className="panel panel-primary">
                            <div className="panel-heading bb-rel clearfix">
                                <div className="bb-test-number">{this.props.count}</div>
                                <h4 className="panel-title bb-test-title mt-15 mb-15 pull-left">{this.props.texts.question}</h4>
                                <span className={countDownClassName}>
                                    <i className="fa fa-clock-o mr-10"></i>
                                    {countDown}
                                </span>
                            </div>
                            <div className="panel-body">
                                <div className="mb-15">
                                    {paragraphs}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}
