class SolutionImageParagraph extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        let className = "bb-test-paragraph";
        let imgClassName;
        let imgSrc;
        if (this.props.data.asset_url) {
            imgClassName = "img-responsive center-block bb-test-paragraph-image";
            imgSrc = this.props.data.asset_url;
        } else {
            className += " bb-test-paragraph-image-waiting";
            imgClassName = "bb-spinner";
            imgSrc = this.props.data.spinner_logo_url;
        }

        return (
            <div className={className}>
                <img className={imgClassName} src={imgSrc} />
            </div>
        );
    }
}