class DeveloperImageParagraph extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div className="form-group bb-test-section-movable bb-test-section-background" data-paragraph-id={this.props.paragraphId}>
                <div className="pt-5 pr-5 pb-5 pl-5 clearfix">
                    <button type="button" className="btn btn-default btn-xs pull-right ml-5 invisible">Spacer</button>
                </div>
                <div className="bb-test-paragraph bb-test-paragraph-upload">
                    <div className="row">
                        <div className="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                            <label for="monkey" className="btn btn-success btn-lg btn-block mt-23">Upload Image</label>
                            <input id="monkey" className="hidden" type="file" />
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
