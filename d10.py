#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    init_n=n
    ans=""
    while (n >= 2):
        rem=int(n%2)
        ans=str(rem)+ans
        n=int(n/2)
    ans=str(n)+ans
    counter=0
    prevCounter=0
    i=0
    for i in range(len(ans)):
        if(ans[i]=='1'):
            counter=counter+1
        else:
            prevCounter=max(prevCounter,counter)
            counter=0
        i=i+1
    print(max(prevCounter,counter))
