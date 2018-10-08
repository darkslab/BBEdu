function PreviewTestObject(component, reportUrl, questions, report, texts) {
    this._component = component;
    this._questions = questions;
    this._report = report;
    this._texts = texts;
}
PreviewTestObject.prototype.stop = function() {
}
PreviewTestObject.prototype.question = function(index) {
    return this._questions[index];
}
PreviewTestObject.prototype.answer = function(index) {
    return this._report.answers[index].answer;
}
PreviewTestObject.prototype.updateAnswer = function(index, data) {
}
PreviewTestObject.prototype.canAnswer = function() {
    return false;
}
PreviewTestObject.prototype.showCorrectAnswer = function() {
    return false;
}
PreviewTestObject.prototype.texts = function() {
    return this._texts;
}
