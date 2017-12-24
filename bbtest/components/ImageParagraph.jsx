function ImageParagraph(props) {
    return (
        <div className="bb-test-paragraph">
            <img className="img-responsive center-block bb-test-paragraph-image"
                 src={props.data.src} />
        </div>
    );
}
