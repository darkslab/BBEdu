DeveloperNISQuantitativeAbility.prototype = Object.create(SuperAbility.prototype);
function DeveloperNISQuantitativeAbility(questionObject) {
    SuperAbility.call(this, questionObject);
}

DeveloperNISQuantitativeAbility.prototype.canDeleteParagraph = function(id) {
    return this.question().paragraph(id).paragraph_class === "SplitTextParagraph" ? false : true;
}
DeveloperNISQuantitativeAbility.prototype.canChooseTextParagraph = function() {
    var paragraphIds = this.question().paragraphIds();
    var i;
    for (i = 0; i < paragraphIds.length; i++) {
        if (this.question().paragraph(paragraphIds[i]).paragraph_class.includes("TextParagraph")) {
            return false;
        }
    }
    return true;
}
DeveloperNISQuantitativeAbility.prototype.canChooseSplitTextParagraph = function() { return false; }
DeveloperNISQuantitativeAbility.prototype.canChooseSolutionTextParagraph = function() { return false; }
DeveloperNISQuantitativeAbility.prototype.canChooseSolutionImageParagraph = function() { return true; }

DeveloperNISQuantitativeAbility.prototype.canDeleteAnswer = function() { return false; }
DeveloperNISQuantitativeAbility.prototype.canAddAnswerChoice = function() { return false; }
DeveloperNISQuantitativeAbility.prototype.canEditAnswerChoice = function(id) { return false; }
DeveloperNISQuantitativeAbility.prototype.canDeleteAnswerChoice = function(id) { return false; }
