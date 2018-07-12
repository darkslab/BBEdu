function PreviewTestObject(component, reportUrl, questions, report) {
    this._component = component;
    this._questions = questions;
    this._report = report;

    this._updateTimer;
}
PreviewTestObject.prototype.stop = function() {
    clearTimeout(this._updateTimer);
}
PreviewTestObject.prototype.question = function(index) {
    return this._questions[index];
}
PreviewTestObject.prototype.answer = function(index) {
    return this._report.answers[index].answer;
}
PreviewTestObject.prototype.updateAnswer = function(index, data) {
    this._report.answers[index] = data;
    this._updateTimer = setTimeout(function() {
        this._component.setState(function(prevState) {
            return {
                toggleFlag: !prevState.toggleFlag
            };
        });
    }.bind(this));
}
