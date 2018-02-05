function PreviewTestObject(questions) {
    this._questions = questions;
}
PreviewTestObject.prototype.question = function(index) {
    return this._questions[index];
}
PreviewTestObject.prototype.push = function(callback) {
    setTimeout(function() {
        callback(true);
    });
}
