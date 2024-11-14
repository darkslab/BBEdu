class FloatingSelector extends React.Component {
    constructor(props) {
        super(props);
        // this.props.id
        // this.props.options
        // this.props.title
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
        const option_selector = []
        for (let i = 0; i < this.props.options.length; i++) {
            const id = this.props.id[i]
            const options = this.props.options[i]
            const title = this.props.title[i]

            option_selector.push(<React.Fragment key={`asd ${i}`} >
                <label key={`label ${i}`} htmlFor={id} className="h5" style={{ "fontWeight": "bold" }}>{title}:</label>
                <select key={`select ${i}`} className="select_v2" id={id}>
                    {options}
                </select>
            </React.Fragment>)


        }

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
            {option_selector}
            </div>
        );
    }
}
