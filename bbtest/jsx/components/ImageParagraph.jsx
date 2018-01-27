class ImageParagraph extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div className="bb-test-paragraph">
                <img className="img-responsive center-block bb-test-paragraph-image"
                     src="/static/img/logo.png" />
            </div>
        );
    }
}
