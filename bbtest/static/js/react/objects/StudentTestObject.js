function StudentTestObject(component, questions, answerSubmission) {
    this._component = component;
    this._questions = questions;
    this._answerSubmission = answerSubmission;
}
StudentTestObject.prototype.question = function(index) {
    return this._questions[index];
}
StudentTestObject.prototype.push = function(callback) {
    // DARK_TODO  implement this
}
StudentTestObject.prototype.answerData = function(index) {
    return this._answerSubmission.answers[index].answer;
}
StudentTestObject.prototype.answerUpdate = function(index, data) {
    // DARK_TODO  implement this
}
