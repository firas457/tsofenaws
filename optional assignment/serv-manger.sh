#!/bin/bash
#check if the first argument is "+"


if [ "$1" == "start" ]; then

  	
sudo ln -sf /home/myhome/.scripts/sleep.service /etc/systemd/system

# Enable and start
sudo systemctl enable sleep.service
sudo systemctl start sleep.service
    
   

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
