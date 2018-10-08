function DeveloperQuestionObject(id, data, paragraphs, texts, questionUrl, paragraphsUrl, uploadStartUrl, spinnerLogoUrl) {
    this._id = id;
    this._data = data;
    this._paragraphs = [];
    this._texts = texts;

    this._contextData = {};
    this._questionUrl = questionUrl;
    this._paragraphsUrl = paragraphsUrl;
    this._uploadStartUrl = uploadStartUrl;
    this._spinnerLogoUrl = spinnerLogoUrl;

    this._isQuestionSaved = true;
    this._isParagraphsSaved = true;

    this._paragraphCounter = 0;
    var i;
    for (i = 0; i < paragraphs.length; i++) {
        this._paragraphs.push({
            id: this._paragraphCounter++,
            token: paragraphs[i].id,
            questionIds: paragraphs[i].question_ids,
            data: this._beforeLoadParagraphDataTransform(paragraphs[i].data)
        });
    }
}
DeveloperQuestionObject.prototype.difficulty = function() {
    return this._data.difficulty;
}
DeveloperQuestionObject.prototype.setDifficulty = function(value) {
    this._data.difficulty = value;
    this._isQuestionSaved = false;
}
DeveloperQuestionObject.prototype.taxonomy = function() {
    return this._data.taxonomy;
}
DeveloperQuestionObject.prototype.setTaxonomy = function(value) {
    this._data.taxonomy = value;
    this._isQuestionSaved = false;
}
DeveloperQuestionObject.prototype.topic = function() {
    return this._data.topic;
}
DeveloperQuestionObject.prototype.setTopic = function(value) {
    this._data.topic = value;
    this._isQuestionSaved = false;
}
DeveloperQuestionObject.prototype.save = function(context, callback) {
    if (!this._contextData.hasOwnProperty(context)) {
        this._contextData[context] = {
            $xhrs: [],
            callback: undefined,
            result: undefined
        };
    }
    if (this.isSaved()) {
        setTimeout(function() {
            callback(true, this);
        }.bind(this));
        return;
    }
    if (this._contextData[context].$xhrs.length) {
        return;
    }

    this._contextData[context].callback = callback;

    if (!this._isQuestionSaved) {
        this._contextData[context].$xhrs.push($.post({
            url: this._questionUrl + this._id + "/",
            headers: {"X-CSRFToken": Cookies.get("csrftoken")},
            data: {
                difficulty: this.difficulty(),
                taxonomy: this.taxonomy(),
                topic: this.topic(),
                answer_class: this.answer().answer_class,
                meta_data: JSON.stringify(this.answer().meta_data)
            },
            success: this._ajaxSuccess.bind(this, context, "question"),
            error: this._ajaxError.bind(this, context, "question")
        }));
    }

    if (!this._isParagraphsSaved) {
        var paragraphs = [];
        var i;
        for (i = 0; i < this._paragraphs.length; i++) {
            if (this._shouldSkipParagraphSave(this._paragraphs[i].data)) {
                continue;
            }
            paragraphs.push({
                id: this._paragraphs[i].token ? this._paragraphs[i].token : this._paragraphs[i].id,
                is_new: this._paragraphs[i].token ? false : true,
                data: this._beforeSaveParagraphDataTransform(this._paragraphs[i].data)
            });
        }
        this._contextData[context].$xhrs.push($.post({
            url: this._paragraphsUrl + this._id + "/paragraphs/",
            headers: {"X-CSRFToken": Cookies.get("csrftoken")},
            data: {
                data: JSON.stringify(paragraphs)
            },
            success: this._ajaxSuccess.bind(this, context, "paragraphs"),
            error: this._ajaxError.bind(this, context, "paragraphs")
        }));
    }
}
DeveloperQuestionObject.prototype.stop = function(context) {
    if (!this._contextData.hasOwnProperty(context)) {
        return;
    }
    var $xhr;
    while ($xhr = this._contextData[context].$xhrs.shift()) {
        $xhr.abort();
    }
    this._contextData[context].result = undefined;
    this._contextData[context].callback = undefined;
}
DeveloperQuestionObject.prototype.isSaved = function() {
    return this._isQuestionSaved && this._isParagraphsSaved;
}
DeveloperQuestionObject.prototype.paragraphIds = function() {
    var ids = [];
    var i;
    for (i = 0; i < this._paragraphs.length; i++) {
        ids.push(this._paragraphs[i].id);
    }
    return ids;
}
DeveloperQuestionObject.prototype.paragraph = function(id) {
    var i;
    for (i = 0; i < this._paragraphs.length; i++) {
        if (id === this._paragraphs[i].id) {
            return this._paragraphs[i].data;
        }
    }
}
DeveloperQuestionObject.prototype.paragraphSharedWith = function(id) {
    var i;
    for (i = 0; i < this._paragraphs.length; i++) {
        if (id === this._paragraphs[i].id) {
            return this._paragraphs[i].questionIds;
        }
    }
}
DeveloperQuestionObject.prototype.updateParagraph = function(id, data) {
    var i;
    for (i = 0; i < this._paragraphs.length; i++) {
        if (id === this._paragraphs[i].id) {
            this._paragraphs[i].data.meta_data = data;
            this._isParagraphsSaved = false;
            break;
        }
    }
}
DeveloperQuestionObject.prototype.addParagraph = function(type) {
    var newParagraph = {
        id: this._paragraphCounter++,
        token: undefined,
        questionIds: [],
        data: {
            paragraph_class: type
        }
    };
    switch (type) {
        case "TextParagraph":
            newParagraph.data.meta_data = {
                text: ""
            };
            break;
        case "SplitTextParagraph":
            newParagraph.data.meta_data = {
                left: {
                    text: ""
                },
                right: {
                    text: ""
                }
            };
            break;
        case "ImageParagraph":
            newParagraph.data.meta_data = {
                asset_uuid: undefined,
                asset_url: undefined,
                upload_start_url: this._uploadStartUrl,
                spinner_logo_url: this._spinnerLogoUrl,
                status: "waiting",
                progress: 0
            };
            break;
    }
    this._paragraphs.push(newParagraph);
    this._isParagraphsSaved = false;
}
DeveloperQuestionObject.prototype.deleteParagraph = function(id) {
    var i;
    for (i = 0; i < this._paragraphs.length; i++) {
        if (id === this._paragraphs[i].id) {
            break;
        }
    }
    this._paragraphs.splice(i, 1);
    this._isParagraphsSaved = false;
}
DeveloperQuestionObject.prototype.setParagraphOrder = function(order) {
    this._paragraphs.sort(function(a, b) {
        var i = order.indexOf(a.id);
        var j = order.indexOf(b.id);
        if (i === j) {
            return 0;
        }
        return i < j ? -1 : 1;
    });
    this._isParagraphsSaved = false;
}
DeveloperQuestionObject.prototype.answer = function() {
    return {
        answer_class: this._data.answer_class,
        meta_data: this._data.meta_data
    };
}
DeveloperQuestionObject.prototype.updateAnswer = function(data) {
    this._data.meta_data = data;
    this._isQuestionSaved = false;
}
DeveloperQuestionObject.prototype.setAnswer = function(type) {
    switch (type) {
        case "MultichoiceOneAnswer":
            this._data.answer_class = type;
            this._data.meta_data = {
                choices: [],
                correct_id: null
            };
            break;
        case "MultichoiceMultiAnswer":
            this._data.answer_class = type;
            this._data.meta_data = {
                choices: [],
                correct_ids: []
            };
            break;
    }
    this._isQuestionSaved = false;
}
DeveloperQuestionObject.prototype.deleteAnswer = function() {
    this._data.answer_class = "";
    this._data.meta_data = null;
    this._isQuestionSaved = false;
}
DeveloperQuestionObject.prototype.texts = function() {
    return this._texts;
}

