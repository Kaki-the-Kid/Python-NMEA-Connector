#bash
# -*- coding: utf-8 -*-

# File for running development server

# The simplest and most widely available method to get user input at a 
# shell prompt is the read command. The best way to illustrate its use 
# is a simple demonstration:

#while true; do
#    read -p "Do you wish to install this program? " yn
#    case $yn in
#        [Yy]* ) make install; break;;
#        [Nn]* ) exit;;
#        * ) echo "Please answer yes or no.";;
#    esac
#done

# Another method, pointed out by Steven Huwig, is Bash's select command. 
# Here is the same example using select:

#echo "Do you wish to install this program?"
#select yn in "Yes" "No"; do
#    case $yn in
#        Yes ) make install; break;;
#        No ) exit;;
#    esac
#done

# The select command is a bit more complicated than read, but it has the
# advantage of being able to display a list of choices to the user. The
# user can then select a choice by typing the number of the choice.

# Taking in arguments from the command line
# Ex. python script.py arg1 arg2 arg3
echo "What do you want to do?"
select choices in "Run Console" "Run GUI" "Run server" "Run tests" "Run coverage" "Run linter" "Exit"; do
    case $choices in
        "Run Console" ) python NMEA_Suite.py --console; break;;
        "Run GUI" ) python NMEA_Suite.py --gui; break;;
        "Run server" ) python NMEA_Suite.py --runserver; break;;
        "Run tests" ) python NMEA_Suite.py --test; break;;
        "Run coverage" ) coverage run --source='.' manage.py test; break;;
        "Run linter" ) pylint --rcfile=.pylintrc --load-plugins pylint_django --django-settings-module=project.settings project; break;;
        "Exit" ) exit;;
    esac
done