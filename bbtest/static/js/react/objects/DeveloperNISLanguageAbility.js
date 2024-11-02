DeveloperNISLanguageAbility.prototype = Object.create(SuperAbility.prototype);
function DeveloperNISLanguageAbility(questionObject) {
    SuperAbility.call(this, questionObject);
}

DeveloperNISLanguageAbility.prototype.canDeleteParagraph = function(id) {
    return this.question().paragraph(id).paragraph_class.includes("ImageParagraph") ? true : false;
}
DeveloperNISLanguageAbility.prototype.canChooseTextParagraph = function() { return false; }
DeveloperNISLanguageAbility.prototype.canChooseSplitTextParagraph = function() { return false; }
DeveloperNISLanguageAbility.prototype.canChooseSolutionImageParagraph = function() { return true; }

DeveloperNISLanguageAbility.prototype.canDeleteAnswer = function() { return false; }
DeveloperNISLanguageAbility.prototype.canAddAnswerChoice = function() { return false; }
DeveloperNISLanguageAbility.prototype.canDeleteAnswerChoice = function(id) { return false; }
