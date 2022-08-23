#!/bin/bash

for FILE in *;do if  [ -d $FILE ]; then echo $FILE; fi; done