DeveloperQuestionObject.prototype._ajaxSuccess = function(context, type, data, status, $xhr) {
    var index = this._contextData[context].$xhrs.indexOf($xhr);
    if (index > -1) {
        this._contextData[context].$xhrs.splice(index, 1);
    }
    if (this._contextData[context].result === undefined) {
        this._contextData[context].result = true;
    } else {
        this._contextData[context].result = this._contextData[context].result && true;
    }

    var i, j;
    switch (type) {
        case "question":
            this._isQuestionSaved = true;
            break;
        case "paragraphs":
            for (i = 0; i < data.update.length; i++) {
                for (j = 0; j < this._paragraphs.length; j++) {
                    if (data.update[i].old === this._paragraphs[j].id) {
                        this._paragraphs[j].token = data.update[i].new;
                        break;
                    }
                }
            }
            this._isParagraphsSaved = true;
            break;
    }

    if (!this._contextData[context].$xhrs.length) {
        this._runCallback(context);
    }
}
DeveloperQuestionObject.prototype._ajaxError = function(context, type, $xhr, status, error) {
    if (status === "abort") {
        return;
    }
    var index = this._contextData[context].$xhrs.indexOf($xhr);
    if (index > -1) {
        this._contextData[context].$xhrs.splice(index, 1);
    }
    this._contextData[context].result = false;
    if (!this._contextData[context].$xhrs.length) {
        this._runCallback(context);
    }
}
DeveloperQuestionObject.prototype._runCallback = function(context) {
    var result = this._contextData[context].result;
    this._contextData[context].result = undefined;
    var callback = this._contextData[context].callback;
    this._contextData[context].callback = undefined;
    setTimeout(function() {
        callback(result, this);
    }.bind(this));
}
DeveloperQuestionObject.prototype._beforeLoadParagraphDataTransform = function(data) {
    switch (data.paragraph_class) {
        case "ImageParagraph":
            return {
                paragraph_class: data.paragraph_class,
                meta_data: {
                    asset_uuid: data.meta_data.asset_uuid,
                    asset_url: data.meta_data.asset_url,
                    upload_start_url: this._uploadStartUrl,
                    spinner_logo_url: this._spinnerLogoUrl,
                    status: "staring",
                    progress: 100
                }
            };
            break;
        default:
            return data;
            break;
    }
}
DeveloperQuestionObject.prototype._beforeSaveParagraphDataTransform = function(data) {
    switch (data.paragraph_class) {
        case "ImageParagraph":
            return {
                paragraph_class: data.paragraph_class,
                meta_data: {
                    asset_uuid: data.meta_data.asset_uuid
                }
            };
            break;
        default:
            return data;
            break;
    }
}
DeveloperQuestionObject.prototype._shouldSkipParagraphSave = function(data) {
    switch (data.paragraph_class) {
        case "ImageParagraph":
            if (data.meta_data.status !== "staring") {
                return true;
            }
            break;
        default:
            break;
    }
    return false;
}
