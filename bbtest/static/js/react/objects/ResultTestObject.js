function ResultTestObject(component, reportUrl, questions, report, texts) {
    this._component = component;
    this._questions = questions;
    this._report = report;
    this._texts = texts;
}
ResultTestObject.prototype.stop = function() {
}
ResultTestObject.prototype.question = function(index) {
    return this._questions[index];
}
ResultTestObject.prototype.answer = function(index) {
    return this._report.answers[index].answer;
}
ResultTestObject.prototype.updateAnswer = function(index, data) {
}
ResultTestObject.prototype.canAnswer = function() {
    return false;
}
ResultTestObject.prototype.showCorrectAnswer = function() {
    return true;
}
ResultTestObject.prototype.texts = function() {
    return this._texts;
}
