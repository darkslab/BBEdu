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
        const option_selector = [];
        for (let i = 0; i < this.props.options.length; i++) {
            const id = this.props.id[i];
            const options = this.props.options[i];
            const title = this.props.title[i];
    
            option_selector.push(
                <div
                    key={`selector-container-${i}`}
                    style={{
                        display: "flex",
                        flexDirection: "row",
                        alignItems: "center",
                        border: "1px solid #ddd",
                        borderRadius: "2px",
                        padding: "2px 3px",
                        margin: "2px 0",
                        backgroundColor: "#f9f9f9",
                        boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.1)",
                        maxWidth: "800px", // Keep a max width to avoid spreading too wide
                        marginLeft: "auto", // Center align within the parent container
                        marginRight: "auto",
                    }}
                >
                    <label
                        htmlFor={id}
                        className="h5"
                        style={{
                            fontWeight: "bold",
                            color: "#333",
                            marginRight: "15px",
                            whiteSpace: "nowrap", // Prevents wrapping of the label text
                        }}
                    >
                        {title}:
                    </label>
                    <select
                        id={id}
                        className="select_v2"
                        style={{
                            flex: 1,
                            padding: "2px 3px",
                            borderRadius: "3px",
                            border: "1px solid #ccc",
                            fontSize: "16px",
                            backgroundColor: "#fff",
                            appearance: "none",
                            width: "100%", // Allows dropdown to fill remaining space
                        }}
                    >
                        {options}
                    </select>
                </div>
            );
        }
    
        return (
            <div
                ref={this.setSelectorRef}
                className={`selector ${this.state.isSticky ? "is-sticky" : ""}`}
                style={{
                    textAlign: "center",
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
                            minWidth: "600px",
                        }
                        : {}),
                }}
            >
                {option_selector}
            </div>
        );
    }
    
}
