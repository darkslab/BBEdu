#!/bin/bash 
# Navigate to your Django project directory 
cd ~/bbwork/BBEdu

mysql -u root -p --force --password=monkey -e "DROP DATABASE IF EXISTS iac; CREATE DATABASE iac CHARACTER SET utf8 COLLATE utf8_general_ci;"
gunzip < ./backup_iac_2024.02.14.sql.gz | mysql -u root -p iac --password=monkey
# gunzip < backup_2024.02.15_iac-v1.6.0.sql.gz | mysql -u root -p iac --password=monkey



# Get a list of tags sorted by creation date 
tags=("iac-v1.5.0" "iac-v1.5.1" "iac-v1.5.2" "iac-v1.5.3" "iac-v1.5.4" "iac-v1.5.5" "iac-v1.6.0" "iac-v1.6.1.2" "iac-v1.6.2" "iac-v1.6.3")
# tags=("iac-v1.6.1.1" "iac-v1.6.2" "iac-v1.6.3")

# Loop through each tag 
for tag in ${tags[@]}; do 
	echo "Checking out $tag..." 
	git checkout $tag 
	echo "Applying migrations for $tag..." 
	# Apply Django migrations 
	python3.4 manage.py migrate 
	# Add any additional commands you need to run after each migration here. 
	# For example, collecting static files or any custom management commands. 
	echo "Migrations applied for $tag." 
done 

# Optionally, checkout back to the main branch or any other branch you wish 
# git checkout main echo "All done."
