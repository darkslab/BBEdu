class TestTimer extends React.Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        // let modal = $("[data-modal]");
        // if (modal.length) {
        //     modal.modal({
        //         backdrop: "static",
        //         keyboard: false
        //     });
        // }
    }
    render() {
        let timer = null;
        if (this.props.hasTimer) {
            let timerClassName = "fa fa-fw mr-10";
            let countDown = "--:--";
            if (this.props.secondsLeft >= 0) {
                countDown = (parseInt(this.props.secondsLeft / 60, 10)) + ":" + ("0" + (this.props.secondsLeft % 60)).substr(-2);
                timerClassName += " fa-clock-o";
            } else {
                timerClassName += " fa-refresh fa-spin";
            }
            let countDownClassName = "bb-test-timer label mt-0 mb-0 pull-right";
            if (this.props.secondsLeft > 10) {
                countDownClassName += " label-success";
            } else {
                countDownClassName += " label-danger";
            }

            timer = (
                <span className={countDownClassName}>
                    <i className={timerClassName}></i>
                    {countDown}
                </span>
            );
        }


        return timer;
    }
}