function DeveloperAttribute(props) {
    let caption = "";
    let options = [];
    for (let i = 0; i < props.data.length; i++) {
        const fullCaption = props.data[i].caption;
        const truncatedCaption = fullCaption.length > 100 ? `${fullCaption.slice(0, 100)}...` : fullCaption;

        if (props.value === props.data[i].value) {
            caption = fullCaption;
            options.push(
                <li key={props.data[i].value} className="active">
                    <a href="javascript:void(0);" title={fullCaption}>
                        {truncatedCaption}
                    </a>
                </li>
            );
        } else {
            options.push(
                <li key={props.data[i].value}>
                    <a
                        href="javascript:void(0);"
                        onClick={props.onChange.bind(null, props.data[i].value)}
                        title={fullCaption}
                    >
                        {truncatedCaption}
                    </a>
                </li>
            );
        }
    }


    return (
        <div className={props.value ? "form-group" : "form-group has-error"}>
            <label className="control-label col-sm-3 text-uppercase">{props.label}</label>
            <div className="col-sm-9">
                <div className="input-group">
                    <input type="text" className="form-control bb-test-section-background pl-10" readOnly value={caption} />
                    <div className="input-group-btn">
                        <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown">
                            <span className="caret"></span>
                        </button>
                        <ul className="dropdown-menu dropdown-menu-right">
                            {options}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
}
