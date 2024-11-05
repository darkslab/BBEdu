class BuyCreditKaspiQRPage extends React.Component {
    constructor(props) {
        super(props);
        /* props pass from django template */
        // props.qr_code_base64
        // props.secondsLeft
        // props.secondsTotal
        this.state = {
            secondsLeft: props.secondsLeft || 60*5, // Default to 100 if not provided
            minutes: Math.floor(Math.max(props.secondsLeft - 1, 0) / 60),
            seconds: Math.max(props.secondsLeft - 1, 0) % 60,
        };
    }

    componentDidMount() {
        // Set interval to decrease `secondsLeft` every 2 seconds
        this.interval = setInterval(() => {

            this.setState((prevState) => ({
                secondsLeft: Math.max(prevState.secondsLeft - 1, 0), // Ensure it doesn’t go below 0
                minutes: Math.floor(Math.max(prevState.secondsLeft - 1, 0) / 60),
                seconds: Math.max(prevState.secondsLeft - 1, 0) % 60,
            }));
        }, 1000);
    }

    componentWillUnmount() {
        clearInterval(this.interval); // Clear interval when the component unmounts
    }

    calculateProgressWidth() {
        const secondsTotal = this.props.secondsTotal || 100;
        const widthPercentage = (this.state.secondsLeft / secondsTotal) * 100;
        return `${widthPercentage}%`;
    }

    render() {
        const progressWidth = this.calculateProgressWidth();

        return (
            <React.Fragment>
                <div className="row">
                    <div className="col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                        <div className="panel panel-default">
                            <div className="panel-body text-center">
                                <p className="text-center">
                                    <strong>Инструкция по оплате</strong> {/* Manual Payment Message */}
                                </p>
                                <img 
                                    src={`data:image/png;base64,${this.props.qr_code_base64}`} 
                                    alt="QR Code" 
                                    className="img-responsive center-block" 
                                />
                                {/* Decreasing centered red line below QR code */}
                                <div 
                                    style={{
                                        height: "5px",
                                        backgroundColor: "red",
                                        width: progressWidth,
                                        margin: "10px auto", // Centers the line
                                        transition: "width 1s linear" // Smoothly update width every second
                                    }}
                                />
                                {/* Timer message */}
                                <p style={{ marginTop: "10px", fontSize: "16px", fontWeight: "bold" }}>
                                    Пожалуйста, оплатите в течение {this.state.minutes} минут и {this.state.seconds} секунд
                                </p>
                            </div>
                            {/* Manual Payment Button */}
                            <div className="text-center pb-10">
                                <a onClick={() => window.location.reload()} className="btn btn-primary">Обновить</a>
                            </div>
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}