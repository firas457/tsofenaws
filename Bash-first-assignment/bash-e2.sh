#!/bin/bash

while true;

do 

echo "Enter your filename"

read newfile1

if [ -f "$newfile1" ]

then

echo "File is found"
break

else

   echo "File is not found"
   

fi

done
