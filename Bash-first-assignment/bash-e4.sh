#!/bin/bash

echo "enter name of directory you want to delete : "

read dirname

if [ $(rmdir "$dirname")] 
then echo "Directory deleted sucefully"

else
    rm -r "$dirname"

fi
