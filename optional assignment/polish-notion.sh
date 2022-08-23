#!/bin/bash

#check if the first argument is "+"
if [ "$1" == "+" ]; then

#define sum = secoend-arg + third-arg + fourth-arg
    sum=$(($2 + $3 + $4))

    echo $sum


#check if the first argument is "-"
elif [ "$1" == "-" ]; then

#define minus = secoend-arg - third-arg - fourth-arg
    minus=$(($2 - $3 - $4))

    echo $minus


#if the first argument is not "+" or "-" then 
#it's not a valid option!
else
    echo "please enter a valid option!"
fi