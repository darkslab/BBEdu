function StudentTestObject(component, reportUrl, questions, report, texts) {
    this._component = component;
    this._reportUrl = reportUrl;
    this._questions = questions;
    this._report = report;
    this._texts = texts;

    this._updateTimer;
    this._$xhr;
    this._queuedReport = false;
}
// DARK_TODO  support a functionality where stop would notify that important request (report) is
//            still in progress, so we can maybe stop users from navigating away?
StudentTestObject.prototype.stop = function() {
    clearTimeout(this._updateTimer);
    if (this._$xhr !== undefined) {
        this._$xhr.abort();
    }
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
    this._push();
}
StudentTestObject.prototype.canAnswer = function() {
    return true;
}
StudentTestObject.prototype.showCorrectAnswer = function() {
    return false;
}
StudentTestObject.prototype._push = function() {
    if (this._$xhr !== undefined) {
        this._queuedReport = true;
        return;
    }
    this._$xhr = $.post({
        url: this._reportUrl,
        headers: {"X-CSRFToken": Cookies.get("csrftoken")},
        data: {
            report: JSON.stringify(this._report)
        },
        success: this._ajaxSuccess.bind(this),
        error: this._ajaxError.bind(this)
    });
}
StudentTestObject.prototype._ajaxSuccess = function(data, status, $xhr) {
    if (!data.success) {
        this._component.reportFailed(data.error_msg);
        return;
    }
    this._$xhr = undefined;
    if (this._queuedReport) {
        this._queuedReport = false;
        this._push();
    }
}
StudentTestObject.prototype._ajaxError = function($xhr, status, error) {
    if (status === "abort") {
        return;
    }
    this._component.reportFailed("StudentTestObject.prototype._ajaxError");
}
StudentTestObject.prototype.texts = function() {
    return this._texts;
}
