#!/bin/bash

shuf -i 1-99  | paste - - - |sort -n 
