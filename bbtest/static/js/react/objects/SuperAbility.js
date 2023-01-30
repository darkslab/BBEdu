function SuperAbility(questionObject) {
    this._question = questionObject;
}
SuperAbility.prototype.question = function() {
    return this._question;
}

SuperAbility.prototype.canAddParagraph = function() { return true; }
SuperAbility.prototype.canDeleteParagraph = function(id) { return true; }
SuperAbility.prototype.canChooseTextParagraph = function() { return true; }
SuperAbility.prototype.canChooseSplitTextParagraph = function() { return true; }
SuperAbility.prototype.canChooseImageParagraph = function() { return true; }
SuperAbility.prototype.canChooseSolutionTextParagraph = function() { return true; }
SuperAbility.prototype.canChooseSolutionImageParagraph = function() { return true; }

SuperAbility.prototype.canDeleteAnswer = function() { return true; }
SuperAbility.prototype.canAddAnswerChoice = function() { return true; }
SuperAbility.prototype.canEditAnswerChoice = function(id) { return true; }
SuperAbility.prototype.canDeleteAnswerChoice = function(id) { return true; }
