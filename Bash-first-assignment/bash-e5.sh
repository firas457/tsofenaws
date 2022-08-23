#!/bin/bash

echo "enter file name : "

read filename

maxword=""
temp=0

for word in $(cat "$filename")
do

if  [ ${#word} -gt ${#max} ];
then maxword=$word
fi
done

echo $maxword
