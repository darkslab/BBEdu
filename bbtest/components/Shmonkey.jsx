function Shmonkey(props) {
    const style = {
        cursor: "pointer",
        WebkitUserSelect: "none",
        MozUserSelect: "none",
        MsUserSelect: "none",
        userSelect: "none"
    };
    return (
        <h1 style={style} onClick={props.handleClick}>{props.title}: {props.counter}</h1>
    );
}
