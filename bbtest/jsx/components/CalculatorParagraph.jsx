class CalculatorParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            originalText: "",
            rawHtml: ""
        };
    }
    componentDidMount() {
        // document.getElementById('embeddable').style.display = 'block'
    }
    componentWillUnmount() {
        // document.getElementById('embeddable').style.display = 'none'
    }

    render() {
        let content = null;
        let className = "bb-test-paragraph";
        let sharedAddon = null;

        if (this.props.isShared) {
            className += " bb-test-paragraph-shared";
            sharedAddon = (
                <h5 className="text-center mt-0 mb-5"><em>{this.props.testTexts.shared_paragraph_header}</em></h5>
            );
        }

        // console.log("CalculatorParagraph this.props", this.props    )
        content = (
            <React.Fragment>
                {sharedAddon}
                <div className={className}>{SimpleFormattedFragment(this.props.data.text)}</div>
            </React.Fragment>
        );
        return content;
    }

     
}
