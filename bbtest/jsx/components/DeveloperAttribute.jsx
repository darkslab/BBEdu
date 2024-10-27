class DeveloperAttribute extends React.Component {
    constructor(props) {
        super(props);
        this.attribute_name = props.attribute_name;
        this.label = props.label;
        this.value = props.value;
        this.data = props.data;
        this.onChange = props.onChange;

    }
    componentDidMount() {
        console.log(this.label);
        console.log(this.value);
        console.log(this.onChange);

        const label = this.label;

        const onChange = this.onChange

        $('#' + this.attribute_name).select2({
            width: '50vw'
        });
        $('#' + this.attribute_name).on('select2:select', function (e) {
            var data = e.params.data;
            console.log(label);
            console.log(data);
            console.log(e);

            onChange(parseInt(data.id));
        });

    }

    render() {
        // let caption = "";
        // let options = [];
        // for (let i = 0; i < this.data.length; i++) {
        //     const fullCaption = this.data[i].caption;
        //     const truncatedCaption = fullCaption.length > 100 ? `${fullCaption.slice(0, 100)}...` : fullCaption;

        //     if (this.value === this.data[i].value) {
        //         options.push(
        //             <li key={this.data[i].value} className="active">
        //                 <a href="javascript:void(0);" title={fullCaption}>
        //                     {truncatedCaption}
        //                 </a>
        //             </li>
        //         );
        //     } else {
        //         options.push(
        //             <li key={this.data[i].value}>
        //                 <a
        //                     href="javascript:void(0);"
        //                     onClick={this.onChange.bind(null, this.data[i].value)}
        //                     title={fullCaption}
        //                 >
        //                     {truncatedCaption}
        //                 </a>
        //             </li>
        //         );
        //     }
        // }

        let options_select2 = [];
        for (let i = 0; i < this.data.length; i++) {
            const fullCaption = this.data[i].caption;
            const truncatedCaption = fullCaption.length > 100 ? `${fullCaption.slice(0, 100)}...` : fullCaption;
            options_select2.push(
                <option
                    key={this.data[i].value}
                    title={fullCaption}
                    value={this.data[i].value}
                >
                    {truncatedCaption}
                </option>
            );
        }

        return (
            <div className={this.value ? "form-group" : "form-group has-error"}>
                <label className="control-label col-sm-3 text-uppercase">{this.label}</label>
                <div className="col-sm-9">
                    <div className="input-group">
                        {/* <input type="text" className="form-control bb-test-section-background pl-10" readOnly value={caption} />
                        <div className="input-group-btn">
                            <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                <span className="caret"></span>
                            </button>
                            <ul className="dropdown-menu dropdown-menu-right">
                                {options}
                            </ul>
                        </div> */}
                        <select
                            id={this.attribute_name}
                            className="form-control bb-test-section-background pl-10"
                            // data-placeholder={this.label}
                            defaultValue={this.value}
                            name="filter_status"
                            onChange={this.onChange.bind(null, (event) => {
                                console.log(event)
                                event.target.value
                            })}
                        >
                            {options_select2}
                        </select>
                    </div>
                </div>
            </div>
        );

    }

}


