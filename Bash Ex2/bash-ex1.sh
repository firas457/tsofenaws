#!/bin/bash
while true;

do 

echo "please enter a word :"

read word


foo="telephone $word"

if grep -ho  -I -rnw `pwd` -e "${foo//-/ -}"; then
    echo "found : $word appears after telephone" 
    echo ""
    echo "----------------------------------------------------------"
else
    echo "not found : $word does not appear after telephone"
    echo ""
    echo "----------------------------------------------------------"
fi

done
