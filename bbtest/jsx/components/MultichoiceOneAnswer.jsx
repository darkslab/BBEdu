class MultichoiceOneAnswer extends React.Component {
    constructor(props) {
        super(props);
        this._alphabet = "ABCDEFGH";
    }
    render() {
        let choices = [];
        for (let i = 0; i < this.props.data.choices.length; i++) {
            let ChoiceClass = eval(this.props.data.choices[i].choice_class);
            choices.push(
                <ChoiceClass key={this.props.data.choices[i].id}
                             data={this.props.data.choices[i].meta_data}
                             label={this._alphabet[i]}
                             chosen={false} />
            );
        }

        return (
            <div className="row">
                <div className="col-xs-12">
                    <div className="panel panel-default mb-15">
                        <div className="panel-heading">
                            <h4 className="panel-title text-center">{this.props.texts.multichoiceOneAnswerTitle}</h4>
                        </div>
                        <div className="panel-body">
                            <div className="mb-15">
                                {choices}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
