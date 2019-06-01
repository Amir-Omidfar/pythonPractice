#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
# If  is odd, print Weird
if N%2 == 1:
    print("Weird\n")
else:
    if (N < 6 and N >1):
        print("Not Weird\n")
    elif ((N > 5) and (N < 21)):
        print ("Weird\n")
    elif (N > 19):
        print("Not Weird\n")


