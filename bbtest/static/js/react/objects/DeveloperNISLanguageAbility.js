DeveloperNISLanguageAbility.prototype = Object.create(SuperAbility.prototype);
function DeveloperNISLanguageAbility(questionObject) {
    SuperAbility.call(this, questionObject);
}

DeveloperNISLanguageAbility.prototype.canAddParagraph = function() { return false; }
DeveloperNISLanguageAbility.prototype.canDeleteParagraph = function(id) { return false; }

DeveloperNISLanguageAbility.prototype.canDeleteAnswer = function() { return false; }
DeveloperNISLanguageAbility.prototype.canAddAnswerChoice = function() { return false; }
DeveloperNISLanguageAbility.prototype.canDeleteAnswerChoice = function(id) { return false; }
