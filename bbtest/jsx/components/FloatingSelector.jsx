class FloatingSelector extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isSticky: false,
        };

        // Define a callback ref
        this.selectorRef = null;
        this.setSelectorRef = element => {
            this.selectorRef = element;
        };

        // Bind the handleScroll function
        this.handleScroll = this.handleScroll.bind(this);
    }

    componentDidMount() {
        // Add scroll event listener
        window.addEventListener("scroll", this.handleScroll);
    }

    componentWillUnmount() {
        // Remove scroll event listener
        window.removeEventListener("scroll", this.handleScroll);
    }

    handleScroll() {
        if (this.selectorRef) {
            const topPosition = this.selectorRef.getBoundingClientRect().top;
            const shouldBeSticky = topPosition <= 0 && window.scrollY !== 0;

            if (shouldBeSticky !== this.state.isSticky) {
                this.setState({ isSticky: shouldBeSticky });
            }
        }
    }

    render() {
        return (
            <div
                ref={this.setSelectorRef} // Set callback ref
                className={`selector ${this.state.isSticky ? "is-sticky" : ""}`}
                style={{
                    textAlign: "center",
                    // transition: "all 0.3s ease",
                    ...(this.state.isSticky
                        ? {
                            position: "fixed",
                            top: 0,
                            left: "50%",
                            transform: "translateX(-50%)",
                            zIndex: 1000,
                            backgroundColor: "white",
                            padding: "10px",
                            boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.2)",
                        }
                        : {}),
                }}
            >
                <label htmlFor="subject-select" className="h5" style={{"fontWeight": "bold"}}>Выбрать Предмет:</label>
                <select className="select_v2" id="subject-select">
                    {/* <option key="option 0" value="0">Total</option> */}
                    {this.props.options}
                </select>
            </div>
        );
    }
}
