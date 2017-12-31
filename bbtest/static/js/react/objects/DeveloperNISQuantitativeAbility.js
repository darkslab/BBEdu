DeveloperNISQuantitativeAbility.prototype = Object.create(SuperAbility.prototype);
function DeveloperNISQuantitativeAbility(questionObject) {
    SuperAbility.call(this, questionObject);
}

DeveloperNISQuantitativeAbility.prototype.canAddParagraph = function() {
    return this.question().paragraphIds().length > 1 ? false : true;
}
DeveloperNISQuantitativeAbility.prototype.canDeleteParagraph = function(id) {
    return this.question().paragraph(id).paragraph_class === "SplitTextParagraph" ? false : true;
}
DeveloperNISQuantitativeAbility.prototype.canChooseSplitTextParagraph = function() { return false; }

DeveloperNISQuantitativeAbility.prototype.canDeleteAnswer = function() { return false; }
DeveloperNISQuantitativeAbility.prototype.canAddAnswerChoice = function() { return false; }
DeveloperNISQuantitativeAbility.prototype.canEditAnswerChoice = function(id) { return false; }
DeveloperNISQuantitativeAbility.prototype.canDeleteAnswerChoice = function(id) { return false; }
