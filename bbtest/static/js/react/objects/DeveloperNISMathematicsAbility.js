DeveloperNISMathematicsAbility.prototype = Object.create(SuperAbility.prototype);
function DeveloperNISMathematicsAbility(questionObject) {
    SuperAbility.call(this, questionObject);
}

DeveloperNISMathematicsAbility.prototype.canAddParagraph = function() { return false; }
DeveloperNISMathematicsAbility.prototype.canDeleteParagraph = function(id) { return false; }

DeveloperNISMathematicsAbility.prototype.canDeleteAnswer = function() { return false; }
DeveloperNISMathematicsAbility.prototype.canAddAnswerChoice = function() { return false; }
DeveloperNISMathematicsAbility.prototype.canDeleteAnswerChoice = function(id) { return false; }
