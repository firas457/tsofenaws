
from random import random

import random


def create_key(key):
    list1=[]  
    for i in range(len(key)):
        list1.append(key[i])
    random.shuffle(list1)

    return ''.join(list1)
  
def decreypt_key(key,enc_key_dict):
    key2=[*key]
    for i in range(0,len(key2)):
        temp=enc_key_dict[key2[i]]
        for j in range(0,len(key2)):
            if key2[j]==temp:
                key2[j]=key2[i]
    return ''.join(key2)

      