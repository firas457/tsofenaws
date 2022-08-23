#!/bin/bash


echo "siiiiii" > ba.sh



echo "if [ -d "dir99" ] 

 then
    echo "Hello Bash" > dir99/hello.txt
    echo "Hello Bash was succefully writen to dir99/hello.txt"

 else

    mkdir -p dir99 && touch dir99/hello.txt

    echo "Hello Bash" > dir99/hello.txt

 fi" > ba.sh

chmod u+x ba.sh
bash ./ba.sh

sleep 1s

rm -rf ba.sh







