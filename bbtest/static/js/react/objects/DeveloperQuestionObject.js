function DeveloperQuestionObject(id, data, paragraphs) {
    this._id = id;
    this._data = data;
    this._paragraphs = paragraphs;

    this._newParagraphCounter = 0;

    var i;
    for (i = 0; i < this._paragraphs.length; i++) {
        this._paragraphs[i].id = this._paragraphs[i].id.toString();
        this._paragraphs[i].isNew = false;
    }
}
DeveloperQuestionObject.prototype.difficulty = function() {
    return this._data.difficulty;
}
DeveloperQuestionObject.prototype.setDifficulty = function(value) {
    this._data.difficulty = value;
}
DeveloperQuestionObject.prototype.taxonomy = function() {
    return this._data.taxonomy;
}
DeveloperQuestionObject.prototype.setTaxonomy = function(value) {
    this._data.taxonomy = value;
}
DeveloperQuestionObject.prototype.topic = function() {
    return this._data.topic;
}
DeveloperQuestionObject.prototype.setTopic = function(value) {
    this._data.topic = value;
}
DeveloperQuestionObject.prototype.save = function(context, callback) {
    callback(true, this);
}
DeveloperQuestionObject.prototype.stop = function(context) {
}
DeveloperQuestionObject.prototype.isSaved = function() {
    return true;
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
DeveloperQuestionObject.prototype.updateParagraph = function(id, data) {
    var i;
    for (i = 0; i < this._paragraphs.length; i++) {
        if (id === this._paragraphs[i].id) {
            this._paragraphs[i].data.meta_data = data;
            break;
        }
    }
}
DeveloperQuestionObject.prototype.addParagraph = function(type) {
    if (["TextParagraph", "SplitTextParagraph"].indexOf(type) <= -1) {
        return;
    }
    var newParagraph = {
        id: "p_" + (this._newParagraphCounter++),
        isNew: true,
        question_ids: [],
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
    }
    this._paragraphs.push(newParagraph);
}
DeveloperQuestionObject.prototype.deleteParagraph = function(id) {
    var i;
    for (i = 0; i < this._paragraphs.length; i++) {
        if (id === this._paragraphs[i].id) {
            break;
        }
    }
    this._paragraphs.splice(i, 1);
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
}
DeveloperQuestionObject.prototype.answer = function() {
    return {
        answer_class: this._data.answer_class,
        meta_data: this._data.meta_data
    };
}
DeveloperQuestionObject.prototype.updateAnswer = function(data) {
    this._data.meta_data = data;
}
