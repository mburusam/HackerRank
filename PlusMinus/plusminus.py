#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive =0
    negative =0
    zero =0
    for num in range(len(arr)):
        if arr[num]>0:
            positive+=1
        elif (arr[num]==0):
            zero+=1
        else:
            negative +=1
    print(positive/len(arr))
    print(negative/len(arr))
    print(zero/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
