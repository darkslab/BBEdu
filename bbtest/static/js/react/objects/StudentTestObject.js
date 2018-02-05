function StudentTestObject(questions) {
    this._questions = questions;
}
StudentTestObject.prototype.question = function(index) {
    return this._questions[index];
}
StudentTestObject.prototype.push = function(callback) {
    // DARK_TODO  implement this
}
