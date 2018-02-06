function PreviewTestObject(component, questions, answerSubmission) {
    this._component = component;
    this._questions = questions;
    this._answerSubmission = answerSubmission;
}
PreviewTestObject.prototype.question = function(index) {
    return this._questions[index];
}
PreviewTestObject.prototype.push = function(callback) {
    setTimeout(function() {
        callback(true);
    });
}
PreviewTestObject.prototype.answerData = function(index) {
    return this._answerSubmission.answers[index].answer;
}
PreviewTestObject.prototype.answerUpdate = function(index, data) {
    this._answerSubmission.answers[index] = data;
    setTimeout(function() {
        this._component.setState(function(prevState) {
            return {
                toggleFlag: !prevState.toggleFlag
            };
        });
    }.bind(this));
}
