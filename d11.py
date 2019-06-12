#!/bin/python3

import math
import os
import random
import re
import sys

def arr_sum(arr):
    return sum(sum(arr,[]))

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

numRows=len(arr)
numCols=len(arr[0])


currentSum=0
MaxSum=-1000

for r in range(0,numRows-2):
    for c in range(0,numCols-2):
        currentSum=0
        i=r
        while i<r+3:
            j=c
            while j<c+3:
                currentSum=currentSum+arr[i][j]
                j=j+1
            i=i+1
        currentSum=currentSum-arr[i-2][j-1]-arr[i-2][j-3]
        '''print("Current Sum is",currentSum)'''
        MaxSum=max(MaxSum,currentSum)
        
print(MaxSum)


    


