#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_num = float('inf')
    max_num = float('-inf')
    total = 0
    for num in arr:
        total += num
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    min_res = total - max_num
    max_res = total - min_num
    print(min_res, max_res)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
