#!/bin/bash
#If you get permission error, run 
#chmod +rx autoformat.sh
# Need to have black and isort installed to run the script

#Formats the sorts the import statements 
echo 'Running isort ... '
isort ./script/*.py

#formats python code according to PEP 
echo 'Running black ... '
black ./script/*.py



echo 'Auto formating complete.'
