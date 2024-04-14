class TestCalculator extends React.Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        _load_calculator()
        console.log("Question componentDidMount")
    }
    componentWillUnmount() {
        _unload_calculator()
        console.log("Question componentWillUnmount")
    }

    render() {
        let calculatorComponent = null;
        if (true) {
            console.log("Question hasCalculator")

            const visible = this.props.hasCalculator ? "block" : "none"

            calculatorComponent = <div id="embeddable" className="pull-right" style={{"display": visible}}>
                <span data-calculator="" data-toggle="popover" data-original-title="" title="" >

                    <img className="periodicTableThumbnail mt-0 mb-0"
                        src={this.props.calculatorIconUrl}
                        alt="Thumbnail"
                    >
                    </img>
                </span>
            </div>
            // setTimeout(() => { 
            //     _unload_calculator()
            //     console.log("Question hasCalculator _unload_calculator")
            // }, 500); 

            // setTimeout(() => { 
            //     _load_calculator(); 
            //     console.log("Question hasCalculator _load_calculator")
            // }, 1000); 
            
        }


        return calculatorComponent;
    }
}