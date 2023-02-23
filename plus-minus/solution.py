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
    pos_cnt = 0
    neg_cnt = 0
    zro_cnt = 0
    for num in arr:
        if num > 0:
            pos_cnt += 1
            continue
        if num < 0:
            neg_cnt += 1
            continue
        zro_cnt += 1
   
    arr_len = len(arr)
    
    pos_ratio = pos_cnt / arr_len
    print(f"%.6f" % pos_ratio)
    
    neg_ratio = neg_cnt / arr_len
    print(f"%.6f" % neg_ratio)
    
    zro_ratio = zro_cnt / arr_len
    print(f"%.6f" % zro_ratio)
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
