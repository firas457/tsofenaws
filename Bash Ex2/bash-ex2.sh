#!/bin/bash
while true;

do 
read input

declare -A arr

arr["israel"]=Jerusalem

arr+=( ["usa"]=Washington ["italy"]=Rome  ["romania"]=Bucharest ["spain"]=Madrid)
 

if echo ${arr[$input]};  then
echo ""  
else 
echo "please choose a valid country from the 5 countries on the list "
fi
done
