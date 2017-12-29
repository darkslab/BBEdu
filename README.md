### BBEdu ###

A testing platform application.


#### System Requirements ####

* Python 3.4.7
* MySQL 5.7 server
    (database character set should be "utf8" and collation "utf8_general_ci")
    (InnoDB tables)


#### How to create translation files ####

    ./manage.py makemessages -v3 -a -i '_.*' -i '__pycache__' -i 'node_modules' -i 'bbtest/static' --no-location --no-obsolete


#### How to compile React components ####

1. In the project root, install required binaries:

        npm install --save-dev

2. Compile with npm:

        npm run build


#### How to make structural changes to Test Paragraph or Answer ####

Test Paragraph and Answer structures are a simple JSON formatted data. When changed,
the changes have to reflect in multiple places:

1. In `bbtest.forms.test.TestForm`: This form provides initial data for questions.
2. In `bbtest/static/js/react/objects/DeveloperQuestionObject.js`: This object creates
   Paragraphs and Answers in frontend.
3. In `bbtest.forms.test.TestQuestionForm`: This form validates Answer.
4. In `bbtest.forms.test.TestParagraphForm`: This form validates Paragraph.
5. Don't forget to also provide the migration for backward compatibility.
