# 03-03-2024
#Arryas -1
#problem: Given an array ‘arr’ of size ‘n’ find the largest element in the array.

from sys import *
from collections import *
from math import *

def largestElement(arr, n):
    maxi = 0
    for i in arr:
        maxi = max(i, maxi)
    print(maxi)        
    
    pass

arr = [4,6,3,2,6,79,1]
n = 7
largestElement(arr, n)
# Answer = 79