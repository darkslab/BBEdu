function StudentTestObject(component, reportUrl, questions, report) {
    this._component = component;
    this._reportUrl = reportUrl;
    this._questions = questions;
    this._report = report;

    this._updateTimer;
}
StudentTestObject.prototype.stop = function() {
    clearTimeout(this._updateTimer);
}
StudentTestObject.prototype.question = function(index) {
    return this._questions[index];
}
StudentTestObject.prototype.answer = function(index) {
    return this._report.answers[index].answer;
}
StudentTestObject.prototype.updateAnswer = function(index, data) {
    this._report.answers[index] = data;
    this._updateTimer = setTimeout(function() {
        this._component.setState(function(prevState) {
            return {
                toggleFlag: !prevState.toggleFlag
            };
        });
    }.bind(this));
}
