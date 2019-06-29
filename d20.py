#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list


totalSwaps=0

for i in range(n):
    numberOfSwaps=0
    for j in range(n-1):
        if (a[j] > a[j+1]):
            swap(a,j,j+1)
            numberOfSwaps+=1
    totalSwaps+=numberOfSwaps
    if (numberOfSwaps == 0):
        break


print("Array is sorted in",totalSwaps,"swaps.")
print("First Element:", a[0])
print("Last Element:", a[n-1])
