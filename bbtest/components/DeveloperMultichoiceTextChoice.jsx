class DeveloperMultichoiceTextChoice extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        let buttons = [];
        // <button type="button" className="btn btn-success btn-xs pull-right ml-5">Formulas On</button>
        // <button type="button" className="btn btn-danger btn-xs pull-right ml-5">Incorrect Answer</button>

        return (
            <div className="form-group bb-test-section-movable bb-test-section-background">
                <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                    {buttons}
                    <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                </div>
                <div className="row">
                    <div className="col-xs-2 col-sm-3 pr-0"></div>
                    <div className="col-xs-10 col-sm-7 pl-0">
                        <textarea className="form-control bb-test-answer bb-test-answer-textarea"
                                  placeholder="Type something!"
                                  value="" />
                    </div>
                </div>
            </div>
        );
    }
}
