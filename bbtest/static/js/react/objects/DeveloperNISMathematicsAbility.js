DeveloperNISMathematicsAbility.prototype = Object.create(SuperAbility.prototype);
function DeveloperNISMathematicsAbility(questionObject) {
    SuperAbility.call(this, questionObject);
}

DeveloperNISMathematicsAbility.prototype.canDeleteParagraph = function(id) {
    return this.question().paragraph(id).paragraph_class === "ImageParagraph" ? true : false;
}
DeveloperNISMathematicsAbility.prototype.canChooseTextParagraph = function() { return false; }
DeveloperNISMathematicsAbility.prototype.canChooseSplitTextParagraph = function() { return false; }

DeveloperNISMathematicsAbility.prototype.canDeleteAnswer = function() { return false; }
DeveloperNISMathematicsAbility.prototype.canAddAnswerChoice = function() { return false; }
DeveloperNISMathematicsAbility.prototype.canDeleteAnswerChoice = function(id) { return false; }
