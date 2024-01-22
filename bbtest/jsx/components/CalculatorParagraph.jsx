class CalculatorParagraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            originalText: "",
            rawHtml: ""
        };
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
                {/* <script src="https://linangdata.com/calculatorEmbed/linangcalc.js"></script> */}
                {/* <div style={{ width: "50px", height: "50px", "backgroundImage": "url('https://linangdata.com/calculatorEmbed/icons/48x48.png')", zIndex: 9999}}>
                  <iframe id="linangcalc" src="https://linangdata.com/calculatorEmbed/embeddable.html?placement=right" 
                      width="500" height="500" scrolling="auto" frameBorder="0" allowtransparency="true"
                      style={{border: 0, position: "absolute", opacity: 1.0, zIndex: 9999}}
                      >
                  </iframe>
                </div> */}
                <script src="/static/Calculator_files/linangcalc.js"></script>
                <div style={{ width: "50px", height: "50px", "backgroundImage": "/static/Calculator_files/48x48.png", zIndex: 0}}>
                  <iframe id="linangcalc" src="/static/Calculator.html?placement=right" 
                      width="370" height="340" scrolling="auto" frameBorder="0" allowtransparency="true"
                      style={{border: 0, position: "absolute", opacity: 1.0, zIndex: 9000}}
                      >
                  </iframe>
                </div>
            </React.Fragment>
        );
        return content;
    }

     
}
