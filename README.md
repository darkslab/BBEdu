### BBEdu ###

A testing platform application.


#### System Requirements ####

* Python 3.4.7
* MySQL 5.7 server
    (database character set should be "utf8" and collation "utf8_general_ci")
    (InnoDB tables)


#### How to create translation files ####

    ./manage.py makemessages -v3 -a -i '_.*' --no-location --no-obsolete


#### How to compile React components ####

1. In the project root, install required binaries:

        npm install --save-dev

2. Compile with npm:

        npm run build
